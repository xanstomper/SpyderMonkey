# 5. Registration walls — verify both layers before documenting

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

- **Edge layer:** Fastly VCL returns `400 ... Error 54113` on non-browser TLS for sensitive
  POSTs (`/signup`) while the same client passes on other endpoints. Python/curl replicas
  die here regardless of headers.
- **Browser layer:** replicate the flow in a real-browser harness (shadow-DOM forms need
  recursive shadow-root piercing; native value-setter + input/change events for React
  inputs; real `.click()` on controlled checkboxes — a failed checkbox blocks submit
  SILENTLY with no error text). If invisible Turnstile never initializes
  (`window.turnstile` undefined, no challenges.cloudflare.com scripts/iframes, no request
  fires on submit), the wall is verified.
- Document the wall, write a ready-made cookie-driven test script for the operator, and
  stop. Never forge captcha tokens.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
