# 6.8 CMS/marketing plane (score 65) — gateway / guest

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-8-cms-marketing-pla.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **guest** · chain role **pivot**

## Route

- probes: `wpscan`, `cmseek`, `droopescan`, `cmsmap`, `nmap-wp-plugins`, `nmap-drupal-enum`
- chains: `cms-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Leaked delivery token (bundle/CMS ref) → scan EVERY entry field for `https?://` — CMS
  content is a SUPERSET of the bundle for hostnames (preview/dev hosts the JS never names).
- prod-on-RC environments, Contentful/Prismic space enumeration from one token.
- WordPress: `wordpress-cloudflare-origin-bypass.md` recipe — direct-origin + `_embed` author
  slug enum + `wp_ajax_nopriv_*` sweep + maintenance-auth-oracle discriminator.

## Probe adjustment (gateway × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
