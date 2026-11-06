# Host-header routing at the edge (vhost collision)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Default/catch-all vhosts serving sibling brands (the oncasi :80 catch-all class). Decisive test: Host: sibling-brand on the origin IP — the wrong-site response = shared-origin evidence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
