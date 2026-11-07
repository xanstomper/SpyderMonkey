# Image carriers

- source canon: `spydermonkey/stego-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
