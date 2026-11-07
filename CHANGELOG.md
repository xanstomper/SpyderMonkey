# Changelog

All notable changes to SPYDERMONKEY, newest first. Dates are UTC; versions are
the dispatcher release (`SKILL.md` frontmatter).



## v5.15.0 — THE CHAINS AS MCP TOOLS (2026-11-06)

- **MCP 52 → 79 tools.** All 23 feeding chains exposed as callable MCP tools
  (arsenal_chain_recon … arsenal_chain_cms_full — dry_run plans without
  executing) + `arsenal_run` for named single/multi-tool runs. Every call is
  scope-gated through the arsenal's shared authority — out-of-estate targets
  refuse at rc=1.
- No installs on the operator box (operator directive): dormant wrappers stay
  defined-and-routable; they activate wherever the fleet runs.
- Verified: mcp --test green (79 tools) · live lab chain call scope_ok=true ·
  selftest + ci_smoke green before push.

## v5.14.0 — THE METHODOLOGIES CLAIMED: WSTG + MASTG FULL CANON (2026-11-06)

- **Arsenal 258 → 296 wrappers.** NSE batch 5 (http-grep, http-malware-host,
  http-method-tamper, http-phpself-xss, http-stored-xss, http-title, http-trace,
  http-vuln-cve2014-8877, http-wordpress-enum, rdp-vuln-ms12-020, rmi-dumpregistry,
  rsync-list-modules, smb2-vuln-uptime, smb-enum-domains/groups, smb-ls,
  smb-mbenum, smb-os-discovery, smb-vuln cve2009-3103/cve2017-7494/ms06-025/
  ms07-029/ms08-067/ms10-054/ms10-061, smtp-vuln cve2010-4344/cve2011-1764,
  snmp-sysdesc, ssh-auth-methods, ssh-hostkey, tftp-enum, whois-domain,
  wsdd-discover) + nuclei ssrf/xss/lfi/rce template lanes + skipfish.
- **Technique corpus 31,172 → 33,052 files** (1,337 base + 31,715 expanded,
  0 orphans): canon-11 — the FULL WSTG test catalog claimed (info-gathering,
  authN, authZ, session, data-validation, error, crypto, business-logic,
  file/upload, API — every test as a technique with probe shape + decisive
  test + walls) + canon-12 — the MASTG check catalog claimed (storage, crypto,
  auth, network, platform, resilience classes, LAB-ONLY framing).
- **The documented universe is now claimed end-to-end:** WSTG + MASTG + API
  top-10 + cloud per-service + framework/CMS + AD/K8s + binary/protocol RE +
  DNS/email + the engagement canons. Every block carries a Route table into
  the 296-tool arsenal.
- Verified: arsenal verify ALL PASS · skilltree ALL PASS · selftest 28/28.

## v5.13.0 — THE BRIEFING DISCIPLINE · ROUTE TABLES · MULTI-STEP GATE (2026-11-06)

- **The mandate changes how agents work (v5.13):** the Briefing Discipline —
  BRIEF ONCE BATCHED: after P0, 3-5 multi-choice option questions in ONE turn
  (scope confirm · noise budget · lanes · vantage · deliverable form) with the
  recommended pick marked and justified; DECISION POINTS batched identically
  (unlocked lane, dry noise budget, ambiguous class, chain pricing); never
  one-question-per-turn, never re-ask; scope.json read FIRST; unanswered
  options default to the recommendation; ZERO-BLOCKER HOLDS between briefings
  (scope-shaping, not permission-seeking); every option set demonstrates a
  capability the operator hadn't considered.
- **Route tables in every technique file (density upgrade):** skilltree now
  emits a `## Route` section per file (base, variant, and chain-composition)
  — class → the exact arsenal probes + chains that fire it, with the scope
  gate reminder. A model reading any of the 31,172 technique files knows the
  live probes to run without touching the index.
- **The multi-step gate:** `_flow_http` (stdlib cookiejar opener) + the flow
  probe shape — flow cards carry a `__PAYLOAD__` marker through a request
  SEQUENCE (login → action → result), baseline/attack runs each substitute
  the marker, the verdict diffs the FINAL step; every step url passes the
  scope gate. Logic chains are now provable, not hypothetical.
- **Hypothesis engine:** 3 new tests (flow marker substitution, per-payload
  substitution, chain-card refusal) — 31 in the hypothesis suite, 61 total.
