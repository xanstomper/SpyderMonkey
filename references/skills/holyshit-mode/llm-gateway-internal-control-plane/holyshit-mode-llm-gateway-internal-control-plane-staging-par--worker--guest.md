# Staging / parallel-environment discovery — worker / guest

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-staging-par.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Brute `*.domain` subdomains; a **staging host** is often AWS-direct (no Cloudflare; IP ranges
  like `16.x/54.x/3.x` = AWS) with its OWN `llms.txt`, `/.well-known/api-catalog`,
  keyless `openapi.json` + `/api/models` catalog, and a `api.staging.<domain>` gateway.
- Staging catalogs can expose MORE hidden internal infra than prod (Modal `*.modal.direct` GPU
  URLs, `stealth/<model>` hidden-tier names, `-private`/`-latest` slugs).
- Modal endpoints may be scale-to-zero (`503 no upstreams available`) — a waking function with
  open auth = free GPU, but usually Modal web-auth applies.

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
