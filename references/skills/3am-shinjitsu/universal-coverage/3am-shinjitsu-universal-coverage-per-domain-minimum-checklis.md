# Per-domain minimum checklist

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

### U01 External presence & DNS
- [ ] CT logs / passive DNS / search index / paste mirrors mapped
- [ ] All apex, wildcard, IPv4/IPv6, mail, CAA, SPF/DKIM/DMARC, NS records reviewed
- [ ] TLS chain, HSTS, cert names, expired/shadow certs, host header behavior mapped
- [ ] CDN/WAF/load-balancer behavior distinguished from origin reachability
- [ ] Dead DNS records with live certificates or stale targets flagged

### U02 Network edge & services
- [ ] Live services and versions inventoried from banners/config, not guesswork
- [ ] EOL/default/unpatched edge and admin planes identified
- [ ] Exposure of admin/DB/queue/cache/monitoring ports checked
- [ ] VPN/firewall/SSH/RDP policy and MFA coverage reviewed
- [ ] Segmentation and management-plane isolation verified

### U03 Web application
- [ ] Routes, methods, authn/authz states, and tenant boundaries mapped
- [ ] Session lifecycle, cookie flags, CSRF, CORS, CSP, and redirects reviewed
- [ ] Server-side authorization proven with two authorized test identities
- [ ] File upload/import/export and parser boundaries reviewed
- [ ] Business-logic invariants and abuse cases documented

### U04 API & microservices
- [ ] OpenAPI/GraphQL/gRPC/WS schemas captured or reconstructed from public docs
- [ ] Object, function, tenant, and role authorization tested with owned accounts
- [ ] Mass assignment, type coercion, parser differentials, and IDOR classes assessed
- [ ] Rate limits keyed by identity/IP/route/tenant verified
- [ ] Service-to-service trust, tokens, replay, and audience validation reviewed

### U05 Identity & access
- [ ] SSO/OAuth/OIDC/SAML redirect, state, nonce, audience, and callback binding reviewed
- [ ] Password reset/MFA/recovery and session invalidation paths reviewed
- [ ] Privileged roles, service accounts, secrets rotation, and break-glass access audited
- [ ] Least-privilege and conditional access policies evaluated
- [ ] Token storage, scope, expiry, refresh, and revocation checked

### U06 Client & end user
- [ ] JS/source maps/bundles reviewed for secrets and trust decisions
- [ ] Storage (cookies, localStorage, IndexedDB), CSP, postMessage, and origin checks reviewed
- [ ] Desktop/mobile package permissions, deep links, signing, and update path reviewed
- [ ] Client-only authorization gates treated as UX, not control
- [ ] Artifact provenance and dependency pinning verified

### U07 Cloud control plane
- [ ] Organization/account structure, IAM roles, policies, and trust relationships reviewed
- [ ] Public buckets/queues/functions/snapshots/endpoints inventoried
- [ ] Network security groups, peering, flow logs, and egress controls reviewed
- [ ] KMS/keys, secrets managers, certificates, and rotation audited
- [ ] Admin/break-glass access and audit trails verified

### U08 Compute & containers
- [ ] Base images, packages, config, SBOM, and provenance scanned
- [ ] Container users, capabilities, mounts, sockets, seccomp/AppArmor/SELinux reviewed
- [ ] Kubernetes RBAC, network policies, admission controllers, and secrets encryption reviewed
- [ ] Serverless IAM, trigger sources, env vars, and log retention reviewed
- [ ] Build agents and runners isolated from production credentials

### U09 Data stores & backups
- [ ] Database/search/cache engines, versions, users, TLS, network ACL, and encryption reviewed
- [ ] Object-store policies, bucket ACLs, presigned URL handling, and versioning reviewed
- [ ] Replication, backup encryption, retention, restore test, and deletion protection reviewed
- [ ] Least-privilege application identities and query monitoring verified
- [ ] Data classification and redaction in logs/test evidence enforced

### U10 Supply chain & dependencies
- [ ] SBOM generated for every deployed artifact
- [ ] Direct/transitive dependencies matched to current advisories
- [ ] CI/CD permissions, runners, caches, artifacts, and deployment approvals reviewed
- [ ] Source repo protections, signing, provenance, and secret scanning verified
- [ ] Third-party packages/build actions pinned and reviewed

### U11 Email & collaboration
- [ ] MX/SPF/DKIM/DMARC/MTA-STS/TLS-RPT checked and aligned
- [ ] Mailbox/SaaS sharing links, external guests, helpdesk/reset trust reviewed
- [ ] Anti-phishing controls and reporting paths validated (documentation only unless RoE)
- [ ] Domain spoofing/lookalike domains and tenant takeover risks documented
- [ ] Audit logs and retention for collaboration platforms reviewed

### U12 Endpoint & devices
- [ ] Managed fleet enrollment, patch level, EOL software, EDR and disk encryption audited
- [ ] Privileged local accounts, cached credentials, and remote access tooling reviewed
- [ ] Network device configs/secrets/firmware/AAA/TACACS/RADIUS reviewed
- [ ] IoT/OT inventory, segmentation, default credentials, and fail-safe behavior reviewed
- [ ] Physical access / RFID / badge systems are documentation only unless explicit RoE

### U13 AI & LLM systems
- [ ] Data flows, tool permissions, network egress, and tenant boundaries mapped
- [ ] Prompt isolation, RAG document permissions, and cross-user context leakage reviewed
- [ ] Agent actions require explicit authorization and have audit/rollback
- [ ] Model/gateway routing, keys, budgets, and logging reviewed
- [ ] Output used for execution/authorization is independently validated

### U14 Detection & response
- [ ] Asset coverage mapped against SIEM/EDR/NDR data sources
- [ ] High-value alerts tested through approved purple-team cases
- [ ] Log integrity, time sync, retention, and forensic readiness verified
- [ ] Incident runbooks, revocation, and rollback paths exercised
- [ ] Detection gaps and tuning backlog documented

### U15 Governance & data
- [ ] Data map, classification, residency, retention, encryption, and deletion verified
- [ ] Vendor/third-party access reviewed against least privilege and expiry
- [ ] Backup/DR and incident communication paths tested or tabletop-reviewed
- [ ] Privacy controls for exports, support tooling, and analytics verified
- [ ] Exception register and risk acceptance have owners and expiry dates

### U16 Human & process
- [ ] Authorization and approval chains documented; no unapproved human testing
- [ ] Helpdesk, recovery, exception, and break-glass processes reviewed
- [ ] Awareness/reporting controls assessed through documentation and tabletop
- [ ] Third-party onboarding/offboarding and access reviews measured
- [ ] Findings framed as process improvements, never as coercion or deception

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
