# Tooling notes

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- holyleadger.py: `add <name> <confirmed|inconclusive|hypothesis|negative> --score N --technique "..." --target X`; report via `report --target X --out path`. Invalid status/class values exit 2 silently — stick to the four.
- Cloudflare 1010 WAF blocks python urllib — use curl with browser UA + `Origin` + `apikey` headers.
- Common failure: calling the wrong tool name (`shell` vs `terminal`) wastes turns. Be deliberate.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
