# Vantage discipline (home PC + Oracle VM) — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-vantage-discipline-home-pc-oracl.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **The family orchestration gate (barbican/shiki) demands a LOCAL libvirt VM and will ABORT
  at step-0 (`ENGAGEMENT GATE CLOSED`) when none runs — even when the sanctioned egress is a
  REMOTE SSH VM (Oracle `vermes`, 92.5.99.31).** Posture with `--vantage vm` satisfies the
  declared-shield rule but not the gate's live VM check, so `shiki assault`/`mission` cannot
  drive the probe engines against this estate from the home box. That abort is the shield
  working, not a bug; do not force it. The correct pattern: run the probe-capable engines
  (undercroft run, target protocol clients, RTP sweeps) by `scp`+`ssh vermes` so traffic
  egresses as the VM, and run the OFFLINE family engines (kairo forge/chain, holyshit
  dossier, shukaku, kage) locally under the stored posture. When the user says "use all of
  spydermonkey," that means fire kairo synth+forge+chain + the armed protocol client on the
  VM + the offline mandates — not force the gate.
- Probe scripts that only READ public endpoints: `scp` to the VM (`vermes`) and run there —
  egress is the sanctioned vantage with zero proxy plumbing. Write every probe/hook script as
  a LOCAL file and scp it — nested-quote heredocs piped through ssh corrupt at the second
  quoting level and cost multiple retries; a local file + `ssh vermes 'node /tmp/x.js <arg>'`
  lands in one shot.
- Family engines that keep state locally: run on the home box behind
  `ssh vermes -D 1080 -N` + `ALL_PROXY/HTTPS_PROXY/HTTP_PROXY=socks5h://127.0.0.1:1080`.
  requests needs pysocks (venv has no pip: `python3 -m ensurepip` first).
- **After a VM-run undercroft, pull the state back BEFORE kairo ingest — and mark poison rows EXHAUSTED first.** A VM-run undercroft writes its own `~/.redteam/campaigns/<t>/undercroft-state.json` ON THE VM; the local `kairo ingest` reads 0 findings until you `scp` it back into the local campaign dir. WAF-challenge hits register as CONFIRMED surface rows (a CF block page is a distinct body, so undercroft's SPA-fallback check cannot tell) — flip every challenge-page row to `EXHAUSTED` with a pointer to the ledger row that proved the poison BEFORE ingesting, or the row feeds chain detection as a phantom seam.
- The socks5h env breaks pip and localhost APIs — wrap those calls in
  `env -u ALL_PROXY -u HTTPS_PROXY -u HTTP_PROXY`.
- **The vermes SOCKS tunnel idle-reaps in ~15–20 min even with ServerAliveInterval
  keepalives** — a dead tunnel manifests mid-batch as curl `000`/proxy connect errors, not a
  clean failure. Re-verify the exit IP (`curl -s -m 15 -x socks5h://127.0.0.1:1080
  https://ifconfig.me` must return the VM IP) at the START of every live-fire batch and
  restart `ssh vermes -D 1080 -N` whenever it dropped.
- **Write probe scripts to files instead of inline bash loops.** Nested quotes, Korean text,
  and payload specials (`'`, `;`, `"`, `%`) break inline `for`/one-liner loops with confusing
  EOF errors; a `write_file`-created `.py` driving `subprocess.run` with ARG LISTS (never a
  shell string) is quoting-immune and reusable across waves.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
