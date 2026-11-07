# B. WEB APP — INPUT

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
