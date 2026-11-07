# Ladder (worked end-to-end in one session) — ci-cd / root

- source canon: `holyshit-mode/operator-infra-access-recovery.md`
- base technique: `holyshit-mode-operator-infra-access-recovery-ladder-worked-e.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **ci-cd** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

1. **Orient on this box:** `hostname -I`, `ip route`, `systemd-detect-virt`, `free -h` —
   establish what the CURRENT machine is so the target isn't self.
2. **LAN sweep if the target is LAN-side:** `nmap -T4 --open -p <common ports> <subnet>/24`,
   then full `-p-` only on candidates. Triage hosts by fingerprinting ports (rokudev digest
   realm = Roku, AirTunes = AirPlay, noVNC/websockify = KVM console, minecraft = game box).
   Don't chase consumer appliances — they're not the target.
3. **Check the target isn't a VM ON the current host:** `ps aux | grep -E "qemu|kvm|virtualbox"`,
   `virsh list`, `lxc-ls`, `docker ps`, listening noVNC ports (5900/6080 websockify).
4. **Mine local credential/SSH artifacts (the high-yield step):**
   - `ls ~/.ssh/` — keys + `known_hosts`; also `ls ~/Downloads/*.key` (Oracle console-downloaded
     keys land there: `ssh-key-YYYY-MM-DD.key`), `chmod 600` before use.
   - `grep -rn "opc@\|ubuntu@\|ssh -i" ~/.hermes/skills/ ~/<deploy-dirs>/` — prior-session skill
     reference files and deploy scripts routinely contain the exact `ssh -i KEY user@IP` line.
     On 2026-10-23 the host+IP+key for the Oracle VPS came from
     `skills/software-development/zynema-maintenance/references/providers-adblock-plugins.md`.
   - Shell history, `~/.oci/config`, `~/.hermes/.env`.
5. **Verify by firing the found command once:** `ssh -i KEY -o BatchMode=yes user@IP 'hostname; free -h'`.
   Match the operator's hint (hostname "poop", 15Gi RAM) before declaring success.

## Probe adjustment (ci-cd × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
