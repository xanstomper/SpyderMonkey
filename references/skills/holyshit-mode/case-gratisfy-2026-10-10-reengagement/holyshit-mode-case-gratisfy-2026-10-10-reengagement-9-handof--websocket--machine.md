# 9. Handoff refinements (score 78) — websocket / machine

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-9-handof.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **websocket** · auth **machine** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `POST /api/auth/platform-handoff/start` accepts ANY target string (admin/platform/internal/dashboard/mission-control all mint codes for unverified users — no role check) with body `{refresh_token, next, target}` + Bearer AT.
- Codes: 32-hex UUID-v4 (128-bit — brute dead, confirmed again). **Replayable within 60s TTL** (single-use only after expiry). Cross-host exchange: code minted at gratisfy.xyz exchanges at platform.gratisfy.xyz.
- Exchange mints a session for the CODE OWNER's account (no takeover by itself — it's self-minted).
- /api/account/session works for unverified accounts (200); every privileged route 403 `email_not_verified`.

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
