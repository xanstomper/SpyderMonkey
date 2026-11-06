# Route-map mining (the big win) — chain composition

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-route-map-mining-the-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The fork has dozens of custom routes invisible to endpoint guessing: `/api/user/reset_by_code`,
`/api/user/login/email/code`, `/api/web/runtime-key`, `/api/web/token/batch`, `/api/admin-auth`,
`/api/user/free-trial/usage`, `/api/user/promo-discount/preview`, `/api/user/membership`,
`/api/user/{stripe,paypal,nowpayments,antom}/pay`, `/api/messages/tickets/*`, `/api/region-access`.

Method: fetch every `src="/_next/static/chunks/*.js"` from ALL page variants (homepage, /console,
/pricing — each page loads different chunks), then regex `["\'](/api/[A-Za-z0-9_/.-]{2,80})["\']`.
Endpoint guessing alone found ~8 routes; chunk mining found 40+.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
