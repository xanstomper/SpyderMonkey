# T3 — Host takeover — container / high-priv

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t3-host-takeover.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **high-priv** · chain role **final**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- RCE confirmation (one command, read-only payload via the box's OWN binaries — LOTL);
  SSH key reuse (test the harvested key on the next host: auth success = proof, then
  stop); secret harvest on the box → cloud creds (env vars, `.aws/`, cloud CLI config,
  agent/runner tokens); cron/init/scripts revealing fleet hosts.
- **DECISIVE PROOF:** `id`/`whoami` over the authenticated channel, or the next host's
  SSH auth success. Then STOP.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
