# How to assess an unknown technology — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-how-to-assess-an-unknown-te.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
