# 6.8 CMS/marketing plane (score 65) — chain composition

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-8-cms-marketing-pla.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Leaked delivery token (bundle/CMS ref) → scan EVERY entry field for `https?://` — CMS
  content is a SUPERSET of the bundle for hostnames (preview/dev hosts the JS never names).
- prod-on-RC environments, Contentful/Prismic space enumeration from one token.
- WordPress: `wordpress-cloudflare-origin-bypass.md` recipe — direct-origin + `_embed` author
  slug enum + `wp_ajax_nopriv_*` sweep + maintenance-auth-oracle discriminator.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
