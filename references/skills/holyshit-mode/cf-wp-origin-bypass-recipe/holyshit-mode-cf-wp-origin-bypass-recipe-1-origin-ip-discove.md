# 1. Origin IP discovery — the SPF leak (the #1 CF-origin reveal)

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
