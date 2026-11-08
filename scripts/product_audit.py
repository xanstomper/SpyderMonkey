#!/usr/bin/env python3
"""SpyderMonkey product audit — automated static review, product-readiness gate.

`./scripts/product_audit.py [--report]` — scans the tracked tree for the
offensive-tooling bug classes that matter for shipping:

  ASTSEC   code injection: os.system / shell=True / eval / exec / pickle
  SECRET   hardcoded credentials or token-like strings in tracked files
  STATE    state-file handling: world-writable open() on estate paths,
           non-atomic writes on scope.json
  PERMS    installer/scripts without exec bits (packaging)
  LEAK     engagement-marker scan (leakscan)
  LOCK     version-audit + jail integration (the release triad)

HIGH findings → rc=1 (the release gate refuses). `--report` writes
references/audit-report.md with findings + residual-risk notes.

Honest scope: automated + self-review. A third-party human audit remains on
the residual-risk list — this file is the machine half of that review.
"""

import ast
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FINDINGS: list[dict] = []


def _f(sev: str, cat: str, loc: str, msg: str) -> None:
    FINDINGS.append({"severity": sev, "category": cat, "location": loc, "message": msg})


def _reviewed_ok(py: Path, node: ast.AST) -> bool:
    """True when the call site carries the reviewed marker (audit trail).

    Convention: `# product-audit: reviewed <date> — <why>` in the enclosing
    function body. A future edit that removes the marker re-flags the site.
    """
    try:
        lines = py.read_text(encoding="utf-8").splitlines()
        parent = None
        for n in ast.walk(ast.parse(py.read_text(encoding="utf-8"))):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                    and n.lineno <= node.lineno <= getattr(n, "end_lineno", node.lineno):
                parent = n
        if parent is None:
            return False
        for i in range(parent.lineno - 1, min(node.lineno + 2, len(lines))):
            if "product-audit: reviewed" in lines[i]:
                return True
    except Exception:
        return False
    return False


def audit_astsec() -> None:
    for py in sorted((REPO / "scripts").glob("*.py")):
        try:
            tree = ast.parse(py.read_text(encoding="utf-8"))
        except SyntaxError:
            _f("HIGH", "ASTSEC", str(py), "unparseable python")
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                fn = node.func
                name = getattr(fn, "id", None) or getattr(fn, "attr", None)
                if name == "system" and _reviewed_ok(py, node):
                    continue
                if name in ("system", "popen", "eval", "exec"):
                    _f("HIGH", "ASTSEC", f"{py}:{node.lineno}",
                       f"{name}() used — verify no untrusted interpolation")
                if name == "run" and node.args:
                    kw = {k.arg: k for k in node.keywords}
                    shell = kw.get("shell")
                    if shell and getattr(shell.value, "value", None) is True:
                        if _reviewed_ok(py, node):
                            continue
                        _f("HIGH", "ASTSEC", f"{py}:{node.lineno}",
                           "subprocess shell=True — verify command is static")
            if isinstance(node, ast.Import) and any(
                    a.name == "pickle" for a in node.names):
                _f("MED", "ASTSEC", f"{py}:{node.lineno}",
                   "pickle imported — never unpickle untrusted data")


def audit_secret() -> None:
    pats = [
        (r"\b(sk-[A-Za-z0-9]{16,})\b", "openai-style key"),
        (r"\b(ghp_[A-Za-z0-9]{20,})\b", "github token"),
        (r"password\s*=\s*['\"][^'\"]{6,}", "password literal"),
        (r"api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{12,}", "api key literal"),
    ]
    for f in sorted(REPO.rglob("*")):
        if not f.is_file() or ".git" in f.parts or "references/skills" in f.parts \
                or f.suffix in (".pyc", ".json", ".png", ".gif"):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for pat, what in pats:
            for m in re.finditer(pat, text):
                _f("HIGH" if what != "password literal" else "MED", "SECRET",
                   str(f), f"{what}: {m.group(0)[:12]}…")
                break


def audit_state() -> None:
    sa = (REPO / "scripts" / "scope_authority.py").read_text(encoding="utf-8")
    if "os.replace" not in sa and ".tmp" not in sa:
        _f("HIGH", "STATE", "scripts/scope_authority.py",
           "no atomic write (os.replace/tmp) visible — scope.json must never be torn")
    if "0o600" not in sa and "600" not in sa:
        _f("MED", "STATE", "scripts/scope_authority.py",
           "no 0600 permission handling visible on scope.json")
    for py in sorted((REPO / "scripts").glob("*.py")):
        text = py.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"open\(([^,)]*),\s*['\"]w", text):
            if "redteam" in text[max(0, m.start() - 300):m.start() + 300] or "scope" in m.group(1):
                _f("MED", "STATE", f"{py}:{text[:m.start()].count(chr(10)) + 1}",
                   "direct write open() on state-adjacent path — prefer atomic tmp+rename")


def audit_perms() -> None:
    for s in ("scripts/install.sh", "scripts/release.sh",
              "scripts/spydermonkey.py", "scripts/scope_gateway.py"):
        p = REPO / s
        if p.exists() and not (p.stat().st_mode & 0o111):
            _f("MED", "PERMS", s, "missing exec bit (packaging)")


def audit_links() -> None:
    va = subprocess.run([sys.executable, str(REPO / "scripts" / "version_audit.py")],
                        capture_output=True, text=True)
    if va.returncode != 0:
        _f("HIGH", "LOCK", "scripts/version_audit.py", va.stdout.strip())
    ls = subprocess.run([sys.executable, str(REPO / "scripts" / "leakscan.py")],
                        capture_output=True, text=True, timeout=600)
    if "worktree clean" not in ls.stdout + ls.stderr:
        _f("HIGH", "LOCK", "leakscan", "engagement markers in tracked files — release blocked")


def main() -> int:
    audit_astsec()
    audit_secret()
    audit_state()
    audit_perms()
    audit_links()
    highs = [f for f in FINDINGS if f["severity"] == "HIGH"]
    print(f"═══ SPYDERMONKEY PRODUCT AUDIT — {len(FINDINGS)} finding(s) "
          f"({len(highs)} HIGH) ═══")
    for f in FINDINGS:
        print(f"  [{f['severity']:4s}] {f['category']} {f['location']}: {f['message']}")
    if "--report" in sys.argv[1:]:
        lines = ["# Product Audit Report — generated by scripts/product_audit.py",
                 "",
                 f"Findings: {len(FINDINGS)} ({len(highs)} HIGH) · "
                 "auto + self-review, machine half of the review.",
                 ""]
        for f in FINDINGS:
            lines.append(f"- **{f['severity']}** {f['category']} `{f['location']}`: {f['message']}")
        lines += [
            "",
            "## Residual risks (not closed by automation)",
            "- Independent third-party human audit: NOT DONE — the remaining half.",
            "- Container/kernel sandboxing of probe execution: opt-in netdist only.",
            "- Model-provider trust: the family rides operator-chosen providers.",
            "- Legal/abuse posture: deliberately absent (zero-document doctrine).",
        ]
        (REPO / "references" / "audit-report.md").write_text("\n".join(lines) + "\n",
                                                             encoding="utf-8")
        print(f"  report → references/audit-report.md")
    return 1 if highs else 0


if __name__ == "__main__":
    sys.exit(main())