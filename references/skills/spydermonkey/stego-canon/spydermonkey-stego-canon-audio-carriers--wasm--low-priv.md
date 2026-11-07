# Audio carriers — wasm / low-priv

- source canon: `spydermonkey/stego-canon.md`
- base technique: `spydermonkey-stego-canon-audio-carriers.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **wasm** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| WAV LSB | `wavsteg` -r (own wav) | embedded payload |
| Spectrum | `sox in.wav -n spectrogram` (own wav) | ghost tones/watermarks |
| MP3 frames | `mp3stego Decode -X` (own mp3) | hidden message |
| Phase/DSSS | `stegify`-class (own wav) | phase-coded data |
| Audio splice | `ffmpeg` + `audacity`-style spectrogram (own) | spliced segment |

## Probe adjustment (wasm × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
