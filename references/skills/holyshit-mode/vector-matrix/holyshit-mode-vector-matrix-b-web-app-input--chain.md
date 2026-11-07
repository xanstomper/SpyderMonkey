# B. WEB APP — INPUT — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-b-web-app-input.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- SQLi: error/boolean/time/stacked/OOB (DNS exfil) on every parameter class
- NoSQLi: `{"$ne":null}`, `$regex`/`$where` injection on JSON APIs
- Command injection: `;`/`|`/backtick/`$()`/newline variants, blind via DNS
- SSTI: `{{7*7}}` `${7*7}` `<%= 7*7 %>` in mailers/report generators/rendered fields
- Path traversal: `../` encoded/double/nested/null-byte; in filenames, ZIP entries, range headers
- XXE: file://, http:// SSRF pivot, OOB exfil, billion-laughs
- Open redirect: //evil, /\evil, %2F%2Fevil, @evil in redirect targets
- SSRF: URL-import/webhook features → 169.254.169.254, localhost, internal CIDRs, DNS rebinding
- Deserialization: Java (ysoserial classes), PHP (phar/unserialize gadgets), Python (pickle)
- Format-string/prototype pollution: `__proto__`, `constructor.prototype` in JSON merges

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
