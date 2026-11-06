# TECHNIQUE CANON II — injection depth, API surface, protocol classes

_Every block is one technique: probe shape, decisive test, walls. WSTG/CWE-anchored, validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## SQL Injection — per-DBMS

### MySQL error and time oracles
ExtractValue/`updatexml` error-channel reflection and `SLEEP(n)`/`BENCHMARK` timing channel — error-first, one timing sample per request against a 3-sample baseline. Decisive test: error string with controlled content echoed, or a stable timing delta ≥ 10× baseline.

### PostgreSQL error and CAST channels
`::int` cast failures and `generate_series` timing — the error text names the query context. Decisive test: cast-error reflection with a marker value embedded.

### MSSQL xp/error channel and stacked-query detection
`CONVERT` errors and batched `;WAITFOR DELAY` acceptance differ per driver. Decisive test: error reflection first; stacked-query acceptance only if the driver evidence suggests it (one probe).

### SQLite and Oracle dialect fingerprints
`sqlite_version()` inline and `dbms_random`/`utl_http` classes — dialect selection is the recon result itself. Decisive test: version-render or dialect-error delta.

### Second-order stored SQLi
Payload stored in profile/asset fields, executed by a LATER query (admin render, export job). Decisive test: your own stored payload flipping an error class in a downstream render you can read — the downstream context is the proof.

## NoSQL / NewSQL injection

### MongoDB operator and type confusion
`$ne`/`$regex`/`$where` and array-typed params accepted server-side. Decisive test: operator body on your own login/owner field — acceptance without the secret = the class; `$where` acceptance is the JS-execution variant (reported, never weaponized).

### Redis unauth command surface
INFO/CONFIG GET unauth = exposure class; never SET/DEL. Decisive test: INFO server on 6379 — the response body is the finding.

### Cassandra/CQL and Dynamo shape confusion
CQL string reflection and Dynamo attribute-condition confusion are the rarer shapes. Decisive test: quote/class marker reflection into the CQL error text.

## SSTI — per-engine

### Jinja2 and Jinja-flavored arithmetic
`{{7*7}}`→49, `{{7*'7'}}`→7777777 fingerprints jinja2; `{{config}}` exposure = the crown. Decisive test: arithmetic marker reflected exactly.

### Twig/Smarty/Freemarker/Velocity fingerprints
`{{7*7}}` variants per engine (twig `{{7*7}}` ok, smarty `{php}` legacy, freemarker `<#assign>`, velocity `#set`) — the fingerprint table IS the class map. Decisive test: one marker per engine until one renders.

### ERB/Mako/pebble/nunjinjucks
`<%= 7*7 %>` (erb), `${7*7}` (mako/pebble/nunjucks ambiguity resolved by error text). Decisive test: marker + engine-error cross-read.

### SSTI → RCE reported-not-executed
Gadget chains (jinja `__mro__` walks, freemarker `Execute`) are DOCUMENTED as the impact ceiling; the deliverable is the writeup with the marker-level proof — never the executed command. NO-GAIN.

## Deserialization — per-language

### Java gadget surface (read-only proof)
 ysoserial-class gadget chains proven via DNS-ping gadgets (URLDNS) only. Decisive test: serialized object whose gadget resolves DNS to your domain — the lookup is the finding; execution chains are reported as the class.

### .NET ObjectStateFormatter / ViewState
MAC-enabled vs legacy ViewState — the `__VIEWSTATE` parameter with tamper acceptance is the class. Decisive test: modified viewstate → distinct MAC error vs acceptance (acceptance = crown; never execute the gadget).

### PHP unserialize pop-chain DNS proof
`unserialize` entry points proven with a DNS-only pop chain (file_put → phar stream wrappers documented as the escalation class). Decisive test: OOB DNS from the phar/jdbc-style wrapper.

### Python pickle and Ruby Marshal
Pickle opcodes/Marshal gadgets DNS-proven the same way — OOB-only, execution reported.

## XXE — depth

### Parameter entities and OOB variants
`%remote;` parameter-entity exfil for filteredXXE contexts, error-based local read. Decisive test: OOB arrival at your listener from the parameter entity; error-message file reflection as the alternate channel.

### XXE → SSRF pivot (metadata)
External entity aimed at 169.254.169.254 = the cloud-pivot class. Decisive test: entity response carrying instance metadata — the pivot is characterized read-only.

### XInclude / SOAP / SVG-doc types
Fragment-level XML parsers (XInclude on a node, SOAP body, SVG/image upload parsing) carry the same entity class without full-document control. Decisive test: OOB marker through each fragment type.

## SSRF — chains

### Redirect-based SSRF
An open redirect chains an SSRF-protected fetch past the allowlist. Decisive test: SSRF-prone param → in-scope redirector → internal marker URL — the fetch following the redirect IS the proof (one hop, read-only).

### DNS rebinding shape
TOCTOU between resolve and fetch — characterized in the lab replica (rebinding needs your own authoritative DNS). The live test registers the TOCTOU hypothesis with the fetch-time evidence you can observe.

