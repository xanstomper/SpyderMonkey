# When to Use This

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Target has any WebSocket endpoint (voice, chat, live updates, gaming, trading).
- Target is behind a CDN that proxies WebSocket (Cloudflare, CloudFront, Fastly).
- You see `socketUrl` or `new WebSocket(` in the JS bundle.
- The endpoint appears to accept unauthenticated upgrades (this is normal and
  does NOT mean it's vulnerable — keep probing).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
