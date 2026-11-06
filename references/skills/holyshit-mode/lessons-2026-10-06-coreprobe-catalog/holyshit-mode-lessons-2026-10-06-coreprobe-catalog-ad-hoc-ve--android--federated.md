# Ad-Hoc Verify Harness Pitfall (hit 3× this session) — android / federated

- source canon: `holyshit-mode/lessons-2026-10-06-c***REDACTED***-catalog.md`
- base technique: `holyshit-mode-lessons-2026-10-06-c***REDACTED***-catalog-ad-hoc-ve.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **android** · auth **federated** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

When a verification-status system demands a fresh `/tmp/hermes-verify-*` script:

1. **Never assert stricter than the repo's own test tolerance.** Asserting EVERY `ios` field parses
   failed because the repo invariant tolerates free-text eras ("pre-iOS4 era", "iPod bootrom (IMG1
   partition handling)"). Scope ad-hoc assertions to exactly the changed behavior (e.g. the 7 new
   entries), not the whole dataset.
2. **Use a FIXED script name** (`/tmp/hermes-verify-<topic>.py`). A `$(date +%s)`-suffixed name
   defeats the subsequent `rm /tmp/hermes-verify-*.py` cleanup glob and leaves junk behind.
3. **Keep it short enough to eyeball** — a variable-name typo (`install` vs `inst`) failed a run.
4. Print `AD-HOC VERIFY: N/N passed` and report explicitly as **ad-hoc, never as suite green**.

## Probe adjustment (android × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
