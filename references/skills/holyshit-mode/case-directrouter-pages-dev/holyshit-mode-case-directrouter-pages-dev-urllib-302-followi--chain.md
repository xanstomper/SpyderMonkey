# urllib 302-following gotcha (operational note) — chain composition

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- base technique: `holyshit-mode-case-directrouter-pages-dev-urllib-302-followi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
