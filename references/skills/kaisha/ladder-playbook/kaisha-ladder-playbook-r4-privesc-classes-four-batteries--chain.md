# R4 — privesc classes (four batteries) — chain composition

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r4-privesc-classes-four-batteries.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Rung | Class | The ONE decisive test | Wall |
|---|---|---|---|
| R4a | sudo misconfig | `sudo -l` → match documented NO_PASSWD/safe-echo classes | listed, never executed for gain |
| R4b | SUID/cred-file | SUID + world-readable cred inventory (counts) | paths only, never contents |
| R4c | token/key-reuse | inventory → reuse-check against OWN second host | one shot, reversed |
| R4d | unit/path-trust | systemd unit + PATH inventory → trust classes | read-only, no modification |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
