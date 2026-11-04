# 3. Keyless internal telemetry/billing ledger — firmware / low-priv

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-3-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`GET https://<internal-gateway>/usage.json` (no auth) dumps the internal usage ledger:
`organization_id`, totals, and a per-`identity[]` breakdown with **internal tenant/account names
(`opflow`, `platform`, `kion-unlimited`, `vincent`) plus per-identity token counts and
`known_estimated_cost_micro_usd`**. `GET /usage` serves the human HTML of the same ledger.
Tenant+spend enumeration = compromise-class (internal account names feed further targeted abuse).

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
