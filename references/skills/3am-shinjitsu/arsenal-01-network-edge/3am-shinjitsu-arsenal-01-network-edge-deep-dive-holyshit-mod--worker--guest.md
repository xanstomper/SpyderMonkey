# DEEP DIVE — holyshit-mode depth (load on confirm) — worker / guest

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-deep-dive-holyshit-mod.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- → holyshit `references/wordpress-cloudflare-origin-bypass.md` + `cf-wp-origin-bypass-recipe.md` — origin-leak→direct-origin full ladder
- → holyshit `references/case-g***REDACTED***-adjacent-infra.md` — era-stack fingerprint recipe (VestaCP 301 path leak, :8083/:3306 banners)
- → holyshit `references/recon-quick-checks.md` — CF-origin leak, engine.io sid, SPA ghost discriminator batteries
- → holyshit `references/engagement-vantage-policy.md` — probe from the VM vantage, never the home IP (attribution law)
```

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
