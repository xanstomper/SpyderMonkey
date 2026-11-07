# A. String-table decoder replay (javascript-obfuscator) — mobile / low-priv

- source canon: `spydermonkey/spa-bundle-extraction.md`
- base technique: `spydermonkey-spa-bundle-extraction-a-string-table-decoder-re.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **mobile** · auth **low-priv** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Do NOT fight it statically — the table is a shuffled array behind a decoder function
and every literal is a hex-index call. Replay the app's own decoder in Node:

1. **Collect the whole chunk graph first.** Grep every downloaded chunk for
   `chunk-[A-Z0-9]+\.js` refs and `import{...}from'./chunk-X.js'` / `import './X.js'`
   statements, download the delta, and loop until the delta is empty. Lazy feature
   chunks (300KB–3MB) carry the real API strings; the initial ~15 never do.
2. **Strip ESM wrappers, then eval per chunk in a bare vm context.** Remove
   `export{...};` and `import{...}from'...';` — with REGEX, not line-greps: obfuscated
   builds emit all imports on ONE line, so `^import...$` per-line strips miss them and
   eval dies on `Cannot use import statement outside a module`. Stub
   `{console,setTimeout,window,document}`; an eval "err" (DOM missing) is fine —
   function declarations still hoist onto the context.
3. **Find the decoder empirically.** For EVERY function property of the context, call
   it over `0..0x4000` and keep the mapping yielding the most strings (>300 = decoder;
   a chunk may define several — take the largest). The decoder works only after the
   checksum-rotation IIFE runs at eval time, which the vm eval already does.
4. **Static call sites use the SAME post-rotation indexes.** To locate where a decoded
   string is used, grep the RAW chunk for `(0x<idx>)` — the hex index is stable even
   though each module aliases its decoder under a different local name. This turns a
   decoded string (`setRsaPrivateKey`, an `/api/hand/history/` path) into its exact
   call site without any deobfuscation tooling.
5. **Sweep the merged tables** across all chunks for `^/api|/hand|/admin|/open|wss?://|token|share|auth` and read them together — router config, HTTP service method
   names (`getHandNarrative`, `getTimelinePromotionsWinterGiveawayMissionBySharedId`),
   and request-param enums (`handhistoryId`, `nickname`, `timelineSharedId`) all
   surface, which is the full authenticated-API test plan for when a session arrives.

Pitfalls:
- The largest arrays in a chunk may be WASM/ICU/font data (`AAAAAA…`, 26–52KB), not
  key material — sanity-check shape before treating a big base64 blob as a key.
- forge/crypto-js library error strings fill the tables (`RSAPrivateKey.modulus`,
  `createDecipher`) and prove NOTHING about app-level key use; TLS-layer AES call
  sites inside forge's own `initConnectionState` are library internals, not the app.
- Enum values that decode to brand/promo codes (`GGMTD`, `WSOPSC`, `REDHORSE`) are
  campaign constants, not passphrases — don't chase them as crypto keys.
- An encrypted response envelope (`{"data":"<hex>"}`, randomized, on EVERY error even
  404s) is normal client-decrypt design, not a finding — record shape + sizes as
  architecture and don't burn the session extracting a key to decrypt ERROR bodies
  (the same envelope wraps data routes that need a session anyway).

## Probe adjustment (mobile × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
