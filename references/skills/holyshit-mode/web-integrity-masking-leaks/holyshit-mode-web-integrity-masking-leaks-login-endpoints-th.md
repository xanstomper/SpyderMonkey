# Login endpoints that mint on any input

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

An API login returning `200 + token + config` for wrong passwords AND
nonexistent users is an UNCONDITIONAL SESSION MINT (an auth-design flaw worth
logging) — it is NOT access.

Discriminator (burned once by a false positive — four "default creds work!"
reports were all the anon shell):

- Compare wrong-password vs nonexistent-user responses FIELD-BY-FIELD.
- Populated `error` field + empty user/panel keys = mint-with-failed-auth.
- Only a real credential pair yielding a POPULATED user/panel = access.
- A naive "response contains token+panel" check false-positives.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
