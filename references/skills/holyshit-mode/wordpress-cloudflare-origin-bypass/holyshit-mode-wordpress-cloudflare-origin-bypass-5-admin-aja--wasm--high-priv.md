# 5. Admin-ajax unauth action sweep — wasm / high-priv

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-5-admin-aja.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Many plugins register `wp_ajax_nopriv_*` handlers that are genuinely public. Sweep:
`POST /wp-admin/admin-ajax.php` with `action=<name>` for each plugin's likely handler names.
- `200` + meaningful JSON = LIVE unauth handler (hit the jackpot).
- `200` body `0` or `-1` = handler ran but dismissed/empty (still registered → tune params).
- `400` = no such handler.
On d 400 — origin is uniformly gated.

## Probe adjustment (wasm × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
