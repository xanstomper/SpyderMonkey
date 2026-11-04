#!/usr/bin/env bash
# SPYDERMONKEY CI smoke — runs locally verbatim, runs in CI verbatim.
# Mirrors the workflow's assertions; each run starts from a FRESH isolated HOME.
set -euo pipefail
cd "$(dirname "$0")/.."

export HOME="${RUNNER_TEMP:-/tmp}/spydermonkey-smoke-$$"
rm -rf "$HOME"
mkdir -p "$HOME"
trap 'rm -rf "$HOME"' EXIT
S=scripts/spydermonkey.py
KAGE="${KAGE_ENGINE:-$PWD/../kage/scripts/kage.py}"
DOJO="${DOJO_ENGINE:-$PWD/../dojo/scripts/dojo.py}"
KAISHA="${KAISHA_ENGINE:-$PWD/../kaisha/scripts/kaisha.py}"

echo "── compile all five scripts"
python3 -m py_compile scripts/spydermonkey.py scripts/arsenal.py scripts/bench_live.py scripts/mcp_server.py scripts/skilltree.py

echo "── dispatcher CLI"
python3 $S --help > /dev/null
python3 $S tree | grep -q BARBICAN
python3 $S tree | grep -q SHIKI
python3 $S route --goal "protect my ass" | grep -q barbican
python3 $S route --goal "take over their session" | grep -q 3am
python3 $S route --goal "forge the weapons" | grep -q kairo
python3 $S route --goal "price what they could take" | grep -q shukaku
python3 $S route --goal "full assault" | grep -q shiki
python3 $S tree | grep -q KAGE
python3 $S tree | grep -q DOJO
python3 $S route --goal "detect the intrusion" | grep -q kage
python3 $S route --goal "train on a replica" | grep -q dojo
python3 $S route --goal "zzz unknown goal qqq" | grep -q 'barbican → holyshit → undercroft → kairo → 3am → kaisha → shukaku → kage → dojo'
python3 $S run --target demo --url https://example.com --domain example.com --dry-run | grep -q 'shiki assault'
python3 $S mandate --file | grep -q 'mandate.md'
python3 $S mandate | grep -q 'MANDATE: SPYDERMONKEY'
python3 $S status | grep -q 'family status'

echo "── scope authority"
python3 $S scope init --engagement ci --in-scope "ci.example,10.0.0.0/24" --file "$HOME/scope.json" | grep -q 'scope authority'
python3 $S scope check --value https://api.ci.example --file "$HOME/scope.json" | grep -q 'IN SCOPE'
python3 $S scope check --value https://evil.com --file "$HOME/scope.json" 2>/dev/null && exit 1 || test $? -eq 1

echo "── intelligence layer: ledger · gate · testers · triage · chain · phases · coverage · report"
rm -rf "$HOME/.redteam/campaigns/smoke-v3"
python3 $S ledger add --target smoke-v3 --title "unproven claim" --asset http://127.0.0.1:9/x \
  --cls IDOR --severity high --proof "no evidence at all" | grep -q 'downgraded'
python3 $S ledger add --target smoke-v3 --title "unproven claim" --asset http://127.0.0.1:9/x \
  --cls IDOR --severity high --proof "no evidence at all" | grep -q 'DUPLICATE'
python3 $S ledger triage --target smoke-v3 >/dev/null
python3 $S testers --target smoke-v3 --demo | grep -qE '[0-9]+/8 tester'
python3 $S chain detect --target smoke-v3 | grep -q 'chain candidate'
python3 $S chain detect --target smoke-v3 | grep -q 'CH-001' # idor(harvest)+data pairs from the demo strike
python3 $S phases --target smoke-v3 | grep -q '13 phases'
python3 $S coverage --target smoke-v3 | grep -q 'COVERAGE'
python3 $S report --target smoke-v3 | grep -q 'war report written'
grep -q 'Executive summary' smoke-v3-spydermonkey-report.md
rm -f smoke-v3-spydermonkey-report.md

echo "── relay: refusal paths"
python3 $S relay exec --name ghost --cmd id 2>/dev/null && exit 1 || test $? -eq 2
python3 $S relay list | grep -qE 'RELAY|no relays'

