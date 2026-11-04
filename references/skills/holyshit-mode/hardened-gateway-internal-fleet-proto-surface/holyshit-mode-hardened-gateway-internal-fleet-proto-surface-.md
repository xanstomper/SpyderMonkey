# Contrast vs the vulnerable GoTrue variant (gratisfy/gonka)

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

The earlier findings (redirect_uri forwarded verbatim, anon key client-exposed, unthrottled code
exchange) come from an **un-hardened GoTrue deployment**. Always fingerprint BEFORE assuming: server-side
PKCE + no client anon key + hardcoded redirect_to ⇒ the gratisfy chain does not apply; pivot.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
