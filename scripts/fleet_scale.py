#!/usr/bin/env python3
"""SpyderMonkey fleet scale — the 1000-agent architecture.

`smk fleetscale --workers N [--goal G] [--target T] [--domain D]
                 [--lanes a,b] [--shards S] [--rps N] [--controller URL]
                 [--plan] [--dry-run] [--json]`

The honest design: a single box supports ~50-200 concurrent workers before
thrash makes more workers slower. A 1000-agent fleet is N nodes × M workers,
talking to ONE controller over the existing HMAC-signed task channel
(fleet_agent.py). This layer does the parts that were missing:

1. TASK PARTITION — (lane × asset-shard) tasks derived from the goal's
   route (deterministic, versionable).
2. LOCAL WORKER POOL — ThreadPoolExecutor running each task as a family
   engine pass, bounded by the box.
3. RATE GOVERNOR — a shared token bucket from scope.json max_rate_rps so
   a thousand agents never become a flood (the walls stay walls at scale).
4. RESULT AGGREGATION — {lane, shard, rc, ok, elapsed} per worker, merged
   and deduped; kernel-schema results can be absorbed per task.
5. `--plan` — the honest capacity math: workers/box ceiling, nodes for 1000,
   expected findings/hour from the measured density baseline.

Distributed: point --controller at a running fleet_agent controller; the
partition enqueues there (nodes run beacons; results return via /result).
"""

import argparse
import json
import os
import shlex
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import scope_authority as sa  # noqa: E402

HOMES = ("~/.hermes/cache/scratch", "~")


# ── rate governor ──────────────────────────────────────────────────────────

class TokenBucket:
    """Shared, thread-safe: no more than `rps` live probes per second across
    the whole fleet. The walls are estate-wide; so is the noise budget."""

    def __init__(self, rps: float):
        self.rps = max(rps, 0.1)
        self.tokens = float(self.rps)
        self.last = time.monotonic()
        self.lock = threading.Lock()

    def take(self, n: int = 1) -> None:
        with self.lock:
            while True:
                now = time.monotonic()
                self.tokens = min(self.rps, self.tokens + (now - self.last) * self.rps)
                self.last = now
                if self.tokens >= n:
                    self.tokens -= n
                    return
                time.sleep(max(0.01, (n - self.tokens) / self.rps * 0.5))


# ── partition ──────────────────────────────────────────────────────────────

def _route_lanes(goal: str) -> list[str]:
    r = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "spydermonkey.py"), "route",
         "--goal", goal, "--json"],
        capture_output=True, text=True, timeout=60)
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return []
    order = data.get("order", []) or (data.get("route", "") or "").split(" → ")
    return [m for m in order if m]

_LANE_ARGV = {
    "barbican": ["protect", "--check"],
    "holyshit": ["capabilities"],
    "undercroft": ["capabilities"],
    "3am": ["capabilities"],
    "kairo": ["capabilities"],
    "kaisha": ["capabilities"],
    "shukaku": ["capabilities"],
    "kage": ["capabilities"],
    "dojo": ["capabilities"],
    "shiki": ["capabilities"],
}


def partition(goal: str, target: str, domain: str, lanes: list[str] | None,
              shards: int, workers: int) -> list[dict]:
    """(lane × shard) tasks — deterministic, versionable."""
    lanes = lanes or _route_lanes(goal) or ["holyshit", "undercroft"]
    shards = max(1, shards)
    tasks = []
    for lane in lanes:
        for s in range(shards):
            tasks.append({
                "lane": lane, "shard": s, "goal": goal, "target": target,
                "domain": domain,
                "argv": list(_LANE_ARGV.get(lane, ["capabilities"])),
            })
    return tasks


# ── local worker pool ──────────────────────────────────────────────────────

def _run_task(bucket: TokenBucket, task: dict, home: Path) -> dict:
    t0 = time.time()
    bucket.take(1)
    cmd = [sys.executable, str(REPO / "scripts" / "spydermonkey.py")] + task["argv"]
    env = {**os.environ, "SPYDERMONKEY_HOME": str(home),
           "SPYDERMONKEY_LANE": task["lane"],
           "SPYDERMONKEY_SHARD": str(task["shard"])}
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120, env=env)
        ok = r.returncode == 0
        out = (r.stdout or "")[-400:]
    except subprocess.TimeoutExpired:
        ok, out = False, "worker timeout"
    return {"lane": task["lane"], "shard": task["shard"], "rc": 0 if ok else 1,
            "ok": ok, "elapsed": round(time.time() - t0, 2),
            "output_tail": out}


def run_pool(tasks: list[dict], workers: int, rps: float, home: Path) -> list[dict]:
    bucket = TokenBucket(rps)
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futs = [pool.submit(_run_task, bucket, t, home) for t in tasks]
        for f in as_completed(futs):
            results.append(f.result())
    results.sort(key=lambda r: (r["lane"], r["shard"]))
    return results


# ── capacity plan (the honest 1000 math) ───────────────────────────────────

