#!/usr/bin/env python3
"""SpyderMonkey version audit — semver discipline.

Every version home must agree: the four engine VERSION constants, the SKILL.md
frontmatter, and the README badge. `--tag` additionally requires the current
git tag to equal the version (`v8.0.0`). rc=1 on any mismatch. Wired into
`verify` so drift fails the gate.
"""

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

HOMES = {
    "scripts/spydermonkey.py": r'^VERSION = "([^"]+)"',
    "scripts/arsenal.py": r'^VERSION = "([^"]+)"',
    "scripts/mcp_server.py": r'^VERSION = "([^"]+)"',
    "scripts/catalog_materialize.py": r'^VERSION = "([^"]+)"',
    "SKILL.md": r"^version: (.+)$",
    "README.md": r"version-([0-9.]+)-blueviolet",
}


def main() -> int:
    found = {}
    bad = []
    for rel, pat in HOMES.items():
        p = REPO / rel
        if not p.exists():
            bad.append(f"{rel}: MISSING")
            continue
        m = re.search(pat, p.read_text(encoding="utf-8"), re.M)
        if not m:
            bad.append(f"{rel}: version pattern not found")
            continue
        found[rel] = m.group(1).strip()
    if not found:
        print("✗ no version homes found", file=sys.stderr)
        return 1
    vals = set(found.values())
    if len(vals) != 1:
        bad.append(f"DISAGREE: {found}")
    version = found.get("scripts/spydermonkey.py", next(iter(found.values())))
    if "--tag" in sys.argv[1:]:
        tag = subprocess.run(["git", "-C", str(REPO), "describe", "--tags",
                              "--exact-match"], capture_output=True, text=True)
        cur = tag.stdout.strip() if tag.returncode == 0 else "(no tag)"
        if cur != f"v{version}":
            bad.append(f"tag mismatch: git={cur} version=v{version}")
    if bad:
        print(f"✗ VERSION AUDIT FAILED — {version}")
        for b in bad:
            print(f"    {b}")
        return 1
    print(f"✓ VERSION AUDIT OK — v{version} in "
          f"{len(found)}/{len(HOMES)} homes" + (" + tag" if "--tag" in sys.argv[1:] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())