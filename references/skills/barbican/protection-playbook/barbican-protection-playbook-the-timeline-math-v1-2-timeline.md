# The timeline math (v1.2 — `timeline`)

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Bursts chunk at ≤25 requests (the family noise budget's atomic unit).
- Intra-burst gap: `--pause` (default 0.2s — matches undercroft's live pacing).
- Inter-burst pause: 1s (a burst boundary is a breath).
- Wall-clock = Σ(count × pause) + Σ(inter-burst gaps) — printed so the operator
  knows the engagement's tempo BEFORE it runs.
- The window: engagement pacing avoids the operator's routine hours (posture
  holds the window; the vantage's timezone is the opsec timezone).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
