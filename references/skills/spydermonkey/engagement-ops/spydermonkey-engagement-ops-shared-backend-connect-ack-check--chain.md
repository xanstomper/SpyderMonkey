# Shared-backend connect-ack check: prove a defect is provider-wide on a sibling socket — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-shared-backend-connect-ack-check.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
