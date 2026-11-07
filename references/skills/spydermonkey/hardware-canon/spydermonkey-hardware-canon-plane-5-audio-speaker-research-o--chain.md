# Plane 5 — Audio & speaker research (OWN files, OWN devices, lab) — chain composition

- source canon: `spydermonkey/hardware-canon.md`
- base technique: `spydermonkey-hardware-canon-plane-5-audio-speaker-research-o.md`
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
| Covert data-over-audio | `minimodem --tx 1200 -f data.wav` (own payload) → `minimodem --rx 1200 -f data.wav` | round-trip bit-exact on own channel |
| Audio data channel audit | `sox in.wav -n stat`/spectral view (own capture) — find out-of-band carriers | unexpected carrier/energy off the voice band |
| Ultrasonic feasibility | `sox`/`ffmpeg` upshift own test tone to 18–22kHz; `arecord` on own device pair | inaudible carrier decodes on own receiver — feasibility ONLY |
| DTMF/telephony tones | `multimon-ng -t dtmf -a AUDIO` (own IVR capture) | digits decoded from own recording |
| Speaker/device fingerprint | `ffmpeg` chirp playback on own speaker → own mic capture — impulse response | stable per-device signature (fingerprint research) |
| Voice-assistant mic wake | own assistant device: play own trigger phrase from owned audio — note LED/mic state | wake triggers on owned device only |
| Audio exfil proof of concept | own lab: encode file → play out of own speaker → record on own mic → decode | bit-exact round trip (lab channel, own gear) |

Walls: everything above runs on the operator's own audio gear or own
recordings; ultrasonic transmission is feasibility on own devices only and
stopped at proof. No surveillance of third parties, no hidden audio capture
of anyone but the operator.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
