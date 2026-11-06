# Cloud footprint: S3 bucket existence probing (no creds needed) — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-cloud-footprint-s3-bucket-existe.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
