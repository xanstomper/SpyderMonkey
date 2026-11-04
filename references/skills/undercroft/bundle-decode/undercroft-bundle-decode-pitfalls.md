# Pitfalls

- source canon: `undercroft/bundle-decode.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
