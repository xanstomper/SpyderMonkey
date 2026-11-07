# Raw-string trap in proxied HTML blobs (cost ~2 restarts)

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Wrapping the playground HTML in a Python `r"""..."""` raw string to silence a `\s` SyntaxWarning
BREAKS the embedded JS — the JS needs Python `\n` → newline translation for SSE buffer scanning
(`buf.indexOf('\n\n')`), which a raw string turns into literal backslashes. Fix the warning by
escaping the specific JS regex backslashes (`[\s\S]`→`[\\s\\S]`, `<\/think>`→`<\\/think>`) so
Python emits literal single-escapes to the browser, NOT by raw-stringing the whole blob. A
SyntaxWarning on a JS regex inside an HTML string is harmless; don't degrade correctness to
silence it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
