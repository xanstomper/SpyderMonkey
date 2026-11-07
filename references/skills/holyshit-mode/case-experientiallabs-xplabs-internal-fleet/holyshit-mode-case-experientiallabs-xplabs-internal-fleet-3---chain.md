# 3. Keyless internal telemetry/billing ledger — chain composition

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-3-.md`
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

`GET https://<internal-gateway>/usage.json` (no auth) dumps the internal usage ledger:
`organization_id`, totals, and a per-`identity[]` breakdown with **internal tenant/account names
(`opflow`, `platform`, `kion-unlimited`, `vincent`) plus per-identity token counts and
`known_estimated_cost_micro_usd`**. `GET /usage` serves the human HTML of the same ledger.
Tenant+spend enumeration = compromise-class (internal account names feed further targeted abuse).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
