# Impact gates (test in order) — chain composition

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- base technique: `holyshit-mode-cookie-toss-and-attribution-gadgets-impact-gat.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Fingerprint hijack**: identity cookie = a device-fingerprint visitorId (e.g. FingerprintJS
  Pro). The SPA typically SKIPS fingerprint generation when the cookie exists (early-return
  before the `import('https://fpjscdn.net/...')`). Verify end-to-end in a real browser:
  toss the cookie via the tracker page → navigate the main site → the value must SURVIVE the
  SPA load (not overwritten) AND the fingerprint library must NEVER be fetched (check the
  network log for the fp CDN) → the attacker value is the adopted device identity. Impact:
  device-ban evasion + risk-model poisoning. Verify the control too: without the toss the lib
  may load LAZILY (not at page load) — absence of the CDN fetch on page load alone is NOT the
  discriminator; the toss-survival is.
- **Attribution/affiliate hijack**: attribution cookies (`stag`, referral) read at signup —
  an attacker link claims commission on the victim's deposits forever. Watch for a
  force-set FIXED default tag (their own ad pipeline) proving the cookie drives attribution.
- **Session fixation surface**: session cookie names missing from the reserved list = plantable.
  The verdict needs the server's Set-Cookie attributes from a real login (host-only vs domain,
  path scope) — before a session exists, rate as a surface, not a chain.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