### Gopher/dict protocol handlers
Legacy URL handlers turn SSRF into protocol talk. Decisive test: a gopher CRLF payload reaching an internal listener you control — handler presence = the class.

### Cloud metadata SSRF per-provider
169.254.169.254 (AWS/Azure/GCP), `metadata.google.internal` — IMDSv2/azure-token enforcement = mitigated negative (bank it). Decisive test: SSRF response carrying instance-id/subscription-id, or the documented refusal.

## API-surface classes

### REST mass assignment depth
Role/entitlement fields beyond the obvious (`role`, `tenantId`, `isStaff`, `quota`) re-bound on PUT/PATCH. Decisive test: unknown-field probe (send one invented field + one plausible) — echoed/persisted = the class; persisted-and-effectful = the crown (your own principal only).

### API version shadowing
`/api/v2` allowing what v1 patched (or v0/internal still live). Decisive test: same request across version prefixes — a privilege delta across versions is the finding.

### API-key-as-URL-parameter
Keys in query strings leak via referrer/logs/history (the SPY-048 class family). Decisive test: the key accepted as query param while the docs demand a header — the acceptance is the finding.

### Webhook SSRF and replay
User-registered webhooks pointing at internal ranges (SSRF class) and unsigned webhook payloads (replay/forge class). Decisive test: webhook delivered to YOUR listener (SSRF proof), or a replayed payload accepted twice (replay proof).

### IDOR beyond the object id — filter/sort leakage
Enumeration via filter operators (`?sort=-balance`) and range queries reading relative order without direct object access. Decisive test: sort/filter on a field across two of YOUR objects revealing a third's rank — the oracle is the finding.

### JWT implementation families
`none`-alg acceptance, kid-injection, jku/x5u self-keying, weak HMAC secrets (tested offline against a known dictionary ONLY on your own tokens). Decisive test per family: acceptance delta of the forged-but-harmless token.

## HTTP/2 & HTTP/3 classes

### h2c smuggling and header-based downgrade
Upgrade: h2c accepted on a proxy front = smuggling class. Decisive test: lab-replica h2c handshake through the front, one probe pair, timing delta — never a burst at a shared edge.

### CONTINUATION flood / rapid reset (documented DoS classes)
Characterize as EXPOSURE (does the edge cap CONTINUATION frames/reset rate?) — register the cap absence as the finding; the flood itself is NEVER fired outside the dojo lab.

### Cookie/HPACK compression crimes-shape
Cross-origin compression oracles (length-differential on secrets echoed into compressed structures). Decisive test: lab replica with a secret + compressed echo — the byte-length oracle is the proof.

## WebSocket classes

### Cross-site WebSocket hijacking (CSWSH)
WS handshake rides cookies without Origin checking — a page YOU control opens the socket with the victim's session. Decisive test: your own two-browser harness — Origin=evil.example accepted = the class (your own principal on both sides).

### WS state confusion across frames
Session/identity state set in frame N trusted in frame N+1 (the SPY-048/069 family). Decisive test: mirror the app's packet types exactly (connect-ack vs data-gate — the engagement-ops recipe) and show frame-level state carry — mis-framing is YOUR bug, not a finding.

### Subprotocol/namespace confusion
`Sec-WebSocket-Protocol` and socket.io namespace gates answering when they should not. Decisive test: the anon namespace CONNECT ack (type-matched to the app) = the exposure class.

## TLS & network-intel classes

### JA3/JA4 client fingerprints (infra intel)
Fingerprint the EGRESS the service expects vs accepts — anomalies map bot-walls and API tiers. Decisive test: same request two fingerprints — differential handling = the intel (register as recon, not vuln).

### Certificate-transparency intel depth
crt.sh/certspotter + live-cert SAN mining (the CT-log lane in the ops canon) — wildcard/SAN/sibling-brand exposure is the inventory crown. Decisive test: SAN list from a live handshake naming hosts DNS never published.

### Session resumption and renegotiation posture
Resumption across IPs and insecure renegotiation accepted = posture findings. Decisive test: openssl -reconnect session-reuse behavior, renegotiation error class.

## Client & browser depth

### XSS per-execution-context
HTML-body, attribute, JS-string, URL-attribute (`href`/`src` javascript:), and CSS contexts each need THEIR encoding-vocabulary variant. Decisive test: the reflected marker in the correct context form — context-specific execution in YOUR session is the proof; stored/cross-principal framing stays hypothesis without a second principal.

### Service-worker and postMessage depth
SW scope hijack class (register SW from a writable path) and postMessage targetOrigin='*' with sensitive payloads. Decisive test: message received from YOUR origin — the acceptance IS the finding.

### XS-Leaks (error/timing/referrer oracles)
Response-length, status-error, and frame-count oracles reading cross-origin state. Decisive test: the oracle's binary answer about YOUR OWN two records — the measurable delta is the finding.

### CSS injection and clickjacking depth
Attribute-exfil CSS and framable state-changers (padding/preview techniques). Decisive test: local harness render — the exfil channel shown in the lab, never against a third party.
