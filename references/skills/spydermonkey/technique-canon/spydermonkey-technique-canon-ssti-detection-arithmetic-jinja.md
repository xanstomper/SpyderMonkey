# SSTI detection arithmetic (jinja/smarty/twig)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV** · **CWE-1336** · **ATT&CK T1059**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

{{7*7}} → 49 is the arithmetic marker; engine fingerprint follows ({{7*'7'}} → 7777777 = jinja2). Decisive test: the arithmetic marker reflected — class confirmed; template execution beyond arithmetic is RCE-class and is REPORTED, not executed (no-gain).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
