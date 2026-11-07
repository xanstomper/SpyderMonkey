# Edge-closed pivots — map the target with zero further contact — chain composition

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-edge-closed-pivots-map-the-tar.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
