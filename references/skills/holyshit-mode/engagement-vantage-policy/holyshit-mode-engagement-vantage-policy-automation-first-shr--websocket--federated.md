# Automation-first + shreddable workspace (operator mandate) — websocket / federated

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-automation-first-shr.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **federated** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (websocket × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
