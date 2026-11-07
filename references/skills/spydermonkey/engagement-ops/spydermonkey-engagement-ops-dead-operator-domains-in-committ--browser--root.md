# Dead operator domains in committed tooling = registerable asset-recovery vector — browser / root

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-dead-operator-domains-in-committ.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

When mining an operator's public org repos, grep EVERY committed HTML/bundle for `src=`/`url`
third-party hosts — an operator's own verifier/fairness pages often hot-load a game logo or
asset from a domain that has since lapsed. A referenced domain that is now DEAD is a
registration-recovery/supply-chain finding, not just a broken image:

1. `grep -rn "<brand>.*\.com\|https://" <org repos>` → collect distinct foreign hosts loaded by committed tooling.

**Grep the operator's INFRA-ORCHESTRATION files too, not just committed pages** — a dead
domain this class surfaces is often the whole trading/game infra family: `docker-compose.yml`
`image:` entries (`hub.<dead-domain>/<svc>:latest` = the image registry is gone → any live deploy
still pulling those images ingests anyone-who-registers content), file-upload hosts in test
fixtures / SQL seed data (`fileupload.<dead-domain>/file/download/<uuid>.png`), and apex domains
in asset_logo_url columns. On the bcgame merchant-integrator repo the dead `ssmartoption.com`
family (NXDOMAIN + whois `No match` = registerable) carried the docker registry `hub.`, the
`fileupload.` host, AND dozens of forex-asset logo URLs in a `*.sql` seed — all behind the same
merchant stack. Register with IN-ESTATE attribution and note whether the dead family is the
TARGET's own infra or (as here) a merchant-INtegrator's trading stack referenced by target-facing
SDK code — the attribution classes the finding's real reach.
2. For each non-bigtech host, test liveness from the VM: `dig +short <host> A`, then `whois <host>`
   filtered for `No match for domain` / `Domain Status: pendingDelete|redemptionPeriod`. NXDOMAIN OR
   whois "No match" = the domain is UNREGISTERED and anyone can register it.
3. If the dead domain is loadable by any live page/tool (or referenced by the operator's own
   provably-fair verifier the players are told to use), that's the vector: re-register it and serve
   attacker content into the operator's tooling — register (MEDIUM) with the IN-ESTATE asset and
   the dead domain + whois result in the proof. Fix demand: re-register or retire the domain, audit
   every committed asset URL in the operator repos for dead/expired domains, and never load
   game/PF-asset from third-party domains without SRI.
4. Scope gate: the dead domain is itself out-of-estate — register with the target's in-estate asset
   (`--asset <target>`), dead domain in title/proof with explicit attribution.

This compounds the personal-worker / no-SRI provider-host findings: every unchecked third-party
asset load on an operator's pages is a delivery point.

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
