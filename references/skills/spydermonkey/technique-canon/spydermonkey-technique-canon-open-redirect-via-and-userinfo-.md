# Open redirect via //, \\, and userinfo tricks

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

//evil.example, https:evil.example, /\evil.example parser-differential confusion. Decisive test: each variant's browser navigation (headless, local) — one variant navigates off-host = the class. Crown: redirect chains into OAuth redirect_uri (pairs with the OAuth class).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
