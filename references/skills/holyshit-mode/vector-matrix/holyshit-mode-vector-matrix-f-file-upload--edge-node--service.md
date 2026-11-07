# F. FILE / UPLOAD — edge-node / service

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-f-file-upload.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **edge-node** · auth **service** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- Content-type confusion, double extensions, polyglots (GIF+JS, ZIP+JS)
- Image parsers: ImageMagick-class (CVE-tracked), SVG with embedded JS
- Archive extraction: zip-slip traversal, symlink entries, decompression bombs
- Resume/range parsing: header injection via filename, path traversal in multipart names

## Probe adjustment (edge-node × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
