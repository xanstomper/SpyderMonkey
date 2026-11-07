# 5. Forced-outcome capability

- source canon: `holyshit-mode/provably-fair-verification.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Watch result events for `forced` / manual-control flags. The flag existing in the
PUBLIC event schema = a staff-side outcome-control surface is a system feature (the
chain would not cover a forced round — that is the escape hatch). All-false captures
= capability present, use unproven; a `forced:true` round in anyone's evidence = the
control in use. Either way this is the caveat that must ride the rebuttal package.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
