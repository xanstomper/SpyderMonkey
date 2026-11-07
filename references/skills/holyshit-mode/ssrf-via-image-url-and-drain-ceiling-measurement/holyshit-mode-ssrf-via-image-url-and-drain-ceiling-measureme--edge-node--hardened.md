# The `image_url` SSRF / error-oracle primitive — edge-node / hardened

- source canon: `holyshit-mode/ssrf-via-image-url-and-drain-ceiling-measurement.md`
- base technique: `holyshit-mode-ssrf-via-image-url-and-drain-ceiling-measureme.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **edge-node** · auth **hardened** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

On an OpenAI-compatible inference server that exposes a keyless or weakly-gated
completion route (here `POST /invocations` on a vLLM worker), the **`image_url`
message-part is fetched SERVER-SIDE** and the fetch result is echoed in the error
message — a live, read-0-cost probe:

- Body: `{"messages":[{"role":"user","content":[{"type":"image_url","image_url":{"url":TARGET}}]}]}`
- The server fetches `TARGET` and returns, per reachability:
  - **`422 "Failed to fetch media from URL: HTTP <N> error"`** → target answered `<N>`
    (status oracle: 404 vs 200 on a given internal host:port/path maps services/routes).
  - **`500 "Cannot connect to host <host>:<port> ssl:default [Connect call failed]"`** →
    port dialed but not HTTP (a TLS/non-HTTP listener, e.g. Postgres on loopback).
  - **`"Failed to load image: cannot identify image file"`** → HTTP 200 with a body that
    isn't an image (real content flowed; loopback `/metrics`/`/docs`/`/openapi.json` pattern).
  - hang/timeout → reachable but slow/queued, or filtered external-host.
- **`file:///etc/passwd` → `Cannot load local files without --allowed-local-media-path`**
  = the vLLM local-file-read is DISABLED (a real hardening flag). Don't chase file-read RCE here.
- **`gopher://` / `dict://` → `The URL must be either a HTTP, data or file URL`** (scheme allowlist).
- IMDS `http://169.254.169.254/latest/meta-data/` → echoed `HTTP 404` = reached the metadata
  endpoint. IMDSv2 404s without a token — **404 ≠ unreachable**, it means reach-confirmed-hardened.
- Cross-fleet reach: the SSRF was NOT loopback-only — it hit `api.<tld>` and `gateway.<tld>`
  and got status echoes. Classify reach by testing internal hostnames + loopback + IMDS, NOT by
  assuming loopback-scope.

**Wiring to control:** the error-status oracle doubles as a **port/host scanner across an
entire internal fleet** from one public request. It is read/enumeration capability; file-read,
gopher, and deserialization are typically hardened on vLLM, so **treat it as internal-reach
+ oracle, not RCE**, and say so honestly rather than overstating it as a forge/escalation.

## Probe adjustment (edge-node × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
