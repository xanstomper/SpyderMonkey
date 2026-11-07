# 2.4 Chunk discovery — the lazy-load law (score 85) — iot-edge / high-priv

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-4-chunk-discovery-the-laz.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- webpack: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js` → fetch each.
- Vite/rolldown: extract the `__vite__mapDeps` manifest array from the main bundle; the
  shell's asset list is a SUBSET — entry `index-*.js` and auth chunks may be absent from it;
  diff referenced-vs-fetched sets, pull the missing ones.
- Re-export stubs (≤1KB chunks) are dead ends — follow `from"./X.js"` to the real module.
- i18n backends: challenge strings live in NO chunk — locate flows by chunk references and
  endpoint patterns, never by grepping message text.
- EVERY fetch: `curl -o file -w '%{http_code} %{size_download}'` — verify size>0 (variant-host
  asset trap: same path 404s on www. while 200ing on apex; empty file = false "no findings").

## Probe adjustment (iot-edge × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
