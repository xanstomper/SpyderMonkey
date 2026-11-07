# Hashing & password storage

- source canon: `spydermonkey/crypto-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Hash identification | `name-that-hash` on OWN dump | plaintext-friendly scheme (md5, lm) |
| Salt presence | `hashid -m` + `john --show` on own dump | unsalted scheme |
| Fast-hash brute | `hashcat` benchmark on own dump (mode table) | runtime < policy floor |
| Length-extension | `hashpump`-class tool on own MAC | length-extendable construction (lab) |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
