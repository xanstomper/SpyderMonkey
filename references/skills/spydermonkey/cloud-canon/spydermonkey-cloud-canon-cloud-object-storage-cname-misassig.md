# Cloud Object Storage CNAME Misassignment (CLOUD-OBJ-02)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-07

## Route

- probes: `subfinder`, `amass`, `dnsx`, `subzy`, `dnstwist`, `dig-cname`, `dig-axfr`, `nuclei-takeover`, `urlcrazy`, `assetfinder`, `findomain`
- chains: `dns`, `takeover-full`, `osint`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: the service bucket still claimed — domtake's cloud cousin
- probe: the takeover engine's dangling-fingerprint class against cloud endpoints
- wall: NO-GAIN — claim status is proof; registration is never performed

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
