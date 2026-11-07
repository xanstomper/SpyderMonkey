# 2026-11-04 re-engagement — first FULL spydermonkey family run — firmware / unauth

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-2026-11-04-re-engagement-first.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **firmware** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

All traffic via Vermes (barbican gate correctly BLOCKED the home IP). Scope authority initialized (gamdom.com, perabet.com, 217.23.12.109; default-deny, max-rate 20). Three passive captures (60s/300s/600s, connect-frames only, zero emits, one connection each):
- **hidden_mode display_username leak STILL LIVE (3rd session)**: 45 unique real names + live walletInfo balances per capture. Unfixed. Disclosure draft still send-ready.
- **Forced-watch**: 3 fresh rounds all `forced:false` (distinct hashes 2b239b4d/cfc2c394/83c019e4). Escape hatch remains schema-only. Chain re-verify stays sealed.
- **Fossil box unchanged**: MariaDB 5.5.68 on 0.0.0.0:3306, VestaCP still mints unauth token + full config per GET, still authoritative DNS for the funnel; golvar8.com + sieveunem.net STILL unregistered (registrar-takeover vector live).
- **Drift**: sustained anon feed ~2.2KB/s (was ~15KB/s) — possible new anon throttle; build rotated (util chunks renamed; sha256 baselines in ledger).
- Family: undercroft 14 seams → kairo 56 vectors + AUTHBYPASS→DBLAYER→MATH chain → 3AM 3 teardowns → kaisha era-stack → kage 12 rules → shukaku no-gain wall held (register empty). WalletInfo forge test remains built-but-NOT-fired (needs authorized session). Deliverable: `~/gamdom-whitearmor-vectors-2026-11-04.md`. Captures wiped zero-documents.

## Probe adjustment (firmware × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
