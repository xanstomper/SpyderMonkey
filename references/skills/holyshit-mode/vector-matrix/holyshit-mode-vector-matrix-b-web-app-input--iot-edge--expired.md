# B. WEB APP — INPUT — iot-edge / expired

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-b-web-app-input.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **iot-edge** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

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

## Probe adjustment (iot-edge × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
