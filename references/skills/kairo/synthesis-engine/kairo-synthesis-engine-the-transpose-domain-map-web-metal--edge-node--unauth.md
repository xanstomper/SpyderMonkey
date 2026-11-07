# The TRANSPOSE domain map (web → metal) — edge-node / unauth

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-transpose-domain-map-web-metal.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **edge-node** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

| Web class | Metal analogue | The transposed probe |
|---|---|---|
| BOUNDARY | HWFLASH | scope-id trust on update/extract paths — swapped slot ids (lab, owned device) |
| REPLAY | HDRADIO | pairing/replay window — capture + replay ack frames (lab spectrum) |
| STATEBYPASS | HWFLASH | out-of-order OTA/bootloader stages — N+2 before N+1 |
| MATH | HDRADIO | precision drift in radio counters — worst values ×N |
| ENTITLEMENT | HWFLASH | provisioning order — entitlement flag before its check |
| AUTHBYPASS | HDRADIO | pairing-material entropy — effective bits from captures |

`kairo crossdomain --target T --from web --to hardware|radio` registers each as a
PROBED plane-ledger plan — lab-first, owned devices, never auto-CONFIRMED, never
distributed.

## Probe adjustment (edge-node × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
