# Re-run the catalog RTP sweep on later sessions — drift and new games are findings — mesh / hardened

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-re-run-the-catalog-rtp-sweep-on-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mesh** · auth **hardened** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

The live game-stat RTP endpoint reflects a ROLLING window, so values drift over time AND the
catalog gains/retires games between sessions. Re-rate the FULL catalog (not just the games you remember) on every visit and diff against the banked table: a game newly >100% (house paying out more than it takes) is a FRESH money-pump, and a game plummeting far below its advertised config
rtp (e.g. a slot at 0.0179 liveRtp_24h vs ~0.96 advertised) is a FRESH player-hostile finding —
both are `report-and-fix` rows, not repeats of the old sweep. Mirror the exact call (for bc.game:
POST `/api/game/home/game-stat/` `{gameUrl:X}` with `Origin`+`Referer`+UA, else CF returns 403
without UA). Include the freshly-observed values in the proof; two reads 30s apart confirming a
stable anomaly strengthens it. Game keys come from the config chunk (distinct per-key `rtp:`),
never a fuzzy display-name guess.

**Sweep key discovery is a SEPARATE step from re-reading the config chunk** — the BC-Originals config
chunk (`key:"...", rtp:.96, freeBet:!0`) enumerates only the in-house games; the third-party
provider-slot tier (betsoft/croco/evolution/pragmatic/tada/belatra/jili...) is entirely absent from it
and from any BC-Originals-only sweep.

**Sweep the FULL slug set from the sitemap/catalog XML, not a hand-rolled key list — that is the jump
from "13 games >1.0" to "231 games >1.0".** A key list you assemble by reading the config chunk or
remembering last session's games caps the RTP surface at what you already know. Pull the operator's
own `sitemap.xml`/`casino.xml` (the casino lobby publishes every routable game slug), walk each slug
through `game-stat`, accept the ~10k `game_not_exists` 4001s, and diff the survivors — one full-estate
sweep of 15,478 slugs found 5,468 live games with 231 reporting `liveRtp_24h>1.0` (148 >1.05), where
the remembered 26-key list had found 13. Verify the TOP outliers (re-read 30s apart, same values) and
bank the >1.0 set with BOTH interpretations — a `6.74` reading on a low-volume slot is most likely a
BROKEN-RTP-ACCOUNTING artifact (a few big free-bet/lucky wins in the 24h numerator without their wagered
denominator), not a genuine 6x house bleed; state both, and foreground any OPERATOR-BRANDED exclusive
slot that reads >2.0 (a `bc-game-<name>-by-<provider>` slug is uniquely reportable). A 0-WAF-block,
15k-request run under ~9min is normal for this endpoint.
it and from any BC-Originals-only sweep, yet it is where the biggest money-pumps hide (one session
found 13 provider slots >1.0 live RTP, dessert-dash-by-betsoft 1.2867 — bigger than the leading BC
Original). Enumerate provider-slot keys from three places: (a) the **casino lobby** hrefs (`bc.game/casino`
DOM anchors carry the `-by-<provider>` slugs), (b) the provider portal catalogs (game-provider.bc.game
+ the `v3.*` portal DOM: 47–48 titles with single/multi-stage + SLOTS groups), and (c) **slug-probing**
— `game-stat` accepts provider slugs even when they are NOT in the portal catalog (gates-of-olympus/
sweet-bonanza/charge-buffalo discovered by guessing `<name>-by-<provider>`). The provider-slot tier
has NO advertised `rtp:` in config chunks, so its >1.0 reading is unverifiable against a claim — bank
Here both interpretations (genuine overpay OR broken provider RTP accounting) and note the deviation
cannot be checked (worse than BC Originals). Also verify a banked slug is still the LIVE key: a key
that now returns `null` (e.g. `wukong` dead vs `wukong-by-croco-gaming` 1.0595 live) means the earlier
test hit a retired entry — re-key by the live slug before concluding a delta.

**Drift applies to the WHOLE live surface, not just RTP — re-hit known-live routes and socket hosts
on every session open.** A portal route that was interactive last session and now returns `404 text/plain`
(a SPA shell that hardened to a real 404), a provider portal that rotated its entry bundle to a thin
loader, or a socket host that went `000` connection-refused are all DRIFT/closure findings, NOT dead ends
or "host is down." A tightened anon surface is itself a reportable row (defenders rotated posture since
last visit) and it re-locks the anon-entry lane you may have planned to work. Keep a mental "was live /
now dead" delta across sessions: re-GET the portal root, re-GET the interactive game/dev-tool routes,
re-dial the socket namespace connects. A render/socket surface that was live but is now gated-or-gone
re-confirms the honest ceiling; a route that was 404 but now REPLIES is a fresh jackpot candidate —
check both directions.

**After a portal surface drift, pull the executing SDK from the SUPPLY-CHAIN origin, not the portal — the
real protocol config survives there.** When a provider portal rotates its entry bundle to a thin `loader.js`
stub (`import(entry)` + `renderGames("#root")`) and its game/dev-tool routes harden to `404 text/plain`, the
FULL merchant SDK is usually still served by the personal/development worker the production pages import
(e.g. `gwth<render>.irene9988.workers.dev/chunks/provider-sdk-*.js`) — the drift closed the portal door but
not the supply-chain asset. Pull that worker's `game-render.js` loader, read the `chunks/<name>-HASH.js`
it imports, and grep the merchant SDK for the ALWAYS-ON config: the `const oa={development:"wss://<dev-socket>",
production:"wss://<prod-socket>"}` host map, `const Ra="development"; mode=n.mode||"development"` (the
default env), `URLSearchParams(window.location.search).get("code")` / `get("mkey")` (URL query cred reads),
`crypto.subtle.generateKey` / `/merchants` auth bind, and `testSocketRoute` (`/test/?p=`). This proves the
code-in-URL + dev-default + keypair-bind takeover path is the LITERALLY SERVED code (not inferred from an
old capture) and is the load-bearing row for the crown chain. Register the dev-default-on-production as its
own CONFIRMED re-validation (SPY-095-class).

