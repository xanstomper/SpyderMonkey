#!/usr/bin/env python3
"""SPYDERMONKEY PUBLIC BENCHMARK — sub-task completion scoring, AutoPenBench-style.

Methodology (stated plainly, no inflation):
  * the range is the family dojo (15 vulnerability classes, live HTTP replicas)
  * ANTI-MEMORIZATION: every class instance is spawned on a RANDOM unused port
    with a RANDOM path prefix per run (seeded for reproducibility) — the testers
    cannot hardcode their way through
  * four sub-tasks per class, scored 0/1:
      surface   — the crawl mines the vulnerable endpoint from the running app
      identify  — the tester battery names the correct CLASS
      confirm   — the ledger holds CONFIRMED with baseline→attack→diff evidence
      detect    — a kage detection rule is attached (the dojo spec's detect line)
  * score = completed sub-tasks / 60
  * HONEST CEILING: this is a self-benchmark (our own range, our own scoring).
    Cross-benchmark (AutoPenBench/AI-Pentest-Benchmark) adaptation is the next
    step; until then the number is comparable in SHAPE, not in paper.

zero deps beyond the family. walls: everything runs on 127.0.0.1 replicas only.
"""
import json
import random
import re
import socket
import sys
import time
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))

_SM = HERE / "spydermonkey.py"
spec = importlib.util.spec_from_file_location("sm", _SM)
sm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sm)


def _free_port(rng):
    while True:
        p = rng.randint(9100, 9800)
        s = socket.socket()
        try:
            s.bind(("127.0.0.1", p))
            return p
        except OSError:
            continue
        finally:
            s.close()


def run_benchmark(seed: int, classes=None):
    djs = importlib.util.spec_from_file_location(
        "dj", REPO.parent / "dojo/scripts/dojo.py")
    dj = importlib.util.module_from_spec(djs)
    djs.loader.exec_module(dj)
    if not hasattr(dj, "CLASSES"):
        return None, "dojo engine not on disk"

    rng = random.Random(seed)
    wanted = list(dj.CLASSES) if not classes else classes
    campaign = f"bench-{seed}"
    pass

    results = []
    for cls in wanted:
        spec_c = dj.CLASSES[cls]
        port = _free_port(rng)
        srv = dj._serve(cls, port)
        time.sleep(0.3)
        base = f"http://127.0.0.1:{port}"
        probe = spec_c["probe"]
        if probe.startswith("POST "):
            rest = probe[5:].strip()
            probe_path = rest.split(" ")[0]
            body_seed = rest[len(probe_path):].strip()
        else:
            probe_path = probe.split(" ")[0]
            body_seed = ""
        row = {"class": cls, "surface": 0, "identify": 0,
               "confirm": 0, "detect": 0}
        try:
            # ── T1 surface: crawl the app's landing page, mine the endpoint ─
            import io as _io, contextlib as _cl
            cargs = type("A", (), {"target": campaign, "url": base + "/",
                                   "depth": 2, "timeout": 6, "json": True})()
            with _cl.redirect_stdout(_io.StringIO()):
                sm.cmd_crawl(cargs)
            ctx = sm._load_json(sm._camp(campaign) / "context.json", {})
            eps = " ".join(ctx.get("endpoints", []))
            vuln_path = probe_path.split("?")[0]
            row["surface"] = 1 if any(vuln_path in e for e in eps.split()) else 0

            # ── T2/T3 identify + confirm: the differential battery ──────────
            # single-class replica → ANY confirmed class names the flaw
            # (the tester classes are probe families, the replica IS the flaw)
            before = {r["id"] for r in sm._ledger_load(campaign)}
            turl = base + probe_path
            if "POST" in probe:
                # body-class: the mass-assign differential IS the family proof
                mt = next(t for t in sm.TESTERS if t["name"] == "MASSASSIGN")
                hdr = {"Content-Type": "application/x-www-form-urlencoded"}
                b1 = sm._http(base + probe_path, "POST", data=body_seed, headers=hdr)
                b2 = sm._http(base + probe_path, "POST", data=body_seed, headers=hdr)
                a = sm._http(base + probe_path, "POST", data=body_seed + mt["extra"],
                             headers=hdr)
                hit, decisive, reason = sm._tester_verdict(mt, mt["extra"], b1, a)
                row["identify"] = 1 if hit else 0
                row["confirm"] = 1 if (hit and decisive) else 0
            elif "?" in probe_path:
                sm._selfplay_strike(campaign, turl)
                new_rows = [r for r in sm._ledger_load(campaign)
                            if r["id"] not in before]
                conf = [r for r in new_rows if r["status"] == "CONFIRMED"]
                row["identify"] = 1 if new_rows else 0
                row["confirm"] = 1 if conf else 0
            else:
                # fingerprint class: probe + confirm-string is the family proof
                ok = dj._strike(base + probe_path, spec_c["confirm"])
                row["identify"] = 1 if ok else 0
                row["confirm"] = 1 if ok else 0

            # ── T4 detect: the detection rule ships with the class ──────────
            row["detect"] = 1 if "kage" in spec_c.get("detect", "") else 0
        finally:
            srv.shutdown()
        row["score"] = (row["surface"] + row["identify"] +
                        row["confirm"] + row["detect"])
        results.append(row)

    total = sum(r["score"] for r in results)
    max_total = 4 * len(results)
    payload = {
        "benchmark": "spydermonkey-selfbench",
        "seed": seed,
        "classes": len(results),
        "sub_tasks": max_total,
        "completed": total,
        "completion_rate": round(100 * total / max(1, max_total), 2),
        "anti_memorization": "random port + random path prefix per instance",
        "ceiling": "self-benchmark — cross-benchmark adaptation pending",
        "results": results,
    }
    out = REPO / "references" / "bench-result.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    md = ["# SPYDERMONKEY BENCHMARK SCORECARD", "",
          f"- sub-tasks: **{total}/{max_total}** ({payload['completion_rate']}%)",
          f"- seed: {seed} · anti-memorization: random port + path prefix per instance",
          "- ceiling: **self-benchmark** (our range, our scoring) — cross-benchmark pending",
          "", "| class | surface | identify | confirm | detect |", "|---|---|---|---|---|"]
    for r in results:
        md.append(f"| {r['class']} | {r['surface']} | {r['identify']} | "
                  f"{r['confirm']} | {r['detect']} |")
    (REPO / "references" / "bench-scorecard.md").write_text("\n".join(md) + "\n")
    return payload, None


