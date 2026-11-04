# Confirmed findings this session — firmware / unauth

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- base technique: `holyshit-mode-case-gratisfy-reengagement2-confirmed-findings.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **unauth** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (firmware × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
