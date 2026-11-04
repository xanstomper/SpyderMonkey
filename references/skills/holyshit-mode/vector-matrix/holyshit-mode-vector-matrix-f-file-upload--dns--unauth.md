# F. FILE / UPLOAD — dns / unauth

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-f-file-upload.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **dns** · auth **unauth** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Content-type confusion, double extensions, polyglots (GIF+JS, ZIP+JS)
- Image parsers: ImageMagick-class (CVE-tracked), SVG with embedded JS
- Archive extraction: zip-slip traversal, symlink entries, decompression bombs
- Resume/range parsing: header injection via filename, path traversal in multipart names

## Probe adjustment (dns × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
