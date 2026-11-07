# 2026-11-03 3AM final: demo inert, PF hypothesis upgraded, T2 stands

- source canon: `holyshit-mode/case-packdraw-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Demo mode: verified INERT for guests (4 click sequences incl post-Continue, DOM dumps,
  zero network) — no unauth seed-observation path exists.
- PF algorithm verbatim (from their fairness page): `ticket = (BigInt('0x'+sha512(
  clientSeed+':'+serverSeed+':'+nonce)) % 1_000_000) + 1`; jackpot = `sha256(eosBlockHash)
  % totalTickets + 1` with contiguous ticket ranges. Their text: nonce is needed "when
  server seeds and client seeds remain unchanged, as is the case when opening multiple
  packs in a single purchase"; the hashed server seed is shown in the account PROFILE
  before purchase and the unhashed seed exposed after. Account-level seed commitment +
  nonce-machinery = fixed-seed architecture hypothesis (58-70 if 2-open test confirms
  non-rotation across purchases). Full verify recipe documented in the ledger class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
