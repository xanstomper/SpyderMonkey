# Jurisdiction gates — classify the deny before hunting a bypass

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
