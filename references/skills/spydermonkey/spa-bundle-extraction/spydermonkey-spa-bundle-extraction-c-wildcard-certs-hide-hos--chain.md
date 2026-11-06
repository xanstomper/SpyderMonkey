# C. Wildcard certs hide hosts from CT logs — DNS wordlist instead — chain composition

- source canon: `spydermonkey/spa-bundle-extraction.md`
- base technique: `spydermonkey-spa-bundle-extraction-c-wildcard-certs-hide-hos.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

CT-log enumeration is blind to every subdomain NOT in a cert when a wildcard covers
it. After the CT pass, hand-probe a plausible-name DNS list (`api`, `ws`, `cashier`,
`wallet`, `my`, `auth`, `account`, `pay`, `download`, `client`, `update`, `admin`,
`test`, `dev`, `crm`...) against each in-scope apex. Prioritize hits on RAW (non-CF)
IPs — origin-visible hosts — and probe what they serve. A live payments app
(`cashier.<brand>`, Next.js) was invisible to 8 CT pulls and visible to one dig.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
