# Edge challenge (Fastly `_fs-ch-*`) anatomy — linux / high-priv

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-edge-challenge-fastly-fs-ch-anat.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **linux** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Challenge page = CSP-locked HTML loading `/_fs-ch-<id>/script.js`; a non-browser client
  gets HTTP 200 + a `Set-Cookie: _fs_ch_st_*`. It is deterministic per client fingerprint
  once triggered, but can be probabilistic (A/B) before triggering — a single success does
  not mean the lane is open.
- The visible fallback is an **image CAPTCHA** ("Enter the characters seen in the image").
  Do not trust the first `data:image/svg` `<img>` — that can be a 455×40 logo strip. The
  real captcha is a separate ~220×120 JPEG `<img>` (enumerate all imgs with bounding boxes
  via CDP and pick the form-adjacent one). Headless Chrome (even `--headless=new`) fails
  the invisible auto-solve; a human reading the pulled image and one CDP submit restores
  the lane — the intended flow, not a bypass.
- If a challenge appears mid-engagement, that itself is a ledger row (posture change —
  `bot_gate` class) and explains every probe that started returning 200-with-HTML.

## Probe adjustment (linux × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
