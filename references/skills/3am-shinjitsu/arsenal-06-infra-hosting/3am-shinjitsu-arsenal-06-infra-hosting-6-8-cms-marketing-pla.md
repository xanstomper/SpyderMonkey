# 6.8 CMS/marketing plane (score 65)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Leaked delivery token (bundle/CMS ref) → scan EVERY entry field for `https?://` — CMS
  content is a SUPERSET of the bundle for hostnames (preview/dev hosts the JS never names).
- prod-on-RC environments, Contentful/Prismic space enumeration from one token.
- WordPress: `wordpress-cloudflare-origin-bypass.md` recipe — direct-origin + `_embed` author
  slug enum + `wp_ajax_nopriv_*` sweep + maintenance-auth-oracle discriminator.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
