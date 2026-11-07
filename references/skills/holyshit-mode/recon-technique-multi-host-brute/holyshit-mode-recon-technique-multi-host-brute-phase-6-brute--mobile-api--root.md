# Phase 6: Brute-Force Execution — mobile-api / root

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-6-brute.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mobile-api** · auth **root** · chain role **final**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- `x-export-password` brute-forced with trivial wordlist — password `madsys` matched on 7th attempt
- Same password worked on `x-refresh-password` — credential reuse confirmed
- Password is the Harvard MaDSys Lab team name — trivially guessable by anyone reading the status page or docs footer
- 20 rapid wrong-password probes returned zero 429s across both endpoints

## Probe adjustment (mobile-api × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
