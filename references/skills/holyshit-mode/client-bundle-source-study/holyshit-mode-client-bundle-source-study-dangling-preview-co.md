# Dangling-preview cookie-toss chain

- source canon: `holyshit-mode/client-bundle-source-study.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Resolve preview wildcards (`deploy-preview-N.*`, `main.*`); fetch root: Netlify
   "Not Found - Request ID: <ulid>" + `Server: Netlify` = deleted deploy on live DNS =
   dangle.
2. Find cookie-TRUST primitives in the main-site client: grep chunks for cookie readers
   (e.g. `function C(e){let t=e+\`=\`;...document.cookie...}`) and trace every call site.
3. Chain: a claimed wildcard host serves a page that `Set-Cookie: <trusted-name>=<json>;
   Domain=.parent.com; Path=/` (domain-suffix rule makes the main origin honor it) →
   victim click → victim's next login ships the attacker's cookie keys in the auth body.
4. Gates: wildcard claimability (infrastructure takeover — operator's explicit call),
   server-side key acceptance (operator console: `document.cookie='<name>=<json>;path=/'`
   then login and diff the profile/me endpoint).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
