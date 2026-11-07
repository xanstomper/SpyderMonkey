# Edge-closed pivots — map the target with zero further contact — ci-cd / unauth

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-edge-closed-pivots-map-the-tar.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Google's verified-bot path renders the SPA through the same WAF: `site:<apex>` plus
  `site:<apex> <feature-keyword>` queries return the route map, rendered component text
  (region blockers, policy language), and embedded algorithm code (seed formats, verifier
  implementations) in snippets alone. Layer in careers/LinkedIn postings for the backend
  stack (framework, ORM, DB, queues) and affiliate-program review pages for platform +
  contacts.
- A domain that SERVFAILs at BOTH the local resolver and a public DoH resolver
  (`curl 'https://1.1.1.1/dns-query?name=<host>&type=A' -H 'accept: application/dns-json'`
  → `EDE(22): No Reachable Authority`) is dead at delegation, not locally filtered —
  recover its published content from the Wayback replay, not by re-resolving.
- Wayback CDX and replay are independent services: when CDX answers "Temporarily
  Offline", replay can still serve — fetch a known capture with
  `curl -sL --compressed 'https://web.archive.org/web/<timestamp>id_/<url>'`. The `id_`
  suffix returns raw archived bytes; without `--compressed` the body arrives gzip-wrapped.
- A published exploit writeup is a HISTORICAL finding: assume patched until proven
  otherwise (read the writeup's aftermath/disclosure section via its Wayback replay if
  the origin DNS is dead). Never re-validate one whose decisive test requires
  state-changing operations — that is impact execution, RoE-forbidden.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
