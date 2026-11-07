# Price-override parameter injection — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-price-override-parameter-inject.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Hidden/ignored client fields (`price`, `discount`, `unitPrice`) that the serializer re-binds into the order. Decisive test: add price=1 to the POST body; a changed order total without a server-side entitlement check is the class. NEVER submit the poisoned order — the preview response is the proof (no-gain).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
