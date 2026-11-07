# TLS-impersonation tooling + wall-shape discriminator — chain composition

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-tls-impersonation-to.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