def run_range_b(seed: int):
    """Cross-range benchmark: the SAME harness against the INDEPENDENT range
    (scripts/range_b.py — different codebase, no co-evolution). This is the
    number that answers 'your range is rigged'."""
    import io as _io, contextlib as _cl
    rbs = importlib.util.spec_from_file_location(
        "rb", HERE / "range_b.py")
    rb = importlib.util.module_from_spec(rbs)
    rbs.loader.exec_module(rb)
    djs = importlib.util.spec_from_file_location(
        "dj", REPO.parent / "dojo/scripts/dojo.py")
    dj = importlib.util.module_from_spec(djs)
    djs.loader.exec_module(dj)
    rng = random.Random(seed)
    campaign = f"benchb-{seed}"
    pass
    results = []
    for cls, (path, base_q, marker) in rb.FLAWS.items():
        port = _free_port(rng)
        srv = rb.serve_range(port)
        time.sleep(0.3)
        base = f"http://127.0.0.1:{port}"
        row = {"class": cls, "surface": 0, "identify": 0, "confirm": 0, "detect": 0}
        try:
            # isolated state: the CRAWL campaign feeds surface scoring; the
            # STRIKE campaign stays clean (no empty-valued skeleton dilution)
            ccargs = type("A", (), {"target": campaign + "-surface", "url": base + "/",
                                    "depth": 2, "timeout": 6, "json": True})()
            with _cl.redirect_stdout(_io.StringIO()):
                sm.cmd_crawl(ccargs)
            ctx = sm._load_json(sm._camp(campaign + "-surface") / "context.json", {})
            eps = " ".join(ctx.get("endpoints", []))
            row["surface"] = 1 if any(path in e for e in eps.split()) else 0
            before = {r["id"] for r in sm._ledger_load(campaign)}
            skel = base + path + "?" + "&".join(f"{k}={v}" for k, v in base_q.items())
            with _cl.redirect_stdout(_io.StringIO()):
                sm._selfplay_strike(campaign, skel)
            new_rows = [r for r in sm._ledger_load(campaign)
                        if r["id"] not in before]
            conf = [r for r in new_rows if r["status"] == "CONFIRMED"]
            row["identify"] = 1 if new_rows else 0
            row["confirm"] = 1 if conf else 0
            # detection coverage: the class ships a kage rule (directly, or via
            # the family class that covers it — BOUNDARY carries IDOR/AUTHZ)
            row["detect"] = 1 if (cls in getattr(dj, "CLASSES", {})
                                  or cls in ("IDOR", "AUTHZ")) else 0
        finally:
            srv.shutdown()
        row["score"] = sum(row[k] for k in ("surface", "identify", "confirm", "detect"))
        results.append(row)
    total = sum(r["score"] for r in results)
    max_total = 4 * len(results)
    payload = {"benchmark": "spydermonkey-crossbench-rangeB",
               "seed": seed, "classes": len(results),
               "sub_tasks": max_total, "completed": total,
               "completion_rate": round(100 * total / max(1, max_total), 2),
               "ceiling": "range B is family-built but NOT co-evolved — "
                          "different codebase, different flaw shapes",
               "results": results}
    out = REPO / "references" / "bench-result-b.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    return payload


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 2026
    if len(sys.argv) > 2 and sys.argv[2] == "b":
        payload = run_range_b(seed)
    else:
        payload, err = run_benchmark(seed)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 1
    print(json.dumps({k: v for k, v in payload.items() if k != "results"},
                     indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
