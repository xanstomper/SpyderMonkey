# The Attack Canon — ATT&CK enterprise + OWASP WSTG families, family-native

> Every entry is a REAL technique with the family's probe shape and wall.
> Header = technique; body = the class, the probe, the wall. Deterministic.

## Recon Active Scanning (T1595)

- class: adversarial scanning of the victim surface — port sweeps, vuln scans, wordlist strikes
- probe: rate-limited sweep of the declared scope only; masscan-class first, then app layer
- wall: in-scope only — the scope authority refuses everything else (rc=1)

## Recon Gather Victim Host Information (T1592)

- class: passive host inventory — software, roles, versions reachable from the outside
- probe: banners, headers, TLS certs, favicon hashes — zero-touch reads
- wall: NO-GAIN — the dossier feeds downstream planning, nothing executes

## Recon Gather Victim Identity Information (T1589)

- class: email formats, employee names, SSO portals, password policies visible pre-auth
- probe: harvest from public pages + error strings; enumerate the auth surface's hints
- wall: passive-first; no account interaction beyond what scope declares

## Recon Gather Victim Network Information (T1590)

- class: IP blocks, DNS topology, routing, trust relationships from public records
- probe: whois/rdap/dns walking; netblock mapping against the scope file
- wall: read-only; everything stays in the estate ledger

## Recon Gather Victim Org Information (T1591)

- class: org structure, locations, business rhythm — the social-engineering surface
- probe: public filings, job posts, status pages; crown the exposure classes
- wall: passive collection only, ledgered with source provenance

## Recon Search Closed Sources (T1597)

- class: paid/registered intel sources for victim data
- probe: only what the operator legally holds credentials for
- wall: no credential use beyond declared scope; nothing purchased mid-run

## Recon Phishing for Information (T1598)

- class: targeted phishing to harvest victim-side info pre-access
- probe: family never sends unsolicited live phishing — lab replicas only
- wall: LAB ONLY — the dojo replays the class; live engagement is refused

## Resource Development Acquire Infrastructure (T1583)

- class: domains, VPSes, botnets the adversary stands up for the engagement
- probe: not exercised live — the estate inventories what ALREADY exists in scope
- wall: NO-GAIN; the family maps, it does not stand up live infra

## Resource Development Compromise Infrastructure (T1584)

- class: staging through third-party/compromised infra
- probe: out of family walls — detection classes only (kage rules for the pattern)
- wall: REFUSED live; detection-side only

## Resource Development Develop Capabilities (T1587)

- class: malware/exploit/cert development
- probe: the family's "capabilities" are validators and provers, never payloads
- wall: NO-GAIN — every shipped script is read-only toward the operator's targets

## Resource Development Obtain Capabilities (T1588)

- class: acquiring existing tooling
- probe: inventory what the operator environment already carries (arsenal.py)
- wall: zero-purchase; the arsenal maps presence, never installs for an engagement

## Initial Access Exploit Public-Facing Application (T1190)

- class: the crown jewel — RCE/deserial/injection on the internet-facing surface
- probe: the full differential battery (11 testers) against every mined endpoint
- wall: documented classes only; no exploit chaining beyond proof-of-reach

## Initial Access Phishing (T1566)

- class: spearphish attachment/link into a user
- probe: LAB ONLY — the dojo replays the pattern; kage rules detect the trace
- wall: REFUSED live against real users, no exceptions

## Initial Access Valid Accounts (T1078)

- class: default/leaked/reused credentials
- probe: only credentials the SCOPE FILE declares; never a live brute against prod
- wall: brute classes run against the dojo replica; prod runs are refusals

## Execution Command and Scripting Interpreter (T1059)

- class: shell/powershell/python interpreters as the execution primitive
- probe: the cmd-injection battery (`;id`, `$(id)`, backticks) — echo differential only
- wall: proof = a benign marker echoed; never a destructive command

## Execution Container Administration Command (T1609)

- class: exec into running containers
- probe: read-only inventory of the container surface; NO exec
- wall: REFUSED — namespace escape execution is outside every wall

## Persistence Create Account (T1136)

