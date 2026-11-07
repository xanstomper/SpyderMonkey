# Reflected-XSS triage: raw query-string reflection and the browser encode-set — worker / service

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-reflected-xss-triage-raw-query-s.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **worker** · auth **service** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

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

## Probe adjustment (worker × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
