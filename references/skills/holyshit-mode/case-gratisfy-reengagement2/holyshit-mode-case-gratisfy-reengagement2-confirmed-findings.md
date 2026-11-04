# Confirmed findings this session

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

| Class | Score | Evidence |
|---|---|---|
| `signup_metadata_into_jwt` | 72 | signup `data:{role:supabase_admin,is_admin:true,tier:enterprise}` persisted verbatim → email-confirmed via public mailinator inbox → JWT `user_metadata` carries the admin claims. GoTrue admin API mitigated (checks app_metadata). |
| `password_grant_no_lockout` | 60 | 20 rapid wrong-pw on same acct: all 400, zero 429/lockout/captcha. |
| `verify_otp_bruteforce` (upgraded) | 55 | 2070 total guesses incl. 100-thread parallel (52 req/s), zero 429. 1M space = 5.3h vs ~1h TTL → TTL is the only defense. |
| `cors_arbitrary_origin_reflected` | 40 | api./chat./platform. ALL reflect `Origin: https://evil.com` + allow `authorization` header. Bearer-in-sessionStorage → not independently exploitable. |
| `custom_api_egress_host` | 20 | TLS cert SAN leaked `custom-api-egress.gratisfy.xyz` + wildcard (absent from DNS + bundles). Base host = live backend (JSON 404s). |
| `platform_handoff_exchange_unthrottled` | 55 | Re-verified: 15 rapid, zero 429. |
| `magiclink_otp_bruteforce` | 55 | 500 guesses/21s, zero 429. |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
