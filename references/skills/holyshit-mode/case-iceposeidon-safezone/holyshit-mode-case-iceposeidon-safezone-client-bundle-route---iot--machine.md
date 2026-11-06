# Client-bundle route recovery — string-array obfuscation — iot / machine

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-client-bundle-route-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iot** · auth **machine** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Route table hidden via string-array + rotation: `Ct()` array, `s(t)=t-497` index shim, IIFE rotation checksum. Decode by extracting the array literal, then read `$get`/`$post` call sites against it → recovers `p.public.store.purchasables`, `cx-bucks/claim`, `gambling/{play,mines,crash}`, `predictions`, `robot/*`, etc.
- Astro islands add a re-export hop: `EventShopApp.DbWwigeP.js` = 74-byte shim → real bundle `EventShopApp.DhsfRWg2.js`. If a bundle greps empty on expected keywords, follow the re-export one hop before concluding.
- **Zod schemas in the client = full API contract**: request shapes, enums, min/max limits, and which response fields are server-held (`.nullable()` until settle). Gambling schemas: `crash_point_hundredths`, mines `seed`/`mine_tiles` all `.nullable()` → server-side, zod-validated → no client oracle. Check nullability BEFORE hypothesizing game-state leaks.

## Probe adjustment (iot × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
