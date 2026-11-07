# TLS-impersonation tooling + wall-shape discriminator — iot-edge / machine

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-tls-impersonation-to.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- **curl-impersonate on OL9:** binaries can't run from /dev/shm (noexec) — keep them in
  `~/dkv-venv/bin`. The bundled wrapper scripts hardcode a Debian CA path
  (`/etc/ssl/certs/ca-certificates.crt`) and fail with error 77 — run the binary directly
  with `-k` plus the `--ciphers`/header flags copied out of the wrapper, or export
  `CURL_CA_BUNDLE`. chrome110-impersonation passes JA3-keyed apex blocks that stop default
  curl/python outright.
- **Wall shapes differ PER HOST — fingerprint each, never generalize.** On one fleet: the
  apex = JA3-keyed (impersonation passes), the API host = IP-reputation hard block (403
  "you have been blocked" EVEN for real chromium navigation), staging hosts = CF Access
  walls, mirrors = managed challenge. Same org, four different gates. Classify per host:
  (a) impersonation passes = TLS-fingerprint rule; (b) real-browser navigation still
  blocked = IP-reputation rule — no script-side fix exists, the vantage is the wall;
  (c) Access/managed-challenge pages = a wall for scripts AND often for DC-vantage
  browsers. Record the shape per host in the ledger so a re-engage doesn't re-derive it.
- **`retry-after` on app-level 429s = the authoritative cooldown** — read it before
  choosing a retry cadence (see recon-quick-checks #32 for the self-DoS trap).

## Probe adjustment (iot-edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
