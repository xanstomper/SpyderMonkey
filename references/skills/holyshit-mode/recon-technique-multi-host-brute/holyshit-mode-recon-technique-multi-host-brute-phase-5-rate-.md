# Phase 5: Rate-Limit Probing (The Critical Gap)

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- `/api/dashboard` and `/api/export` return 401 on wrong password with **ZERO rate limiting**
- 20 rapid wrong-password attempts → all 401, zero 429
- Contrast: `/auth/signup` on main domain has working rate limiting (429 after 10 attempts)
- The rate-limit inconsistency between openinfra (unguarded) and freeinference.org (guarded) is the vulnerability pattern

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
