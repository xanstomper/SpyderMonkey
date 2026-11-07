# Joomla/Drupal config and update-server classes

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

configuration.php exposure class, update-server MitM posture, Drupal services endpoints anonymous. Decisive test: config-path probe distinct from the SPA-control; services endpoint anonymous response.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
