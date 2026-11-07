# 9.4 CT-log pivot ladder (score 85, zero contact)

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `curl -s 'https://crt.sh/?q=%25.<domain>&output=json' | jq -r '.[].name_value' | sort -u`
- Chain: CT names → partner brands (bundle `/providers/<brand>-originals`) → mirror/entrance
  hosts → passive DNS → bare-AWS origins. Dead DNS ≠ dead server: live cert + stripped DNS =
  "internal control panel" signature (→ §1.7).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
