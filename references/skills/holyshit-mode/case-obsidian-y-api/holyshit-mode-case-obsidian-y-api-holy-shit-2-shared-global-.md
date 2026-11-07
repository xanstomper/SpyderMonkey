# HOLY SHIT #2 — Shared global conversation context / cross-user disclosure (score 85)

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `prompt_tokens` DRIFTED on identical input across requests (21k → 30k → 50k) → context is server-side state, not static per-request injection. **PTOK drift on identical input = shared-context oracle.**
- No cookies/sessions at all, yet the model recalled ALL prior turns from earlier separate curls → global buffer keyed on nothing.
- Foreign users' roleplay content (character personas never sent by us) appeared in context. Anyone can read out other users' conversations via a summarization oracle and poison the shared context for everyone.
- The model itself CONFIRMED the history ("Turns 1–8...") when asked — the disclosure oracle is one prompt away for any user.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
