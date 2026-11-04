# Staging / parallel-environment discovery — aws / low-priv

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-staging-par.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **aws** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Brute `*.domain` subdomains; a **staging host** is often AWS-direct (no Cloudflare; IP ranges
  like `16.x/54.x/3.x` = AWS) with its OWN `llms.txt`, `/.well-known/api-catalog`,
  keyless `openapi.json` + `/api/models` catalog, and a `api.staging.<domain>` gateway.
- Staging catalogs can expose MORE hidden internal infra than prod (Modal `*.modal.direct` GPU
  URLs, `stealth/<model>` hidden-tier names, `-private`/`-latest` slugs).
- Modal endpoints may be scale-to-zero (`503 no upstreams available`) — a waking function with
  open auth = free GPU, but usually Modal web-auth applies.

## Probe adjustment (aws × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
