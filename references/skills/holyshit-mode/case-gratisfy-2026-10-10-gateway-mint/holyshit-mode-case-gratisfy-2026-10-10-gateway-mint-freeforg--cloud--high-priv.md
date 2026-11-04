# FreeForge wiring (what was actually changed — reusable pattern for adding a second backend) — cloud / high-priv

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-freeforg.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `gratisfy_backend.py`: `GRATISFY_GW_MODELS` table (public_id, upstream name, note),
  `gratisfy_gw_chat()` — pass-through of tools/tool_choice/temperature/max_tokens verbatim,
  in-process `_gw_throttle()` honoring both rate windows, 429→sleep 11 / 5xx→sleep 3 retries,
  `gratisfy_list_models()` extended with `backend: gratify-gw` entries, `is_gateway_model()`.
- `server.py`: gateway-model branch in routing BEFORE legacy (first match wins), new
  `_gateway_chat` handler mirroring `_gratisfy_chat`'s SSE chunk-shape (buffered non-stream
  converted to proper `data:` chunks — covers the upstream streaming bug).
- Deploy cycle gotcha that cost a debugging round: **the `patch` tool reported success on
  server.py but both copies were stale** (mtime pre-dated the edit, `grep -c _gateway_chat`
  = 0). Recovery: re-apply edits via python string-replace in execute_code, verify
  `grep -c` on the DEPLOY copy, then restart. Rule: after any patch, `grep` the deployed file
  for the new symbol before restarting the service — don't trust the tool's success message
  for deploy-critical edits.
- Old-server kill gotcha: `kill $(pgrep -f 'server.py')` inside a shell whose own command
  line matches the pattern kills the shell itself (exit -15/-9). Use `pgrep -f … | head -1`
  against the python PID only, or match the full unique path.

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
