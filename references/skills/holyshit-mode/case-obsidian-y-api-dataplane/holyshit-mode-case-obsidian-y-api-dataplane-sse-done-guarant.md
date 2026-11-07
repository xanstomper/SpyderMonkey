# SSE `[DONE]` guarantee

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Upstream SSE streams can truncate without `data: [DONE]`. A browser reader loop that waits for
the terminator hangs forever. The proxy's `sse_wrap` must gated-yield `data: [DONE]\n\n` in a
`finally` when the upstream didn't. (For the browser half: a `finalize()` guard that always runs
on stream end / error / catch, so the meta/status line always renders.)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
