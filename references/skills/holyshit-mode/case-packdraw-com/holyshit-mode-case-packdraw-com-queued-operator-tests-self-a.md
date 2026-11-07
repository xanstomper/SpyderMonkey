# Queued operator tests (self-account, non-destructive)

- source canon: `holyshit-mode/case-packdraw-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. **Seed-rotation test** (the top finding): register → open 2 cheap packs → record
   pre-open hashed seed + post-open revealed seed for each; check (a) hash(revealed) ==
   pre-open hash (commitment discipline), (b) seeds differ between opens (rotation), or
   (c) same seed persists (PREDICTIVE → guaranteed-win exploit).
2. **Battle verification**: join/observe one battle → after EOS block, verify
   `sha256(blockHash) → ticket → winner` against the recorded winner.
3. **Cross-user Pusher**: with an account, request `/api/pusher/auth` for
   `private-encrypted-user-<OTHER>` channel → 403 = good; 200 = cross-user realtime.
4. **Create-pack validation**: user-created packs — can the user set odds/weights/price
   such that EV > price (self-dealing), or is validation server-side?
5. **Tokenize iframe config** POST shape (may leak tokenExId/timestamp config).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
