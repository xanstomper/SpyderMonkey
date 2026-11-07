# 2026-11-03 vector sweep round (customer info / control panels / wallet)

- source canon: `holyshit-mode/case-packdraw-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
