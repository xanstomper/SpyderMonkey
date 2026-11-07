# Client-bundle route recovery — string-array obfuscation — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-client-bundle-route-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Route table hidden via string-array + rotation: `Ct()` array, `s(t)=t-497` index shim, IIFE rotation checksum. Decode by extracting the array literal, then read `$get`/`$post` call sites against it → recovers `p.public.store.purchasables`, `cx-bucks/claim`, `gambling/{play,mines,crash}`, `predictions`, `robot/*`, etc.
- Astro islands add a re-export hop: `EventShopApp.DbWwigeP.js` = 74-byte shim → real bundle `EventShopApp.DhsfRWg2.js`. If a bundle greps empty on expected keywords, follow the re-export one hop before concluding.
- **Zod schemas in the client = full API contract**: request shapes, enums, min/max limits, and which response fields are server-held (`.nullable()` until settle). Gambling schemas: `crash_point_hundredths`, mines `seed`/`mine_tiles` all `.nullable()` → server-side, zod-validated → no client oracle. Check nullability BEFORE hypothesizing game-state leaks.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
