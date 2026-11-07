# Common WebSocket Auth Patterns to Discover — grpc / federated

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-common-websocket-auth-p.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **grpc** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Mine the JS bundle for the auth flow. Search for the `WebSocket` constructor and the
first `send()` call. Typical patterns:

1. **Token in first frame** (most common):
   ```js
   this.socket = new WebSocket(socketUrl);
   this.socket.onopen = () => {
     this.send({type: "authenticate", token: r.token});
   };
   ```
   → Auth lives in the **token source** (usually `POST /api/.../session`), not the WS itself.

2. **Token as query param**:
   ```js
   new WebSocket(`wss://target/socket?token=${token}`)
   ```
   → Test: does the server validate the token, or accept any string? Does the token expire?

3. **Cookie-based** (invisible in upgrade headers):
   ```js
   new WebSocket(socketUrl);  # cookies auto-sent
   ```
   → Test: does an unauthenticated session get a working socket?

4. **Signed URL with expiry**:
   ```js
   new WebSocket(signedUrl)  # server signs the URL with HMAC + expiry
   ```
   → Test: replay, expiry bypass, HMAC key extraction.

## Probe adjustment (grpc × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
