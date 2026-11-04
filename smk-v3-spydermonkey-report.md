# SPYDERMONKEY War Report — smk-v3

_generated 2026-11-04T17:28:03.433161+00:00 · scope: gamdom-reengage_

## Executive summary

- **7** finding(s) registered · **7** confirmed (3-gate evidence)
- severity mix: high=3, medium=4
- **0** chain candidate(s) — low findings combining into high-impact chains
- **0** detection rule(s) mirrored (kage)
- harvest crown rows: 0 (shukaku pricing)

## Findings

### SPY-001 — IDOR differential on param 'org_id' [CONFIRMED · high · conf 0.95]
- class: IDOR · asset: http://127.0.0.1:33121/api/orders?org_id=acme
- proof: baseline: 200 len=36 (param org_id=acme); attack: 200 len=38 (param org_id=acme+1); diff: baseline vs attack differ on IDOR

### SPY-002 — AUTHZ differential on param 'role' [CONFIRMED · medium · conf 0.95]
- class: AUTHZ · asset: http://127.0.0.1:33121/role?role=user
- proof: baseline: 200 len=33 (param role=user); attack: 200 len=30 (param role=1); diff: baseline vs attack differ on AUTHZ

### SPY-003 — MASSASSIGN differential on param 'body' [CONFIRMED · medium · conf 0.95]
- class: MASSASSIGN · asset: http://127.0.0.1:33121/api/user?name=bob&email=bob@lab
- proof: baseline: 200 len=80 (param body=+base fields); attack: 200 len=133 (param body=&role=admin&is_admin=1&price=0&balance=999999); diff: baseline vs attack differ on MASSASSIGN

### SPY-004 — AUTHN differential on param 'token' [CONFIRMED · medium · conf 0.95]
- class: AUTHN · asset: http://127.0.0.1:33121/api/token?token=abc
- proof: baseline: 200 len=24 (param token=abc); attack: 200 len=39 (param token=); diff: baseline vs attack differ on AUTHN

### SPY-005 — BIZLOGIC differential on param 'amount' [CONFIRMED · medium · conf 0.95]
- class: BIZLOGIC · asset: http://127.0.0.1:33121/api/coupon?amount=5
- proof: baseline: 200 len=32 (param amount=5); attack: 200 len=33 (param amount=-1); diff: baseline vs attack differ on BIZLOGIC

### SPY-006 — SSRF differential on param 'url' [CONFIRMED · high · conf 0.95]
- class: SSRF · asset: http://127.0.0.1:33121/fetch?url=http://example.com
- proof: baseline: 200 len=21 (param url=http://example.com); attack: 200 len=35 (param url=http://127.0.0.1:9/); diff: baseline vs attack differ on SSRF

### SPY-007 — FILEATTACK differential on param 'path' [CONFIRMED · high · conf 0.95]
- class: TRAVERSAL · asset: http://127.0.0.1:33121/file?path=etc
- proof: baseline: 404 len=4 (param path=etc); attack: 200 len=32 (param path=../../etc/passwd); diff: baseline vs attack differ on FILEATTACK

## Phase coverage

- completed   scope_analysis (barbican)
- blocked     passive_recon (holyshit)
- blocked     active_recon (undercroft)
- blocked     technology_profiling (kaisha)
- completed   authentication_testing (3am)
- blocked     session_management (3am)
- completed   authorization_testing (spy)
- blocked     input_validation (spy)
- completed   business_logic (undercroft)
- blocked     data_protection (shukaku)
- completed   api_security (spy)
- blocked     infrastructure (kaisha)
- blocked     reporting (spy)

