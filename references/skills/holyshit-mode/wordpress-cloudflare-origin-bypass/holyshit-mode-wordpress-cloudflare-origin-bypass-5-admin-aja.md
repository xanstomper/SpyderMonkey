# 5. Admin-ajax unauth action sweep

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Many plugins register `wp_ajax_nopriv_*` handlers that are genuinely public. Sweep:
`POST /wp-admin/admin-ajax.php` with `action=<name>` for each plugin's likely handler names.
- `200` + meaningful JSON = LIVE unauth handler (hit the jackpot).
- `200` body `0` or `-1` = handler ran but dismissed/empty (still registered → tune params).
- `400` = no such handler.
On d 400 — origin is uniformly gated.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
