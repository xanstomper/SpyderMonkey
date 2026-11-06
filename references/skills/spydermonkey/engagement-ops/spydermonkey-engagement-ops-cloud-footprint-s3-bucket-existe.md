# Cloud footprint: S3 bucket existence probing (no creds needed)

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
