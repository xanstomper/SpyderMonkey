# 2. Use `http.client` over a raw socket, not curl/urllib, for origin work

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
