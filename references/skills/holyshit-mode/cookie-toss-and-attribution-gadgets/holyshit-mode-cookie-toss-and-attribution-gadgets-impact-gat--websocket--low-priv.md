# Impact gates (test in order) — websocket / low-priv

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- base technique: `holyshit-mode-cookie-toss-and-attribution-gadgets-impact-gat.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

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

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
