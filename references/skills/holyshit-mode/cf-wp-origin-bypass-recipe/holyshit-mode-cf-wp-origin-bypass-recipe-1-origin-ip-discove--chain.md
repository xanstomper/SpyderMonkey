# 1. Origin IP discovery — the SPF leak (the #1 CF-origin reveal) — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-1-origin-ip-discove.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
