# Vendor bug-bounty pages = zero-document authorization — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-vendor-bug-bounty-pages-zero-doc.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A self-published `/bugbounty` page is an authorization document that needs no paperwork —
parse it into the engagement before any probe: §3 in-scope list → `scope add` entries (domains
AND the feature list: auth/session/KYC/wallet/bonus/APIs/game-launch/business-logic), §4
out-of-scope → the exclusion gates (enumeration-without-impact, headers-only hardening,
scanner-spam-without-proof, DoS/volumetric), §5 report channel + subject format, §7
safe-harbor walls. Bank the parsed program in the holyleadger `program` field — its severity
tier table defines what the vendor pays for and pre-ranks the report. Program walls stack on
top of the family's own: validation-only + no other-user data + no disruption stay absolute,
and program-excluded classes (bare DMARC/headers, cosmetics) register as informative at most.

**Feeding the bounty page into 3AM (shinjitsu) needs the FULL manifest schema, and `--target` must be
a scope entry.** `validate --authorization <file>` refuses partial manifests — it requires
`authorization_id, authorized, operator, engagement, approved_by, roe_reference, expires_at, targets,
allowed_methods`; point `approved_by`/`roe_reference` at the program's own page and contact address.
The `--target` value must match an entry in the manifest's `targets[]` — pass the DOMAIN
(`ggpoker.com`), never the campaign nickname (`ggpoker`), or the gate refuses with "not in the
authorization scope". Without DNS control add `dns_control:false` — validation still passes but the
method downgrades to passive/active-read-only, and the sweep runs as `plan --target <domain>
--state <campaign>/3am-state.json` + honest `set-status` verdicts (EXHAUSTED/BLOCKED per domain)
instead of a live sweep. That is the wall holding, not a failure. (shinjitsu has NO sweep command —
validate → challenge → verify-dns → plan → set-status → report IS the interface.)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
