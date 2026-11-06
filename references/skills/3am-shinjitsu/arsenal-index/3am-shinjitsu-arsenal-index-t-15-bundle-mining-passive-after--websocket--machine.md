# T+15 — bundle mining (passive after fetch, always `-w '%{http_code} %{size_download}'`) — websocket / machine

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-15-bundle-mining-passive-after.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **machine** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 16 | Chunk discovery | webpack: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js`; Vite: extract `__vite__mapDeps` manifest; follow re-export stubs | lazy admin portal / auth wiring invisible in main bundle |
| 17 | Env-object dump | grep `VITE_[A-Z_0-9]+:` (backtick-aware: Vite strings are template literals) | prod flags ON, license keys, internal hosts |
| 18 | Schema-library extraction | locate zod/io-ts chunk → full request shapes → valid-shape authz matrix | gate-order proof without a session (`arsenal-03` §2.2) |
| 19 | Backdoor grep | `user.id === N`, `is_admin`, `window.hide*Gate`, `postMessage(` targets | client-only gates; map EVERY module independently |
| 20 | Socket factory decode | hostname templates, `path:`, `transports:`, EIO version | host+namespace+transport policy in one read |
| 21 | Anon-key harvest | `VITE_SUPABASE_ANON_KEY` / `supabase.co` refs | GoTrue surface map via `apikey` header |

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