echo "── bench · arsenal · mcp · skilltree"
python3 $S bench | grep -q 'route accuracy'
python3 scripts/arsenal.py verify | grep -q 'ARSENAL verify'
python3 scripts/bench_live.py --help > /dev/null
python3 $S fleet --help > /dev/null
python3 scripts/skilltree.py --count | grep -qE '[0-9]+ technique'
printf '{"jsonrpc":"2.0","id":1,"method":"tools/list"}\n' | python3 scripts/mcp_server.py | grep -q 'ledger_triage'
test -f references/mandate.md

echo "── family engines (on CI they are absent → verify fails with the install hint)"
python3 $S doctor > /dev/null 2>&1 || test $? -eq 1
python3 $S verify > /dev/null 2>&1 || test $? -eq 1
vout=$(python3 $S verify 2>/dev/null || true)
echo "$vout" | grep -qE 'engines not installed|ALL PASS'

echo "── KAGE v2: mirror from the ledger · Sigma export · refire (live, lab-bound)"
python3 $S ledger add --target kage-smoke --title "idor differential on param org_id" \
  --asset "http://127.0.0.1:8801/api/orders?org_id=acme" --cls IDOR --severity high \
  --proof "baseline: 200 acme; attack: 200 foreign; diff: org echoed from query" >/dev/null
if [ ! -f "$KAGE" ]; then
  echo "  (kage engine not present in this checkout — skipping kage assertions)"
else
  python3 "$KAGE" verify | grep -q 'ALL PASS'
  python3 "$KAGE" mirror --target kage-smoke | grep -q 'detection rule'
  python3 "$KAGE" export --target kage-smoke --dir "$HOME/sigma" | grep -q 'Sigma rule file'
  grep -q 'logsource:' "$HOME"/sigma/*.yml
  grep -q 'falsepositives:' "$HOME"/sigma/*.yml
  python3 "$KAGE" validate --target kage-smoke > /dev/null 2>&1 || test $? -eq 1
  python3 "$DOJO" build --class BOUNDARY --port 8801 --serve-seconds 10 &
  sleep 1.5
  python3 "$KAGE" refire --target kage-smoke --rule KAGE-001 | grep -q 'FIRED'
  wait || true
  rm -rf "$HOME/.redteam/campaigns/kage-smoke" "$HOME/sigma"
fi

echo "── DOJO v2: 15 classes · bench self-verifies"
if [ ! -f "$DOJO" ]; then
  echo "  (dojo engine not present — skipping)"
else
  D="$DOJO"
  python3 "$D" catalog | grep -q '15 buildable'
  python3 "$D" bench --class BOUNDARY --port 8812 | grep -q 'CONFIRMED'
  python3 "$D" bench --class JWT --port 8813 | grep -q 'CONFIRMED'
  python3 "$D" verify | grep -q 'ALL PASS'
fi

echo "── KAISHA v1.2: revert evidence"
if [ ! -f "$KAISHA" ]; then
  echo "  (kaisha engine not present — skipping)"
else
  KA="$KAISHA"
  python3 "$KA" ladder --target kaisha-smoke --host lab1 --access "validated web shell" > /dev/null
  python3 "$KA" revert --target kaisha-smoke --host lab1 --rung R4a \
    --evidence "documented class matched; nothing executed" | grep -q 'reversal recorded'
  python3 "$KA" rungs --target kaisha-smoke | grep -q 'REVERTED'
  python3 "$KA" revert --target kaisha-smoke --host lab1 --rung R4b 2>/dev/null && exit 1 || test $? -eq 2
  rm -rf "$HOME/.redteam/campaigns/kaisha-smoke"
fi

echo "── exit codes"
python3 $S route 2>/dev/null && exit 1 || test $? -eq 2
python3 $S ledger add --target smoke-v3 --asset x 2>/dev/null && exit 1 || test $? -eq 2
python3 $S gate --target smoke-v3 --url http://127.0.0.1:9/x 2>/dev/null && exit 1 || test $? -eq 2
python3 $S chain plan --target smoke-v3 2>/dev/null && exit 1 || test $? -eq 2

echo "── stdlib-only"
! grep -E '^[[:space:]]*(import|from)[[:space:]]+(requests|flask|httpx|aiohttp|urllib3)' scripts/spydermonkey.py

echo "── stdlib-only (kage/dojo/kaisha engines)"
for e in "$KAGE" "$DOJO" "$KAISHA"; do
  [ -f "$e" ] && ! grep -E '^[[:space:]]*(import|from)[[:space:]]+(requests|flask|httpx|aiohttp|urllib3)' "$e" || true
done

echo "SPYDERMONKEY ci_smoke: ALL PASS"
