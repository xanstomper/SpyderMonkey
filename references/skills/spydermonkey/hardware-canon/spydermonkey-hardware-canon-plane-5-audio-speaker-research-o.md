# Plane 5 — Audio & speaker research (OWN files, OWN devices, lab)

- source canon: `spydermonkey/hardware-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
