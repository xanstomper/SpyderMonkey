# T+15 — bundle mining (passive after fetch, always `-w '%{http_code} %{size_download}'`)

- source canon: `3am-shinjitsu/arsenal-index.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 16 | Chunk discovery | webpack: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js`; Vite: extract `__vite__mapDeps` manifest; follow re-export stubs | lazy admin portal / auth wiring invisible in main bundle |
| 17 | Env-object dump | grep `VITE_[A-Z_0-9]+:` (backtick-aware: Vite strings are template literals) | prod flags ON, license keys, internal hosts |
| 18 | Schema-library extraction | locate zod/io-ts chunk → full request shapes → valid-shape authz matrix | gate-order proof without a session (`arsenal-03` §2.2) |
| 19 | Backdoor grep | `user.id === N`, `is_admin`, `window.hide*Gate`, `postMessage(` targets | client-only gates; map EVERY module independently |
| 20 | Socket factory decode | hostname templates, `path:`, `transports:`, EIO version | host+namespace+transport policy in one read |
| 21 | Anon-key harvest | `VITE_SUPABASE_ANON_KEY` / `supabase.co` refs | GoTrue surface map via `apikey` header |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
