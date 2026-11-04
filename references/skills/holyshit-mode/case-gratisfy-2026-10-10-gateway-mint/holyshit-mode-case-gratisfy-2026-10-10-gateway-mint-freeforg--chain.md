# FreeForge wiring (what was actually changed — reusable pattern for adding a second backend) — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-freeforg.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
