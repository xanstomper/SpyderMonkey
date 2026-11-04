# T4 — Cloud account takeover — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t4-cloud-account-takeover.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Secret leak → `sts get-caller-identity` success in the target account; bucket/object
  keys → deeper IAM; metadata/SSRF → instance role credential (one `get-caller-identity`,
  owned infra only for the decisive call); exposed snapshot/AMI → root volume → secrets;
  OIDC federation misconfig (documented-PoC); over-scoped service principals.
- **DECISIVE PROOF:** the harvested identity resolves to the target account and lists
  one resource. Then STOP.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
