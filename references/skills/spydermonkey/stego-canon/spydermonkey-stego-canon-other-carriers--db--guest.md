# Other carriers — db / guest

- source canon: `spydermonkey/stego-canon.md`
- base technique: `spydermonkey-stego-canon-other-carriers.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **db** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the engine's own handshake/banner first — auth-stage reachability is the inventory row
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Polyglot | `file` + `binwalk` (own artifact) | two formats valid |
| Video frames | `ffmpeg` frame extraction → zsteg per frame (own) | frame-embedded data |
| PDF layers | `qpdf --show-objects` (own pdf) | hidden layers/attachments |
| Office content | `olevba`/`oleid` + `unzip -l` (own doc) | embedded objects |
| Trailing bytes | `xxd` tail + `strings` tail (own file) | appended payload |
| Cover vs stego | same-image diff (own pair) | byte drift located |

## Probe adjustment (db × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
