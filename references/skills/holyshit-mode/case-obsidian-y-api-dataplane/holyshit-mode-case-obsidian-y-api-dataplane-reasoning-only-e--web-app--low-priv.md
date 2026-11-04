# Reasoning-only empty-content failover (general upstream-proxy hardening) — web-app / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-reasoning-only-e.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The biggest "models aren't working in Hermes" trap: upstream returns 200 with non-zero
`completion_tokens` but **`message.content: ""`** — the model burned tokens on the CoT/reasoning
field and never populated `content`. Any client that requires text (Hermes, SDKs) sees an
"empty answer" and looks broken. Two fixes in the proxy:
1. `_salvage_reasoning`: if `content` empty but `reasoning_content`/`reasoning` present, promote
   it to `content` (mark `_from_reasoning`). muse's real answer lives in `reasoning_content`.
2. `_is_empty_completion` must flag empty-`content` even when tokens>0 (`completion_tokens>0`
   is NOT evidence of a usable answer), then fail over to next host / mark model dead (TTL'd)
   rather than serve a blank 200.
3. **Upstream availability churns HARD on free vectors** — a model serving content at 06:00 can
   502/degrade within 15 min. The dead-cache TTL (fail-open: re-probe after TTL, return 200 if
   upstream recovered) is the correct recovery, not a permanent hard-502. Assert that in tests
   (a "model now 200" after a prior fail is the fail-open working, NOT a regression).

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
