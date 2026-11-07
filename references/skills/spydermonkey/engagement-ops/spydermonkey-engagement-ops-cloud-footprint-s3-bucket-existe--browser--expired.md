# Cloud footprint: S3 bucket existence probing (no creds needed) — browser / expired

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-cloud-footprint-s3-bucket-existe.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **expired** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

When an operator uses AWS (hint: they fork `pacu`/pentest toolkits into their org), map the
bucket estate without credentials:

1. **Sweep candidate names** (`<brand>`, `<brand>-assets`, `<brand>-static`, `<brand>-cdn`, ...)
   against `https://<name>.s3.amazonaws.com/`.
2. **Read the distinction**: `403 AccessDenied` XML = bucket EXISTS (listing denied).
   `404 NoSuchBucket` = does not exist. `301` = EXISTS but in another region — S3
   redirects the global endpoint to the canonical region.
3. **Pin the region**: probe `https://s3.<region>.amazonaws.com/<name>` across regions —
   the region returning `403` (not 301) is where the bucket lives (e.g. ap-northeast-1
   for a `bcgame` bucket).
4. **Probe common paths** (`/backups`, `/dump.sql`, `/.env`, `/config`, `/keys`, `/logs`,
   `/admin`) — all-403 means locked, not enumerable: register the finding as the
   asset's EXISTENCE + region (a persistent AWS footprint and a target for monitored
   ACL drift), never as a data exposure. A single 200 with a listing = the crown class
   of its own.

This is read-only GET probing, in-estate by domain adjacency; keep the 403-vs-404
distinction in the proof or the row reads as noise.

## Probe adjustment (browser × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
