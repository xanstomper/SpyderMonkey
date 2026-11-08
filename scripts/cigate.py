#!/usr/bin/env python3
"""SpyderMonkey CI gate — every code delta tested, machine-gated.

`smk cigate [--fast]` runs the release triad + the suite and exits non-zero
on any failure: version audit → product audit → leakscan → jail check →
test suite. Wire it into ANY pipeline (GitHub Actions, pre-commit, cron,
a developer's fingers) with one command. `--install-precommit` writes a
`.git/hooks/pre-commit` for THIS repo (opt-in — the hook gates every
commit once installed; operator decides).
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _run(name: str, argv: list[str], timeout: int = 900) -> bool:
    print(f"── {name} ", flush=True)
    r = subprocess.run([sys.executable] + argv, cwd=REPO,
                       capture_output=True, text=True, timeout=timeout)
    tail = (r.stdout or "")[-400:] + (r.stderr or "")[-200:]
    print(f"   {'✓' if r.returncode == 0 else '✗'} {tail.strip().splitlines()[-1] if tail.strip() else ''}")
    return r.returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="smk cigate")
    ap.add_argument("--fast", action="store_true",
                    help="skip the full suite; run the release triad only")
    ap.add_argument("--install-precommit", action="store_true")
    a = ap.parse_args()

    if a.install_precommit:
        hook = REPO / ".git" / "hooks" / "pre-commit"
        hook.parent.mkdir(parents=True, exist_ok=True)
        hook.write_text(
            "#!/bin/bash\n# SpyderMonkey CI gate — every commit gated.\n"
            "exec python3 scripts/cigate.py --fast\n", encoding="utf-8")
        hook.chmod(0o755)
        print(f"⚙ pre-commit hook installed: {hook}")
        print("  (this gates every commit in THIS repo — remove the file to disarm)")
        return 0

    gates = [
        ("version audit", ["scripts/version_audit.py"]),
        ("product audit", ["scripts/product_audit.py"]),
        ("leakscan", ["scripts/leakscan.py"]),
        ("jail check", [str(REPO / "scripts" / "jail_security.py"), "check"]),
    ]
    results = [(n, _run(n, argv)) for n, argv in gates]
    if not a.fast:
        results.append(("test suite",
                        _run("test suite", ["-m", "unittest", "discover",
                                            "-s", "tests"], timeout=900)))
    ok = all(r for _, r in results)
    print(f"═══ CI GATE {'PASS' if ok else 'FAIL'} ═══")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())