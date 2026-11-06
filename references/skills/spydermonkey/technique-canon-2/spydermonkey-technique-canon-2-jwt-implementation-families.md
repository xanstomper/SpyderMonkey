# JWT implementation families

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

`none`-alg acceptance, kid-injection, jku/x5u self-keying, weak HMAC secrets (tested offline against a known dictionary ONLY on your own tokens). Decisive test per family: acceptance delta of the forged-but-harmless token.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
