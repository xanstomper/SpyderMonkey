# Other carriers

- source canon: `spydermonkey/stego-canon.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Polyglot | `file` + `binwalk` (own artifact) | two formats valid |
| Video frames | `ffmpeg` frame extraction → zsteg per frame (own) | frame-embedded data |
| PDF layers | `qpdf --show-objects` (own pdf) | hidden layers/attachments |
| Office content | `olevba`/`oleid` + `unzip -l` (own doc) | embedded objects |
| Trailing bytes | `xxd` tail + `strings` tail (own file) | appended payload |
| Cover vs stego | same-image diff (own pair) | byte drift located |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
