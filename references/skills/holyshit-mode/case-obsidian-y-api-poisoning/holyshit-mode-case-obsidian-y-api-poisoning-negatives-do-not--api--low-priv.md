# Negatives (do not re-probe without code change) — api / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-negatives-do-not.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **api** · auth **low-priv** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `private_model_gate_hardened` (20): 11-variant bypass matrix (case, space, %00, dot, //, :latest, ?query, array-typed model, stream, second host, URL-encoding) all 403/404. `no_access`(403) vs `model_not_found`(404) = model-exists oracle; gate is real code.
- `jwt_key_uniform_errors` (15): all Bearer/JWT/alg-none/Basic/prefix variants → uniform invalid_api_key 401. Keys are opaque strings; NO JWT path exists — don't chase forging.
- `header_path_bypass_negative` (15): 13 path-confusion variants + 8 admin-header injections + tool-role override + type-confusion bodies all held.
- No admin panel: 24-path admin wordlist + 19-path /pg/* wordlist + 35-path secondary sweep all uniform-JSON-404; `allow:` method probes show only ~7 routes (/, /docs, /playground, /status, /pg/chat, /v1/models, /v1/chat/completions). No hardcoded keys: server-rendered app, zero inline JS bundles.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
