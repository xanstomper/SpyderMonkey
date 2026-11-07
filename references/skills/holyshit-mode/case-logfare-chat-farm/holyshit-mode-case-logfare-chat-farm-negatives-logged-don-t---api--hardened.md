# Negatives (logged, don't re-probe) — api / hardened

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-negatives-logged-don-t-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **api** · auth **hardened** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Tier-2 consent gate holds: glm-5/grok-4.6 → 403 `consent_required` (real server gate; mass-assigned tier/role/can_use_premium/consent fields accepted `{"ok":true}` but stripped — verify by GET-back + retry, not the 200).
- Cross-session conversation IDOR → 404; client-supplied `conversation_id` ignored; no shared global buffer (PTOK constant 7-36/fresh session, cross-user probe → NONE).
- Model-field path traversal → clean 502 upstream-404 passthrough (no SSRF via model routing).
- SvelteKit escapes stored conversation titles; settings theme not reflected into HTML.

## Probe adjustment (api × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
