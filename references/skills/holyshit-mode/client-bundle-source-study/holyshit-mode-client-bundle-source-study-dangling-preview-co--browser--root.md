# Dangling-preview cookie-toss chain — browser / root

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-dangling-preview-co.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

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

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