- class: new account for durable access
- probe: never exercised — detection rule ships instead (kage T1136)
- wall: NO-GAIN — the family leaves zero persistence artifacts

## Persistence Boot or Logon Autostart (T1547)

- class: run-key/systemd/launchd autostart for durability
- probe: read-only enumeration of autostart locations on in-scope hosts
- wall: read-only; the finding is the exposure, not a planted hook

## Privilege Escalation Abuse Elevation Control (T1548)

- class: sudo/sudoers misconfiguration abuse
- probe: `sudo -n -l` inventory — what can THIS principal do
- wall: read-only; rung climbing stops at the exposure statement (kaisha)

## Privilege Escalation Exploit for Privilege Escalation (T1068)

- class: kernel/driver CVE elevation
- probe: era-stack banner mapping (kaisha cve) — the CLASS is crowned, never fired
- wall: NO-GAIN — kernel exploits are never executed by the family

## Privilege Escalation Process Injection (T1055)

- class: ptrace/injection into running processes
- probe: REFUSED live — detection classes only
- wall: the kage rule carries the technique; the family does not inject

## Defense Evade Impair Defenses (T1562)

- class: disabling logging/AV/EDR
- probe: NEVER — the opposite: protect scan proves the family leaves logs intact
- wall: REFUSED; impairing defenses violates every family law

## Defense Evasion Clear Logs (T1070)

- class: log tampering to erase the trail
- probe: NEVER; the estate memory + tamper-evident hash chain exists to resist this
- wall: REFUSED — the ledger is append-only, hash-chained, tamper-evident

## Defense Evasion Obfuscated Files or Information (T1027)

- class: encoding/packing to hide intent
- probe: the encoding batteries (double-encoded, unicode, hex-host) as DETECTION canon
- wall: the family ships encodings as probe vocabulary, not as stealth

## Defense Evasion Deobfuscate/Decode (T1140)

- class: decoding on the endpoint
- probe: lab replicas decode the encoded probes; prod never runs decode steps
- wall: analysis-only

## Credential Access Brute Force (T1110)

- class: password spraying, credential stuffing
- probe: dojo replica only — the AUTHN battery proves the class shape
- wall: live spraying is a refusal (rc=1) every time

## Credential Access Unsecured Credentials (T1552)

- class: keys/secrets in files, env, registries, object storage
- probe: read-only harvest scans (`.env`, `.git`, backup dumps, bucket listings)
- wall: NO-GAIN — found secrets are redacted in the ledger, never reused

## Credential Access Credentials from Password Stores (T1555)

- class: browser/keychain credential extraction
- probe: REFUSED on any live endpoint; the class exists as a detection pattern
- wall: kage rule only

## Credential Access Steal Application Access Token (T1528)

- class: OAuth/app token theft
- probe: token-handling review of the in-scope app — where tokens land in logs/artifacts
- wall: read-only analysis

## Discovery System Information Discovery (T1082)

- class: OS/build/hostname enumeration
- probe: banner + header differentials; error-page fingerprinting
- wall: read-only

## Discovery File and Directory Discovery (T1083)

- class: locating sensitive files
- probe: the traversal battery (8 encodings) — the response body diff is the proof
- wall: read paths only; no deletion/modification probes

## Discovery Network Service Discovery (T1046)

- class: service/port enumeration
- probe: scope-bounded sweep, rate-capped
- wall: out-of-scope hosts refuse at the socket layer

## Discovery Account Discovery (T1087)

- class: valid account enumeration
- probe: response-differential username classes (login vs reset timing/length)
- wall: length/timing DIFFERENTIALS only — no successful logins attempted

## Discovery Permission Groups Discovery (T1069)

- class: group/role enumeration
- probe: the AUTHZ battery (role-flip, level-flip, upward-only)
- wall: read-only against the declared principal

## Discovery System Network Connections (T1049)

- class: connection/route enumeration
- probe: passive — headers/proxies reveal topology without touching hosts
- wall: NO-GAIN

## Lateral Movement Remote Services (T1021)

