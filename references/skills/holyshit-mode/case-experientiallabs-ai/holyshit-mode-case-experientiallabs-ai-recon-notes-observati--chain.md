# Recon Notes (observation class, not scored as compromise) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-recon-notes-observati.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `api.experientiallabs.ai` public gateway: all `/v1/*` + management routes properly 401/no-auth.
  Well-hardened.
- Full public model catalog (500 models) keyless via `/api/models` + `/api/models/<slug>`:
  internal provider wiring, billing fields, and 8 leaked internal `base_url`s:
  `gateway.xplabs.ai/glm|glm3|qwen`, `wm.xplabs.ai`, `clef.xplabs.ai(|/flash)`.
- Internal fleet DNS fully enumerated & publicly reachable (GCP 34.44.x, Azure 20.125.x).
- Next.js admin console routes exist (`/admin/*`) but are signin-gated.
- Signup/onboarding, MFA, BYOK, provisioning-key flows all behind session auth — not
  bootstrapped (doctrine: no credential bootstrapping on operator's own estate; operator to
  supply a session/key for management-API IDOR depth).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
