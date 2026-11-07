# 2. Token/auth hunt (puppeteer on the VM) — chain composition

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-2-token-auth-hunt-puppeteer-on-t.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Pass the CF challenge first: `page.goto` the main page, wait 10s+ (see
   SKILL.md SPA-probing note).
2. Capture auth-relevant traffic: `page.on('request')` / `page.on('response')`,
   keep headers matching `auth|token|jwt|bearer|session|device|x-|cookie`, dedupe
   by url + sorted header names.
3. Dump `localStorage` / `sessionStorage` / `document.cookie`; regex-hunt for
   JWTs (`eyJ….….`); decode hits via base64url (header.alg + payload claims).
4. Scan EVERY JS chunk with auth patterns: JWT literal, `Authorization`/`Bearer`
   usage, token storage keys, WS auth query params, jwt decode/verify code,
   `alg` hints, `x-api-key`-style headers. Filter placeholder/library false
   positives (axios emits generic `Authorization: Basic` builder code — it is
   not app usage).
5. **JWT-absence across the whole stack is itself a finding** — opaque-token
   design; state it, don't keep hunting for JWTs that don't exist.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
