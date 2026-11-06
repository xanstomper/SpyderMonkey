# Region-wall discriminator (auth-plane 403 ≠ IP-quality) — chain composition

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-region-wall-discrimi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Datacenter vantage + `403 general.Forbidden` on auth endpoints while READ surfaces (feeds,
sockets, configs) answer 200 = a RESTRICTED-MARKET geo block on the vantage, not IP-quality.
Confirm via the target's own signal: the realtime socket pushes `blocked:{reason:"region_page",
location:"de"}` naming the geolocated country. Never churn request variants on ONE route
(signing modes, address casings, claimed country params) — they fail identically and the
churn burns the vantage. DO sweep route BREADTH once per route: the region gate is
PER-ROUTE, not per-host — one host answered `/auth/token` 201, `/auth/blockCheck` 200,
`/auth/web3` 403, and `/auth/steam` + `/auth/google` 302 in the same engagement. The 302
OAuth login starters (steam/google/discord) are the likeliest exemptions, so probe every
login-method starter BEFORE declaring the auth plane walled. Gated routes need a
residential unrestricted vantage; open starters do not — say once which is which.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
