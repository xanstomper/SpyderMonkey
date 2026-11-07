# Request smuggling CL.TE / TE.CL differential

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Two conflicting-header probes with a timing/response-length delta — ONE probe pair, never a burst against a shared edge. Decisive test: the differential timeout/smuggled-response signature in the lab replica first (dojo has the replica).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
