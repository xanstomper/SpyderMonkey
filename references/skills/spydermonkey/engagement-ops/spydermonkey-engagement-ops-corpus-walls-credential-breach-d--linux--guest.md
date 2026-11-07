# Corpus walls (credential/breach data) — linux / guest

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-corpus-walls-credential-breach-d.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **linux** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

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

## Probe adjustment (linux × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
