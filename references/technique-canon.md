# TECHNIQUE CANON — dense per-class blocks for the expanded corpus

_Every block below is one technique: probe shape, decisive test, walls. WSTG/PTES-anchored, validation-only, NO-GAIN. These sections feed skilltree.py — one `###` = one technique file._

## Auth & Session Classes

### Basic-auth and form brute geometry
The brute class is a RATE problem before it is a CREDENTIAL problem: lockout windows, per-IP vs per-account throttling, and response-length uniformity decide feasibility. Decisive test: 5 wrong-password requests on one account, one on the next — a lockout on the first and none on the second means per-account throttling with per-IP rotation potential. Register the geometry (window, scope, response delta), never a harvested credential.

### JWT algorithm confusion (rs256 → hs256)
If the verification library accepts `alg` from the token, an rs256-signed scheme falls to hs256 with the public key as HMAC secret. Decisive test: sign a token with alg=hs256 using the fetched public key PEM as the secret, send it, and require a measurable behavioral delta (accepted vs 401) — token acceptance without privilege movement is a hypothesis, not a finding. Validation-only: a forged token is PROVEN but never used for access.

### JWT kid path traversal and jku/x5u injection
`kid` is a file-path or SQL lookup in many libraries; `jku`/`x5u` let the token name its own key source. Decisive test: kid=<harmless traversal string> that flips the error class (signature error → file-not-found), and a jku pointing at YOUR registered domain serving a key — the 200-vs-400 delta is the proof. Never persist a forged trust chain.

### OAuth implicit-flow token leakage
Implicit flow puts the access token in the URL fragment, which leaks via referrer and history. Decisive test: register a redirect_uri under your control in a dev client (or find the fragment echoed in any in-scope page), and observe `access_token` in the fragment path — proof is the fragment reaching a second-party surface. Crown: token lifetime + scope carried by the leak.

### OAuth code interception (redirect_uri looseness)
A permissive redirect_uri validation (prefix match, wildcard subdomain, open redirect chained) makes the authorization code interceptable. Decisive test: redirect_uri=https://in-scope.host.evil.example — accepted or rejected by the AS; if accepted, the code arrives at your host. The finding is the validation looseness class, proven by one redirect.

### OIDC scope/audience downgrade
Resource servers trust the AS's audience tag; an attacker-controlled client registration (or a lax AS) can mint tokens for scopes the principal never granted. Decisive test: request scope=X with prompt=none from a fresh session and compare the minted token's scope/aud claims against the consent screen's promises — a delta is the finding.

### SAML response signature wrapping
Multiple assertion signatures or an unsigned assertion beside a signed one let a wrapping attack move the subject. Decisive test: duplicate the assertion with a wrapped subject and observe acceptance — acceptance of ANY forged assertion is confirmed; the account used must be your own test principal.

### SSO single-logout non-propagation
Logout at the SP that leaves the IdP session (or a sibling SP) alive turns "logout" into a UI state. Decisive test: log out at SP-A, replay SP-B's deep link — an authenticated render is the finding. Crown: session lifetime after logout.

### Session fixation via URL-borne tokens
A session id accepted from the URL (`?sid=`) and re-issued as a cookie lets an attacker pre-set the victim's session. Decisive test: set sid=attacker-value in the URL, authenticate, and read the session cookie — identical value = fixation prep confirmed. NO-GAIN: never let a third party authenticate through your fixed session.

### Cookie __Host- prefix and scoping regressions
Missing `__Host-`, missing Secure, or Domain=.parent leaves cookies portable across sibling hosts. Decisive test: set a cookie on sub.in-scope.host and read it from sibling.in-scope.host over HTTPS — cross-subdomain readability is the finding.

### Password reset token reuse and non-expiry
The reset flow that accepts the same token twice (or after password change) fails single-use semantics. Decisive test: request a reset, consume it, replay it — a second 200 (vs 400/410) is the class. Crown: token TTL and whether the OLD password still works after reset.

### Reset host-header poisoning
The reset email's link built from the Host header (or X-Forwarded-Host) redirects the token to attacker infrastructure. Decisive test: request a reset for YOUR OWN account with Host=your.domain, read the emailed link's host — proof is in your own inbox, never a third party's.

