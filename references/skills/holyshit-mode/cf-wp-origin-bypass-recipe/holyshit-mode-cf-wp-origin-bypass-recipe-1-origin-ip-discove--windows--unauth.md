# 1. Origin IP discovery — the SPF leak (the #1 CF-origin reveal) — windows / unauth

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-1-origin-ip-discove.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **windows** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

When the HTML surface is a CF JS challenge and you can't reach the origin, the origin IP is
often leaked by **SPF** (it must list the real sending/mail IP, which is usually the origin
host):

```
dig +short 
  "v=spf1 ip4:88.119.163.60 ~all"
```

The `ip4:` in SPF is frequently the origin octet. Confirm with `nmap -Pn -T4 --top-ports 60`
on that IP — an open 80/443 alongside mail ports (465/587/993) = it's a full web+mail origin,
not just a mail gateway. PTR (`saturnus.space`) confirms the host identity.

Other origin-leak sources when SPF is absent: crt.sh certificate transparency (look for
certs bound to the origin IP or non-CF SANs), historical DNS the operator forgot to update,
TLS SAN enumeration (`echo | openssl s_client ... | openssl x509 -noout -ext subjectAltName`),
and vhosts that resolve to non-CF IPs. Subdomain DNS is usually a dead end — everything
returns the CF anycast pair.

## Probe adjustment (windows × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
