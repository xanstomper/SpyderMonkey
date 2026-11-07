# HOLY SHIT #2 — Shared global conversation context / cross-user disclosure (score 85) — mobile-api / federated

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-holy-shit-2-shared-global-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `prompt_tokens` DRIFTED on identical input across requests (21k → 30k → 50k) → context is server-side state, not static per-request injection. **PTOK drift on identical input = shared-context oracle.**
- No cookies/sessions at all, yet the model recalled ALL prior turns from earlier separate curls → global buffer keyed on nothing.
- Foreign users' roleplay content (character personas never sent by us) appeared in context. Anyone can read out other users' conversations via a summarization oracle and poison the shared context for everyone.
- The model itself CONFIRMED the history ("Turns 1–8...") when asked — the disclosure oracle is one prompt away for any user.

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