### OTP brute window and rate geometry
OTP validation with per-request cost < lockout threshold is enumerable (6-digit, 10 tries/lockout, no window reset = 1-in-10000 per lockout cycle). Decisive test: measure the exact counters — wrong-OTP responses until lock, lock TTL, and whether attempts decrement on resend. Register the arithmetic; never extract a live OTP.

### OTP multi-submit race
The verify endpoint that accepts concurrent submits can validate one OTP across N sessions. Decisive test: same OTP payload fanned to 5 parallel requests with distinct session tokens — >1 success = the class. The race is measured in the lab replica first (dojo replica reproduces the semantics).

### MFA grace-window and trusted-device abuse
"Remember this device" tied to a long-lived cookie outlives the OTP it certified. Decisive test: complete MFA once, capture the device cookie, and read its expiry + behavior after password change — MFA bypassed by a stolen cookie is the finding (characterize on your own principal).

### Magic-link entropy and single-use semantics
Magic login links with short token entropy or replayable semantics are the passwordless brute. Decisive test: request two links, compare token structure/entropy (e.g. 22-char base62 ≈ 128-bit = NOT enumerable — bank the negative), and replay the consumed link for a second auth.

## Business-Logic Classes

### Coupon stacking and chain arithmetic
Multiple discount codes applied per cart (or a code re-applied per item) is arithmetic the server should refuse. Decisive test: apply code A then B — final total below the item floor = the class; capture the order-preview JSON before/after as baseline/attack/diff.

### Negative and fractional quantity
Quantity=-1 or 0.5 submitted to a cart/checkout inverts the math server-side. Decisive test: quantity=-1 on the cheapest line, read the recalculated total — negative TOTAL is the crown; rejected = bank the negative.

### Currency and price-mismatch substitution
A client-supplied currency code (or price object) re-priced by the server at a stale rate is a rounding/repricing seam. Decisive test: switch currency mid-checkout and diff the converted line prices against the live FX the page displays — persistent mismatch = the finding.

### Price-override parameter injection
Hidden/ignored client fields (`price`, `discount`, `unitPrice`) that the serializer re-binds into the order. Decisive test: add price=1 to the POST body; a changed order total without a server-side entitlement check is the class. NEVER submit the poisoned order — the preview response is the proof (no-gain).

