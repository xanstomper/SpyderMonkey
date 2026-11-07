# Client-bundle route recovery — string-array obfuscation

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Route table hidden via string-array + rotation: `Ct()` array, `s(t)=t-497` index shim, IIFE rotation checksum. Decode by extracting the array literal, then read `$get`/`$post` call sites against it → recovers `p.public.store.purchasables`, `cx-bucks/claim`, `gambling/{play,mines,crash}`, `predictions`, `robot/*`, etc.
- Astro islands add a re-export hop: `EventShopApp.DbWwigeP.js` = 74-byte shim → real bundle `EventShopApp.DhsfRWg2.js`. If a bundle greps empty on expected keywords, follow the re-export one hop before concluding.
- **Zod schemas in the client = full API contract**: request shapes, enums, min/max limits, and which response fields are server-held (`.nullable()` until settle). Gambling schemas: `crash_point_hundredths`, mines `seed`/`mine_tiles` all `.nullable()` → server-side, zod-validated → no client oracle. Check nullability BEFORE hypothesizing game-state leaks.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
