# Plane 5 — Audio & speaker research (OWN files, OWN devices, lab) — firmware / unauth

- source canon: `spydermonkey/hardware-canon.md`
- base technique: `spydermonkey-hardware-canon-plane-5-audio-speaker-research-o.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **firmware** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (firmware × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
