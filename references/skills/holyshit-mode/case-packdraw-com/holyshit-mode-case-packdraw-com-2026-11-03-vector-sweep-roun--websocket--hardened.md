# 2026-11-03 vector sweep round (customer info / control panels / wallet) — websocket / hardened

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-vector-sweep-roun.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **hardened** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- **Customer info:** NOT reachable unauth. Public `pack-result`/`created` stream verified =
  product+price only (live DOM + RSC checked); private channels 403; SSR anonymized.
- **Control panels:** absent on every plane (prod 404/ghost, alias host-level-405, staging
  Vercel-auth 401; admin staff dashboard internal names all 404).
- **Wallet/drain plane:** money APIs = server actions behind auth; deposit/cashout
  mechanics invisible unauth. The only drain-class chain remains PF seed-prediction
  (operator 2-open test). Alias = static shell, POST blocked host-level (405 everywhere =
  Vercel frozen deployment, NOT routes - discriminator: 405-on-all-paths means host-level
  block, not route existence).

## Probe adjustment (websocket × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
