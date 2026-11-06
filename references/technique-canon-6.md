# TECHNIQUE CANON VI — crypto classes, auth-protocol depth, anti-abuse posture

_Every block is one technique: probe shape, decisive test, walls. Validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## Cryptographic classes

### Entropy/PRNG weakness classes
Predictable tokens (Math.random, time-seeded PRNG, sequential ids) — the SPY-048/058 fingerprint-mint family is the live example. Decisive test: N sampled tokens from YOUR OWN sessions → entropy arithmetic (pairwise deltas, structure) — a sub-64-bit space or visible structure = the finding; an evenly-distributed space is the banked negative (the ggpoker alias test).

### IV reuse and nonce-counter classes
Deterministic ciphertext prefixes across messages (ECB-class visual repetition) and IV/nonce reuse detectable from ciphertext pairs of YOUR OWN test material. Decisive test: two same-prefix plaintexts → ciphertext prefix delta (ECB) or equality (IV reuse).

### Padding-oracle classes
Distinguishable padding errors (status/length/timing) on ciphertext-bearing params — the lab replica proves the oracle shape; live characterization is ONE probe pair against your own ciphertext. The Manger/Vaudenay recovery itself is never executed live (no-gain).

### Hash length-extension
HMAC-less `hash(secret||data)` schemes fall to length extension — the class is the MAC construction, tested against YOUR OWN captured token pair in the lab.

### Key-material-in-code classes
Hardcoded keys/salts in bundles (the crash-verifier salt class, SPY-067 repo prefill) — the string context proves it is KEY MATERIAL (used in a live crypto op), not decoration. Decisive test: the key string + its use-site in the decompiled path — the pairing is the finding.

### Signature-verification gaps (server-trust asymmetry)
The SPY-101 family: mint endpoints open, verify endpoints gated — asymmetric hardening. Decisive test: mint without credentials vs verify's bean-validation — the asymmetry IS the finding.

### Subkey derivation and cross-protocol key reuse
Same key material across protocols/tiers (the mkey+securityKey class) — proven from bundle/config co-occurrence + one probe showing cross-tier acceptance on YOUR test material.

## Auth-protocol depth

### Kerberos class set (read-only enum)
AS-REP-roastable accounts, kerberoastable SPNs, unconstrained-delegation CONFIG exposure — all ENUMERABLE read-only (canon-III); the crack/capture stays the no-gain wall. Decisive test: enum output naming the accounts — the list is the finding.

### NTLM relay classes (documented mechanisms)
SMB signing absent / channel-binding gaps — the CONFIG posture (signing required?) is the read-only finding; the relay is never executed. Decisive test: SMB negotiation flags — the flag absence is the class.

### OAuth per-grant-type classes
Implicit (canon-I), password-grant legacy, device-flow cross-device pollution, refresh-token rotation gaps — one class per grant type, decisive test = the token-exchange differential on YOUR registered client.

### SAML per-profile depth
Web-SSO signature wrapping (canon-I), ECP/Artifact-profile residue, metadata trust reuse across SPs. Decisive test: metadata parse + one wrapped-assertion acceptance on your test SP.

### WebAuthn/FIDO classes
Origin/RP-ID scoping gaps, challenge entropy, credential-id enumeration, the SPY-101 allowCredentials:[] mint class. Decisive test: ceremony parameters observed on your own enrollment — the scoping delta is the finding.

### Session-token format depth
Opaque-token structure decoding (canon-I), JWT families (canon-II), PASETO/other formats misused, cross-tier token sharing. Decisive test: token decode + cross-tier acceptance probe on your own tokens.

### Cookie jar depth
__Host- enforcement (canon-I), SameSite=None sprawl, cookie-count overflow eviction (forced-logout class), chstate/confusion via name collisions. Decisive test: your own cookie jar manipulations in the lab browser — the eviction/collision behavior is the finding.

## Anti-abuse & edge posture

### CAPTCHA-gate anatomy (the Fastly _fs-ch class family)
The challenge SVG/logo-strip is NOT the captcha — the form-adjacent JPEG is (engagement-ops). Decisive test: challenge-object inventory on the live edge — the anatomy map is the finding; solving is NOT attempted (the wall).

### Anti-bot posture (JS challenges, managed challenge)
Which lanes get challenged (curl/requests vs headless vs real browser) — the differential map is the recon crown (drives all lane strategy). Decisive test: same endpoint three clients — the treatment matrix.

### WAF per-vendor evasion vocabulary (documented classes)
The encoding vocabulary exists FOR the WAF tier (canon-I hardened state): double-encode, unicode, case-split, comment-split — one variant per request, the differential must clear WITHOUT tripping. Decisive test: variant-acceptance vs WAF-flag delta on your own benign probe.

### Rate-limit architecture classes
Header-trust (canon-I), per-route vs global buckets, burst-then-sustain shapes observable from response headers (Retry-After, X-RateLimit-*). Decisive test: header telemetry over N paced requests — the bucket model is the finding.

### DDoS/edge-capacity posture (exposure row)
Cap-absence classes (canon-II HTTP/2) — registered from edge config signals only, floods never fired.

## Verification-fairness math (the casino canon)

### Provably-fair chain verification (decisive-negative)
hash(N-1)=SHA256(hash(N)) across 99 live rounds = committed chain; 0/95 derivations matching your own recomputation = server-secret-backed multiplier (SPY-059). The chain arithmetic IS the finding — no prediction claimed beyond the math.

### RTP telemetry sweep discipline
Rolling-window liveRtp sweeps every session (fresh money-pump rows), DISTINCT leading words per title (dedupe discipline), mirror the exact POST verb+headers. Decisive test: liveRtp_24h from the public endpoint — the repricing pattern across sweeps is the crown class.

### Client-parameterized bet APIs
`game.bet(amount, payout)`-style client-controlled targets — the client-trust surface (SPY-048 family). Decisive test: the API signature from the bundle + server-validation absence in the protobuf — the signature map is the finding; the funded exploit is never authored (boundary rule a).

### Two-salt and ticket-mint traps
The t1 ticket = clock-embedded identity-mint (not input echo); salt pairs that LOOK like PF are server traps — characterize the mint anatomy from the bundle before claiming any prediction class.

### Feed-fabrication block-test
Config-fabricated feeds vs server-settled rounds — the block-test (client-side fabrication refused by the settle path) is the banked negative proving settlement integrity; its absence = the class.
