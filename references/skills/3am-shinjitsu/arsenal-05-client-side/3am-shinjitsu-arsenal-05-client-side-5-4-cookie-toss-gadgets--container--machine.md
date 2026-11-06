# 5.4 Cookie-toss gadgets (score 85 — rainbet-verified class) — container / machine

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-4-cookie-toss-gadgets.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **machine** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- PLATFORMS: dangling preview wildcards (Netlify/Vercel/Cloudflare preview families) + the
  target's OWN tracker/attrib pages — any page that can `Set-Cookie: name=value;
  Domain=.<target>` for ANY name.
- GADGET: `media.<target>`-class pages writing ANY param as a 90d cookie on the MAIN domain
  (`?stel_token=<x>` → `stel_token` cookie) = fingerprint hijack by LINK when reserved names
  miss the auth/fingerprint cookie family (FingerprintJS client context included).
- DECISIVE: read the cookie-writer page's script; list reserved names; find the gap; craft
  the toss link; verify via operator's own browser session (no third-party accounts).
- Affiliate/stag hijack: same gadget overwriting attribution cookies.

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
