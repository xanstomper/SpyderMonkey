# T3 — Host takeover

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- RCE confirmation (one command, read-only payload via the box's OWN binaries — LOTL);
  SSH key reuse (test the harvested key on the next host: auth success = proof, then
  stop); secret harvest on the box → cloud creds (env vars, `.aws/`, cloud CLI config,
  agent/runner tokens); cron/init/scripts revealing fleet hosts.
- **DECISIVE PROOF:** `id`/`whoami` over the authenticated channel, or the next host's
  SSH auth success. Then STOP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
