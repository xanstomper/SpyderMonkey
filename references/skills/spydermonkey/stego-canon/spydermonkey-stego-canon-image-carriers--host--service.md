# Image carriers — host / service

- source canon: `spydermonkey/stego-canon.md`
- base technique: `spydermonkey-stego-canon-image-carriers.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Metadata | `exiftool -a` (own image) | comments/gps/soft markers |
| LSB detect | `zsteg -a` (own png/bmp) | lsb data found |
| DCT/Jsteg | `stegdetect -t jopi` (own jpeg) | jsteg/outguess hit |
| Whitespace | `snow -C` (own file) | whitespace payload |
| Palette/alpha | `pngcheck` + channel compare (own) | palette anomalies |
| Brute passphrase | `stegseek` (own file, own wordlist) | passphrase recovered |
| Carve | `foremost`/`binwalk -e` (own container file) | hidden archive |
| Color tables | `zsteg -E` channel walk (own) | data in color index |

## Probe adjustment (host × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
