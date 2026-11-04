# Negatives (do not re-probe without code change) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-negatives-do-not.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `private_model_gate_hardened` (20): 11-variant bypass matrix (case, space, %00, dot, //, :latest, ?query, array-typed model, stream, second host, URL-encoding) all 403/404. `no_access`(403) vs `model_not_found`(404) = model-exists oracle; gate is real code.
- `jwt_key_uniform_errors` (15): all Bearer/JWT/alg-none/Basic/prefix variants → uniform invalid_api_key 401. Keys are opaque strings; NO JWT path exists — don't chase forging.
- `header_path_bypass_negative` (15): 13 path-confusion variants + 8 admin-header injections + tool-role override + type-confusion bodies all held.
- No admin panel: 24-path admin wordlist + 19-path /pg/* wordlist + 35-path secondary sweep all uniform-JSON-404; `allow:` method probes show only ~7 routes (/, /docs, /playground, /status, /pg/chat, /v1/models, /v1/chat/completions). No hardcoded keys: server-rendered app, zero inline JS bundles.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
