# Phase 2: TLS + SAN Extraction — chain composition

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-2-tls-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- OpenSSL `s_client -connect` cert SAN revealed: `openinfra.freeinference.org`, `*.opendata.freeinference.org`
- These internal infra hosts are not linked from the public site — SAN extraction is the only discovery vector
- Technique: `openssl s_client -connect freeinference.org:443 -servername freeinference.org`

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
