#!/usr/bin/env python3
"""SpyderMonkey industrial ops tools: density harness + ticket interface.

density — the finding-density scorecard. Runs the family's real benches
(bench_live exploit level, optional --suite route level) against lab targets
and reports the numbers that matter for "raw finding power": confirmed
findings, accuracy, findings-per-hour, coverage. Any claim about density
starts from this file — measured, never vibed.

ticket — the industrial interface. Pushes CONFIRMED ledger rows to issue
trackers (GitHub via gh CLI today; Jira via API when creds are configured).
`--dry-run` previews; nothing is created without the operator's hand on it.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


# ── density ────────────────────────────────────────────────────────────────

def _density_map() -> dict:
    return {
        "live": "scripts/bench_live.py",
        "suite": "scripts/bench_public.py",
    }


def cmd_density(args) -> int:
    start = time.time()
    kind = args.bench or "live"
    script = REPO / _density_map()[kind]
    if not script.exists():
        print(f"✗ bench script missing: {script}", file=sys.stderr)
        return 1
    if args.json:
        body = {"kind": kind, "elapsed_s": None, "error": None}
    run = subprocess.run(
        [sys.executable, str(script)] + (["--suite", args.suite] if args.suite else [])
        + ["--json"],
        capture_output=True, text=True, timeout=args.timeout)
    elapsed = time.time() - start
    try:
        out = json.loads(run.stdout)
    except json.JSONDecodeError as e:
        if args.json:
            _emit(args, {"kind": kind, "ok": False,
                         "error": f"bench produced no JSON: {e}",
                         "stderr_tail": run.stderr[-500:]})
        else:
            print(f"✗ density: bench produced no JSON ({e})")
            print(run.stderr[-500:])
        return 1
    passed = out.get("passed", 0)
    total = out.get("total", 0)
    accuracy = out.get("accuracy", 0.0)
    per_hour = round((passed / max(elapsed / 3600.0, 1e-9)), 2)
    scorecard = {
        "kind": kind,
        "bench": out.get("version", "?"),
        "confirmed": passed, "total": total, "accuracy": accuracy,
        "elapsed_s": round(elapsed, 1),
        "findings_per_hour": per_hour,
        "engine": out.get("engine"),
        "ok": out.get("ok", False),
        "checks": out.get("checks", []),
    }
    if args.json:
        _emit(args, scorecard)
        return 0
    print("═══ SPYDERMONKEY DENSITY SCORECARD ═══")
    print(f"  bench:       {kind} ({scorecard['bench']})")
    print(f"  confirmed:   {passed}/{total} · accuracy {accuracy}%")
    print(f"  throughput:  {per_hour} findings/hour (measured, lab)")
    print(f"  elapsed:     {elapsed:.1f}s · engine {out.get('engine')}")
    print(f"  verdict:     {'PASS' if out.get('ok') else 'FAIL'}")
    return 0 if out.get("ok") else 1


# ── ticket ─────────────────────────────────────────────────────────────────

def _ledger_rows(target: str) -> list[dict]:
    p = REPO.parent.parent  # not used; real path from SPYDERMONKEY_HOME
    import os
    home = Path(os.environ.get("SPYDERMONKEY_HOME", Path.home() / ".redteam"))
    lp = home / "campaigns" / target / "ledger.jsonl"
    if not lp.exists():
        return []
    rows = []
    for line in lp.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def _ticket_body(row: dict) -> str:
    ev = row.get("evidence") or {}
    lines = [
        f"**SPY-{row.get('id', '?')}** — {row.get('title', 'untitled')}",
        f"- asset: `{row.get('asset', '?')}`",
        f"- class: {row.get('class', '?')} · severity: {row.get('severity', '?')}",
        f"- status: {row.get('status', '?')} (evidence-gated)",
    ]
    for k in ("baseline", "attack", "diff"):
        if ev.get(k):
            lines.append(f"- {k}: `{ev[k][:400]}`")
    lines.append("") 
    lines.append("_auto-filed by SpyderMonkey ticket · verify before triage_")
    return "\n".join(lines)


def cmd_ticket(args) -> int:
    rows = _ledger_rows(args.target)
    confirmed = [r for r in rows if r.get("status") == "CONFIRMED"]
    if not confirmed:
        print(f"✗ no CONFIRMED ledger rows for '{args.target}' "
              f"({len(rows)} total rows)")
        return 1
    if args.json:
        _emit(args, {"target": args.target, "confirmed": len(confirmed),
                     "dry_run": bool(args.dry_run),
                     "tickets": [{k: r.get(k) for k in ("id", "title", "asset",
                                                        "severity", "class")}
                                 for r in confirmed]})
        return 0
    print(f"═══ TICKET — {args.target} · {len(confirmed)} confirmed finding(s) "
          f"({'DRY RUN' if args.dry_run else 'LIVE'}) ═══")
    for r in confirmed:
        title = f"[SPY-{r.get('id')}] {r.get('title')} ({r.get('asset')})"
        print(f"  • {title}")
        if args.dry_run:
            continue
        if args.provider == "gh":
            body = _ticket_body(r)
            cmd = ["gh", "issue", "create", "--title", title, "--body", body]
            if args.repo:
                cmd += ["--repo", args.repo]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if res.returncode == 0:
                print(f"    → {res.stdout.strip()}")
            else:
                print(f"    ✗ gh failed: {res.stderr.strip()[:300]}", file=sys.stderr)
        elif args.provider == "jira":
            jurl = os.environ.get("JIRA_URL", "").rstrip("/")
            jtok = os.environ.get("JIRA_TOKEN", "")
            jproj = os.environ.get("JIRA_PROJECT", "")
            if not (jurl and jtok and jproj):
                print("✗ Jira not configured — set JIRA_URL, JIRA_TOKEN, "
                      "JIRA_PROJECT", file=sys.stderr)
                return 1
            import urllib.request
            body = {
                "fields": {
                    "project": {"key": jproj},
                    "summary": title,
                    "description": _ticket_body(r),
                    "issuetype": {"name": "Bug"},
                }
            }
            req = urllib.request.Request(
                f"{jurl}/rest/api/2/issue",
                data=json.dumps(body).encode(),
                method="POST",
                headers={"Content-Type": "application/json",
                         "Authorization": f"Bearer {jtok}"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                created = json.loads(resp.read())
            print(f"    → {jurl}/browse/{created.get('key', '?')}")
    return 0


def _emit(args, payload: dict) -> None:
    print(json.dumps(payload, indent=2))


def main() -> int:
    ap = argparse.ArgumentParser(prog="smk ops")
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("density")
    d.add_argument("--bench", choices=("live", "suite"), default="live")
    d.add_argument("--suite", help="suite file for --bench suite")
    d.add_argument("--timeout", type=int, default=600)
    d.add_argument("--json", action="store_true")

    t = sub.add_parser("ticket")
    t.add_argument("push", nargs="?", default="push")
    t.add_argument("--target", required=True)
    t.add_argument("--provider", choices=("gh", "jira"), default="gh")
    t.add_argument("--repo", help="gh: target repo (default: repo owning gh auth)")
    t.add_argument("--dry-run", action="store_true")
    t.add_argument("--json", action="store_true")

    a = ap.parse_args()
    if a.cmd == "density":
        return cmd_density(a)
    if a.cmd == "ticket":
        return cmd_ticket(a)
    return 2


if __name__ == "__main__":
    sys.exit(main())