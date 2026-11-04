# Technique: auth-mode header split discovery

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

Multi-tenant SPA bundles carry an auth-mode selector header (`X-Chat-Auth-Mode: account|platform_key`). The error chain enumerates itself: endpoint bare → 400 naming the header → each value names the next required credential. Each branch validates DIFFERENT credentials against DIFFERENT backends — treat each branch as its own auth surface.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
