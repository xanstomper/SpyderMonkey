# Third-Party Audit Package — reviewer onboarding

This package is the machine half of the review, packaged FOR the human half.
An independent reviewer should be able to start here and spend their time on
the security-relevant core, not on repo archaeology.

## What this package contains

- `scripts/product_audit.py` — the automated gate (ASTSEC/SECRET/STATE/PERMS/
  LEAK/LOCK). Run: `python3 scripts/product_audit.py --report`. Last run:
  0 findings, 0 HIGH.
- `SECURITY.md` — the threat model: enforcement chain, the walls, release
  posture, residual risks.
- `scripts/version_audit.py` + `scripts/leakscan.py` — release triad
  companions (version homes; engagement-marker scan).
- `references/audit-report.md` — regeneration target of the audit (the
  findings file, refreshed with --report).
- `references/activation-proof.md` — the takeover chain verified end-to-end
  (coherence sweep, P0 walk, live agent activation transcript).

## Suggested review order (highest-value first)

1. **`scripts/scope_authority.py`** — the single estate verdict. Everything
   that touches a live target passes through it; a defect here is a defect in
   every engine. Check: matching semantics, deny precedence, expiry, atomic
   writes (0600 tmp+rename), audit.
2. **`scripts/scope_gateway.py`** — transport enforcement. Check: CONNECT
   tunnel correctness, host parsing edge cases (IDN? ports? userinfo?),
   audit logging, the netdist generator.
3. **`scripts/claude_hook_scope.py` / `claude_hook_sessionstart.py`** — the
   host-level gates. Check: marker detection bypasses, exit-code semantics,
   feedback leakage.
4. **`references/mandate-session.md`** (SM8.3) — the contract: de-injection
   resistance, release ritual, walls integrity.
5. **`scripts/fleet_agent.py` + `scripts/fleet_scale.py`** — the distributed
   path: HMAC task signatures, node scope gating, the rate governor, result
   verification.
6. **`scripts/arsenal.py`** — the acquisition lane (the `_TOOL_NAME_RE` gate
   and the shell=True reviewed site, marked `product-audit: reviewed`).

## The standing questions we want answered

- Are there paths where a retrieved-content directive (web/file/tool output)
  can become an instruction to a live probe? (The contract declares
  data-vs-directive; verify no engine actually executes retrieved strings.)
- Can any engine bypass `scope_authority.check` on a live path?
- Is the HMAC fleet channel sound against replay/mutation?
- Does the release pipeline (cigate) actually block a leaking or
  version-drifted tree?

## Honest scope of THIS package

The machine audit is a static scan with self-review markings; it is not a
substitute for a human reading the code. This package exists to make that
human read fast. Findings land in `references/audit-report.md`; fixes land
with `product-audit: reviewed <date> — why` markers at the call sites.