# Weak local crypto classes — chain composition

- source canon: `spydermonkey/technique-canon-10.md`
- base technique: `spydermonkey-technique-canon-10-weak-local-crypto-classes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

ECB mode, static IV, MD5/SHA1 for tokens in the app's own code. Decisive test: decompiled crypto-site inventory + two-ciphertext prefix test = the class.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
