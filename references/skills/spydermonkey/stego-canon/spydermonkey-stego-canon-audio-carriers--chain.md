# Audio carriers — chain composition

- source canon: `spydermonkey/stego-canon.md`
- base technique: `spydermonkey-stego-canon-audio-carriers.md`
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

| Probe | Test | Confirmed-when |
|---|---|---|
| WAV LSB | `wavsteg` -r (own wav) | embedded payload |
| Spectrum | `sox in.wav -n spectrogram` (own wav) | ghost tones/watermarks |
| MP3 frames | `mp3stego Decode -X` (own mp3) | hidden message |
| Phase/DSSS | `stegify`-class (own wav) | phase-coded data |
| Audio splice | `ffmpeg` + `audacity`-style spectrogram (own) | spliced segment |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
