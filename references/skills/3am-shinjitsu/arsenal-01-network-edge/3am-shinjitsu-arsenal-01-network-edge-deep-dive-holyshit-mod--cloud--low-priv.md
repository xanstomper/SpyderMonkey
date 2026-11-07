# DEEP DIVE — holyshit-mode depth (load on confirm) — cloud / low-priv

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-deep-dive-holyshit-mod.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- → holyshit `references/wordpress-cloudflare-origin-bypass.md` + `cf-wp-origin-bypass-recipe.md` — origin-leak→direct-origin full ladder
- → holyshit `references/case-g***REDACTED***-adjacent-infra.md` — era-stack fingerprint recipe (VestaCP 301 path leak, :8083/:3306 banners)
- → holyshit `references/recon-quick-checks.md` — CF-origin leak, engine.io sid, SPA ghost discriminator batteries
- → holyshit `references/engagement-vantage-policy.md` — probe from the VM vantage, never the home IP (attribution law)
```

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
