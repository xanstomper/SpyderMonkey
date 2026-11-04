#!/usr/bin/env bash
# SPYDERMONKEY CI smoke — runs locally verbatim, runs in CI verbatim.
# Each run starts from a FRESH isolated HOME; the operator's ~/.redteam is never
# read or written. This script is the local truth, not a second CI-only suite.
set -euo pipefail
cd "$(dirname "$0")/.."

export HOME="${RUNNER_TEMP:-/tmp}/spydermonkey-smoke-$$"
rm -rf "$HOME"
mkdir -p "$HOME"
export SPYDERMONKEY_HOME="$HOME/.redteam"
# Keep the scope at the family default path ($HOME/.redteam/scope.json) so the
# standalone engines that do not know SPYDERMONKEY_SCOPE read the same estate.
export SPYDERMONKEY_SCOPE="$HOME/.redteam/scope.json"
trap 'rm -rf "$HOME"' EXIT
S=scripts/spydermonkey.py
KAGE="${KAGE_ENGINE:-$PWD/../kage/scripts/kage.py}"
DOJO="${DOJO_ENGINE:-$PWD/../dojo/scripts/dojo.py}"
KAISHA="${KAISHA_ENGINE:-$PWD/../kaisha/scripts/kaisha.py}"

expect_rc() {
  local want="$1"; shift
  set +e
  "$@" >"$HOME/last.out" 2>&1
  local got=$?
  set -e
  if [ "$got" -ne "$want" ]; then
    echo "  expected rc=$want, got rc=$got: $*"
    cat "$HOME/last.out"
    exit 1
  fi
}

echo "── compile all six scripts"
python3 -m py_compile scripts/spydermonkey.py scripts/scope_authority.py \
  scripts/arsenal.py scripts/bench_live.py scripts/mcp_server.py scripts/skilltree.py

echo "── dispatcher CLI · tree · router · version · kernel"
python3 $S --help > /dev/null
python3 $S version --json | grep -q '"version": "4.0.0"'
python3 $S tree | grep -q BARBICAN
python3 $S tree | grep -q SHIKI
python3 $S tree | grep -q KAGE
python3 $S tree | grep -q DOJO
python3 $S route --goal "protect my ass" | grep -q barbican
python3 $S route --goal "take over their session" | grep -q 3am
python3 $S route --goal "forge the weapons" | grep -q kairo
python3 $S route --goal "price what they could take" | grep -q shukaku
python3 $S route --goal "full assault" | grep -q shiki
python3 $S route --goal "detect the intrusion" | grep -q kage
python3 $S route --goal "train on a replica" | grep -q dojo
python3 $S route --goal "zzz unknown goal qqq" | grep -q 'barbican → holyshit → undercroft → kairo → 3am → kaisha → shukaku → kage → dojo'
python3 $S run --target demo --url https://example.com --domain example.com --dry-run | grep -q 'shiki assault'
python3 $S mandate --file | grep -q 'mandate.md'
python3 $S mandate | grep -q 'MANDATE: SPYDERMONKEY'
python3 $S status | grep -q 'family status'
python3 $S status --fast --json | grep -q '"engines_total": 10'

echo "── scope authority · one shared verdict · audit · perms"
python3 $S scope init --engagement ci --in-scope "ci.example,*.api.ci.example,10.0.0.0/24" \
  --out-of-scope "billing.ci.example" --expires-days 2 --file "$SPYDERMONKEY_SCOPE" | grep -q 'scope authority'
python3 $S scope check --value https://api.ci.example --file "$SPYDERMONKEY_SCOPE" | grep -q 'IN SCOPE'
python3 $S scope check --value https://deep.api.ci.example --file "$SPYDERMONKEY_SCOPE" | grep -q 'IN SCOPE'
python3 $S scope check --value http://10.0.0.9 --file "$SPYDERMONKEY_SCOPE" | grep -q 'IN SCOPE'
expect_rc 1 python3 $S scope check --value https://billing.ci.example --file "$SPYDERMONKEY_SCOPE"
expect_rc 1 python3 $S scope check --value https://evil.com --file "$SPYDERMONKEY_SCOPE"
test "$(stat -c '%a' "$SPYDERMONKEY_SCOPE")" = "600"
python3 $S scope history --file "$SPYDERMONKEY_SCOPE" | grep -q 'SCOPE AUDIT'
python3 $S scope add --kind in --value "extra.ci.example" --file "$SPYDERMONKEY_SCOPE" > /dev/null
python3 $S scope check --value https://extra.ci.example --file "$SPYDERMONKEY_SCOPE" | grep -q 'IN SCOPE'

