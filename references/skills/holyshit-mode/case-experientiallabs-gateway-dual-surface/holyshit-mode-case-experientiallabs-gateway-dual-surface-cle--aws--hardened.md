# Clean negatives (do not re-probe) — aws / hardened

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-cle.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **aws** · auth **hardened** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- SSRF via inference params: `url`/`endpoint` -> timeout, `base_url` ignored.
- Cloud-role/metadata: `/metadata`, `/logs`, `/internal/status`, `/debug/zpages` all 404
  under `Host:127.0.0.1` (the Caddy loopback site returns a 200 shell, not a real proxy).
- `/kv_event_sources`: GET 200 `{}`, POST 405. No enumeration.
- Web + public-edge management: EVERY `/api/*` + `/api/orgs/<id>/*` + `/admin/*` + `/auth/*`
  server-side 401/Turnstile/session-gated. No unauth IDOR/broken-authz/mass-assignment.

## Probe adjustment (aws × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
