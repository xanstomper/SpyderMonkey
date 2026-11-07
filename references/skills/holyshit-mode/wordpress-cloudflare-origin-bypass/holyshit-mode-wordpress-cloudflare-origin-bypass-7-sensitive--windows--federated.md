# 7. Sensitive-file soft-404 discriminator (don't false-positive) — windows / federated

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-7-sensitive.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **windows** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

On this origin, every missing path under `.env.bak`, `/.htpasswd`, `/backup.zip`, `/dump.sql`,
`/.git/config`, `/wp-config.php` returned **`200 text/html`** with the same generic
"DOCTYPE html / charset=utf8 / viewport" page. That identical template is a **custom soft-404**,
NOT file content. Discriminate by body: real secrets would differ / be smaller; an identical
shell = file does not exist. A plain `st==200` is a false-positive trap.

## Probe adjustment (windows × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