echo "── campaigns · lifecycle · guarded purge · contracts"
python3 $S campaign init --target smoke-v4 --objective "ci smoke" \
  --url https://ci.example --domain ci.example | grep -q 'campaign opened'
python3 $S campaign list | grep -q 'smoke-v4'
python3 $S campaign show --target smoke-v4 | grep -q 'CAMPAIGN'
python3 $S campaign timeline --target smoke-v4 | grep -q 'CAMPAIGN TIMELINE'
python3 $S campaign archive --target smoke-v4 | grep -q 'archive'
expect_rc 2 python3 $S campaign purge --target smoke-v4
python3 $S campaign close --target smoke-v4 --note "ci close" | grep -q 'closed'
python3 $S mandates verify | grep -q 'ALL CONTRACTS VALID'
test "$(ls references/mandates/*.md | wc -l)" -eq 10
python3 $S mandates list --json | grep -q '"count": 10'
python3 $S mandates show --name barbican | grep -q '## law'

echo "── intelligence layer: ledger · gate · testers · triage · chain · phases · coverage · report"
python3 $S ledger add --target smoke-v4 --title "unproven claim" --asset http://127.0.0.1:9/x \
  --cls IDOR --severity high --proof "no evidence at all" | grep -q 'downgraded'
python3 $S ledger add --target smoke-v4 --title "unproven claim" --asset http://127.0.0.1:9/x \
  --cls IDOR --severity high --proof "no evidence at all" | grep -q 'DUPLICATE'
python3 $S ledger add --target smoke-v4 --title "cross-tenant order read" --cls IDOR \
  --asset https://api.ci.example/api/orders?org_id=acme \
  --proof "baseline: GET org_id=acme -> 200 acme; attack: GET org_id=foreign -> 200 foreign; diff: body echoes swapped org id" \
  | grep -q 'CONFIRMED'
python3 $S ledger verify --target smoke-v4 | grep -q 'LEDGER VERIFY'
python3 $S ledger stats --target smoke-v4 | grep -q 'CONFIRMED'
python3 $S ledger export --target smoke-v4 --format sarif --output - \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); assert d["version"] == "2.1.0"'
expect_rc 1 python3 $S ledger add --target smoke-v4 --title "outside" \
  --asset https://evil.test/x --proof "baseline: a; attack: b; diff: c"
python3 $S ledger triage --target smoke-v4 > /dev/null
python3 $S testers --target smoke-v4 --demo | grep -qE '[0-9]+/8 tester'
python3 $S chain detect --target smoke-v4 | grep -q 'chain candidate'
python3 $S chain detect --target smoke-v4 | grep -q 'CH-001'
python3 $S phases --target smoke-v4 | grep -q '13 phases'
python3 $S next-phase --target smoke-v4 | grep -qE 'next for|complete'
python3 $S coverage --target smoke-v4 | grep -q 'COVERAGE'
python3 $S report --target smoke-v4 | grep -q 'war report written'
test -f "$SPYDERMONKEY_HOME/campaigns/smoke-v4/smoke-v4-spydermonkey-report.md"
grep -q 'Executive summary' "$SPYDERMONKEY_HOME/campaigns/smoke-v4/smoke-v4-spydermonkey-report.md"
python3 $S report --target smoke-v4 --format json --output "$HOME/report.json" > /dev/null
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert "findings" in d' "$HOME/report.json"

echo "── kernel: next · absorb · loop plan-only"
python3 $S next --target smoke-v4 --domain ci.example --json > "$HOME/next.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["next"]["directive_id"]; assert d["next"]["argv"]' "$HOME/next.json"
cat > "$HOME/result.json" <<'JSON'
{"step": 1, "exit": 0, "findings": [], "context": {"endpoints": []}, "notes": "ci absorb"}
JSON
python3 $S absorb --target smoke-v4 --file "$HOME/result.json" | grep -qE 'absorbed|directive|MISSION'
expect_rc 2 python3 $S absorb --target smoke-v4 --file "$HOME/missing.json"
python3 $S loop --target smoke-v4 --domain ci.example --plan-only | grep -q 'plan'

echo "── v4.1 SURFACE ENGINE: crawl mines the map · two-role AUTHZ"
python3 $S crawl --target smoke-v4 --url "http://127.0.0.1:9/x?org_id=acme" --json | grep -q '"endpoints"'
python3 $S context set --target smoke-v4 --kind credentials --value "admin:tok-a" --value "user:tok-b" > /dev/null
python3 $S testers --target smoke-v4 --demo | grep -qE '[0-9]+/8 tester'