### Shipping and tax zeroing
The shipping/tax line recomputed per address/region can be zeroed by a region string the tax table lacks. Decisive test: region=XX-UNKNOWN at checkout — total drops the tax line = the finding (characterize, don't purchase).

### Refund/partial-refund idempotency
A refund endpoint without idempotency key dedupe re-issues on retry. Decisive test: identical refund request twice on a test order (sandbox) — second success vs idempotent replay = the class. This is REPLAY canon: same key, server state advanced twice.

### Trial reset and signup-limit bypass
Trial entitlement tied to a client-controllable identity fragment (device id, email alias) is a logic seam. Decisive test: second trial via email+1 alias on your OWN address — entitlement granted = the finding (the abuse class, not the grant).

### Referral/gift-card self-pairing
Referral credit for self-pairing (A refers A) or gift-card enumeration (sequential codes). Decisive test: gift-card code structure sampled from 2 legit cards — sequential/predictable = enumerable (register the entropy math, never brute a live range).

### Withdrawal threshold and fee dodge
Min-withdrawal/fee logic enforced client-side (button disable, computed fee in JS) while the API accepts the raw request. Decisive test: submit the raw withdrawal POST for 1 cent below threshold on a test account — acceptance = the class; the payload is never the point, the server's acceptance is.

### Rounding-difference accrual
Per-line rounding (banker's vs half-up) accumulated over many lines differs from the total the user authorized. Decisive test: 100-line synthetic cart, server total vs sum-of-lines — the diff is the accounting class ( dojo replica reproduces the arithmetic).

### Idempotency-key reuse across intents
The same idempotency key replayed for a DIFFERENT operation that the server accepts = cross-intent replay. Decisive test: key K on op-A then op-B — op-B returns op-A's cached result = the finding.

### State-machine escape (order status skip)
Order transitions (cart → paid → shipped) accepted out of order by direct API calls. Decisive test: call shipped-confirm on a test order still in cart — 200 = the class; the escape is characterized on your own order only.

## Injection Classes

### SQLi ORDER BY / second-order
ORDER BY injection (no UNION needed) and second-order (payload stored, executed in another query) are the two shapes scanners miss. Decisive test: ORDER BY (CASE WHEN 1=1 THEN col ELSE col2 END) — row-order delta = injectable; second-order requires your own stored payload re-read in the admin/profile render.

### SQLi time-based discipline
SLEEP/BENCHMARK probes at ONE request per measurement, never a burst — a time-based confirmation is a timing histogram over 3 samples against a baseline 3, not a flood.

### NoSQL operator injection ($ne, $regex)
JSON body operators accepted server-side ({"pass":{"$ne":""}}). Decisive test: {"$ne":null} on the login body of YOUR test account — a 200 without the password = the class.

### LDAP filter injection
(&(objectClass=*)) metachar reflection into an LDAP filter. Decisive test: value=*)(uid=* — a changed result count = filter injection.

### Command injection via double-quote/pipe variants
The documented class vocabulary (backtick, $( ), newline, %0a) applied ONE variant per request. Decisive test: an out-of-band marker (DNS to your registered domain) beats response-diff for blind injection — the marker arrival is the proof.

### SSTI detection arithmetic (jinja/smarty/twig)
{{7*7}} → 49 is the arithmetic marker; engine fingerprint follows ({{7*'7'}} → 7777777 = jinja2). Decisive test: the arithmetic marker reflected — class confirmed; template execution beyond arithmetic is RCE-class and is REPORTED, not executed (no-gain).

### XXE out-of-band and local-file
DOCTYPE + external entity to your DNS/HTTP listener = OOB proof; file:///etc/hostname echoed = local-file proof. Decisive test: OOB marker arrival at your listener; file read limited to hostname/ident material.

### XInclude and SOAP param XXE
Client-side XML parsers (XInclude on a fragment, SOAP body param) carry the same entity class without a full document control. Decisive test: the OOB marker through the fragment param.

### PHP filter chain and wrapper rce-shape
php://filter chains (convert.iconv) produce arithmetic-signed output for blind detection. Decisive test: chain produces the expected signature byte pattern — class confirmed read-only.

### Deserialization gadget DNS-ping
The safe proof of a deserialization class is a DNS-only gadget (no command execution). Decisive test: serialized payload whose gadget list ends in a DNS resolution to your domain — the lookup arrival is the finding. Execution gadgets are REPORTED as the class, never fired.

### GraphQL introspection and field suggestion
Introspection enabled (or disabled-but-suggested via DidYouMean errors) maps the full schema. Decisive test: introspection query 200 with schema JSON = surface map; wrong-field error naming the right field = suggestion leak.

### GraphQL batched-mutation and alias abuse
Batched operations/aliases bypass per-field rate logic. Decisive test: 10 aliased identical mutations in one request on a test object — 10 executions = the class.

### gRPC reflection and plaintext services
grpcurl list on plaintext = service inventory without auth. Decisive test: reflection output names services the web app never exposes — crown the inventory gap.

## Client & Browser Classes

### DOM XSS via location.hash / postMessage
hash-borne sinks and postMessage handlers without origin checks. Decisive test: postMessage from YOUR page to the in-scope window — handler executes with your payload; the alert/echo in YOUR browser session is the proof (self-XSS framing stays hypothesis unless it crosses principals).

### Prototype pollution (__proto__ / constructor.prototype)
Client-side merge sinks (or query-string ?__proto__[x]=y) that reach a gadget. Decisive test: pollution observable in-page (Object.keys diff) — gadget reach = the severity; no gadget = informational.

### CSP absent / base-uri + script-src gaps
CSP missing base-uri or allowing script-src with a JSONP/file-upload host = injectable. Decisive test: CSP header parse + one blocked/allowed probe — the header itself is the finding when dangerous sinks exist.

### Open redirect via //, \\, and userinfo tricks
//evil.example, https:evil.example, /\evil.example parser-differential confusion. Decisive test: each variant's browser navigation (headless, local) — one variant navigates off-host = the class. Crown: redirect chains into OAuth redirect_uri (pairs with the OAuth class).

### Clickjacking without X-Frame-Options / frame-ancestors
Framable state-changing pages. Decisive test: local framing harness — the frame renders the sensitive control = the class (register per-endpoint).

## Infrastructure & Config Classes

### .git /.env /backup discovery discipline
Distinguish SPA-fallback 200 shells from REAL exposure: require content distinct from the canonical nonexistent-path control (size/content-type delta). Decisive test: control path vs candidate path — identical shell = exhausted, different = the finding.

### Source-map disclosure
.map files ship original source to anyone. Decisive test: GET /app.js.map → 200 JSON with sources — the finding; original code with secrets in comments = the crown.

### Host-header injection and password-reset poisoning
Host header reaching generated links/emails/redirects. Decisive test: Host=your.domain on a state-changing POST — the generated URL in the response/email carries your host = the finding (pairs with the reset class).

### Web cache poisoning (unkeyed input reflect)
Unkeyed header values cached into the response. Decisive test: header X with a unique marker, then a second unauthenticated request returning the marker = poisoned (one cache entry, your own marker, never a real user's path).

### Web cache deception
A path like /settings/nonexistent.css served cached with the victim's session when THEY request it — characterize on your own session only, register the cache-key behavior.

### Request smuggling CL.TE / TE.CL differential
Two conflicting-header probes with a timing/response-length delta — ONE probe pair, never a burst against a shared edge. Decisive test: the differential timeout/smuggled-response signature in the lab replica first (dojo has the replica).

### DNS zone transfer (AXFR)
 AXFR against all nameservers for the domain. Decisive test: full zone listing from ANY nameserver = the finding (read-only inventory).

### Dangling CNAME / subdomain takeover
CNAME to NXDOMAIN + claimable service = takeover prep. Decisive test: cname → resolution failure + the target service's fingerprint (e.g. "There isn't a GitHub Pages site here") = the class. Register the claimability, never claim a third-party domain you lack rights to.

### SPF record +all / ?all and DMARC p=none
Spoofability is record arithmetic: SPF ending +all (or ?all with no fallback), DMARC p=none with no rua = spoofable domain posture. Decisive test: TXT record parse — the arithmetic IS the finding (no spoofed mail sent).

### DKIM key length and selector hygiene
DKIM RSA key < 1024 bits or stale selectors pointing at dead infra. Decisive test: selector DNS lookup + published key size parse = the posture finding.

## Cloud & Container Classes

### S3/GCS/Azure bucket anonymous list
Bucket LIST permission without auth is read-only inventory. Decisive test: anonymous LIST (s3 ls / public GET) — the listing = the finding; never write.

### Cloud metadata SSRF (169.254.169.254)
SSRF reaching instance metadata = the class. Decisive test: SSRF response carrying instance-id/ami-id (hypothesis-grade until a 3-gate diff) — IMDSv2 token-required = the mitigated negative, bank it.

### Kubernetes API anonymous and service-account exposure
API server reachable anonymously (system:anonymous binding) or a leaked SA token with cluster-scope list. Decisive test: GET /api/v1/namespaces with the token/anonymous — read-only listing = the finding.

### Docker socket / containerd exposure
Socket mounted or TCP-exposed = full host control class — characterize as the exposure (never execute the escape).

### Container registry anonymous pull
Private registries allowing anonymous catalog/list. Decisive test: /v2/_catalog 200 = the inventory finding; image contents stay uncrowned beyond the manifest listing.

### CI pipeline config exposure (.circleci/.github workflows)
Runner configs with secrets referenced (not values) map the secret inventory. Decisive test: workflow YAML naming secrets + the pull-request trigger surface = the supply-chain finding.

## Rate & Abuse Classes

### Rate-limit key rotation (X-Forwarded-For trust)
Limits keyed on a client-supplied header = limit-free access. Decisive test: same request 6× with rotating X-Forwarded-For — all 200 past the documented limit = the class (the arithmetic, not a brute).

### Login throttling response differential
Locked vs unlocked account responses differ (message/timing/length) = enumeration oracle. Decisive test: your test account (existing) vs random string (nonexisting) — differentiable = the finding.

### Resource-exhaustion class (validation-only)
Unbounded expensive endpoints (report generation, image resize) — characterize as the class with ONE request's measured cost delta, never a sustained drain.
