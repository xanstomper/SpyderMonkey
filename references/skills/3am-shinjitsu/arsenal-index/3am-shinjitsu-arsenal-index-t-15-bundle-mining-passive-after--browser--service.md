# T+15 — bundle mining (passive after fetch, always `-w '%{http_code} %{size_download}'`) — browser / service

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-15-bundle-mining-passive-after.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 16 | Chunk discovery | webpack: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js`; Vite: extract `__vite__mapDeps` manifest; follow re-export stubs | lazy admin portal / auth wiring invisible in main bundle |
| 17 | Env-object dump | grep `VITE_[A-Z_0-9]+:` (backtick-aware: Vite strings are template literals) | prod flags ON, license keys, internal hosts |
| 18 | Schema-library extraction | locate zod/io-ts chunk → full request shapes → valid-shape authz matrix | gate-order proof without a session (`arsenal-03` §2.2) |
| 19 | Backdoor grep | `user.id === N`, `is_admin`, `window.hide*Gate`, `postMessage(` targets | client-only gates; map EVERY module independently |
| 20 | Socket factory decode | hostname templates, `path:`, `transports:`, EIO version | host+namespace+transport policy in one read |
| 21 | Anon-key harvest | `VITE_SUPABASE_ANON_KEY` / `supabase.co` refs | GoTrue surface map via `apikey` header |

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
