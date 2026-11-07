# Session summary

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Target: gratisfy.xyz (Supabase/Kong auth stack on Cloudflare).
Focus: live OAuth redirect_uri override verification, free-API access, unthrottled brute surfaces.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
