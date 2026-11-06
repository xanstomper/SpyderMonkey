# Web cache poisoning (unkeyed input reflect)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Unkeyed header values cached into the response. Decisive test: header X with a unique marker, then a second unauthenticated request returning the marker = poisoned (one cache entry, your own marker, never a real user's path).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
