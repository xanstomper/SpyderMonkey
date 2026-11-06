# Jurisdiction gates — classify the deny before hunting a bypass — chain composition

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-jurisdiction-gates-classify-th.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
