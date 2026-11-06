# 5. Registration walls — verify both layers before documenting — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-5-registration-wall.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
