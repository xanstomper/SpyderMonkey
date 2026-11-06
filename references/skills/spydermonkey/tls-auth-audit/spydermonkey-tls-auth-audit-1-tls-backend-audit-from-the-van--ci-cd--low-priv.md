# 1. TLS backend audit (from the vantage VM) — ci-cd / low-priv

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-1-tls-backend-audit-from-the-van.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

1. Enumerate hosts to cover: main domain, API/socket subdomains, every CT-log
   host, sister brands, file/KYC tiers, any host named in bundles.
2. Run an openssl loop per host:port — protocol support (`tls1`, `tls1_1`,
   `tls1_2`, `tls1_3`), then `openssl s_client -connect h:p -servername h` piped
   to `openssl x509 -noout -subject -issuer -dates -ext subjectAltName` for
   subject/issuer/validity/SANs, key type + size from `-text`, negotiated cipher.
   Write the script to /tmp, `scp` to the VM, `ssh` execute (see SKILL.md
   egress rules).
3. **CF 526 diagnosis**: 526 = origin certificate fails verification under
   full-strict. `openssl s_client` the EDGE cert — if it is valid and covers the
   hostname, the ORIGIN server cert is broken. A 526 on a KYC/file tier is an
   incident on its own (identity-document infrastructure failing TLS).
4. **Cert SANs are infrastructure intel**: a sister brand's cert can list hidden
   host fleets (`render.*`, `*.render.*`) that appear in neither DNS enumeration
   nor CT logs. Read SANs on every live host.
5. Security headers per host: HSTS (+preload), CSP (note `unsafe-eval`, or
   frame-ancestors-only weakness), XFO, nosniff, referrer-policy,
   permissions-policy. A host that serves executable third-party code with NO
   security headers is a finding, not a footnote.
6. **Read the handshake verdict from BYTES, not the client's printout.** A
   modern OpenSSL 3.x client prints a `Protocol: TLSv1.3`-style session line even
   for FAILED handshakes — the real verdict is `SSL handshake has read N bytes`:
   `read 0 bytes and written 7` = the server REJECTED that protocol version,
   whatever `Protocol:` says beside it. And `curl --tlsv1.0` sets a MINIMUM, not
   a pin — a 200 from `curl --tlsv1.0` means the connection negotiated UP to
   1.3; never cite it as TLS 1.0 support. Pin per-version with
   `openssl s_client -tls1` and judge by the byte count.
7. **TRACE test**: `TRACE /path` with a canary Cookie header — a 200 echoing the
   full request including cookies = `TraceEnable On`. Browsers block TRACE XHR,
   so this is hygiene-class on any target; register it low with the echoed
   request in the proof, never as XST-exploitable.

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
