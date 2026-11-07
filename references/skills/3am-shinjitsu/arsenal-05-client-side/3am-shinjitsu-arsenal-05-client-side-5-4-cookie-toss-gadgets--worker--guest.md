# 5.4 Cookie-toss gadgets (score 85 — rainbet-verified class) — worker / guest

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-4-cookie-toss-gadgets.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