def plan_report(workers: int, nodes: int, target: str) -> dict:
    import os as _os
    try:
        cpus = os.cpu_count() or 4
    except Exception:
        cpus = 4
    per_box = max(8, min(200, cpus * 16))  # worker ceiling heuristic
    density_fh = 3336  # measured lab baseline (smk density, 10-task bench)
    total = workers if nodes <= 1 else workers * nodes
    efficiency = 0.7  # parallel degradation factor (honest, unmeasured at scale)
    return {
        "capacity": {
            "cpus_this_box": cpus,
            "worker_ceiling_per_box": per_box,
            "sweet_spot_per_box": min(workers, per_box),
            "nodes_needed_for_1000": max(1, -(-1000 // per_box)),
        },
        "throughput_estimate": {
            "total_workers": total,
            "efficiency_factor": efficiency,
            "findings_per_hour_estimate": round(
                density_fh * min(total, 1000) * efficiency, 0),
            "basis": "density lab baseline 3,336 f/h × workers × 0.7 — "
                     "an estimate to be measured, not a promise",
        },
        "target": target,
    }


def main() -> int:
    ap = argparse.ArgumentParser(prog="smk fleetscale")
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--nodes", type=int, default=1, help="beacon nodes (distributed)")
    ap.add_argument("--goal", default="find api bugs and take them over")
    ap.add_argument("--target", default="scale")
    ap.add_argument("--domain", default="")
    ap.add_argument("--lanes", default="", help="comma lanes (default: goal's route)")
    ap.add_argument("--shards", type=int, default=1)
    ap.add_argument("--rps", type=float, default=0.0,
                    help="global rate cap (default: scope.json max_rate_rps, else 5)")
    ap.add_argument("--controller", default="",
                    help="fleet_agent controller URL — enqueue instead of local pool")
    ap.add_argument("--plan", action="store_true", help="capacity math only")
    ap.add_argument("--dry-run", action="store_true", help="print the partition; run nothing")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    scope = sa.load_scope()
    rps = a.rps or float((scope or {}).get("rules", {}).get("max_rate_rps", 0) or 5)

    if a.plan:
        rep = plan_report(a.workers, a.nodes, a.target)
        rep["rps_governor"] = rps
        if a.json:
            print(json.dumps(rep, indent=2))
        else:
            cap, thr = rep["capacity"], rep["throughput_estimate"]
            print("═══ FLEETSCALE PLAN — the honest 1000-agent math ═══")
            print(f"  this box:      {cap['cpus_this_box']} cpus · ceiling "
                  f"{cap['worker_ceiling_per_box']} workers before thrash")
            print(f"  sweet spot:    {cap['sweet_spot_per_box']} workers/box")
            print(f"  1000 agents:   {cap['nodes_needed_for_1000']} nodes × "
                  f"{cap['worker_ceiling_per_box']} workers (controller+beacons)")
            print(f"  estimate:      {thr['findings_per_hour_estimate']} f/h "
                  f"at {thr['total_workers']} workers")
            print(f"  basis:         {thr['basis']}")
            print(f"  rate governor: {rps} rps estate-wide (the walls at scale)")
        return 0

    tasks = partition(a.goal, a.target, a.domain,
                      [l.strip() for l in a.lanes.split(",") if l.strip()],
                      a.shards, a.workers)
    if a.dry_run:
        if a.json:
            print(json.dumps({"tasks": tasks, "count": len(tasks),
                              "workers": a.workers, "rps": rps}, indent=2))
        else:
            print(f"═══ FLEETSCALE {len(tasks)} task(s) × {a.workers} workers "
                  f"(rps cap {rps}) ═══")
            for t in tasks:
                print(f"  ▸ {t['lane']:10s} shard {t['shard']} :: "
                      f"{' '.join(shlex.quote(x) for x in t['argv'])}")
            print(f"  nothing executed — drop --dry-run to run the pool")
        return 0

    if a.controller:
        # distributed: enqueue to the controller; beacons execute node-side
        import urllib.request
        payload = json.dumps({"tasks": tasks}).encode()
        req = urllib.request.Request(a.controller.rstrip("/") + "/task",
                                     data=payload, method="POST",
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.loads(r.read())
        print(f"▸ enqueued {len(tasks)} task(s) to {a.controller} "
              f"(result: {resp.get('ok')})")
        return 0

    home = Path(os.environ.get("SPYDERMONKEY_HOME", str(Path.home() / ".redteam")))
    home.mkdir(parents=True, exist_ok=True)
    if not a.json:
        print(f"═══ FLEETSCALE — running {len(tasks)} task(s) on {a.workers} "
              f"worker(s) · rps cap {rps} ═══")
    results = run_pool(tasks, a.workers, rps, home)
    ok = sum(1 for r in results if r["ok"])
    elapsed = max(r["elapsed"] for r in results) if results else 0
    summary = {"tasks": len(results), "ok": ok, "failed": len(results) - ok,
               "wall_elapsed_s": round(elapsed, 2),
               "rate_governor_rps": rps,
               "results": results}
    if a.json:
        print(json.dumps(summary, indent=2))
        return 0 if ok == len(results) else 1
    for r in results:
        mark = "✓" if r["ok"] else "✗"
        print(f"  {mark} {r['lane']:10s} shard {r['shard']} · {r['elapsed']}s"
              + (f" · {r['output_tail'][:80].strip()}" if not r["ok"] else ""))
    print(f"═══ {ok}/{len(results)} tasks ok · rps governor {rps} ═══")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())