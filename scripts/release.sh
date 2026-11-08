#!/bin/bash
# SpyderMonkey release pipeline — the product-readiness shipping lane.
#
#   ./scripts/release.sh            build the release artifact for the CURRENT version
#   ./scripts/release.sh --tag      bump-check + git tag v<VERSION> + push
#
# Produces: dist/spydermonkey-v<VERSION>.tar.gz (repo, licenses, manifest) +
# dist/SHA256SUMS (the SBOM-lite manifest). Refuses to tag a dirty tree or a
# version that fails the version audit.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

VERSION="$(grep -h '^VERSION = ' scripts/spydermonkey.py | cut -d'"' -f2)"
DIST="$REPO/dist"

python3 scripts/version_audit.py || { echo "✗ version audit failed — fix version homes first"; exit 1; }

git diff --quiet || { echo "✗ working tree dirty — commit (or stash) before release"; exit 1; }

mkdir -p "$DIST"
TARBALL="$DIST/spydermonkey-v$VERSION.tar.gz"

# the release artifact: everything except git state, caches, scratch
git ls-files -z | tar --null -T - -czf "$TARBALL"
echo "✓ tarball   $TARBALL ($(du -h "$TARBALL" | cut -f1))"

# SBOM-lite: sha256 manifest of every file in the artifact
(cd "$REPO" && git ls-files -z | xargs -0 sha256sum > "$DIST/SHA256SUMS")
echo "✓ manifest  $DIST/SHA256SUMS ($(wc -l < "$DIST/SHA256SUMS") files)"

if [[ "${1:-}" == "--tag" ]]; then
    git tag -s "v$VERSION" -m "SpyderMonkey v$VERSION — product-readiness release" 2>/dev/null \
        || git tag "v$VERSION" -m "SpyderMonkey v$VERSION — product-readiness release"
    git push origin "v$VERSION"
    echo "✓ tagged    v$VERSION (pushed)"
fi

echo "═══ RELEASE v$VERSION READY ═══"
echo "  artifact: $TARBALL"
echo "  verify:   sha256sum -c $DIST/SHA256SUMS"
echo "  install:  tar -xzf $TARBALL && ./scripts/install.sh"