# 5.4 Cookie-toss gadgets (score 85 — rainbet-verified class) — chain composition

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-4-cookie-toss-gadgets.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- PLATFORMS: dangling preview wildcards (Netlify/Vercel/Cloudflare preview families) + the
  target's OWN tracker/attrib pages — any page that can `Set-Cookie: name=value;
  Domain=.<target>` for ANY name.
- GADGET: `media.<target>`-class pages writing ANY param as a 90d cookie on the MAIN domain
  (`?stel_token=<x>` → `stel_token` cookie) = fingerprint hijack by LINK when reserved names
  miss the auth/fingerprint cookie family (FingerprintJS client context included).
- DECISIVE: read the cookie-writer page's script; list reserved names; find the gap; craft
  the toss link; verify via operator's own browser session (no third-party accounts).
- Affiliate/stag hijack: same gadget overwriting attribution cookies.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
