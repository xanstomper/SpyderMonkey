# Jurisdiction gates — classify the deny before hunting a bypass — browser / root

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-jurisdiction-gates-classify-th.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Geolocate the agent's OWN egress first (`curl -s ipinfo.io/json`): the cf-ray suffix
  on any response names the serving PoP. A residential/class-1 egress still denied
  means a jurisdiction rule; a datacenter ASN denied means IP-reputation. Root-cause
  the deny from what you are before spending requests on what they block.
- A hard block that persists across curl v4, curl v6, a spoofed browser UA, AND the real
  browser harness is IP-class/jurisdiction keyed, not fingerprint keyed. Confirm the
  jurisdiction read with two zero-contact checks: the target's own region-blocker text
  surfaced in Google's index of its pages, and the prohibited-GEO list on its affiliate
  program (search `<brand> affiliate prohibited GEO` — review aggregators publish the
  country list verbatim).
- `server-timing: cfEdge;dur=<n>,cfOrigin;dur=0` on a 403 means the origin was never
  touched — pure edge rule. Do not spend further requests hunting origin-reach tells.
- A jurisdiction deny is a STOP for access testing, not a vantage problem: switching
  egress to evade it is unauthorized access stacked on a legal control. The sanctioned
  door is the target's own disclosure/bounty program — verify it exists and pays from
  public writeups, then name it in the closeout instead of a bare "wall".

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
