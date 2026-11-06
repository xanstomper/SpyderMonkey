# Context — mobile-api / low-priv

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-context.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Second engagement of logfare.ai (baseline 2026-10-03: CORS arbitrary-origin + credentials
CVSS ~9.1, broken rate limiting, FastAPI openapi.json exposure). Target rebuilt since
baseline: SPA → server-rendered FastAPI (inline `<script>` blocks, no hashed JS bundle),
plus a NEW OAuth-provider surface (`/oauth/authorize`, `/v1/me/apps`, device flow).

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
