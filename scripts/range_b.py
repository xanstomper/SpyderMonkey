#!/usr/bin/env python3
"""RANGE B — the INDEPENDENT benchmark range.

Different codebase, different app shape, zero shared code with the dojo:
one multi-page 'shop' app (cookie session, cart, admin panel, order lookup)
with eight flaw instances the tester batteries did NOT co-evolve against.
If the family confirms here, the benchmark number stops being self-scored.

walls: 127.0.0.1 only, read-only differentials, family exit-code discipline.
"""
import json
import threading
import time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

# flaw → (path, benign baseline query, confirm marker in the ATTACK response)
FLAWS = {
    "IDOR":      ("/orders",   {"id": "5"},
                  "customer-two"),
    "AUTHZ":     ("/panel",    {"level": "user"},
                  "admin-panel"),
    "XSS":       ("/reviews",  {"q": ""},
                  "<svg"),
    "SSRF":      ("/fetch",    {"url": "http://example.com"},
                  "INTERNAL-CONFIG"),
    "REDIRECT":  ("/go",       {"url": "https://shop.example"},
                  "evil.example"),
    "TRAVERSAL": ("/file",     {"path": "invoice.txt"},
                  "root:x:0:0"),
    "BIZLOGIC":  ("/cart",     {"qty": "1"},
                  '"total": -'),
    "SESSION":   ("/session",  {"sid": "1000"},
                  '"sid": "1001"'),
}

_PAGE = """<html><body><h1>shop.example</h1>
<a href="/orders?id=5">orders</a><a href="/panel?level=user">panel</a>
<a href="/reviews?q=">reviews</a><a href="/fetch?url=http://example.com">fetch</a>
<a href="/go?url=https://shop.example">go</a><a href="/file?path=invoice.txt">file</a>
<a href="/cart?qty=1">cart</a><a href="/session?sid=1000">session</a>
</body></html>"""


class _Shop(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="text/html"):
        b = body.encode() if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def _q(self, k):
        from urllib.parse import unquote as _uq
        return (_uq(self.path.split(k + "=")[1].split("&")[0])
                if k + "=" in self.path else "")

    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/":
            return self._send(200, _PAGE)
        if p == "/orders":                      # IDOR: id trusted from the query
            cust = {"5": "customer-one", "6": "customer-two"}.get(self._q("id"))
            if cust:
                return self._send(200, json.dumps({"customer": cust}))
            return self._send(404, "no order")
        if p == "/panel":                        # AUTHZ: level trusted from query
            if self._q("level") in ("admin", "1", "true"):
                return self._send(200, "admin-panel: revenue=all")
            return self._send(200, "user-panel: revenue=own")
        if p == "/reviews":                      # XSS: q reflected unencoded
            return self._send(200, f"<p>reviews for {self._q('q')}</p>")
        if p == "/fetch":                        # SSRF: client-named url fetched
            u = self._q("url")
            if u.startswith(("http://127.", "http://localhost", "http://169.254.")):
                return self._send(200, json.dumps({"fetched": "INTERNAL-CONFIG"}))
            return self._send(200, json.dumps({"fetched": "denied"}))
        if p == "/go":                           # REDIRECT: Location from input
            self.send_response(302)
            self.send_header("Location", self._q("url") or "/")
            self.end_headers()
            return
        if p == "/file":                         # TRAVERSAL: path never normalized
            from urllib.parse import unquote as _uq
            path = _uq(self.path)
            if "../" in path:
                return self._send(200, "root:x:0:0:root:/root:/bin/bash")
            if self._q("path") == "invoice.txt":
                return self._send(200, "invoice: total=42")
            return self._send(404, "no file")
        if p == "/cart":                         # BIZLOGIC: qty accepted raw
            try:
                qty = int(self._q("qty") or "1")
            except ValueError:
                qty = 1
            return self._send(200, json.dumps({"qty": qty, "total": qty * 10}))
        if p == "/session":                      # SESSION: sequential ids
            return self._send(200, json.dumps({"sid": self._q("sid") or "1000"}))
        return self._send(404, "nope")


def serve_range(port):
    srv = ThreadingHTTPServer(("127.0.0.1", port), _Shop)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.3)
    return srv


if __name__ == "__main__":
    srv = serve_range(9777)
    print("range B on http://127.0.0.1:9777 — Ctrl-C to stop")
    try:
        time.sleep(3600)
    except KeyboardInterrupt:
        srv.shutdown()
