# Pitfalls — websocket / hardened

- source canon: `undercroft/bundle-decode.md`
- base technique: `undercroft-bundle-decode-pitfalls.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **hardened** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Guessing API paths from docs alone misses the auth-gated surface — docs list
  public routes only; the client contract lists everything the app calls.
- A 404 with an EMPTY body on every guessed path means wrong base host or wrong
  prefix, not hidden routes — go back to the client's URL builder instead of
  brute-forcing prefixes.
- Vendor chunks (tone.js, zod, maplibre, react) are noise — grep for the app's own
  route vocabulary, not generic SDK strings.
- A string-table entry like `40IlQxWv` is a build-hash, not a route — filter
  entries to path/verb/host shapes before reading the table as an endpoint list.

## Probe adjustment (websocket × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
