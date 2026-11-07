# Automation-first + shreddable workspace (operator mandate)

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **Automate every queued test on the VM before asking the operator for anything.**
  "Operator console" tests (auth flows, wallet signatures) get a VM kit first: write a phased
  python kit at home, `scp` it over, run phases paced (3.5–6.5s jitter, adaptive backoff on
  403/429, hard stop at 3 consecutive blocks, JSONL verdict log). Hand the operator a console
  test ONLY when the VM wall for that endpoint class is PROVEN — never assumed.
- **Workspace:** all engagement data (results, captures, burner keys, session tokens) goes in
  `/dev/shm/.dkv/` (RAM tmpfs: gone on reboot) plus a `shred.sh` (`rm -rf` the dir) for the
  one-command wipe. NEVER store engagement data on the home box.
- **/dev/shm is mounted noexec on OL9** — venvs/binaries can't execute from RAM. Venv +
  tooling live on disk (`~/dkv-venv`), artifacts in RAM; the shred script wipes both.
- Step 0 of any VM session: `curl -s https://api.ipify.org` to log the egress IP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
