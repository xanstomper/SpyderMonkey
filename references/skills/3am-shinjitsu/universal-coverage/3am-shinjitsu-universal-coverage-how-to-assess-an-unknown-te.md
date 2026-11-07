# How to assess an unknown technology

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Use this decision tree when the stack is unfamiliar:

1. **Identify the trust boundary.** Who calls it, with what authority, and what does it
   trust by default? (browser→server, service→service, tenant→control plane, device→cloud)
2. **Enumerate identities and secrets.** Humans, services, tokens, certificates, workloads,
   break-glass accounts. Stale and over-privileged identities are the universal failure.
3. **Map inputs to privileged actions.** Any field/header/message/event that changes
   authorization, routing, tenancy, billing, execution, or data access is a candidate.
4. **Check the negative space.** Missing verification, missing expiry, missing audience,
   missing tenant check, missing revocation, missing audit — not just implemented crypto.
5. **Verify read-only.** Prefer configuration review, logs, policy diffs, and one-request
   proofs. Never pivot from a finding into persistence, data extraction, or disruption.
6. **Ledger the exact test.** A negative without its exact procedure is not durable.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
