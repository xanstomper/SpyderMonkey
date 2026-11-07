# Error-code vocabulary = the API feature map

- source canon: `holyshit-mode/client-bundle-source-study.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Grep all chunks for the platform's error-code prefix (e.g. `er_[a-z0-9_]+`) and sort: every
`er_<feature>_<failure>` names an endpoint family that may not appear in any fetch site
(kick, telegram, sol, kyc/persona, vault+2fa, raffles, seeds, party). 150+ codes = a full
hidden-surface inventory; score only after probing, but USE the map to pick probe targets
(and to spot auth methods the current UI hides, e.g. sol-wallet sign-in codes without a UI
button).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
