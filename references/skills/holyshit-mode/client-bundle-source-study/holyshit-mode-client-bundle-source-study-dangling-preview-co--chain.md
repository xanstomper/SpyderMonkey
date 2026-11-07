# Dangling-preview cookie-toss chain — chain composition

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-dangling-preview-co.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
