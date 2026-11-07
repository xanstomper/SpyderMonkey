# Price-override parameter injection — browser / expired

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-price-override-parameter-inject.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **browser** · auth **expired** · chain role **final**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

Hidden/ignored client fields (`price`, `discount`, `unitPrice`) that the serializer re-binds into the order. Decisive test: add price=1 to the POST body; a changed order total without a server-side entitlement check is the class. NEVER submit the poisoned order — the preview response is the proof (no-gain).

## Probe adjustment (browser × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
