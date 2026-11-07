# 2. SSRF / upstream-credential exfil (the real prize if open)

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Stand up an attacker catcher + tunnel, then probe whether the proxy forwards client-chosen
endpoints (which would carry stored upstream API keys to a host you control):
- Listener: `/tmp/catcher.py` (http.server that logs method/path/ALL headers/body, 0.0.0.0,
  high port). Tunnel: `cloudflared tunnel --url http://localhost:<port> --no-autoupdate` —
  grep the trycloudflare URL from the log.
- Self-check the catcher BEFORE probing (POST your own tunnel URL, confirm `SSRF-HIT`).
- Injection matrix on `/pg/chat` (or proxy): model=full `https://` URL, model=`http://` URL,
  model=provider-prefixed URL/host, and top-level override fields
  `base_url/endpoint/host/upstream/api_url/proxy/url/provider_url/target/forward_to`.
- **Zero inbound on the catcher across all variants = hard-gated.** In this case the model
  field returned 404 `model_not_found` (catalog-validated) and extra fields were ignored
  (server routed to the real model). Client cannot supply upstream endpoint → NO SSRF, NO
  stored-credential exfil. Log `ssrf_credential_exfil=negative` and stop chasing it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
