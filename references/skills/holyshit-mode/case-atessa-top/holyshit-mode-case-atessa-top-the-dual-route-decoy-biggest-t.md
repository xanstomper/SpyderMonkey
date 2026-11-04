# The dual-route decoy (biggest time sink — learn it)

- source canon: `holyshit-mode/case-atessa-top.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Bare paths (`/auth/login`, `/vouchers/redeem`) 422 with `"input":null` on EVERY field despite valid JSON = SPA-fallback router where the body never reaches Pydantic. Looks like "captcha strips the body" — it isn't.
- Real API lives under `/api/*`: `/api/auth/login` → `CAPTCHA verification required`; `/api/auth/signup` 422 echoes `input:{...your body...}` back.
- **Rule:** any 422 with `input:null` on all fields → immediately re-probe the same path under `/api` + `/api/v1` prefixes.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
