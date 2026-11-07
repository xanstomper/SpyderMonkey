# Kind 1 — contestant location fixes (record size 11) — wasm / root

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- base technique: `holyshit-mode-i***REDACTED***-binary-map-protocol-kind-1-contest.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **wasm** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

Layout after header (offsets are absolute, `o=36`, `l=recordCount`):
- `o+0` u32 definitionSequence (>0)
- `o+4` f64 ageBaseMs (epoch ms, grid of 100)
- `o+12` i32 latBase (scale 1e5, i.e. value/1e5 = degrees)
- `o+16` i32 lngBase (scale 1e5)
- `o+20` per-record i16 latDelta  (lat = (latBase + delta)/1e5)
- `o+20+l*2` per-record i16 lngDelta
- `o+20+l*4` per-record u16 slot
- `o+20+l*6` per-record u8 flags (bit1 = mock, bit2 = has age)
- `o+20+l*8` per-record u16 accuracyM (divide by 10 → meters)
- `o+20+l*10` per-record u16 ageSecondsAgo (at = ageBaseMs − v*100)

Example decode: header `01 01 01 00 ...`, latBase=3025493 lngBase=-9773031 → contestants slots 21/27/67 at lat 30.25479–30.25508, lng -97.73009…-97.73053.

## Probe adjustment (wasm × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
