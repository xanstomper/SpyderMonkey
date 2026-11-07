# Raw-string trap in proxied HTML blobs (cost ~2 restarts) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-raw-string-trap-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Wrapping the playground HTML in a Python `r"""..."""` raw string to silence a `\s` SyntaxWarning
BREAKS the embedded JS — the JS needs Python `\n` → newline translation for SSE buffer scanning
(`buf.indexOf('\n\n')`), which a raw string turns into literal backslashes. Fix the warning by
escaping the specific JS regex backslashes (`[\s\S]`→`[\\s\\S]`, `<\/think>`→`<\\/think>`) so
Python emits literal single-escapes to the browser, NOT by raw-stringing the whole blob. A
SyntaxWarning on a JS regex inside an HTML string is harmless; don't degrade correctness to
silence it.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
