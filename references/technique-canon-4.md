# TECHNIQUE CANON IV — server & platform misconfigs, DB engines, queues, remote-access

_Every block is one technique: probe shape, decisive test, walls. Validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## Web-server misconfig classes

### Nginx alias traversal and off-by-slash
`alias` directives without trailing slash make /path../ escape the root. Decisive test: the off-by-slash variant (location /x { alias /srv/x/; } → /x../secret) against a control path — distinct file content = the class.

### Nginx merge_slashes and path normalization differentials
merge_slashes off plus auth-by-location lets //admin bypass location checks. Decisive test: doubled-slash and %-decoded variants of a protected path — one variant 200s where the canonical 401s = the finding.

### Apache .htaccess and directory-move classes
.htaccess exposure itself (fetch it), Options +Indexes (already DIRECTORY canon), and mod_userdir legacy. Decisive test: direct fetch of .htaccess — the file content IS the harvest.

### IIS short-name (8.3) enumeration
`~1` short-name requests enumerate files/dirs despite listing denial. Decisive test: /~s/~1 style probes yielding distinct 404-vs-200 classes for the control vs candidate — the oracle is the finding (read-only inventory).

### Tomcat manager and examples residue
/manager/html, /host-manager, /examples residue with default or weak gate. Decisive test: HTTP 401-vs-404 classification (401 = surface exists — the inventory finding), never a credential push.

### Spring Boot actuator exposure
/env, /heapdump, /actuator/env, /actuator/gateway — the actuators leak config/secrets/heap. Decisive test: GET each actuator path — JSON config with secret keys = the crown (values masked in the report to their presence, length-masked — NO-GAIN on the material itself).

### Spring Cloud Gateway and routing-injection classes
Documented actuator-driven route injection is REPORTED as the mechanism writeup; decisive test is the config-diff endpoint's presence, not the executed reroute.

### PHP-CGI and known wrapper classes
php:// wrapper acceptance and cgi-bin residue classes. Decisive test: the wrapper's error-class differential (documented variants only).

## Framework & app-server classes

### Django debug mode and ALLOWED_HOSTS gaps
DEBUG=true tracebacks (settings/secrets in the error page) and the 404 debug page. Decisive test: trigger a controlled 404/500 — the traceback panel is the finding.

### Rails mass-assignment and render-params classes
`render params[]` legacy and to_json exposure of sensitive columns. Decisive test: crafted params[:object] nested keys accepted on YOUR test record — the persisted field is the finding.

### Laravel .env and storage exposure
/.env fetch (already HARVEST), /storage path listing, APP_KEY in artifacts. Decisive test: control-path differential fetch — distinct content = the harvest.

### Node/Express stack-trace and source disclosure
Error handlers dumping stack + cwd, sourcemaps (already canon-I), .map on chunk files. Decisive test: forced error on a non-route — stack text with paths = the finding.

### Next.js/Nuxt data-leak classes
_next data payloads leaking props, static export leaking private pages, middleware bypass via _next paths. Decisive test: page props diff for auth-gated routes — private data in the payload = the finding.

### GraphQL operation-depth and cost classes
Depth/cost limiting absent → the CLASS is the missing guard, characterized with a bounded depth-10 introspection-style query (one request), never a sustained flood.

## Database-engine exposure classes

### PostgreSQL unauth and trust-posture
5432 reachable + trust/md5 posture revealed by error text. Decisive test: connection attempt reaching the AUTH stage (not network-refused) — the auth-stage response is the inventory finding.

### MySQL unauth and skip-grant residue
3306 reachable; error text reveals auth plugin posture. Decisive test: handshake banner + one anonymous connect attempt's error class.

### MongoDB unauth (27017) — the classic
No auth = full read exposure class. Decisive test: `mongosh --host` list-databases — inventory only; never write. A 200-ish auth-less listing = the finding.

### Elasticsearch unauth cluster (9200)
Cluster health + indices readable unauth. Decisive test: GET / and /_cat/indices — index inventory (names/shapes) = the finding; document reads stay sample-only (your own test doc).

### Memcached unauth (11211)
stats/version unauth — the exposure class (the 2016 amplification history is context). Decisive test: `memcstat`/stats command — the response = the finding.

### ClickHouse/CouchDB/InfluxDB exposure classes
Ping/version endpoints unauth → the posture row per engine. Decisive test: the engine's own ping URL — version + auth-refusal text = the inventory.

## Message-queue & streaming classes

### RabbitMQ management and AMQP anonymous
15672 management UI gate class; AMQP anonymous connect posture. Decisive test: management UI 401-vs-404 + AMQP connect reaching auth stage — inventory rows.

### Kafka anonymous and advertised-config leak
PLAINTEXT listeners unauth metadata reads. Decisive test: metadata fetch listing topics — the topic inventory = the finding.

### Redis pub/sub and staging keys
Subscribe-to-internal-channels class (read-only listen on YOUR session channel) — the channel taxonomy is the finding.

## Remote-access & VPN posture

### SSH posture depth
Algorithm inventory (ssh-audit lane), auth-methods ordering, MaxAuthTentрад behavior reflected in error cadence. Decisive test: ssh-audit output + banner parse — the posture table is the finding.

### RDP/NLA posture and NLA-absent classes
NLA required vs not (documented class), banner/tls posture. Decisive test: protocol handshake reaching the NLA stage — the stage reached IS the finding.

### OpenVPN/WireGuard control-channel posture
Management interfaces exposed, static-key legacy configs indicated by handshake types. Decisive test: control-channel handshake response class — posture row only.

### VNC/exposed-desktop classes
5900 unauth-ready banners (VNC auth none) — the banner = the exposure class (viewing is NEVER executed; the banner is the finding).

### Jump-host/bastion artifacts
Trusted host-key drift and banner/version disclosure on bastion lanes — era-stack mapping (kaisha canon) applied to remote-access tiers.
