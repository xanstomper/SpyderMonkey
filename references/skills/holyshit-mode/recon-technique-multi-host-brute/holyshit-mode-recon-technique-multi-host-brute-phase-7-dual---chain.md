# Phase 7: Dual Auth-Path Testing — chain composition

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-7-dual-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Tested JWT forge, CRLF injection, X-API-Key vs Bearer header variants
- JWT forge rejected (401), CRLF injection rejected (401, no header injection — parser is safe)
- Main `/v1/chat/completions` accepts both `Authorization: Bearer` and `X-API-Key` — dual auth path but both properly key-gated

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
