# Vite lazy-chunk inventory mining (`__vite__mapDeps` + in-page fetch) — ios / root

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-vite-lazy-chunk-inventory-mining.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ios** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

A Vite-bundled SPA's lazy chunks are names by purpose but rotated by hash; you can still fetch ANY
specific module if you mine the chunk inventory. The tricks that make this fast:

1. **The route-map / dependency-map file is a COMPLETE chunk inventory.** A `__vite__mapDeps` array
   (or a `path:"...",component:()=>import("./name-HASH.js")` route table) lists every lazy chunk by
   hashed filename AND often a purpose-revealing name — `getVerifyType-DYqfJP5P.js`, `whiteList-*`,
   `twofa-verify-*`, `withdraw-*`, `hack-verify-*`. Grep the main bundle or a captured entry chunk for
   `__vite__mapDeps([` / `import("./<name>-<hash>.js"` to both enumerate the estate AND learn which
   chunk governs which feature and the withdrawal/2FA/etc routes (`/wallet/withdraw/confirm`, `/auth/twofa-verify`) — a goldmine for targeted reversing.
2. **Route-chunk fetches return the CF "Just a moment" HTML (not the JS) to curl AND to a bare
   `page.evaluate(fetch)`** — the hashed chunks are challenge-gated to the app's own load path. Fetch
them from the CLEARED page context (`await page.goto(<app>); await page.evaluate(()=>fetch("https://<origin>/assets/<name>-HASH.js"))`) and use an ABSOLUTE URL — relative `/assets/...` throws `TypeError: Failed to parse URL` inside evaluate. A sub-5KB "chunk" that is `<!DOCTYPE html><title>Just a moment` is the challenge page, not the module — you were challenged, not missing the asset.
3. **A `xx-yyy-HASH.js` naming pair usually means `xx-yyy` is a thin loader** (e.g. a 1.4KB `user-action-*` importing the real 660KB `index-*`); read the small loader to find the real module before grepping the huge one for feature strings.

## Probe adjustment (ios × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
