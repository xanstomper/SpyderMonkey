# SPA endpoint + body-shape mining (minified bundle) — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-spa-endpoint-body-shape.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `grep -oE '"/[a-zA-Z0-9_/.-]{2,60}"' app.js | sort -u` → route + endpoint list.
2. All fetch calls: `grep -oE 'fetch\("[a-z0-9/_-]+"' app.js | sort -u`.
3. Body shapes live at CALL SITES of the wrapper fn, not the fetch itself — find the wrapper
   (e.g. `async function Y8(e,t){fetch("/api/chat"...}`), then grep its callers:
   `grep -oE 'Y8\(\{[^}]{0,150}' app.js` → reveals real body keys (`{modelId, message}` not
   the guessed `{model, messages}`). Server error strings are the oracle.
4. **Code-split chunk discovery**: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js` → fetch each chunk, mine for endpoints.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
