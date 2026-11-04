# Route-map mining (the big win)

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

The fork has dozens of custom routes invisible to endpoint guessing: `/api/user/reset_by_code`,
`/api/user/login/email/code`, `/api/web/runtime-key`, `/api/web/token/batch`, `/api/admin-auth`,
`/api/user/free-trial/usage`, `/api/user/promo-discount/preview`, `/api/user/membership`,
`/api/user/{stripe,paypal,nowpayments,antom}/pay`, `/api/messages/tickets/*`, `/api/region-access`.

Method: fetch every `src="/_next/static/chunks/*.js"` from ALL page variants (homepage, /console,
/pricing — each page loads different chunks), then regex `["\'](/api/[A-Za-z0-9_/.-]{2,80})["\']`.
Endpoint guessing alone found ~8 routes; chunk mining found 40+.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
