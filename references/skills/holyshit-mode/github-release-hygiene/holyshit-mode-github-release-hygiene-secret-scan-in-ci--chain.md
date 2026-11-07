# Secret Scan in CI — chain composition

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-secret-scan-in-ci.md`
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

The workflow greps for `sk-[a-z0-9]{20,}`, `gho_[a-z0-9]{20,}`, `api_key = '<20+ chars>'`,
`Bearer <20+ chars>` on every push. Exclusions: `.env.example` (placeholder values only)
and env-var NAMES like `HOLYSHIT_API_KEY` (no value).

**Rule:** never put real key material in any repo file, even "temporarily". CI catches it.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
