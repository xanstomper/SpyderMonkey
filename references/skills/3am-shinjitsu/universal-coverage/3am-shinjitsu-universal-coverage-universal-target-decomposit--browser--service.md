# Universal target decomposition — browser / service

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-universal-target-decomposit.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **browser** · auth **service** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

No matter how unfamiliar the technology is, map it to these domains. Probe a domain or
mark it **N/A with a concrete reason**. "Didn't recognize it" is not N/A.

| ID | Domain | Covers | Minimum discovery pass | Evidence standard |
|---|---|---|---|---|
| U01 | External presence & DNS | domains, subdomains, CT logs, DNS, TLS, origin hints | passive CT/DNS/cert enumeration, header and redirect mapping | requests/log refs; no origin touch without scope |
| U02 | Network edge & services | hosts, CDN/WAF, LB, VPN, SSH/RDP, mail, file transfer, monitoring | banner-first inventory; exposure map; EOL/default triage | service/version/banner, EOL evidence, reachability |
| U03 | Web application | routes, sessions, authz-vs-authn, business logic, uploads | 405 matrix, route/source-map review, authz matrix on owned test accounts | HTTP transcript, before/after screenshots, read-only proof |
| U04 | API & microservices | REST/GraphQL/gRPC/WebSocket, schemas, service trust | OpenAPI/schema extraction, authorization matrix, rate-limit/keying review | request/response pair, role matrix result, call graph |
| U05 | Identity & access | SSO, MFA, password reset, tokens, service accounts, PAM | flow diagram, redirect/state review, session inventory, stale-credential review | config evidence, policy export, read-only token check |
| U06 | Client & end user | browser storage/postMessage/CSP, desktop apps, mobile packages | static bundle/package review, storage inventory, origin/permission audit | artifact hashes/snippets; no victim interaction |
| U07 | Cloud control plane | AWS/Azure/GCP/OCI accounts, IAM, networking, logging | account/inventory export, IAM/policy review, exposed-service review | policy diff, account ID/config ref, least-privilege gap |
| U08 | Compute & containers | VMs, containers, K8s, serverless, images, CI runners | image/config scan, privilege/mount review, network policy review | scanner output, manifest snippets, node/pod refs |
| U09 | Data stores & backups | SQL/NoSQL/cache/search/object storage/queues/backups | config/consistency review, exposure audit, backup/restore verification | config export, reachability, restore log, redacted samples |
| U10 | Supply chain & dependencies | source, packages, CI/CD, signing, secrets, SBOM | SBOM diff, lockfile review, secret scan, pipeline/permission review | package+version, CVE/advisory ref, pipeline permission |
| U11 | Email & collaboration | mail auth, phishing resilience, SaaS sharing, helpdesk trust | MX/SPF/DKIM/DMARC review, sharing audit, helpdesk trust documentation | DNS/config evidence; never send phishing without RoE |
| U12 | Endpoint & devices | workstations, mobile, network devices, IoT, OT | inventory/config review, patch/EOL status, credential/default audit | asset refs; OT/human testing only with explicit owner RoE |
| U13 | AI & LLM systems | models, agents, tools, RAG, prompt boundaries, budgets | data-flow map, tool-permission review, isolation test plan | trace IDs, config refs, redacted prompt/output pairs |
| U14 | Detection & response | logging, SIEM, alert fidelity, forensics, recovery | telemetry coverage matrix, alert test in authorized lab/prod-safe window | log query refs, alert IDs, replay evidence |
| U15 | Governance & data | classification, retention, privacy, vendor access, DR | policy/data-flow review, retention/encryption audit, vendor entitlement review | policy refs, DLP/report exports, restore-test records |
| U16 | Human & process | approvals, support flows, awareness, third-party access | documentation only: trust-gap writeup, drill design | never execute social engineering; record owner-approved plan |

## Probe adjustment (browser × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
