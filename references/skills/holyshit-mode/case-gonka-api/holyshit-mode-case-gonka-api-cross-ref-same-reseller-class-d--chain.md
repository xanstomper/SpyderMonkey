# Cross-ref: same reseller class, different stack (apimart.ai, 2026-10-06) — chain composition

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-cross-ref-same-reseller-class-d.md`
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

apimart.ai = the OneAPI/new-api variant of the sketchy-reseller class (SEO-spam
botnet on GitHub, `x-oneapi-request-id` fingerprint, 309 models). Full recipe +
route-mining method: `references/case-apimart-newapi-fork.md`. Use both files
together when engaging this class — Supabase/Lovable stack vs Go/OneAPI fork
have different recon ladders (chunk-mining + upstream-source reading vs
PostgREST oracles).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
