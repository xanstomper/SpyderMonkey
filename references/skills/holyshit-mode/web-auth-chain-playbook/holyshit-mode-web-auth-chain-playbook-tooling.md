# Tooling

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Cloudflare 1010 blocks python urllib — use curl with browser User-Agent + Origin headers.
- holyleadger.py: statuses are only {confirmed, hypothesis, inconclusive, negative};
  report flags are `--target X --out file`; needs `HOLYSHIT_SCRIPT_DIR=/home/jewboy420/.hermes/scripts`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
