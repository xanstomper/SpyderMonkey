# Playground UI (user requirement: "working playground to test all models")

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Single-file Flask route serving the SPA at `/` and `/playground`:
- Model quick-pick sidebar with tool-capability badges; params (max_tokens/temp); system prompt;
  tools JSON textarea; stream toggle.
- Streaming via fetch + ReadableStream SSE parse; non-stream fallback.
- Playwright headless verification (chromium-headless-shell install needed on first run) drove
  the REAL flow and caught 3 bugs the DOM assertions missed:
  1. `.meta` node never created by `add()` but written by `finalize()` → `Cannot set properties
     of null`, send button stuck. Fix: create `.meta` at message creation; single idempotent
     finalize() closure used by BOTH stream and non-stream paths.
  2. Raw `车展` tags rendered literally → collapse via regex into a `<details>` toggle.
  3. Sidebar overflow hid the params/system/tools controls → `overflow-y:auto`.
- Screenshot + vision check REQUIRED even after Playwright PASS (UI claims need visual proof).
- Truncated upstream SSE (no [DONE]) hung the reader loop → the sse_wrap finally fix above.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
