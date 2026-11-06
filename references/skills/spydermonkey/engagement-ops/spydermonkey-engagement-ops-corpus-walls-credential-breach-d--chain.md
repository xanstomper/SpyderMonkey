# Corpus walls (credential/breach data) — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-corpus-walls-credential-breach-d.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The family catalogs breach intel — counts, field censuses, catalog state (HIBP, aggregator
indexes) — never corpora. Buying from extortionists, hacking their infrastructure, or
downloading a leak drop are all walls (criminal-held data; possession converts an observer
into a target). A field-NAME census over public feeds is the legitimate version of
"check for credential exposure": flag email/pass/hash/token/phone field NAMES, never
harvest values.

**HIBP is NOT exhaustive — vendor indexes diverge, and a clean HIBP does not clear the target.**
On each later session, sweep MULTIPLE catalog indexes for the brand (the ones with no login-gated
report are ideal): LeakRadar (`leakradar.io/en/report/<domain>` — the counts render CLIENT-SIDE, so curl sees
only the shell; headless-render the report on the VM to extract the verdict — "Matching
records were found. A volume estimate is currently unavailable." is a CONFIRMED presence
without an account), Breachsense, and any aggregator
whose public report lists stealer-log + combolist splits. Vendor coverage differs wildly — a
target that HIBP catalogs nothing for can still have 200k+ stealer-log pairs on LeakRadar
(field census + count = catalog-legal; the vendor page itself is the public report, screenshot the
values). A breach-vendor count CFR-CORRECTS an earlier "HIBP catalogs nothing" negative. Also mine
public victim/forum reports (Bitcointalk /r/gambling threads, consumer-sites) that document actual
drains — a reported withdrawal-without-2FA-prompt + auto-added-whitelist pattern with blockchain
evidence can upgrade a HYPOTHESIS account-takeover finding toward corroborated, and it names the
real drain vector the session-bearer finding predicts. Keep the claim's epistemology honest: vendor
counts are indexes (do not prove server breach; user-device stealer infections count too), and forum
reports are unverified victim narratives unless evidence-documented.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
