# Confirmed findings (by score) — android / high-priv

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-confirmed-findin.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- 95 `pg_shared_context_poisoning_persistent` — standing directive planted via one unauth POST /pg/chat persisted in the GLOBAL buffer and fired in other users' later completions. Proof: 3-request pattern (clean baseline → plant+ACK → clean request; reasoning trace leaked the planted text verbatim; subtle [SYSTEM NOTICE] banner payload appeared in user-visible content). Chain: pg_chat_no_auth→plant_standing_instruction→persists_in_global_buffer→injected_into_other_users_completions→content_control:confirmed.
- 90 `pg_chat_unauthenticated_free_ai` — /v1/chat/completions 401s, /pg/chat serves live completions no key (ollama/*, meituan/longcat-2.0, muse/*, laguna/*, ling/*; hyb/*+asdisunknown/* were 502 upstream at test time).
- 85 `pg_shared_global_conversation_context` — global shared buffer; PTOK drift 21k→30k→50k on identical input; foreign personas (Avery/Kael Dagger cheerleader RP, Dracie Malfoid HP-RP) visible; cross-user readout via structural-summarization oracle.
- 70 `pg_chat_no_rate_limit` — 15-burst all 200 zero 429.
- 60 `pg_roleplay_platform_stack_leak` — 20+-section adult-RP framework + character sheets extractable structurally.
- 45 `status_json_hidden_model_map` — GET /status?json=1 unauth: private models (anthropic/claude-opus-5, claude-sonnet-5, claude-fable-5, stealth/ox-alpha, deepseek/deepseek-v4.1-flash) + upstream vendor names (kallme, gonka, hyb, yjs, kiosapi, stealth) + verbatim upstream error bodies.
- 35 `pg_stream_passthrough` — stream:true works; chunks leak upstream model names (glm-4.7-flash:latest, fp_ollama).
- 30 `vercel_host_same_backend` — /pg/chat vuln identical on second host.

## Probe adjustment (android × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
