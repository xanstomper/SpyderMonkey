# urllib 302-following gotcha (operational note) — grpc / high-priv

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- base technique: `holyshit-mode-case-directrouter-pages-dev-urllib-302-followi.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`urllib.request.urlopen` follows 302s silently. The apparent "huge HTML response" from
`/api/auth/discord` was Discord's login page, not the target's response. The
target's function returned 302 with a `Location:` header. To extract the OAuth start URL:

```python
import urllib.request
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)  # or use `requests`
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None
opener = urllib.request.build_opener(NoRedirect)
try:
    opener.open(req)
except urllib.error.HTTPError as e:
    print(e.headers.get('Location'))  # the OAuth start URL
```

Or just use `requests` with `allow_redirects=False`.

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
