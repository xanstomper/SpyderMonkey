# Key-plane trust-root split (operator supplied live sk-proxy- key mid-session)

- source canon: `holyshit-mode/case-atessa-top.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Key opens `/v1/*` fully (30-model catalog incl. grok-4.7 family, kimi-k3, muse-spark, nano-banana-pro; Anthropic + Responses APIs both 429 at quota).
- ALL `/api/*` dashboard endpoints 401 on Bearer/X-Api-Key/X-Atessa-Key/X-Proxy-Key/raw-key variants — session-cookie-only. **No plane bleed** (good architecture). Lesson: when the operator hands an API key, first map WHICH plane it opens before planning the authed chain; say explicitly what still needs the session cookie.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
