# Honest-ceiling discipline under operator pressure ("find one") — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hon.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The operator repeatedly demanded a true escalation/forge/destructive vector. After
exhausting SSRF (url/base_url params ignored), cloud-metadata/IMDS (no internal proxy),
JWT-forge (opaque DB `session_id`, no signing secret), org-IDOR, admin broken-authz, and
mass-assignment (Turnstile-gated), the correct move was to **state the verified ceiling and
refuse to fabricate** — record the negative in the ledger, don't re-probe in a loop. Real
forges/escalations (key-mint, provisioning, org-admin, BYOK-drain) were all **behind the
auth wall**; without a supplied `xpl_` key/session, they were unreachable by design. Key
lesson: on a hardened dual-surface gateway, the compromisable surface is the misconfigured
internal fleet; the escalation plane is the auth-walled management API — and self-provisioning
credentials to reach it is account fraud, out of scope.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
