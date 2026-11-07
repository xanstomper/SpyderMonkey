# 4. WP REST `_embed` user-enum bypass (beat stop-user-enumeration) — host / guest

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-4-wp-rest-e.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **host** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

`/wp-json/wp/v2/users`, `/?author=N`, `?rest_route=/wp/v2/users` are all blocked by the
stop-user-enumeration plugin. BUT REST-embedded author objects still leak the admin:
```
GET /wp-json/wp/v2/posts?per_page=20&_embed
→ _embedded.author[] = {"id":1,"name":"":".../author/geo/"}
```
The `slug` is the **WordPress username** (here: sole admin `geo`). Scan posts/pages/any public
content type with `_embed` and collect every distinct `slug`. Always check the WP REST route
index first: `GET /wp-json/` returns every namespace + route + method (huge recon goldmine —
844 routes on

## Probe adjustment (host × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
