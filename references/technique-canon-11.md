# TECHNIQUE CANON XI — WSTG full test canon (the standard methodology, claimed)

_Every block maps one OWASP WSTG test: probe shape, decisive test, walls. Validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## Information gathering

### Robots and sitemap intel
robots.txt and sitemap.xml enumerate paths the operators hid from crawlers. Decisive test: fetch both — disallowed paths probed with the SPA-shell control differential.

### App-server fingerprint
Server header, default error pages, and file extensions fingerprint the tier. Decisive test: three independent signals agreeing = the era-stack row.

### App-framework fingerprint
Cookie names, asset paths, and meta tags fingerprint the framework. Decisive test: two signals agreeing (e.g. JSESSIONID + /wicket) = the class row.

### WAF/edge fingerprint
Malicious-probe detection class and vendor markers in challenge pages. Decisive test: nmap-waf-detect/fingerprint + the challenge anatomy = the posture row.

### Page info-leak review
Comments, meta tags, and mailto/phone strings leaking internal details (estate artifacts only). Decisive test: regex sweep of the mirrored source = the inventory.

### Entry-point mapping
Links, forms, and JS-fetch paths map the attack surface (the crawl engine's canon). Decisive test: the session-context endpoint count pre/post crawl.

### Favicon intel
Favicon hash lookup correlating hidden hosts sharing the asset. Decisive test: hash computed from the live favicon = the sibling-host row.

### Debug endpoints inventory
Common debug paths (__debug__, /debug/, actuator family) probed with the control differential. Decisive test: distinct content vs control = the finding.

## Authentication testing

### Credentials-over-TLS posture
Login forms served/posted over http or mixed-content. Decisive test: form action scheme audit from the mirror = the row.

### Default-cred class
Vendor default credentials checked against the login (the CHECK class — one attempt each, never brute). Decisive test: acceptance on your test instance = the class.

### Lockout-mechanism geometry
Wrong-password counters, lock TTL, and reset behavior mapped. Decisive test: 5+1 attempts measuring the geometry = the row (the arithmetic, not a crack).

### Auth-schema bypass classes
Auth forced-browsing/parameter-tampering variants of the gate. Decisive test: gated page 200 with a mutated session marker = the class.

### Remember-password weakness
Stored credentials recoverable from the client (autofill/cookie storage). Decisive test: your own browser storage shows the plaintext = the row.

### Browser-cache weakness
Authed pages cached with Cache-Control absent. Decisive test: back-button render after logout on your session = the class.

### Password-policy weakness
Length/complexity/rotation rules enforced client-side only. Decisive test: server accepts a policy-violating change on your own account = the finding.

### Security-question weakness
Questions with enumerable answers + no rate limit. Decisive test: the geometry documented (never guessed live).

### Reset-password flow class
Token entropy, single-use, host-header poisoning (the canon-I depth). Decisive test: replay + poisoned link on your own inbox.

### Change-password flow class
Old-password verification absent or CSRF-able. Decisive test: change without the old password on your account = the class.

## Authorization testing

### Path-traversal classes
The documented traversal vocabulary against file params (canon-II depth). Decisive test: /etc/hostname marker reflected = confirmed.

### Authz-schema bypass
Role checks enforced per-UI only. Decisive test: privileged action via direct API with the low-priv token = the class.

### Privilege-ladder classes
The R1-R5 ladder inventory (kaisha canon) — rung reachability mapped read-only. Decisive test: the rung map = the finding.

### IDOR object-swap
The BOLA differential (canon-VIII). Decisive test: swapped-id content echo = CONFIRMED.

### WebDAV enablement class
DAV methods live on content tiers. Decisive test: davtest CHECK = the row.

## Session management

### Session-schema strength
Token entropy/structure analysis (canon-VI). Decisive test: entropy arithmetic on your own tokens = the row.

### Cookie-attribute posture
Secure/HttpOnly/SameSite/__Host- absence per cookie. Decisive test: Set-Cookie audit = the matrix.

### Session-timeout behavior
Server-side expiry absent (token valid post-idle). Decisive test: replay after the documented idle window on your session = the class.

### Logout effectiveness
Server-side session termination absent post-logout (canon-I SSO twin). Decisive test: replayed cookie alive = the finding.

### Session-fixation class
Pre-auth token carried into the authed session. Decisive test: token-identity across the auth boundary = the class.

### CSRF class
State-changing endpoints without anti-CSRF tokens. Decisive test: cross-origin form POST accepted on your session = the class.

### Session-puzzling classes
One session variable doubling for two purposes (the variable-reuse family). Decisive test: role/state confusion via the shared variable on your accounts = the finding.

## Data validation

### Reflected-XSS class
Context-specific reflection (canon-II per-context depth). Decisive test: context-correct execution in your session = confirmed.

### Stored-XSS class
Persistent payloads in your own objects rendering for OTHER principals — needs two principals (the two-role context rule). Decisive test: your own second account renders it = confirmed; single-principal = hypothesis.

### DOM-XSS class
hash/postMessage sinks (canon-II). Decisive test: in-page execution from your payload = confirmed.

### CSS-injection class
Attribute/style exfil shapes (canon-II). Decisive test: the style sink accepting your payload = the class.

### Verb-tampering class
GET-only enforcement bypassed via POST/PUT/HEAD overrides. Decisive test: 405-vs-200 across verbs on the gated route = the class.

### SQLi per-engine classes
Error/boolean/time channels per DBMS (canon-II full depth). Decisive test: the oracle delta = confirmed.

### NoSQL-injection class
Operator/type-confusion bodies (canon-II). Decisive test: acceptance without the secret = confirmed.

### LDAP-injection class
Filter metachar reflection. Decisive test: result-count delta = confirmed.

### ORM-injection class
ORM mass-assignment/query-param leakage classes. Decisive test: unintended filter honored = the row.

## Error handling

### Error-code taxonomy class
Custom codes revealing route existence (the 1901 canon). Decisive test: the error map per route family = the intel.

### Stack-trace class
Debug traces on prod errors (canon-IX framework depth). Decisive test: forced error content = the finding.

## Cryptography

### Weak-TLS posture
Ciphers/protocol inventory (the tls lanes). Decisive test: cipher matrix = the posture rows.

### Padding-oracle class
Distinguishable padding errors (canon-VI shape). Decisive test: the error differential on your own ciphertext = the class.

### Cleartext-sensitive class
Secrets in unencrypted transport/storage (the mobile storage twin). Decisive test: captured cleartext on your session = the finding.

### Weak-encryption class
ECB/static-IV/deprecated-cipher use-sites in the app's own code. Decisive test: two-ciphertext prefix test = the class.

## Business logic

### Data-validation bypass classes
Server-side validation absent for range/type/format on state-changing ops. Decisive test: the raw payload accepted on your own record = the class.

### Request-forgery classes
Forged requests completing flows the UI guards (the client-trust family). Decisive test: the flow completing via raw API = the class.

### Integrity-check absence
Signed payloads/updates verified client-side only. Decisive test: unsigned payload accepted on your test flow = the class.

### Process-timing classes
Race/replay windows on state transitions (the REPLAY canon). Decisive test: the idempotency/replay differential = confirmed.

### Misuse-resistance absence
Abuse-case behaviors (self-pairing, threshold dodge) unguarded (canon-III depth). Decisive test: the abuse arithmetic on your own accounts = the class.

## File & upload

### Upload-class set
Extension/content-type/size validation absent — DETECTION via benign markers. Decisive test: upload accepted with mismatched type + the served path = the class (never a working payload).

### Malware-upload framing
The eicar-class marker as the upload CHECK = the documented safe test. Decisive test: marker stored+reachable = the class.

### Upload-path traversal class
Filename traversal landing outside the upload dir. Decisive test: the landed path visible = confirmed (benign file).

## API testing

### GraphQL surface classes
Introspection/suggestion/batching (canon-II). Decisive test: schema map = the inventory.

### API-contract drift
Docs/OpenAPI vs live behavior divergence. Decisive test: spec-vs-live diff = the finding.

### API-chain exposure
Internal endpoints reachable only via the API tier's trust. Decisive test: the trust differential = the class.
