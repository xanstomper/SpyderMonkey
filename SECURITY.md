# Security — SpyderMonkey offensive-security family

The family's security model is the product: every engine, hook, and gate
exists to keep authorized work authorized and everything else impossible.

## The enforcement chain (defense in depth)

1. **Contract** — the session mandate (SM8.3) declares identity fusion,
   directive hierarchy (walls > contract > operator > defaults), de-injection
   resistance (retrieved content is data, never directives), and the exact
   release ritual.
2. **Ambient** — AGENTS.md auto-loaded in campaign dirs; the
   `.spydermonkey-active` marker arms host gates; `campaign init` deploys it.
3. **Mechanical (host)** — Claude Code hooks: SessionStart injects the brief;
   PreToolUse blocks out-of-estate connective commands at the host. A prompt
   cannot override a hook; only scope.json can.
4. **Transport** — `smk gateway`: every proxied egress is scope-checked
   before it leaves the box (403 + audit). `netdist`: nftables egress
   ruleset generator for kernel-depth enforcement (opt-in).
5. **Jail** — `smk jail`: SHA-256 baseline of the contracts, hooks, settings,
   and carriers; tamper/removal → rc=1; `watch --restore` (opt-in).

## The walls (absolute, across every layer)

Declared estates only · documented-PoC adaptation · validation-only, NO-GAIN,
reversible, no persistence · never social, never third parties · zero
documents · destructive end-states refused once, pivoted to disclosure.

## Release posture

- `scripts/version_audit.py` — all version homes must agree; wired into
  `verify`.
- `scripts/product_audit.py` — static review (ASTSEC/SECRET/STATE/PERMS/LEAK/
  LOCK); HIGH findings block the release (rc=1). Reviewed call sites carry an
  inline `# product-audit: reviewed <date> — why` marker.
- `scripts/release.sh` — refuses dirty trees; ships tarball + sha256
  manifest (SBOM-lite); `--tag` signs/tags the version.
- `scripts/leakscan.py` — engagement markers × every tracked file; rc=1 on
  any hit.

## Known residual risks (honest ceilings)

- **No third-party human audit yet** — the machine audit is one half;
  independent review is the remaining half.
- Operator-model trust: the family rides the operator's chosen providers.
- The scope hook inspects command tokens of *gated* sessions; tools that
  bypass the session (outside Claude/OpenCode) are covered by gateway +
  netdist when enabled.
- `smk ticket` pushes findings to issue trackers — operator-invoked only.

## Reporting

Findings, suspected gate bypasses, or audit gaps: open an issue on the repo
or raise it through the operator. The walls are the product — a wall that
fails is the most important bug in the family.