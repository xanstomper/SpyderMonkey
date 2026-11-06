# Reporting when operator demands "extortion-group-level" material — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-reporting-when-operator-demands-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When the operator escalates past live vectors to "what an extortion group would run / attack-map level / we need to report X to the target," the deliverable that lands is a **documented-playbook attack map**: take a PUBLICLY DOCUMENTED group playbook (e.g. WhiteArmor's Gamdom V2 listing: old never-rotated machine account → control panels/secrets → full 146-column DB → provably-fair-manipulation evidence → $15M extortion → cross-brand dump) and map it STAGE-BY-STAGE onto the verified estate, each stage = real surface + ledger finding + extortion impact. Verify first whether the group has ALREADY listed the target (leak trackers / press — a "not yet listed" result is the window, state it). **ransomware.live's API (api.ransomwhe.re) is AUTH-GATED now — every call answers `{"message":"Missing Authentication Token"}`; the free working source is RansomLook:** `https://www.ransomlook.io/api/group/<name-lowercase>` returns a 2-element array `[site-meta, posts]` (site-meta carries the onion slug + `available` + lastscrape; posts carry `post_title`/`discovered`/`description`/`link`), no auth, scraped within hours. Scan every post's full JSON blob (title+description+links) for the estate strings — brand names, vendor names, payment-rail names — and read the group's recruiting/program posts ("we are hiring", "project X", "updates") for the entry-class evidence: those posts name the group's actual MO (access-buying desks, insider recruiting, demonstrated auth-bypass classes, tempo). and check the leak-catalog for a target-named combolist file (`leakradar.io/en/leaks/<id>` `bc.game.txt`-style, 100k+ lines = catalog-legal corpus evidence). Close with ranked fixes keyed to map stages, the operator's own triage history as the "why payment/ack is unlikely" context, and the honest caveat that a mapped playbook is threat modeling, not a claim of ongoing compromise. This satisifies "find things we can report to the target" where further anonymous exploitation is gated — and remember the reporting discipline above: availability/telemetry-class rows are recon coverage, never the crown the operator is asking for.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
