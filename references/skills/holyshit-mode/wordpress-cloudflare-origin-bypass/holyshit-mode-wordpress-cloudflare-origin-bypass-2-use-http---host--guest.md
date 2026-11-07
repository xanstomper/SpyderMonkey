# 2. Use `http.client` over a raw socket, not curl/urllib, for origin work — host / guest

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-2-use-http-.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **host** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

When you must set an arbitrary `Host` + SNI and control TLS verification, `http.client` with
an unverified `SSLContext` is far cleaner than curl flag soup or raw `socket+ssl` string builds.
It also **handles chunked transfer-encoding automatically** — a raw TCP reader does not.

**Raw-socket chunking pitfall (hit this session):** a bare `socket+ssl` read returns the
chunked body *with* `10000\r\n` size-prefix lines interleaved. JSON.parse fails with
`Extra data: line 2 column 1 (char 7)`. Either (a) use `http.client` (auto-deframes), or (b)
manually decode: read hex size lines, consume that many bytes, repeat until `0`. Also note:
`re.search(bytes_pattern, str)` raises `TypeError: cannot use a string pattern on a bytes-like
object` — keep pattern/input types matched.

## Probe adjustment (host × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
