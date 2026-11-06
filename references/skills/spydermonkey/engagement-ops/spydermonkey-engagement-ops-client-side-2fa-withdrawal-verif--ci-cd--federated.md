# Client-side 2FA / withdrawal-verify gate: reverse it read-only from the app bundle — ci-cd / federated

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-client-side-2fa-withdrawal-verif.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **federated** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

When a victim report claims a 2FA-bypass drain (withdrawal completed with NO OTP prompt, an new
whitelist address riding in the same window), you can CHARACTERIZE the mechanism from the target's own
client code without ever executing a state-changing withdrawal — the read-only, within-walls move.

1. **Mine the route chunk manifest for the withdrawal-verify modules.** On a Vite-bundled SPA the
   lazy chunk names often leak the purpose: grep the main bundle / a dependency map file for
   `getVerifyType|twofa-verify|withdraw.*|VerifyCodeInput|whiteList|getVerifyType` patterns — the
   `getVerifyType`-style module is the one that DECIDES how hard the withdrawal check is.
2. **Pull the module and read its scenario decision.** The pattern that exposes the flaw:
   ```js
   let n = 2;                                   // default = full 2FA ("TWO_STEPS")
   n = (yield post('/payment/withdraw/<x>/get/getVerifyType/', {currency,amount})).optionCount ?? n;
   if (n === 2) scenario 'WITHDRAW_TWO_STEPS'   // server demands a real OTP
   else         scenario 'WITHDRAW_ONE_STEP'    // single step, no 2FA
   ```
   If the CLIENT decides two-step vs one-step from a server `optionCount` it blindly trusts, and the
   `else` branch is the one-step/no-OTP path, then ANY authenticated caller who hits the non-2 branch
   gets a withdrawal past the 2FA wall. That is the mechanism behind the "no-OTP drain" — the client
   short-circuits 2FA whenever `optionCount!==2`, and the whitelist-address add often rides the same
   degraded path.
3. **Cross-reference the app's login-source → 2FA-method map** (`phone-code→phone`, `email-code→email`,
   `google-2step-auth→google_2fa`) and the error taxonomy (`TWOFA_ERROR:4002`, `SESSION_ERROR:6003`,
   `NEED_LOGIN:6002`) from the main bundle — they confirm server distinguishes 2FA-fail from
   session-fail, which pins the decision to the flow you found.
4. **Confirm what a caller can see anonymously.** POST the `getVerifyType` endpoint anonymously: a 200
   SPA-shell body (not JSON) means `optionCount` is only returned to an authenticated caller — the
   structural flaw is proven from the code but the live `optionCount` value is session-gated. State
   that gap honestly; CONFIRMED finding = "client-trusted optionCount can downgrade withdrawal 2FA to
   one-step" (severity HIGH, CWE-306 into AUTHN), with the fix demands: the verification scenario must
   be SERVER-ENFORCED (server says which code types are required for THIS transaction, never a
   client-decided count), and adding a whitelist address must independently require full 2FA server-side.
5. **Walls:** never EXECUTE the one-step withdrawal to prove it — that is state-changing on a
   financial target. The code-level characterization + the optionCount-read is the deliverable.

This ordering (reverse the verify-decider, then probe the endpoint read-only) turns a "reverse 2FA"
request into a bankable AUTHN finding without crossing the no-fund-movement line.

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
