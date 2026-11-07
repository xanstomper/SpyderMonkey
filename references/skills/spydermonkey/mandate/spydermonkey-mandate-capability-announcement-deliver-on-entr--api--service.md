# Capability Announcement (deliver on entry) — api / service

- source canon: `spydermonkey/mandate.md`
- base technique: `spydermonkey-mandate-capability-announcement-deliver-on-entr.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **api** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

```
▸ SPYDERMONKEY — DISPATCHER ONLINE
  ═══════════════════════════════════
  [ OK ] barbican   — the shield: posture · vantage · sanitize · wipe
  [ OK ] holyshit   — the finder: 31+ case canon · recon · dossiers · handoff
  [ OK ] undercroft — the descent: live auto-engagement (scan/JWT/routes/boundary)
  [ OK ] 3AM        — the performer: sweep · takeover · growth loop
  [ OK ] kairo      — the synthesizer: findings → attacks → chains → distributed
  [ OK ] kaisha     — the ladder: era-stack · privesc rungs · lateral (depth leg)
  [ OK ] shukaku    — the harvester: crown register · valuation · disclosure map
  [ OK ] kage       — the mirror: confirmed attacks → detection rules (purple)
  [ OK ] dojo       — the range: vulnerable replicas · lessons (lab-bound)
  [ OK ] shiki      — the command: assault · parallel · adaptive · resume · close
  ⚡ THE FAMILY IS UP · contracts verified · awaiting P0: target · objective · authorization
```

## Probe adjustment (api × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
