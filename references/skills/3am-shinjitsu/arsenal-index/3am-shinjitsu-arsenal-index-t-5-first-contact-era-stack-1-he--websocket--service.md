# T+5 — first-contact era-stack (1 HEAD request) — websocket / service

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-5-first-contact-era-stack-1-he.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 7 | Header stack | `curl -sI https://<domain>` | Server/X-Powered-By/via/x-kong-*/x-served-by fingerprints → EOL table (`arsenal-01` §1.12) |
| 8 | Kong-fronted Supabase | `www-authenticate: Basic realm="service"` + `x-kong-response-latency` + ACAH contains `apikey` | GoTrue chain unlocks (`arsenal-04` §3.1) |
| 9 | Origin-verify | `python3 http.client` → origin IP, `Host:`/SNI=<domain>, unverified TLS, expect real app HTML vs CF interstitial | full WAF bypass (`arsenal-01` §1.2) |

## Probe adjustment (websocket × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
