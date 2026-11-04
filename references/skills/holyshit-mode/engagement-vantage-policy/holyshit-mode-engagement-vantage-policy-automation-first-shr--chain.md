# Automation-first + shreddable workspace (operator mandate) — chain composition

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-automation-first-shr.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
