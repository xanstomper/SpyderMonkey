# Reflected-XSS triage: raw query-string reflection and the browser encode-set — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-reflected-xss-triage-raw-query-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When a parameter reflects into HTML, run the DELIVERY test before registering any XSS claim —
most reflections die at the BROWSER, not the WAF:

1. **Identify the reflection mode**: send a marker with percent-encoded specials
   (`page=aa%22QQ1%22bb%27QQ2%27`). If the page shows `%22`/`%27` literally, the server echoes
   the RAW QUERY STRING (no decode) — encoded payloads are inert and only literal bytes inject.
2. **Map every reflection context** (the marker usually lands N times): canonical/hreflang/
   og:url attributes, `<a href>`, and inline event handlers
   (`onclick="location.href='...?page=MARKER'"` — the JS-string context is the exploitable one;
   pure-attribute contexts need a SPACE, which query strings cannot carry).
3. **A literal space is protocol-impossible in a query string** — it terminates the
   request-target, so any breakout needing attribute separation (`" onload=`) can never ride a
   query param. The space-free contexts are JS-string injection (`'` + `;`) and
   slash-separated tags (`<svg/onload=`).
4. **The decisive negative: browsers encode the break characters.** Chromium AND Firefox
   percent-encode `'` `"` `<` `>` in query strings. Verify in the LAB with ZERO target
   traffic: `python3 -m http.server` on 127.0.0.1 + headless firefox `--screenshot` on a
   payload URL, read the captured request path — `%27` in the log proves a victim browser
   never delivers raw bytes. curl sends raw; browsers never will. Register such a reflection
   as HARDENING (low), not XSS: "raw query-string echo, unescaped into N locations incl. an
   onclick JS-string; NOT browser-exploitable (decisive Chrome+Firefox encode test)".
5. **Map the combo-block pattern list with single probes**: pattern blockers
   (uniform small 400 bodies) block attack COMBOS (`"><svg/onload=`,
   `<img/src=x/onerror=`, `../`, `/etc/passwd`, `javascript:`) while raw single
   bytes (`" < > = ( ' ;`) pass individually. **Attribute the block layer from
   the 400 BODY before naming it a WAF**: a JSON app-error body
   (`{"status":"0","message":"Invalid request data."}`) is the APP's own input
   filter (framework hook), not mod_security — same combo-blocking, but it means
   no Apache-layer bypass exists to hunt and the app's validation code is the
   audit target. Combo-block + browser encoding together closes the
   zero-interaction lane; the click-required JS-string injection is the
   residual — register at its honest tier.
6. **No CSP/XSS/frame headers is the enabler context** for any residual injection — note it
   inside the same row, never as its own finding (headers-only rows are program-excluded).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