- **CI wired:** .github/workflows/ci.yml runs scripts/ci_smoke.sh verbatim on
  every push (the maintenance doctrine's closure — stale commits fail CI).
- **README synced** to v5.13 counts (31,172 corpus · 1,255 base · 258 tools).
- Verified: selftest + ci_smoke green locally before push.

## v5.12.0 — ROUTING SURFACE ×13: 258 TOOLS · 31,172 TECHNIQUES (2026-11-06)

- **Arsenal 212 → 258 wrappers, chains 16 → 23.** NSE batch 4 (http-auth-finder,
  robots/sitemap intel, waf-detect/fingerprint, traversal, sqli-oracle,
  slowloris-capacity CHECK, smb-vuln webexec/doublepulsar, dns brute/SRV/AXFR,
  smtp-enum-users, iscsi, mssql-empty, ntp, s7-info (ICS), upnp, x11-access) +
  script-family lanes (nmap-script-http/smb/ssl/discovery/default) + nuclei
  per-tag lanes (tech/network/dns/config) + netexec protocol splits (smb/ldap/
  winrm/mssql) + dnsrecon zonewalk/reverse + tools (tlsfuzzer, rdp-sec-check,
  snmp-check, kcat, davtest) + deep-sweep plans (dirsearch-deep, wfuzz-deep).
- **New lanes:** cve-sweep · exposure-sweep · takeover-full · cloud-full ·
  db-full · mail-full · cms-full.
- **Technique corpus 28,296 → 31,172 files** (1,255 base + 29,917 expanded,
  0 orphans): canon-8 (API top-10 + AWS/Azure/GCP/K8s per-service), canon-9
  (framework/CMS depth: WordPress/Drupal/Joomla/Spring/Django/Rails/Laravel/
  Express/Next/ASP.NET/Java/CRM/chat-integrations), canon-10 (MASTG mobile
  depth, binary/protocol RE, DNS depth, email infrastructure) — written
  in-session after the model provider 503'd the delegated canon writers.
- **Densifier:** _extract_blocks now splits #### headers too — deeper canon
  = denser tree.
- **Hypothesis engine completed:** path-probe + cve-map card shapes wired into
  _hypothesis_request_pair (the shipped tests now pass; CI green).
- **Verified:** arsenal verify ALL PASS (258 tools · 23 chains) · skilltree
  ALL PASS (1,255 + 29,917 links, 0 orphans) · selftest 28/28 · ci_smoke ALL
  PASS · both trees identical.

## v5.11.0 — VULN-CHECK DEPTH + SOURCE-PULL LANE (2026-11-06)

- **Arsenal 200 → 212 wrappers.** Vuln CHECK batch 3 (nmap http-vuln CVE checks:
  Struts cve2017-5638, Drupalgeddon cve2014-3704, http.sys ms15-034, php-cgi
  cve2012-1823, ColdFusion cve2010-2861, Rails cve2013-0156 — all DETECTION-only
  scripts; ftp-vsftpd-backdoor, ftp-proftpd-backdoor, http-default-accounts) +
  the **source-pull lane** (wget-mirror depth-2 recursive pull, httrack full
  public-source mirror, nmap-allports thorough sweep). Mirror lane feeds the
  content chain.
- **Tunneling note:** the relay lane (dispatcher `relay init|list|exec` —
  Ed25519 ssh-paired nodes, scope-gated) + the sanctioned SOCKS egress recipe
  (vermes -D 1080) remain the family's tunneling capability — arsenal wrappers
  do not duplicate plumbing the relay system already owns.
- **Wall held:** destructive/DoS tooling NOT added — the family's own doctrine
  (destructive end-states refused; DoS = capacity-exposure rows, never fired).
  Verified: arsenal verify ALL PASS (212 tools) · selftest 27/27.

## v5.10.0 — THE 200-TOOL ARSENAL (2026-11-06)

- **Arsenal 103 → 200 wrappers, ALL REAL entries.** Three honest levers:
  (a) **17 targeted NSE validation probes** batch 1 — named checks the model
  routes to directly (http-enum, http-git, http-backup-finder, http-methods,
  http-cors, http-userdir-enum, http-shellshock, ssl-heartbleed, ssl-ccs,
  ssl-enum-ciphers, smb-security-mode, smb-vuln-ms17-010, mysql-empty-password,
  ftp-anon, dns-nsec-enum, smtp-open-relay, vulners);
  (b) **28 NSE probes batch 2** — vuln CHECKs + service inventories (ssl-poodle,
  ssl-drown, ssl-logjam, smtp-commands, imap/pop3-capabilities, mongodb-info/
  -databases, redis-info, mysql-info, ms-sql-info, http-devframework,
  http-iis-short-name, http-aspnet-debug, http-drupal-enum, http-wordpress-plugins,
  http-apache-server-status, http-php-version, smb-enum-shares/-users,
  smb2-capabilities, smb-vuln-conficker, nfs-showmount/nfs-ls, rpcinfo,
  ipmi-cipher-zero, http-open-proxy, ftp-bounce, rdp-ntlm-info, vnc-info,
  telnet-encryption, sip-methods, ssl-cert, http-cookie-flags);
  (c) **mode splits + distinct tools** — nmap udp/fast/discovery/vuln modes,
  gobuster vhost/dns/s3, nuclei cve/misconfig/exposure/takeover/token tag lanes,
  dnsx brute/reverse, dig AXFR/MX/TXT/NS/SOA/CNAME record lanes, amass-intel,
  ffuf-vhost/deep, gobuster-deep, ldapsearch-enum, curl-cors/trace,
  testssl-protocols/ciphers, sslyze-cert, arp-scan-lan, netdiscover-passive,
  gowitness, cmseek, webanalyze, urlcrazy, cloudlist, smbmap, crackmapexec
  (legacy-name coverage), finalrecon, gitleaks, o-saft, paramspider, swaks,
  ssh-keyscan, asnmap.
- **Every entry is a distinct probe shape** — no filler, no invented binaries.
  The arsenal counts real routable checks, not double-counted duplicates.
- **Verified:** arsenal verify ALL PASS (200 tools · 16 chains · scope refusal ·
  kernel --out) · selftest 27/27 · 18 wrappers live-installed on the operator box.

## v5.9.0 — THE BIG ARSENAL: 103 TOOLS · 28,296 TECHNIQUES (2026-11-06)

- **Arsenal 73 → 103 wrappers.** Packet lane (hping3, nping, traceroute, mtr,
  fping, arp-scan, netdiscover, tcpdump, tshark, ngrep, nc, zmap — capture lanes
  read-only), cloud lane (s3scanner, cloudbrute, kube-hunter), fuzz confirm-aid
  lane (xsstrike, commix, tplmap, nosqlmap, dotdotpwn), crawlers (dirhunt,
  gospider), API discovery (kiterunner, webtech), secret scan (trufflehog
  verified-only), kerberos enum (kerbrute), device lane (adb lab), file-exposure
  (snallygaster), BMC (ipmitool mc info), capture proxy (mitmdump). Chains
  13 → 16: `cloud`, `packet`, `fuzz`.
- **Technique corpus 22,888 → 28,296 files.** canon-7 (MASTG depth: storage/
  clipboard/logcat/CT-of-mobile-APIs/key-extraction/attestation/posture; binary
  & protocol RE: the chunk-extraction recipe, string-table replay, runtime
  crypto hooks, wire-format replication, WASM modules, packet-type taxonomy,
  dangling versions; edge/CDN: vhost collisions, origin-cert tri-brand class,
  526 incidents, cache-key, geo/WAF inconsistency; ledger-discipline classes)
  + the **`machine` auth axis** (service-principal/API-key/SA-token differential
  — key scope, cross-tenant reach, audit trail) multiplying the whole corpus.
- **Matrix:** 195 binding keys (WSTG · MASTG · PTES-WIN/ICS/RA/OPSEC · CWE ·
  ATT&CK · ICS T-code 0886) · 20 platform families.
- **Verified:** skilltree --verify ALL PASS (1,126 base + 27,170 expanded,
  0 orphans) · arsenal verify ALL PASS (103 tools · 16 chains) · selftest 27/27.

## v5.8.0 — MAX SCALE: 22,888 TECHNIQUES · 73 TOOLS · 13 CHAINS (2026-11-06)

- **Arsenal 65 → 73 wrappers.** DB confirm-aid lane (psql, mysql, mongosh,
  memcstat), takeover lane (subzy), harvest lane (git-dumper, cewl), WAF
  fingerprint (whatwaf). Chains 11 → 13: `db` (engine handshake/auth-stage
  probes) + `takeover` (subzy/dnstwist/dnsx/subfinder).
- **Technique corpus 21,521 → 22,888 files.** Three new canon volumes:
  `technique-canon-4.md` (server misconfig per-webserver: nginx alias/off-by-slash,
  IIS 8.3, Tomcat residue, Spring actuators; framework classes Django/Rails/
  Laravel/Express/Next; DB-engine exposure PostgreSQL/MySQL/Mongo/Elasticsearch/
  Memcached/ClickHouse/CouchDB/InfluxDB; queues RabbitMQ/Kafka; remote-access
  SSH/RDP/VNC/VPN posture), `technique-canon-5.md` (OSINT depth: breach row-
  correlation, code-search dorking, git-object recovery, CT lifecycle, ASN/
  passive-DNS, zero-document artifact strings; LAB-ONLY wireless/hardware: WiFi/
  BLE/SDR/NFC/UART/JTAG/SPI; supply-chain: dependency-confusion, vendor-SDK
  SPY-095 class, SRI/CSP; ICS/SCADA read-only pointers), `technique-canon-6.md`
  (crypto classes: entropy/PRNG, IV/ECB, padding-oracle shape, length-extension,
  key-in-code; auth-protocol depth: Kerberos enum set, NTLM relay config posture,
  OAuth per-grant, SAML profiles, WebAuthn, cookie depth; anti-abuse: CAPTCHA
  anatomy, anti-bot matrix, WAF evasion vocabulary, rate architecture; the
  casino verification canon: PF chains, RTP sweep discipline, client-bet APIs,
  two-salt traps, feed-fabrication).
- **Matrix widened:** new platforms db, queue, lb, wireless (LAB-ONLY), embedded,
  desktop + 41 new binding keys (182 total, WSTG/MASTG/PTES-ICS/CWE/ATT&CK).
- **Verified:** skilltree --verify ALL PASS (1,102 base + 21,786 expanded,
  0 orphans) · arsenal verify ALL PASS (73 tools · 13 chains) · selftest 27/27.

## v5.7.0 — CANON DEPTH: TECHNIQUE UNIVERSE CLAIMED (2026-11-06)

- **Arsenal 48 → 65 wrappers.** New lanes: CMS (wpscan, joomscan, droopescan,
  cmsmap), Windows/SMB (smbclient, rpcclient, ldapsearch, enum4linux-ng,
  netexec read-only module pass), OSINT (assetfinder, findomain, dnstwist,
  shodan, hakrawler, linkfinder, xsser, zaproxy baseline). Chains 8 → 11
  (`cms`, `win`, `osint` feeding chains added; feed parsers + canon classes
  CMS/SECRET extended).
- **Technique corpus 20,041 → 21,521 files.** Two new canon volumes:
  `technique-canon-2.md` (injection depth per-DBMS/engine/language, API-surface
  classes, HTTP/2+3, WebSocket, TLS/JA3, XS-Leaks) and `technique-canon-3.md`
  (cloud per-provider AWS/Azure/GCP, K8s/Docker/CI-CD, AD read-only enum
  classes, MASTG mobile classes, CMS depth, mail/DNS depth, business-abuse
  depth). ~110 new base blocks; 141 binding keys (was 103); new platform
  families: cms, mail depth, windows/SMB, mobile MASTG.
- **Verified:** skilltree --verify ALL PASS (1,028 base + 20,493 expanded,
  0 orphans) · arsenal verify ALL PASS (65 tools · 11 chains) · selftest 27/27.

## v5.6.0 — THE REASONING ENGINE (2026-11-06)

- **`hypothesis gen|brief` — the engine that guides a model to NEW findings.**
  A new stdlib module (`scripts/hypothesis.py`, pure reasoning — no live fire)
  turns the family's EXISTING datasets into ranked, testable, wall-checked
  hypothesis cards:
  - **surface** — the testers' own param vocabularies + endpoint shapes
    (13 param patterns, 12 endpoint patterns) reason from the mined context
    (or the ledger's own assets, when the crawler has not run) to candidate
    classes not yet confirmed on each asset.
  - **cve-map** — tech fingerprints (express/php/jvm/python/graphql/dotnet/
    jwt/edge) map to DOCUMENTED CVE-class families (CWE-anchored: CWE-943
    operator injection, CWE-98 wrapper traversal, CWE-1336 SSTI, CWE-347
    alg=none, CWE-200 exposure…) each with a ready probe shape.
  - **variant** — every CONFIRMED finding opens its documented
    encoding/marker variant families (overlong-UTF8, double-encoding, wrapper
    streams, mixed separators + `....//` filter evasion, unicode CRLF,
    scheme-relative redirects, blind-bool operators, kid-path markers,
    event-handler XSS contexts, rare loopback encodings) — the payloads the
    standard battery never fired on that asset.
  - **chain** — when a kill chain's `need` classes are confirmed but its
    `give` classes are not, a completion card is emitted (5 chain specs).
- **The ranker** — priors-weighted (base class prior × learned prior from
  self-play × kind weight × confirmed-elsewhere boost), scores bounded 0–1.
- **The model brief** (`hypothesis brief`) — the guidance document any model
  consumes: top-ranked cards + the exact loop (read the `why` trace → load
  the lazy citations → fire the probe through `gate` → CONFIRMED lands in
  the ledger → regenerate) + the rules (documented classes only; novel
  INSTANCES, never novel weapon classes; every claim through the 3-gate).
- **The wall, in code** — every card whose asset fails the scope authority is
  marked `scope: blocked` at generation (execution would refuse anyway); all
  cards restate the five walls. Generation is offline; execution stays in the
  dispatcher's scope-gated, evidence-gated kernel.
- **The kernel plans it** — a new `hypothesis-gen` directive fires when
  confirmed classes and untested surface coexist; MCP exposes
  `hypothesis_gen` + `hypothesis_brief` (54 tools now).
- **PROVEN end-to-end on the lab**: the engine ranked a `....//` filter-
  evasion TRAVERSAL variant the 18 batteries never fired → the gate confirmed
  it (404→200, passwd content, confirm-token) → SPY-019 CONFIRMED →
  regeneration absorbed it (the variant is no longer proposed on that asset;
  the surface dedupe closed). The "find new ones" loop is closed and honest:
  DISPROVEN variants (e.g. octal-loopback SSRF against a resolver that will
  not parse it) register nothing.
- **Gate hardening from the loop proof**: dedupe now compares
  scheme+host+path (a query-form difference never defeats it) and fired-
  payload matching handles the URL-encoded form the gate stores.
- **Tests**: 18 new hypothesis tests (surface mapping, dedupe semantics,
  variant fired-matching, chain closure, rank ordering, learned-prior shift,
  brief shape, corrupt-ledger tolerance) — 48 total, all green.

## v5.5.0 — THE BATTERY EXPANSION (2026-11-06)

- **Seven new differential testers — 11 → 18 batteries.** Every one a
  documented-PoC class, differential, evidence-gated, NO-GAIN:
  - **REDIRECT** (CWE-601) — open redirect; the proof lives in the Location
    header swapping to a foreign origin. Probes use the `.invalid` TLD: it never
    resolves, so no third party is ever contacted. The dangling
    `SSRF/REDIRECT` Location fallback in the sweep finally has its tester.
  - **CORS** (CWE-942) — Origin-reflection differential: neutral Origin is the
    baseline, a foreign Origin the attack; ACAO echoing the foreign origin
    (or `*` with allow-credentials) is the proof. Read-only — the Origin header
    triggers no fetch.
  - **NOSQL** (CWE-943) — operator injection: `$ne` / `$gt` / `$regex` /
    `[$ne]=1` reaching a document interpreter; auth-bypass marker is decisive.
  - **CRLF** (CWE-113) — header injection: `%0d%0aX-Probe` / `Set-Cookie`
    markers; an attacker-controlled header appearing in the attack response's
    header block (and not the baseline's) is the split proof.
  - **HARVEST** — 15 predictable paths (`.env`, `.git/HEAD`, `backup.zip`,
    `debug`, `actuator/env`, `swagger.json`…); a guaranteed-missing control
    path is the baseline, so a soft-404 target registers NOTHING.
  - **DIRECTORY** (CWE-548) — 10 autoindex roots; `Index of /` is decisive.
  - **REPLAY** (CWE-837) — idempotency differential: the same logical request
    fired twice (N=2, validation-only); a countable effect that increments is
    the proof. Stateless endpoints register nothing.
- **The header-aware differential gate.** `_tester_verdict`'s early
  identical-response gate now also diffs non-volatile headers for the
  header-evidence classes (CORS · CRLF · REDIRECT) — a body-identical pair with
  a header delta is still a live differential, and the clock never becomes a
  finding.
- **The demo replica grew the matching flaws** (`/redirect`, `/api/data`,
  `/api/login2`, `/greet`, `/.env` + 5 more harvest paths, `/files/` autoindex,
  the webhook idempotency counter) — `testers --demo` proves all seven new
  classes CONFIRMED with zero setup. Bonus: the replica's `/redirect` endpoint
  also reflects raw values into the Location header, and the CRLF battery
  catches it — two classes proving on one flaw.
- **Two new chain patterns — 8 → 10.** `cors_credential_read` (ACAO reflection
  + credential endpoint → cross-origin credential read) and `nosql_authn`
  (operator injection + auth surface → forged authentication).
- **The arsenal grew — 20 → 30 executors, 4 → 6 feeding chains.** New: arjun
  (hidden params), corsy, crlfuzz, subzy (dangling-CNAME checks — pairs with
  the takeover engine), s3scanner + cloud_enum (read-only cloud exposure), the
  Harvester (passive OSINT), dirsearch + feroxbuster (content discovery),
  gitleaks (in-scope repo secret scanning). New chains: **cloud**
  (s3scanner → cloud_enum) and **osint** (theharvester → subfinder → dnsx).
  Four new canon classes feed the ledger bindings: REDIRECT · CORS · CRLF ·
  NOSQL.
- **Counts updated everywhere**: `verify` pins 18 testers, the sweep banners
  are dynamic, `capabilities` introspects 22 confirmable classes live,
  ci_smoke asserts count-agnostically. README/SKILL numbers match the code.

## v5.4.0 — THE SESSION INJECTION (2026-11-06)

- **`/spydermonkey` — one word, the mandate owns the session.** The canonical
  contract lives in `references/mandate-session.md` (print with
  `spydermonkey mandate --session [--file]`). It declares the dispatcher's role,
  the loop (state → directive → act → absorb → report), the evidence discipline
  (gate or hypothesis), the persistence clause (every message is a mandate
  message until release), and the absolute stop conditions — walls intact,
  always.
- **THE HOLD** — persistence protocol baked into the contract: persist the P0 to
  campaign manifest + context on entry, re-read the campaign files (ledger ·
  phases · chains · estate memory) every session, re-inject after context
  compaction, and close with `train` (priors the planner re-weights).
- **`mandate --session`** flag added to the dispatcher. Tests pin the contract's
  shape (walls present, persistence clause, release phrase).
- **Wired agents:** OpenCode — `/spydermonkey` switches the session to the
  global `spydermonkey` primary agent (`~/.config/opencode/agents/spydermonkey.md`,
  mandate = the agent's system prompt; `/build` switches back). Claude Code —
  `/spydermonkey` command (`~/.claude/commands/spydermonkey.md`). Hermes —
  `/spydermonkey` (skill). Cline CLI — `spydermonkey-cline "<brief>"`
  (system-prompt override via `cline -s`). Any other agent — `mandate --session`
  prints the contract for any prompt slot.
- **`mandate --session`** flag added to the dispatcher. Tests pin the contract's
  shape (walls present, persistence clause, release phrase).
- **Reliability + self-improvement loop closed.** Trace collection now actually
  works end-to-end: `--trace-file` lives on the `loop` parser (previously added to
  `watch` only — the collector could never be enabled) and `watch` forwards it to
  the `loop` subprocess; the trace mislabels `directives_planned` → `step_number`.
- **The chain-detector fixes upstreamed.** `_chainable_estate` / `_chainable_signal`
  (estate-scoped chain pairing + SPA-shell/lookalike-negative poisoning) and the
  content-derived `UND-<sha1>` ids (a running counter orphaned saved chain rows as
  the ledger grew) are now in the repo, not only in the hermes skill copy — the
  skill copy was then re-synced over the repo (scripts, tests, catalog, contracts;
  personal SKILL.md engagement notes preserved).
- **The agent remembers.** Global `AGENTS.md` now carries a one-line reminder to
  invoke `/spydermonkey` for offensive-security engagements — reminder, not a
  hijack; the walls remain non-negotiable.
- Walls unchanged and non-negotiable: the mandate is a persona contract, not a
  bypass. Injected everywhere, the scope authority is still the estate's only
  verdict — findings that survive are the product.

## v5.3.0 — THE KNOWN-TOOL CATALOG (2026-11-06)

- **`catalog` — 1,053 known offensive tools, lazy-loaded on any machine.** A
  reference index in `references/tool-catalog.json` (152 KB, zero deps):
  names, categories, one-line descriptions, mode (passive/active), and source
  pedigree (**curated** 636 hand-picked entries · **apt** 130 harvested from the
  Ubuntu package index with real short-descriptions · **kali** 290 from Kali's
  official tools index). Actions: `stats` · `categories` · `list [--cat]`
  · `search <term>` · `show <name>` — all `--json`-clean for agents.
- **Info only, never execution.** The catalog executes NOTHING. Firing any
  tool still goes through `arsenal` (installed executors only, 4 feeding
  chains, shared scope authority, kernel `--out` schema). The map is not the
  gun — an agent reads the catalog to pick the tool, the scope wall still
  decides whether it may run.
- **Lazy by construction.** The JSON is loaded once per process, on first use
  (`_catalog()`), never injected into a prompt; agents pay for the 3 rows they
  query, not the 1,053.
- **MCP 50 → 52.** New `catalog_search` and `catalog_show` tools (same
  scope/doctrine as everything else). Docs updated.

## v5.0.0 — SELF-KNOWLEDGE · SELF-PROTECTION · GROWTH (2026-11-04)

- **`capabilities` — the mirror of self.** The live-introspected capability
  registry: engines × presence, every confirmable class, per-tester battery
  sizes, takeover fingerprints, executor inventory (real tools installed on THIS
  machine), kernel directives, corpus size, learned priors. Read from the code,
  never from a doc — the planner and any agent ground on it.
- **`protect` — the family guards the OPERATOR.** `protect posture` prints what
  this machine can leak (user · hostname · home · git emails · LAN IPs);
  `protect scan [--target T | --all-campaigns]` walks every campaign artifact
  and finds each operator string in it (git-email · lan-ip · home-path ·
  identity leaks), rc=1 while anything leaks, state written for barbican
  sanitize to strip — and protect re-proves it clean.
- **Payload batteries + the 9th tester.** Every tester now carries a real
  battery (INJECTION 14 markers: SQL error-oracles, SSTI families
  {{}}/${}/<%}/#{}, command `;id`/`$(id)`/backticks, LDAP wildcard; TRAVERSAL 8
  encodings incl. double-encoded + unicode; SSRF 7 targets incl. dword/hex/
  decimal-host and IPv6 loopback; IDOR 6 swaps; AUTHZ 6 flips; AUTHN 8;
  BIZLOGIC 6 incl. float-overflow) and the JWT tester joins (alg=none,
  empty-signature, confused-deputy).
- **Gate v2 — body differentials.** `--json-body` + `--attack-body` (JSON POST
  baseline vs swapped attack body — the mass-assignment/price-tamper proof
  shape) and `--cookie` riding both requests.
- **`train` — SELF-PLAY.** The family attacks the dojo range (every replica
  class), measures per-class hit rates, and writes the priors file; the
  planner ORDERS PROBES BY WHAT WORKS. The family gets sharper every run.
- **`memory` — ESTATE MEMORY.** Every completed loop writes what was confirmed
  per target; the next campaign on that estate re-ranks the planner ("estate
  memory: JWT confirmed here before — priority"). `--forget` wipes.

## v4.0.0 — THE CONTROL PLANE (2026-11-04)

- **One scope authority.** New `scripts/scope_authority.py` is the single estate
  verdict for the dispatcher, Arsenal, the MCP server, the live bench, and every
  live probe. Exact host, subdomain, `*` wildcard, CIDR, URL-path, and port
  matching; deny precedence; expiry; lab allowance; rate rules; audit history;
  atomic `0600` writes. `scope add|remove|extend|history` and `doctor --fix`
  complete the lifecycle.
- **Campaign lifecycle.** `campaign init|list|show|timeline|archive|purge|close`
  with a manifest, append-only `events.jsonl`, timestamped archives, and a purge
  that refuses without `--force`. Target names are normalized before any path is
  built — traversal is closed.
- **Ten machine-checked mandate contracts.** `references/mandates/00-barbican.md`
  … `09-dojo.md`, each with axis · law · handoff · evidence · fleet · failure.
  `mandates list|show|verify` checks presence, numbering, phase, and sections;
  the same registry drives `tree`/`route`/`fleet`/`next`.
- **Machine-readable by default.** `--json` works on any command in any position;
  `--scope-file` and `--version` are global; structured errors stay on stderr.
  Exit codes: `0` ok · `1` gate/scope/verify · `2` usage · `130` interrupted.
- **Tamper-evident, exportable ledger.** Findings are hash-chained; `ledger
  verify` checks integrity, `--strict` requires signatures, and `export` emits
  JSON/JSONL/CSV/markdown/SARIF. Dedupe attaches evidence instead of dropping it;
  scope-refused rows never enter the file.
- **The kernel.** `next` emits the one state-driven directive (phase, mandate,
  exact argv, why, expect, walls), `absorb` validates an agent result through
  scope + ledger + evidence gates, and `loop` runs plan → execute → absorb with
  the engines as the state machine. `--plan-only` is free. The old phase action
  remains as `next-phase`.
- **Self-test.** `selftest` runs 27 checks in a throwaway `HOME`: scope allow/
  deny, ledger evidence/dedupe/integrity, a live 3-gate proof on the built-in
  lab, testers, chains, phases, coverage, report, campaign lifecycle, contracts,
  MCP, Arsenal, and the live bench. `selftest --quick` is the 14-check fast gate.
- **Hardening and fixes.** `bench_live.py` now uses a throwaway `HOME` and a
  dynamic port — it can never overwrite or delete the operator's real
  `~/.redteam/scope.json`. Arsenal honors CIDR, deny rules, expiry, and
  per-target normalization. The HTTP gate no longer follows redirects and caps
  response bodies. Engine self-checks that collide on lab ports are retried
  serially instead of reporting a healthy engine red. Reports default to the
  campaign directory; `--output` still overrides.
- **Surfaces.** MCP 18 → 43 tools (`--test`, `--list`, batching, notifications,
  dispatcher/engine adapters, structured content; `kernel_absorb` + `kernel_loop`
  expose the autonomous loop to any MCP client); `skilltree.py` gains
  `--verify` and `--count --json` (722 links/files bindings verified) AND the
  **context corpus**: `--expand` crosses every technique × applicable platform ×
  auth state into 8.8k chain-role-tagged files (deterministic, git-stable,
  sampled verification) — scale parity with the 7.6k-skill competitors, grown
  from real canon instead of a community; `bench` is 29/29 (25 first-hop + 4
  sequence); **`arsenal.py` v5**: 13 → 20 executors (ffuf · naabu · amass ·
  katana · dalfox · tlsx · gau) wired into 4 feeding chains (recon · web ·
  tls · net — subfinder's domains become dnsx's input, katana's urls become
  dalfox's strikes, cap 50/stage) and `run --out` emits the kernel result
  schema the loop absorbs; `arsenal verify` and `bench_live` are green with
  and without engines.
- **Docs and CI.** README, SKILL.md, the persona contract, and this changelog
  describe v4; `ci_smoke.sh` exercises campaigns, contracts, JSON, the kernel,
  the report default, skilltree verify, and the refusal paths; a new stdlib
  `tests/test_spydermonkey.py` runs the same truth locally and in CI.

## v3.0.0 — THE INTELLIGENCE LAYER (2026-11-04)

- **The engagement brain.** Derived from CyberStrike's methodology engine,
  rewritten family-native (stdlib-only, walls as exit codes, scope default-deny):
  `phases` (13-phase methodology board, statuses computed from real state-file
  deliverables), `ledger` (findings: scope-blocked · deduped by class+asset+title ·
  evidence-gated — downgraded to hypothesis, never suppressed; `triage` = triager
  gates with blocking violations), `gate` (the 3-GATE CONFIRMATION engine:
  baseline → attack → measurable diff + confirm token; `--prove` replays evidence),
  `chain` (8 chain patterns: low findings → high-impact kill chains with plans),
  `context` (session context: endpoints/roles/credentials/functions), `testers`
  (the 8 PARALLEL sub-testers — IDOR/AUTHZ/MASSASSIGN/INJECTION/AUTHN/BIZLOGIC/
  SSRF/FILEATTACK — differential probes, deduped into the ledger, `--demo` lab
  replica with zero setup), `coverage` (matrix + histogram + gap list), `report`
  (the joint war report), `relay` (remote execution nodes: Ed25519 ssh pairs,
  scope-checked exec), and `mission` (one command: scope gate → fleet → triage →
  chains → coverage → report).
- **The live-fire rule.** gate/testers fire at localhost freely (the lab); any
  other host requires a scope authority containing it — rc=1 refusal otherwise.
- **verify now proves the engine live**: spins the lab replica, runs a real
  3-gate confirmation, requires CONFIRMED. bench: 13/13 route accuracy.
- **MCP surface 12 → 18 tools** (ledger_triage · chain_detect · phases_board ·
  coverage · relay_list · war_report).
- **CI migrated to `scripts/ci_smoke.sh`** (script = local truth = CI truth):
  the new engines are exercised for real — ledger dedupe, testers demo, chain
  CH-001, kage mirror→Sigma export→refire FIRED against a live dojo replica,
  dojo bench self-verification, kaisha revert evidence, refusal exit codes.

## v1.8.0 — consistency/release polish

- **Docs match the ten-mandate family.** README, SKILL.md, the injectable mandate
  and the MCP server metadata now say ten mandates (KAGE #8 the purple layer and
  DOJO #9 the range were added in v1.5.0/v1.7.0 but never reached the docs).
  Version badges, `related_skills`, family buttons, clone list, relations, chain
  one-liners, router table and STANDARD RELAY all updated.
- **Dispatcher docs/CLI brought up to date.** `spydermonkey.py` docstring, the
  `bench` note, README's CLI table and SKILL's Tooling section now list `scope`,
  `doctor`, `bench`, `arsenal` and `fleet`, plus the companion scripts.
- **Skilltree generator hardened.** `skilltree.py` now folds in the kage and dojo
  canons (all mandate `references/` dirs present on disk), appends a stable hash
  on slug collisions instead of silently overwriting earlier techniques, and
  preserves the `generated:` date of files that already exist. Library
  regenerated: **722** technique files, index deduplicated (722/722 links valid).
- **Bench covers the new legs.** `bench` now asserts the kage and dojo routes;
  11/11 = 100% at v1.8.0.
- **CI mirrors the docs.** Workflow compiles all five scripts, greps the tree for
  KAGE/DOJO, asserts the full relay, and smoke-tests `arsenal verify`,
  `bench_live --help` and `fleet --help`.

## v1.7.0 and earlier

See git history — v1.7.0 DOJO (the Range) · v1.6.0 ARSENAL (the execution layer,
13 scope-gated tool wrappers) · v1.5.0 KAGE (the Mirror, the purple layer) ·
v1.4.0 the agent FLEET · v1.3.0b the MCP server (12 tools) + `bench_live` + the 612-file skilltree · v1.3.0 the scope authority + doctor + bench · v1.2.0 SHUKAKU reason/hunt/feed · v1.1.0 the persona contract · v1.0.0 initial release.