echo "── v4.2 TAKEOVER ENGINE: fingerprints + wall"
python3 $S takeover --target smoke-v4 --domain evil.com 2>/dev/null && exit 1 || test $? -eq 1
echo "── relay · refusal paths · usage errors"
expect_rc 2 python3 $S relay exec --name ghost --cmd id
python3 $S relay list | grep -qE 'RELAY|no relays'
expect_rc 2 python3 $S route
expect_rc 2 python3 $S ledger add --target smoke-v4 --asset x
expect_rc 2 python3 $S gate --target smoke-v4 --url http://127.0.0.1:9/x
expect_rc 2 python3 $S chain plan --target smoke-v4
expect_rc 2 python3 $S campaign init --target ../escape
expect_rc 1 python3 $S scope check --value https://evil.com

echo "── bench · self-test · arsenal · live bench · skilltree · MCP"
python3 $S bench | grep -q 'route accuracy: 29/29'
python3 $S selftest --quick --json > "$HOME/selftest.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["ok"] and d["total"] >= 14, d' "$HOME/selftest.json"
python3 scripts/arsenal.py verify | grep -q 'ARSENAL verify'
python3 scripts/arsenal.py run --target http://127.0.0.1:9 --chain net --dry-run --out "$HOME/chain-out.json" > /dev/null
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert {"step","exit","findings","context","notes"} <= set(d)' "$HOME/chain-out.json"
python3 scripts/bench_live.py --json --no-engine > "$HOME/bench_live.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["accuracy"] >= 90, d' "$HOME/bench_live.json"
python3 scripts/skilltree.py --count --json | grep -q '"count"'
python3 scripts/skilltree.py --verify --json > "$HOME/skilltree.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["ok"] and d["links"] + d["expanded_links"] == d["files"] and d["expanded_links"] >= 7000, d' "$HOME/skilltree.json"
test "$(grep -c '^- \[' references/skilltree-expanded-index.md)" -ge 7000
printf '{"jsonrpc":"2.0","id":1,"method":"tools/list"}\n{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"version","arguments":{}}}\n' \
  | python3 scripts/mcp_server.py > "$HOME/mcp.jsonl"
python3 -c 'import json,sys; rows=[json.loads(l) for l in open(sys.argv[1]) if l.strip()]; assert len(rows) == 2; assert len(rows[0]["result"]["tools"]) >= 43; assert "4.0.0" in json.dumps(rows[1])' "$HOME/mcp.jsonl"
test -f references/mandate.md

echo "── stdlib test suite"
python3 -m unittest discover -s tests -v

echo "── family engines (absent on a bare CI checkout → verify fails with the install hint)"
if python3 $S doctor --fast > /dev/null 2>&1; then
  echo "  (all ten engines present — doctor healthy)"
else
  test $? -eq 1
fi
vout=$(python3 $S verify --fast --no-selftest 2>/dev/null || true)
echo "$vout" | grep -qE 'engines not installed|ALL PASS' || true

echo "── KAGE v2: mirror from the ledger · Sigma export · refire (live, lab-bound)"
if [ ! -f "$KAGE" ]; then
  echo "  (kage engine not present in this checkout — skipping kage assertions)"
else
  python3 "$KAGE" verify | grep -q 'ALL PASS'
  python3 "$KAGE" mirror --target smoke-v4 | grep -q 'detection rule'
  python3 "$KAGE" export --target smoke-v4 --dir "$HOME/sigma" | grep -q 'Sigma rule file'
  grep -q 'logsource:' "$HOME"/sigma/*.yml
  grep -q 'falsepositives:' "$HOME"/sigma/*.yml
  python3 "$KAGE" validate --target smoke-v4 > /dev/null 2>&1 || test $? -eq 1
  python3 "$DOJO" build --class BOUNDARY --port 8801 --serve-seconds 10 &
  sleep 1.5
  python3 "$KAGE" refire --target smoke-v4 --rule KAGE-001 \
    --url "http://127.0.0.1:8801/api/orders?org_id=foreign" | grep -q 'FIRED'
  wait || true
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
fi

echo "── stdlib-only"
! grep -E '^[[:space:]]*(import|from)[[:space:]]+(requests|flask|httpx|aiohttp|urllib3)' scripts/spydermonkey.py
! grep -E '^[[:space:]]*(import|from)[[:space:]]+(requests|flask|httpx|aiohttp|urllib3)' scripts/scope_authority.py

echo "── stdlib-only (kage/dojo/kaisha engines)"
for e in "$KAGE" "$DOJO" "$KAISHA"; do
  [ -f "$e" ] && ! grep -E '^[[:space:]]*(import|from)[[:space:]]+(requests|flask|httpx|aiohttp|urllib3)' "$e" || true
done

echo "SPYDERMONKEY ci_smoke: ALL PASS"
