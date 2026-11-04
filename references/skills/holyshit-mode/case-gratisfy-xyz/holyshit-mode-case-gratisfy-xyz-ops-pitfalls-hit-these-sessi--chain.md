# Ops pitfalls hit these sessions — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-ops-pitfalls-hit-these-sessi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **holyleadger.py path drift**: SKILL.md cites scripts/holyleadger.py but the active profile's skill dir didn't have it — real file at `~/holyshit-mode/scripts/holyleadger.py`. Verify referenced scripts exist in the ACTIVE skill dir before relying on them (bit twice).
- **holyleadger CLI grammar**: `add <class_id> <status> --target T --score N --technique "..."` — BOTH class_id and status are positional, status SECOND (e.g. `add hypothesis hypothesis --target gratisfy.xyz --score 65 --technique "..."`). Omit positional status → `the following arguments are required: status`, exit 2, entry silently never lands (exit code is the only signal). Statuses lowercase only: confirmed|negative|hypothesis|inconclusive; requires `--target` or `export HOLYSHIT_TARGET`. BLOCKED/RE-VERIFY aren't valid statuses — map BLOCKED→negative. (Bit twice: gratisfy 10-04, iceposeidon 10-20 — check exit code, not stdout.)
- **Asset fetch variant-host trap**: the `www.gratisfy.xyz` variant of an asset URL 404'd silently while apex `gratisfy.xyz` served it — `-o` created an empty file and grep read garbage. Always `-w "%{http_code} %{size_download}"` on every chunk fetch to catch silent 404/empty bodies.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
