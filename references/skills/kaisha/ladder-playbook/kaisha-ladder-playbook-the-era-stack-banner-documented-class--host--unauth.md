# The era-stack (banner → documented classes) — host / unauth

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-the-era-stack-banner-documented-class.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **host** · auth **unauth** · chain role **pivot**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

KAISHA never authors exploits. A banner maps to the era's documented technique
classes (3AM canon) — the ladder then plans those classes' validation tests:

| Banner pattern | Era | Documented classes | Canon |
|---|---|---|---|
| `nginx/1.(0-19).` | nginx legacy | header/parser-differential (9) · cache/edge-separation (7) | arsenal-01/02 |
| `apache/2.2|2.4` | apache legacy | validation-order (1) · parser-differential (9) | arsenal-01 |
| `openssh_(0-8).` | openssh old-major | entropy/forge (10) · identifier-trust (6) | arsenal-01 |
| `iis/7|8` | iis legacy | parser-differential (9) · type-coercion (3) | arsenal-06 |
| `tomcat/8|9 · jetty/9` | java app-server legacy | type-coercion (3) · state-machine-gaps (5) | arsenal-06 |
| windows / microsoft | windows estate | session/cookie-confusion (8) · operational-planes (20) | arsenal-06 · session-lessons |
| linux / ubuntu / debian | linux estate | state-machine-gaps (5) · database-exposure (15) | arsenal-06 |

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
