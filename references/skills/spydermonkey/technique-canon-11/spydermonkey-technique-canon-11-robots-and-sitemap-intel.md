# Robots and sitemap intel

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

robots.txt and sitemap.xml enumerate paths the operators hid from crawlers. Decisive test: fetch both — disallowed paths probed with the SPA-shell control differential.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
