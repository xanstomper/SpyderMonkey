# Capability Announcement (deliver on entry) — chain composition

- source canon: `spydermonkey/mandate.md`
- base technique: `spydermonkey-mandate-capability-announcement-deliver-on-entr.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
