# T3 — Host takeover — ci-cd / machine

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t3-host-takeover.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **machine** · chain role **final**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- RCE confirmation (one command, read-only payload via the box's OWN binaries — LOTL);
  SSH key reuse (test the harvested key on the next host: auth success = proof, then
  stop); secret harvest on the box → cloud creds (env vars, `.aws/`, cloud CLI config,
  agent/runner tokens); cron/init/scripts revealing fleet hosts.
- **DECISIVE PROOF:** `id`/`whoami` over the authenticated channel, or the next host's
  SSH auth success. Then STOP.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
