# Evidence discipline (repeat offenders this session)

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Retract inflated findings when the full response disproves them (mass-assignment case).
- Hypothesis ≠ confirmed: Discord renders identical HTML for valid/invalid redirect_uri
  (error only after JS exec) — server-side curl cannot distinguish; keep such chains
  as hypothesis until a real browser session proves them.
- Decode JWT payloads (`cut -d. -f2 | base64 -d`) to enumerate claims the backend may
  mistakenly trust, but test the actual gate before claiming escalation.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
