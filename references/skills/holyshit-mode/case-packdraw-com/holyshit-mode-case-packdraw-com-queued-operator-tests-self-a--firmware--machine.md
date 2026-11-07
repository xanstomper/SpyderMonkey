# Queued operator tests (self-account, non-destructive) — firmware / machine

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-queued-operator-tests-self-a.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (firmware × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
