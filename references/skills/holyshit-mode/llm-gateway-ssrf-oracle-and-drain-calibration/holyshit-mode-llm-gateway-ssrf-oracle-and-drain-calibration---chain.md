# 1. SSRF via `image_url` media-fetch → internal HTTP/port/connect ORACLE (zero token burn) — chain composition

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- base technique: `holyshit-mode-llm-gateway-ssrf-oracle-and-drain-calibration-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A vLLM/OpenAI-style endpoint accepting an `image_url` (multimodal) content part performs a
**server-side URL fetch**, and the error message **echoes the fetch result**:

```
POST https://<internal-gateway>/invocations
{"model":"deepseek-v4-flash",
 "messages":[{"role":"user","content":[{"type":"image_url","image_url":{"url":"http://169.254.169.254/latest/meta-data/"}}]}]}
→ 422 {"error":{"message":"Failed to fetch media from URL: HTTP 404 error (...)"}}
```

Discrimination matrix (all from the error echo; **do NOT let it generate a completion** — read the
media-fetch error):
- `HTTP 404 error` → reachable, answering with status 404.
- `cannot identify image file` ("Failed to load image") → **got a real HTTP 2xx BODY** (loopback-only
  route serving content that isn't an image).
- `Cannot connect to host <h>:<p> [Connect call failed]` → closed/filtered; a TLS listener answers the
  plain-HTTP probe with `ssl:default` connect errors.
- Timeout/hang → host resolves but connect blocked (non-loopback/down).
- **Port-scan:** iterate `http://127.0.0.1:<port>/` and classify. Cheap.
- **Cross-fleet test:** `http://api.<target>/`, `http://gateway.<target>/v1/` often echo real statuses →
  the SSRF reaches OTHER internal hosts, not just loopback. Probe host 80/443 even if a specific port hung.

**Exotic-protocol ceiling (run once, they're free + definitive for the RCE question):**
- `file:///etc/passwd` → `Cannot load local files without --allowed-local-media-path` = **local-file
  read disabled** (no OOB file-read/RCE; log as mitigation, stop probing that path).
- `gopher://` / `dict://` → rejected ("URL must be HTTP, data or file URL") = no protocol smuggling.
- `http://[::1]:<port>` → connect-fail = IPv6 loopback separate/closed.

SSRF **exfil limit (verified):** text-body-read-through-vision does NOT work — a non-image response
errors `cannot identify image file` before any vision/OCR flows. The oracle is status/connect-only
unless the internal target serves an actual image. So this is internal-reach + recon, not a data dump.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