- class: ssh/smb/winrm hopping
- probe: never fired — the AUTHZ ladder CROWNS the reachability, stops there
- wall: NO-GAIN; lateral movement execution is refused

## Lateral Movement Use Alternate Authentication Material (T1550)

- class: pass-the-hash/ticket, session hijack
- probe: session-id enumeration class only (sequential/weak ids — CWE-384)
- wall: the SESSION tester proves structure weakness; no replay against prod

## Collection Data from Local System (T1005)

- class: staging local data
- probe: the HARVEST class — backup/source-map/env exposure proof
- wall: proof-of-exposure only; files are listed, not exfiltrated

## Collection Email Collection (T1114)

- class: mailbox reading
- probe: REFUSED live; detection pattern ships
- wall: kage T1114

## Command and Control Application Layer Protocol (T1071)

- class: C2 over 443/dns/http
- probe: out of family walls entirely
- wall: REFUSED — no C2 infrastructure, ever

## Command and Control Proxy (T1090)

- class: tunneling through proxies
- probe: the family maps proxy headers (x-forwarded chains) as inventory only
- wall: read-only

## Exfiltration Over Web Service (T1567)

- class: data out through trusted clouds
- probe: never exercised; the IMPACT LEG is priced by shukaku instead
- wall: NO-GAIN — exfiltration is priced hypothetically, never performed

## Impact Data Destruction (T1485)

- class: wiping victim data
- probe: ABSOLUTE REFUSAL — this is the family's hardest wall
- wall: no code path exists that reaches this class

## Impact Network Denial of Service (T1498)

- class: volumetric DoS
- probe: REFUSED — rate-limit bypass classes are proven with 2 requests, never a flood
- wall: proof = the differential, not the outage

## WSTG Information Gathering (WSTG-INFO)

- class: fingerprinting, disclosure, open ports, error pages
- probe: banner/error/source-map/harvest classes — all read-only
- wall: ledger every source with provenance

## WSTG Authentication Testing (WSTG-AUTHN)

- class: credentials, reset flows, remember-me, logout, browser cache
- probe: the AUTHN battery (empty/forged factors) + JWT alg=none
- wall: no real credential abuse; differentials against the replica shape

## WSTG Authentication Bypass (WSTG-AUTHB)

- class: auth-bypass via parameter pollution, verb tampering, path confusion
- probe: verb/path/parameter variants in the differential harness
- wall: proof-of-bypass on the replica or lab only

## WSTG Authorization Testing (WSTG-AUTHZ)

- class: idor, privilege escalation, forced browsing
- probe: the IDOR battery (±1/0/-1/999999) + AUTHZ flips, upward only
- wall: never downward — never touch other tenants' data beyond the probe

## WSTG Session Management Testing (WSTG-SESS)

- class: cookie flags, session fixation, logout, timeout
- probe: the SESSION battery (sequential ids) + cookie attribute inventory
- wall: read-only; fix=secure flags in the report

## WSTG Input Validation Testing (WSTG-INPT)

- class: injection families — sql, ldap, xss, xxe, ssti, cmd, deserialization
- probe: the 14-marker INJECTION battery + 8-encoding traversal battery
- wall: reflected/evaluated markers only; never destructive payloads

## WSTG Error Handling (WSTG-ERRH)

- class: stack traces, debug output leaking through errors
- probe: malformed inputs forcing 500s; harvest the trace for class crowns
- wall: read-only

## WSTG Cryptography (WSTG-CRPT)

- class: weak ciphers, padding oracles, predictable keys
- probe: TLS inventory (tlsx chain); oracle classes lab-replica only
- wall: no live oracle exploitation

## WSTG Business Logic Testing (WSTG-BUSL)

- class: price tampering, quantity abuse, rounding, race conditions
- probe: the BIZLOGIC battery (negative/zero/overflow quantity) — replica proof
- wall: live business-logic abuse is refused; the differential is the deliverable

## WSTG API Testing (WSTG-API)

- class: graphql introspection, mass assignment, rate limits, versioning
- probe: the MASSASSIGN POST battery + graphql alias/batch checks
- wall: documented classes; no data modification beyond the proof request
