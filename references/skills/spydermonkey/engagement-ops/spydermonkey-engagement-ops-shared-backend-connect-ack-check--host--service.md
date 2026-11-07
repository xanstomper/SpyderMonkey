# Shared-backend connect-ack check: prove a defect is provider-wide on a sibling socket — host / service

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-shared-backend-connect-ack-check.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **host** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

The anonymous namespace-connect-ACK test is cheap and portable — run it on ANY sibling brand's
socket host found in the provider stack (a new `v3.*` portal or `socketv4.<brand>` host) to prove
a forgeable-device-fingerprint / anonymous-connect defect is provider-wide, not a single-host
quirk. Identical connect-ACKs on all namespaces across brands = one shared backend design defect;
that multiplies every finding about it (a code bound to either brand's socket = control on the
shared pool). Register each reproducible brand as its own extension row ("vector reproducible on
<host>") with the shared-backend attribution in the proof.

**Enumerate and test the CONTROL-PLANE namespaces, not just the read-game ones.** The read-only
data namespaces (`/bet/log`, `/user`, `/game-support`) being anon-ACKed is MEDIUM; the finding
jumps to HIGH when an attacker-chosen fingerprint is also ACKed on the account/balance control
planes — the socket namespaces whose event layer moves money or changes security settings. On
socket.io/Vite estates these usually carry self-explanatory names discovered from the bundle's
route-guard strings (a `guards:[()=>"/user-action/..."]`-style path in the auth bundle names the
account-actions namespace; `/** merchants **/` or a merchant-protobuf in the SDK names the
balance socket). Dial the FULL namespace set — default set plus the ones you mined from guards —
and report which control-plane ones ACK. On bc.game the anonymous socket was ACKed on ALL FIVE
including `/user-action` (account-security / 2FA-bind surface) and `/merchants` (the balance-moving
socket) — the identity-provisioning surface is fully attacker-controlled on the money socket, which
completes the SPY-048 merchant-code-to-fingerprint takeover path. The event/data layer still gates
("connect-accept vs data gate" rule above) — but a forgeable identity reaching the balance socket's
connect layer is itself the HIGH finding.

## Probe adjustment (host × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
