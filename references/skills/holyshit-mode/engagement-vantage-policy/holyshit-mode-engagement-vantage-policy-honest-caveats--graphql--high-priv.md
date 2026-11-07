# Honest caveats — graphql / high-priv

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-honest-caveats.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Datacenter IPs get challenged harder by some WAFs (Fastly/Turnstile fingerprints ASN) —
  if a wall appears that the same probe never hit from home, diff the vantage before blaming
  the probe.
- Vermes holds keys (reverse-tunnel identity, hermes/mochi auth) — probe scripts stay
  read-only curl/socket work; never drop stored target credentials on the VM.
- Never re-probe gamdom.com from the home IP while the ban stands (and don't from the VM
  either without re-checking the case file first).

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
