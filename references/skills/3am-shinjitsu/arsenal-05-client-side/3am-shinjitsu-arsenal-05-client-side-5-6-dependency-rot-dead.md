# 5.6 Dependency rot / dead references (score 75)

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- Third-party scripts, invites, widgets, CDN links in the bundle → 404/NXDOMAIN = hijackable
  reference (registration-takeover the domain → code execution in context).
- DECISIVE: extract every external URL from all chunks → resolve each → dead ones scored by
  what the page does with the loaded content.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
