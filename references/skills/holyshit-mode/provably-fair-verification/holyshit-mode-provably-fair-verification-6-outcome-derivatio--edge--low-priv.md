# 6. Outcome-derivation test — edge / low-priv

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-6-outcome-derivatio.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **edge** · auth **low-priv** · chain role **pivot**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Apply the standard hash→multiplier formula (bustabit-style: first 52 bits of the hash
→ house-edge curve) to captured rounds and compare to observed crash points. Mismatch
= the operator uses their own curve — locate it in the client math chunk (grep the
pooled bundle for the game's math/config module). Not a finding alone, but full public
verification requires the exact derivation to be documented.

## Probe adjustment (edge × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
