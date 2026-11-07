# The Correct Test — worker / guest

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-the-correct-test.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Exchange actual WebSocket frames. Use Python `socket+ssl` (NOT `websockets` library —
the library often auto-handshakes and masks the raw protocol behavior you need to see).
After the 101, send a frame and observe the response:

```python
import socket, ssl, base64, os, struct

def make_frame(payload, opcode=0x1):
    b1 = 0x80 | opcode
    length = len(payload)
    header = struct.pack('!BB', b1, length | 0x80)  # client frames MUST be masked
    mask = os.urandom(4)
    masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
    return header + mask + masked

def ws_connect(host, port, path, extra_headers=None):
    key = base64.b64encode(os.urandom(16)).decode()
    headers = {
        'Host': host, 'Upgrade': 'websocket', 'Connection': 'Upgrade',
        'Sec-WebSocket-Key': key, 'Sec-WebSocket-Version': '13',
        'Origin': 'https://target',
    }
    if extra_headers: headers.update(extra_headers)
    req = f'GET {path} HTTP/1.1\r\n'
    for k, v in headers.items(): req += f'{k}: {v}\r\n'
    req += '\r\n'
    ctx = ssl.create_default_context()
    s = socket.create_connection((host, port), timeout=10)
    s = ctx.wrap_socket(s, server_hostname=host)
    s.sendall(req.encode())
    buf = b''
    while b'\r\n\r\n' not in buf:
        chunk = s.recv(4096)
        if not chunk: break
        buf += chunk
    return s

# After handshake, send frames and read responses
s = ws_connect('target.com', 443, '/api/socket')
s.sendall(make_frame(b'{"type":"hello"}'))  # or any probe message
s.settimeout(2)
data = s.recv(8192)
# Parse first byte: 0x88 = CLOSE frame, 0x81 = TEXT frame
if data and data[0] == 0x88:
    close_code = struct.unpack('!H', data[2:4])[0]
    print(f'Server closed: code={close_code}')
    # 1008 = Policy Violation (auth failed), 1000 = Normal closure
```

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
