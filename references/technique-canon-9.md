# TECHNIQUE CANON IX — framework & CMS deep canon

_Every block is one technique: probe shape, decisive test, walls. Validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## WordPress depth

### REST user inventory
/wp/v2/users leaking login/slug/display-name of authors. Decisive test: anonymous GET — the identity list = the enumeration row.

### REST view/post-state leak
Status queries exposing draft/private posts via REST params. Decisive test: your own draft visible unauth = the class.

### Plugin fingerprint via assets
Plugin versions readable from asset paths/readme/changelog files. Decisive test: asset-path version map = the inventory crown.

### Theme upload path classes
Deprecated theme-upload remnants and zip-install endpoints reachable. Decisive test: endpoint auth-class = the row.

### Debug log exposure
debug.log under wp-content readable — its content IS the harvest. Decisive test: fetch with the control-path differential.

### XMLRPC posture
xmlrpc.php enabled with system.listMethods + pingback amplification posture. Decisive test: method list response = the finding.

### Ajax admin-probe classes
admin-ajax.php actions enumerable unauth (taxonomy/user hints). Decisive test: action catalog from the bundle + one benign action = the map.

### Update-channel posture
Plugin update URLs over http or unsigned — the MitM-class posture. Decisive test: update-source scheme audit = the row.

## Drupal / Joomla depth

### Services endpoint classes
Drupal services/controller endpoints anonymous (the /json paths). Decisive test: endpoint 200 vs the anon-gate class = the finding.

### Update-module exposure
update.php/authorize.php reachable = the posture row. Decisive test: reachability + auth-gate class.

### Twig detection class
Twig syntax acceptance (the {{7*7}} arithmetic at Drupal tier) — DETECTION only. Decisive test: arithmetic marker reflected.

### Joomla config classes
configuration.php exposure class + session handler posture. Decisive test: control-path differential fetch.

### Joomla update-server
Update server URL + scheme posture (http = the row). Decisive test: manifest parse.

## Spring depth

### Actuator env classes
/env /actuator/env returning config with secrets masked-or-not. Decisive test: response key inventory — unmasked secret keys = the crown.

### Heapdump class
/actuator/heapdump downloadable — the memory-material exposure (contents characterized only, never mined live). Decisive test: the artifact's presence + size = the finding.

### Gateway route classes
/actuator/gateway/routes exposing internal route map (the route-injection mechanism REPORTED, never fired). Decisive test: route listing = the inventory.

### Logfile actuator
/actuator/logfile serving live logs = the harvest class. Decisive test: fetch with control-differential.

### Jolokia/JMX classes
/jolokia reachable = the JMX bridge class (detection-only). Decisive test: version probe response = the finding.

### Devtools class
Spring devtools remote secret + restart endpoints in prod = the dev-in-prod class. Decisive test: endpoint behavior signature = the row.

## Django / Rails depth

### Debug page classes
DEBUG tracebacks exposing settings/secrets. Decisive test: forced 404/500 — the debug panel = the finding.

### Static/media exposure
MEDIA_ROOT serving uploads unauth + directory posture. Decisive test: upload-path fetch class = the inventory.

### ALLOWED_HOSTS gaps
Host-header acceptance producing cache/link poisoning (the canon-I twin). Decisive test: poisoned link in a response on your own session.

### Rails secrets-in-repo
secrets.yml/master.key committed classes (the repo-mining canon). Decisive test: recovered file content = the harvest.

### Rails render-params
render params[] legacy acceptance = the LFI class (detection). Decisive test: the error-class delta on your own request.

## Laravel / Node depth

### Laravel .env class
/.env fetchable — credentials material = the harvest (values masked in reports). Decisive test: control-path differential.

### APP_KEY class
APP_KEY exposure enabling signed-value forgery — DETECTION only (the mechanism documented, never forged live). Decisive test: the key string paired with its use-site.

### Storage listing class
/storage/app listing = the harvest row. Decisive test: directory-listing signature.

### Express stack-trace class
Error handler dumping stack/cwd/env fragments. Decisive test: forced error on a non-route = the finding.

### Node source disclosure
Sourcemaps/.map on chunks + source in prod = the info class. Decisive test: map fetch = the inventory.

### Prototype pollution server-side
Merge/deep-extend sinks reachable via JSON body __proto__. Decisive test: property-diff observable on your own session object = the class.

## Next / Nuxt depth

### Next-data payload leaks
__NEXT_DATA__ embedding private props for auth-gated routes. Decisive test: page payload diff unauth = the finding.

### Middleware bypass classes
_next path variants skipping middleware (the encoded-path family). Decisive test: variant through the edge = the class.

### Static-export exposure
Private pages in static exports (out/ directory). Decisive test: gated-route fetch unauth = the row.

### Nuxt payload/SSR leaks
window.__NUXT__ carrying internal state. Decisive test: payload parse on your own session = the class.

## ASP.NET / Java servers depth

### ViewState MAC classes
MAC validation absent/enforcement disabled — DETECTION-only (the deserialization mechanism reported). Decisive test: tamper → distinct MAC error vs acceptance.

### Machine-key exposure
machineKey in public configs/repos. Decisive test: recovered key string + use-site pairing = the harvest.

### customErrors off class
Stack traces on production errors. Decisive test: forced error page content = the finding.

### Tomcat manager residue
/manager,/host-manager 401-vs-404 classification (the residue class). Decisive test: the status class = the inventory.

### JBoss/JMX exposure
/jmx-console,/web-console residue classes. Decisive test: reachability + auth-gate = the rows.

### WebLogic/consola classes
Console endpoints default-posture detection. Decisive test: banner + auth-class = the inventory.

## CRM & integration platforms depth

### Salesforce LWR/Aura exposure
Component/Aura endpoints revealing metadata/guest-accessible data (the SF LWR canon class). Decisive test: the endpoint's guest response = the finding.

### Apex guest classes
Guest-profile Apex reachable = the platform class (detection-only). Decisive test: endpoint auth-stage classification.

### Webhook URL exposure (chat platforms)
Discord/Slack/Telegram webhook URLs in client bundles/repos — possession = forge-class. Decisive test: URL string + provider-format validation = the finding (never posted to).

### Bot-token-in-bundle class
Chat bot tokens embedded client-side = the takeover-prep class. Decisive test: token format + the API's validation response class (no authenticated action performed).

### Integration callback abuse
Platform callbacks (oauth/intercom-class) accepting forged payloads — signature posture detection. Decisive test: the callback's signature-verification refusal/acceptance behavior on YOUR test payload = the row.
