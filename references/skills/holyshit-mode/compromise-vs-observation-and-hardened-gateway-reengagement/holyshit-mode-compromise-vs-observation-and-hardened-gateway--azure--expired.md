# 2. SSRF / upstream-credential exfil (the real prize if open) — azure / expired

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- base technique: `holyshit-mode-compromise-vs-observation-and-hardened-gateway.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **azure** · auth **expired** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

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

## Probe adjustment (azure × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
