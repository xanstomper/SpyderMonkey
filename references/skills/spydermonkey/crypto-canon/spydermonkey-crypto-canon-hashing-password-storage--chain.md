# Hashing & password storage — chain composition

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-hashing-password-storage.md`
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

| Probe | Test | Confirmed-when |
|---|---|---|
| Hash identification | `name-that-hash` on OWN dump | plaintext-friendly scheme (md5, lm) |
| Salt presence | `hashid -m` + `john --show` on own dump | unsalted scheme |
| Fast-hash brute | `hashcat` benchmark on own dump (mode table) | runtime < policy floor |
| Length-extension | `hashpump`-class tool on own MAC | length-extendable construction (lab) |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
