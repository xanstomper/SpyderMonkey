# CloudFront/CDN origin and behavior gaps

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Origin-host mismatch, behavior path overlap (e.g. `/api/*` bypass via encoding at the edge), custom-origin header trust. Decisive test: edge request with encoded path variants — differential status from origin = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
