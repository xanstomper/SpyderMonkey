# 2.4 Chunk discovery — the lazy-load law (score 85) — websocket / high-priv

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-4-chunk-discovery-the-laz.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- webpack: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js` → fetch each.
- Vite/rolldown: extract the `__vite__mapDeps` manifest array from the main bundle; the
  shell's asset list is a SUBSET — entry `index-*.js` and auth chunks may be absent from it;
  diff referenced-vs-fetched sets, pull the missing ones.
- Re-export stubs (≤1KB chunks) are dead ends — follow `from"./X.js"` to the real module.
- Next.js/Turbopack: `_buildManifest.js` (path `/_next/static/<buildId>/_buildManifest.js`,
  buildId from homepage HTML) is the FULL route map in one fetch — 200+ routes with zero
  405-matrix probing. Route "chunks" are tiny `__turbopack_load_page_chunks__` loaders —
  follow each to the real page chunks (verifier/game math ships there, not in the loader).
- Live HTML vantage-blocked? Pull the archived homepage (wayback replay rules in
  edge-gate-recon) and extract `<script src>` chunk names from it — the static plane is
  commonly WAF-exempt even when app paths are denied; chunk fetches then run direct.
- `__NEXT_DATA__` pageProps mining: featureFlags, analyticsId, buildId, requestTime —
  flag names name the feature surface (payment methods, sockets, fingerprint vendors).
- i18n backends: challenge strings live in NO chunk — locate flows by chunk references and
  endpoint patterns, never by grepping message text.
- EVERY fetch: `curl -o file -w '%{http_code} %{size_download}'` — verify size>0 (variant-host
  asset trap: same path 404s on www. while 200ing on apex; empty file = false "no findings").

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
