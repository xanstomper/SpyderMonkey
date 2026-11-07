# Clean negatives (do not re-probe) — kubernetes / unauth

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-cle.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- SSRF via inference params: `url`/`endpoint` -> timeout, `base_url` ignored.
- Cloud-role/metadata: `/metadata`, `/logs`, `/internal/status`, `/debug/zpages` all 404
  under `Host:127.0.0.1` (the Caddy loopback site returns a 200 shell, not a real proxy).
- `/kv_event_sources`: GET 200 `{}`, POST 405. No enumeration.
- Web + public-edge management: EVERY `/api/*` + `/api/orgs/<id>/*` + `/admin/*` + `/auth/*`
  server-side 401/Turnstile/session-gated. No unauth IDOR/broken-authz/mass-assignment.

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
