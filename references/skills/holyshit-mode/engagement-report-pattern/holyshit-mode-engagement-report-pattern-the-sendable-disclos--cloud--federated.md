# The sendable disclosure variant (Obsidian/client-ready) — cloud / federated

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-the-sendable-disclos.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

When the operator wants findings documented **to send to the target** (bounty, responsible
disclosure, or leverage), write a SECOND document distinct from the internal report — same
facts, different framing:

- **Professional disclosure tone, no tooling or vantage reveals** beyond what reproduces the
  bug: PoC links/requests a defender can run, code citations from THEIR OWN bundle, fixes per
  finding. No operator infrastructure names, no burner identities, no attack-tooling names.
- **Severity-ranked with honest credit**: state mitigations that work (a respected opt-out, a
  held gate) inside the finding — credibility with the target's security team is leverage,
  padding is not.
- **Claim-channel check BEFORE promising a bounty** (and before burning hours): fetch
  `/.well-known/security.txt`, grep the ToS for disclosure/bounty language, and search the
  platforms (Bugcrowd/HackerOne/Intigriti/Immunefi/YesWeHack/Cantina) for the target or its
  family. No program + no security.txt + silent ToS = **no payout channel exists** — say so
  early and frame the work as a disclosure package or portfolio, never as income. Never
  promise a bounty for a target with no claim channel.
- Deliverable placement: the operator's Obsidian vault (`~/Documents/Obsidian Vault/<Target>
  Redteam/`) as one markdown note per engagement, named for sending. Link the internal case
  file by name, not by content — the internal report keeps tooling/vantage detail; the sendable
  doc keeps only what the target may see.
- If raw evidence exists (socket captures, header dumps), say where it is preserved and offer
  the walkthrough — an offer to reproduce on demand is what converts a report into a bounty
  conversation.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
