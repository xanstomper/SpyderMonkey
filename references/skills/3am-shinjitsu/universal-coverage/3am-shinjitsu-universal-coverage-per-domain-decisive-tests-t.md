# Per-domain decisive tests — the compromise battery

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

The checklists above are the audit pass. THIS is the exploitation pass: for every
U-domain, the decisive tests that prove actual control on authorized targets.
Each is minimal, read-only or one-request, documented-PoC adaptation only (§15).
Score §14 before running; ledger every negative with its exact test. A positive
triggers OP-ESCALATE (hunt the consumer) immediately.

### U01 External presence & DNS
- [ ] AXFR: `dig AXFR <domain> @<ns>` — records pulled without auth (read-only, loud — once)
- [ ] Dangling CNAME: fingerprint provider takeover signature (read-only resolution + provider page)
- [ ] Dead-NS / expired-registrar drift: `whois` vs live NS set
- [ ] Wildcard cert shadow hosts: TLS SAN set ∖ DNS set (→ U02 probes)

### U02 Network edge & services
- [ ] Fingerprint → `searchsploit <component> <version>` for every banner (documented-PoC adaptation only)
- [ ] SNMP public community: `snmpget -v2c -c public <host> sysDescr.0`
- [ ] NFS: `showmount -e` — world-readable export?
- [ ] SMB NULL session: `smbclient -N -L //<host>`
- [ ] VNC/RDP pre-auth auth-type negotiation
- [ ] SSH: banner + auth-method list (`ssh -o PreferredAuthentications=none` — expects denial, misconfig = finding)

### U03 Web application — arsenal-02 (deep battery), ghost-route sweep, upload/parser boundaries
### U04 API & microservices — arsenal-03 (deep battery), schema-library extraction, IDOR structural scan
### U05 Identity & access — arsenal-04 (deep battery), OAuth state/redirect_uri, GoTrue chain, reset-flow abuse
### U06 Client & end user
- [ ] Mobile package (operator-provided APK/IPA): exported components via `aapt`/jadx, `android:exported`, deep-link schemes
- [ ] Signing/update trust: unsigned or plaintext update package inspection
- [ ] Electron/desktop: ASAR secrets + nodeIntegration exposure (local artifact, operator-provided)
- [ ] Browser storage audit: cookies/localStorage/IndexedDB secrets + CSP/postMessage (→ arsenal-05)

### U07 Cloud control plane
- [ ] Public object store: `GET <bucket>?list-type=2` unauth (S3/Azure/GCS naming canon + CT/SSL search)
- [ ] IAM privesc path scan: AssumeRole/PassRole over-permission in policy diff (read-only)
- [ ] Cross-account role assumption (staging → prod)
- [ ] Exposed cloud snapshots/AMIs/public images
- [ ] Cloud metadata SSRF grooming: every web/API SSRF candidate pointed at 169.254.169.254 (owned infra only for the decisive call)

### U08 Compute & containers
- [ ] kubelet unauth: `GET https://<node>:10250/pods`
- [ ] etcd unauth: `GET :2379/version` then key prefix (operator-owned)
- [ ] Docker socket: `GET :2375/containers/json`
- [ ] Unauthenticated container registries: `GET /v2/_catalog`
- [ ] CI runner env/secret exposure via exposed services or PR-based pipelines (documentation + read-only evidence)

### U09 Data stores & backups
- [ ] Redis anon `INFO`, Elasticsearch `GET :9200/_cat/indices`, Mongo no-auth db list (operator-owned only)
- [ ] Backup artifacts on web-adjacent paths: `.bak .sql .gz .dump .zip` + `backup/` `db/` `dumps/`
- [ ] Object-store presigned URL leakage in client bundles/requests
- [ ] Default/empty credentials on internal DB listeners (documented vendor defaults only)

### U10 Supply chain & dependencies
- [ ] SBOM → advisory match → documented-PoC adaptation per vulnerable version
- [ ] CI/CD takeover paths: exposed registry creds, mutable tags, unprotected production branch protection
- [ ] Typosquat/lookalike package or dependency confusion feasibility on OWN package names

### U11 Email & collaboration
- [ ] MX/SPF/DKIM/DMARC bypass assessment (spoof test ONLY on operator-owned domains)
- [ ] SaaS OAuth app over-grant: installed app requesting full-tenant scopes
- [ ] Webhook/connector registration: URL accepted as SSRF candidate (register with internal/link-local URL on authed session)
- [ ] External sharing links: enumeration/access without identity

### U12 Endpoint & devices
- [ ] Default/vendor credentials on network gear and IoT (documented vendor lists, banner+login attempt)
- [ ] Firmware/update-package extraction: strings/secrets/unsigned OTA (operator-provided artifact, local work)
- [ ] MQTT unauth subscribe on owned brokers: connect + subscribe to `#`
- [ ] RTSP/ONVIF open streams: `DESCRIBE` without creds
- [ ] OT (operator-owned only): Modbus read coils, DNP3 read — read-only register reads
- [ ] Serial/UART console exposure: physical access required — document, never execute beyond owner opt-in

### U13 AI & LLM systems — arsenal-10 (deep battery): status-json hidden-model map, PTOK drift, playground-proxy bypass, model substitution
### U14 Detection & response — purple-team replay of CONFIRMED findings in lab/prod-safe window; alert-fidelity matrix; log-integrity review
### U15 Governance & data — policy/entitlement review, retention/encryption audit, restore-test records (evidence-class, not exploit-class)
### U16 Human & process — documentation only, never executed (trust-gap writeup, drill design)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
