# Playground UI (user requirement: "working playground to test all models") — grpc / machine

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- base technique: `holyshit-mode-case-obsidian-y-api-reengage5-provider-wiring-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