**Partial-remediation drift: probe the HTTP mint endpoint PER-HOST and SEPARATELY from the transport lane —
they diverge, and the divergence is the finding.** After a session proves an anonymous primitive (e.g. the
`/test/?p=<fp>` t1 signing-ticket mint + forgeable-fingerprint socket connect), the next session's re-probe
can find the TRANSPORT (WS engine.io upgrade) 503-edge-gated on ALL socket hosts while the HTTP `test/` MINT
stays 200 on SOME hosts and the main-brand host hardens to a CF managed-challenge 403 (`_cf_chl_opt`
nonce page served to curl/VM).

**Mint-response bodies carry the state-creation proof — read the BODY, not just the status.** A `/test/`
mint is NOT "200-empty": an EMPTY body is the fingerprint-format REJECT (8-char `p` → empty; valid
t1-length fingerprint → a 23-25 char signed ticket with an embedded hex clock block like `1a1af8b...`
matching the login-pre `random` field format). Mint the SAME valid fingerprint twice and md5 the bodies —
different token each time = fresh server-side state per request, i.e. the mint is a conditional
state-creation oracle, and repeated mints at speed are an exhaustion surface even before any socket
connect. Always capture body + md5-pair + per-fingerprint-format behavior in the proof. This per-host, per-layer divergence is an authentic PARTIAL-REMEDIATION finding,
not a "host is down": the operator gated the connect lane but left the signing-ticket mint live on the sibling
hosts, and hardened only the top brand host to a browser challenge. Sweep EVERY socket host's `/test/` (root +
`?p=<fp>` + `?p=<48 a's>`) AND dial each WS upgrade separately — record which lane is open on which host. Do
not conclude "the primitive is gone" from the 503 on one host, and do not accept a sub-5KB `<!DOCTYPE
html><title>Just a moment` 403 body as a real mint response — that is the CF challenge page, meaning the host
was CHALLENGE-hardened (different class from the still-200 sibling mint). Bank it as a HIGH AUTHN partial-closure
with the per-host/per-lane matrix in the proof; the still-open sibling mint keeps the SPY-048-class primitive live.

**A large bundled "game-render"-style module can be render/CSS-ONLY with zero logic — sanity-check before
mining.** Not every big JS chunk is the protocol/API logic bundle. A ~340KB module served by a render CDN
may be pure styling/shell (inline CSS, `touch-action`, placeholder strings) with obfuscated `sDkQs*`-style
CSS-class tokens and NO `wss?://` host, NO socket namespace, NO `URLSearchParams` query-param read, NO
API path strings. Before spending time reversing a large bundle, grep for the logic signals
(`wss?://`, `socket`, `URLSearchParams`, API paths); if it's ~zero on every one, classify it as render-only
and look for the thin loader/chunk that imports the REAL module (a small `loader.js` that `import()`s
`game-render.js` = trace the next hop; the render module itself is dead weight for vuln mining). Don't
register "no socket/API in the game module" as a finding — the module was never the protocol surface.

**Title every fresh RTP finding with a DISTINCT leading word — the ledger dedupe key is `cls+asset+normalized
title`, so two findings in the same class whose titles share the leading word COLLIDE and the new one
silently merges its evidence into the old row instead of landing as its own numbered finding.** This bit a
provider-slot money-pump that led with "FRESH live-RTP sweep…" and deduped into the earlier BC-Originals
RTP row (its evidence attached, but it lost its visible standalone identity). When a new sweep turns up a
different-class anomaly (provider tier vs BC Originals, a new game class, a separate backend), lead the
new title with the distinguishing noun ("Provider-slot tier money pump…") — not the shared verb + subject
("FRESH RTP sweep…") — so it registers as its own CONFIRMED row. The generic title-rule lives in SKILL.md;
this is the RTP-sweep instance that actually fired.

**Map shared origins with a Host-header + SNI sweep — CF Origin certificates PROVE the box.**
One physical origin serving several casino brands is the norm on white-label platforms; prove
it three ways: (a) Host-header vhost map — `curl --resolve <host>:443:<ip>` per candidate
brand (or `Host:` over :80); DISTINCT response bodies per Host = real vhosts, and a stale
lander surviving after the brand's DNS moved elsewhere (AWS GA/CF) proves an old vhost was
left on the box; (b) SNI cert harvest — `openssl s_client -connect <ip>:443 -servername
<host>` per host: a **CloudFlare Origin CA certificate** is installed ONLY on the real origin
behind that brand's Cloudflare, so sibling-brand Origin certs on the target's own box
CERT-PROVE shared origin (stronger than DNS inference); `CN=localhost.localdomain`
self-signed = default-vhost fallback, no dedicated cert; (c) the :80 catch-all — any Host
over HTTP redirecting to one brand names the box's default vhost. Register as INFRA (low)
with the cross-brand blast radius; sibling brands stay OUT of scope for active probes.

## Probe adjustment (mesh × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
