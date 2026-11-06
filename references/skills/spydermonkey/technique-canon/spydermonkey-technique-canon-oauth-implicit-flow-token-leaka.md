# OAuth implicit-flow token leakage

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Implicit flow puts the access token in the URL fragment, which leaks via referrer and history. Decisive test: register a redirect_uri under your control in a dev client (or find the fragment echoed in any in-scope page), and observe `access_token` in the fragment path — proof is the fragment reaching a second-party surface. Crown: token lifetime + scope carried by the leak.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
