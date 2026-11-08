#!/usr/bin/env python3
"""SpyderMonkey model router — per-lane model orchestration.

`smk model list|set|resolve` — the config that lets different lanes ride
different providers/models (XBOW-style orchestration, self-hosted):
  smk model set lane=holyshit provider=vyceai model=glm-5.3-flash
  smk model resolve --lane undercroft   → provider/model for scripting
Store: ~/.redteam/models.json (0600). The agent launcher and fleet lanes
read `resolve` when composing their drivers; unset lanes fall back to the
operator's default provider.
"""

import argparse
import json
import os
import sys
from pathlib import Path

CONFIG = Path(os.environ.get("SPYDERMONKEY_HOME",
                             str(Path.home() / ".redteam"))) / "models.json"

DEFAULT_LANES = ("barbican", "holyshit", "undercroft", "3am", "kairo",
                 "kaisha", "shukaku", "kage", "dojo", "shiki", "default")


def _load() -> dict:
    if CONFIG.exists():
        try:
            return json.loads(CONFIG.read_text())
        except json.JSONDecodeError:
            pass
    return {}


def _save(cfg: dict) -> None:
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    CONFIG.write_text(json.dumps(cfg, indent=2) + "\n")
    try:
        CONFIG.chmod(0o600)
    except OSError:
        pass


def main() -> int:
    ap = argparse.ArgumentParser(prog="smk model")
    sub = ap.add_subparsers(dest="action", required=True)
    sub.add_parser("list")
    ap_set = sub.add_parser("set")
    ap_set.add_argument("--lane", required=True)
    ap_set.add_argument("--provider", required=True)
    ap_set.add_argument("--model", required=True)
    ap_res = sub.add_parser("resolve")
    ap_res.add_argument("--lane", default="default")
    ap_res.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cfg = _load()

    if a.action == "set":
        if a.lane not in DEFAULT_LANES:
            print(f"✗ unknown lane '{a.lane}' (lanes: {', '.join(DEFAULT_LANES)})",
                  file=sys.stderr)
            return 1
        cfg[a.lane] = {"provider": a.provider, "model": a.model}
        _save(cfg)
        print(f"⚙ model: {a.lane} → {a.provider}/{a.model}")
        return 0

    if a.action == "list":
        for lane, m in sorted(cfg.items()):
            print(f"  {lane:12s} {m['provider']}/{m['model']}")
        return 0

    if a.action == "resolve":
        entry = cfg.get(a.lane) or cfg.get("default", {})
        if a.json:
            print(json.dumps({"lane": a.lane, "provider": entry.get("provider", ""),
                              "model": entry.get("model", "")}))
        else:
            print(f"{entry.get('provider', '')}/{entry.get('model', '')}")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())