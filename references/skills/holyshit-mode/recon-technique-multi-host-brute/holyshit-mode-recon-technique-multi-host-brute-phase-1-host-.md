# Phase 1: Host Discovery

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-04

## The technique

- Subdomain brute-force using a short AI-infra wordlist: `api`, `doc`, `internal`, `status`, `staging`, `metrics`, etc.
- Hit: `internal.f***REDACTED***.org` → 107.173.46.170 (non-Cloudflare IP — separate infra tier, ports filtered)
- Hits: `doc.`, `staging.`, `status.` → Cloudflare-protected hosts
- Note: DNS resolution of internal/ staging/ status subdomains is itself an info leak (infra topology exposure)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
