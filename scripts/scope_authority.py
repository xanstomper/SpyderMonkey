#!/usr/bin/env python3
"""
SPYDERMONKEY SCOPE AUTHORITY — one estate gate for every family layer.

This module is the single implementation of "is this value inside the declared
engagement?" used by the dispatcher, the arsenal, the MCP server and the live
bench. It replaces the earlier per-script scope checks, which drifted: one knew
CIDRs, another did not; one ignored out_of_scope, another allowed "*" silently.

The model (schema 2):
  {
    "schema": 2,
    "engagement": "acme-p1",
    "in_scope":  ["acme.com", "*.acme.com", "https://api.acme.com/v1",
                  "10.0.0.0/24", "203.0.113.7:8443"],
    "out_of_scope": ["billing.acme.com", "10.0.0.5"],
    "rules": {"max_rate_rps": 10, "passive_first": true, ...},
    "expires": "2026-12-31T23:59:59+00:00" | null,
    "created": "...", "updated": "..."
  }

Matching rules, highest precedence first:
  1. An expired authority matches NOTHING (the estate is closed).
  2. out_of_scope wins over in_scope (deny beats allow), always.
  3. in_scope entries match by:
       - explicit "*" / "all"             → any non-denied host
       - CIDR                             → IP address within the network
       - IPv4/IPv6 literal (+ optional port) → exact address
       - URL                              → host; when the URL carries a path
                                            deeper than "/", the value's path
                                            must begin with it
       - "*.example.com"                  → subdomains only (not the apex)
       - "example.com"                    → apex and all subdomains
  4. Anything unmatched is OUT OF SCOPE.

Lab hosts (127.0.0.1 / localhost / ::1) are always lab-legal unless
rules.allow_lab is explicitly false. That keeps dojo replicas and CI useful
without opening a production estate.

Paths:
  scope file   $SPYDERMONKEY_SCOPE, else $SPYDERMONKEY_HOME/scope.json,
               else ~/.redteam/scope.json
  audit log    <scope dir>/scope-audit.jsonl (mode 0600)
  env home     $SPYDERMONKEY_HOME, else ~/.redteam

Stdlib only. Exit-code discipline: callers turn a False verdict into rc=1.
"""
from __future__ import annotations

import ipaddress
import json
import os
import re
import threading
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

SCHEMA = 2
_LOCK = threading.Lock()
_AUDIT_LOCK = threading.Lock()
_LAST = {"at": 0.0}


class ScopeError(Exception):
    """Raised for malformed scope files or invalid operations."""


# ── paths ────────────────────────────────────────────────────────────────────

def redteam_home() -> Path:
    """$SPYDERMONKEY_HOME or ~/.redteam — the one data root for the family."""
    env = os.environ.get("SPYDERMONKEY_HOME", "").strip()
    if env:
        return Path(env).expanduser().resolve()
    return Path.home() / ".redteam"


def campaigns_root() -> Path:
    return redteam_home() / "campaigns"


def scope_path(file: str | os.PathLike | None = None) -> Path:
    if file:
        return Path(file).expanduser().resolve()
    env = os.environ.get("SPYDERMONKEY_SCOPE", "").strip()
    if env:
        return Path(env).expanduser().resolve()
    return redteam_home() / "scope.json"


def audit_path(file: str | os.PathLike | None = None) -> Path:
    return scope_path(file).parent / "scope-audit.jsonl"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ── safe names ───────────────────────────────────────────────────────────────

_SAFE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def safe_name(name: str, what: str = "name") -> str:
    """Validate a campaign/relay name before it becomes a path component.

    Rejects traversal, absolute paths, hidden files, control characters and
    anything that is not a single path segment. Returns the name unchanged so
    it reads naturally at call sites.
    """
    name = (name or "").strip()
    if not name or name in (".", "..") or "/" in name or "\\" in name \
            or "\x00" in name or name.startswith(".") or len(name) > 64:
        raise ScopeError(f"invalid {what}: {name!r} (one path segment, no leading dot)")
    if not _SAFE.match(name):
        raise ScopeError(f"invalid {what}: {name!r} (use letters, digits, . _ -)")
    return name


# ── scope file IO ────────────────────────────────────────────────────────────

def _normalize(raw: dict) -> dict:
    if not isinstance(raw, dict):
        raise ScopeError("scope must be a JSON object")
    scope = dict(raw)
    scope.setdefault("schema", 1)
    scope.setdefault("engagement", "unnamed")
    for k in ("in_scope", "out_of_scope"):
        v = scope.get(k) or []
        if not isinstance(v, list):
            raise ScopeError(f"{k} must be a list")
        scope[k] = [str(x).strip() for x in v if str(x).strip()]
    scope.setdefault("rules", {})
    if not isinstance(scope["rules"], dict):
        raise ScopeError("rules must be an object")
    scope.setdefault("expires", None)
    return scope


def _validate_entry(entry: str) -> None:
    """Reject entries that cannot mean what the operator thinks they mean.

    A scope file is a safety control, so a typo must fail closed at write time
    instead of silently matching nothing (or everything).
    """
    e = (entry or "").strip()
    if not e:
        raise ScopeError("scope entries cannot be empty")
    low = e.lower()
    if low in ("*", "all"):
        return
    if any(ch in e for ch in "\x00\r\n\t"):
        raise ScopeError(f"invalid scope entry {entry!r}: control characters")
    if e.startswith("*."):
        if len(e) < 4 or "." not in e[2:]:
            raise ScopeError(f"invalid wildcard entry {entry!r}")
        return
    if "://" in e:
        sp = urlsplit(e)
        if not sp.hostname:
            raise ScopeError(f"invalid URL entry {entry!r}: no host")
        return
    # bare host, host:port, host/path, or CIDR
    if "/" in e and not e.startswith("*"):
        host, _, suffix = e.partition("/")
        try:
            ipaddress.ip_network(e, strict=False)
            return
        except ValueError:
            if suffix.isdigit():
                raise ScopeError(f"invalid CIDR in scope entry {entry!r}")
        # host/path form
        if not host or not suffix:
            raise ScopeError(f"invalid scope entry {entry!r}")
    hostpart = e.split("/", 1)[0]
    if hostpart.count(":") == 1:
        host, _, port = hostpart.rpartition(":")
        if not port.isdigit() or not 0 < int(port) < 65536:
            raise ScopeError(f"invalid port in scope entry {entry!r}")
        hostpart = host
    if not hostpart or hostpart == "." or hostpart.startswith("."):
        raise ScopeError(f"invalid scope entry {entry!r}")
    if " " in hostpart:
        raise ScopeError(f"invalid scope entry {entry!r}: whitespace in host")


def validate(scope: dict) -> None:
    """Validate the whole authority before it is written."""
    for key in ("in_scope", "out_of_scope"):
        for entry in scope.get(key, []):
            _validate_entry(entry)
    rules = scope.get("rules", {})
    rps = rules.get("max_rate_rps")
    if rps is not None:
        try:
            rps = float(rps)
        except (TypeError, ValueError) as e:
            raise ScopeError("rules.max_rate_rps must be a number") from e
        if rps < 0 or rps > 10000:
            raise ScopeError("rules.max_rate_rps must be between 0 and 10000")


def load_scope(file: str | os.PathLike | None = None) -> dict | None:
    f = scope_path(file)
    if not f.exists():
        return None
    try:
        raw = json.loads(f.read_text())
    except Exception as e:
        raise ScopeError(f"scope file {f} is not valid JSON: {e}") from e
    return _normalize(raw)


def save_scope(scope: dict, file: str | os.PathLike | None = None,
               force: bool = False) -> Path:
    f = scope_path(file)
    if f.exists() and not force:
        raise ScopeError(f"scope authority already exists at {f} (use --force to replace)")
    scope = _normalize(scope)
    validate(scope)
    scope["schema"] = SCHEMA
    scope["updated"] = now_iso()
    scope.setdefault("created", scope["updated"])
    f.parent.mkdir(parents=True, exist_ok=True)
    tmp = f.with_suffix(f.suffix + f".tmp.{os.getpid()}")
    tmp.write_text(json.dumps(scope, indent=2, sort_keys=False) + "\n")
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    os.replace(tmp, f)
    return f


def update_scope(mutator, file: str | os.PathLike | None = None) -> dict:
    """Atomic read-modify-write of the scope authority."""
    with _LOCK:
        scope = load_scope(file)
        if scope is None:
            raise ScopeError("no scope authority — run: spydermonkey scope init")
        mutator(scope)
        save_scope(scope, file, force=True)
        return scope


# ── matching ─────────────────────────────────────────────────────────────────

def _host_path(value: str) -> tuple[str, str, int | None]:
    """Return (host, path, port) for a URL, host[:port], or domain."""
    v = (value or "").strip().lower()
    if not v:
        return "", "", None
    if "://" in v:
        sp = urlsplit(v)
        host = (sp.hostname or "").strip("[]")
        try:
            port = sp.port
        except ValueError:
            port = None
        return host, sp.path or "/", port
    # bare host[:port], possibly with a path
    if "/" in v:
        v, path = v.split("/", 1)
        path = "/" + path
    else:
        path = "/"
    if v.startswith("["):                      # [::1]:8080
        host, _, rest = v.partition("]")
        host = host.lstrip("[")
        port = int(rest[1:]) if rest.startswith(":") and rest[1:].isdigit() else None
        return host, path, port
    port = None
    if v.count(":") == 1:
        h, p = v.rsplit(":", 1)
        if p.isdigit():
            host, port = h, int(p)
        else:
            host = v
    else:
        host = v
    return host.strip("[]"), path, port


def _is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def _entry_match(entry: str, value: str) -> bool:
    """Does one scope entry cover the value? Used for allow and deny lists."""
    e = entry.strip().lower()
    if not e:
        return False
    if e in ("*", "all"):
        return True
    v_host, v_path, v_port = _host_path(value)
    e_host, e_path, e_port = _host_path(e)
    if not v_host or not e_host:
        return False

    # CIDR entry
    if "/" in e and not e.startswith("*") and "://" not in e:
        try:
            net = ipaddress.ip_network(e, strict=False)
        except ValueError:
            net = None
        if net is not None:
            try:
                return ipaddress.ip_address(v_host) in net
            except ValueError:
                return False

    # port constraint, when declared
    if e_port is not None and v_port != e_port:
        return False

    # Path constraint: an entry that declares a deeper path only covers that
    # subtree. This applies to URLs and to the bare "host/path" form.
    if e_path not in ("", "/"):
        if not (v_path == e_path or v_path.startswith(e_path.rstrip("/") + "/")):
            return False

    if e_host.startswith("*."):
        base = e_host[2:]
        return v_host.endswith("." + base) and v_host != base
    if _is_ip(e_host):
        return v_host == e_host
    return v_host == e_host or v_host.endswith("." + e_host)


def match(scope: dict | None, value: str) -> tuple[bool, str]:
    """Return (in_scope, reason). A None scope matches nothing except lab."""
    if scope is None:
        return False, "no scope authority"
    if _expired(scope):
        return False, f"scope authority expired at {scope.get('expires')}"
    for entry in scope.get("out_of_scope", []):
        if _entry_match(entry, value):
            return False, f"denied by out_of_scope entry '{entry}'"
    for entry in scope.get("in_scope", []):
        if _entry_match(entry, value):
            return True, f"matched in_scope entry '{entry}'"
    return False, "not in the declared estate"


def _expired(scope: dict) -> bool:
    exp = scope.get("expires")
    if not exp:
        return False
    try:
        dt = datetime.fromisoformat(str(exp).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return datetime.now(timezone.utc) > dt
    except ValueError:
        # A malformed expiry must not silently open the estate.
        return True


def is_lab(value: str) -> bool:
    host, _, _ = _host_path(value)
    return host in ("127.0.0.1", "localhost", "::1", "0.0.0.0")


def check(value: str, file: str | os.PathLike | None = None,
          strict: bool = False, audit: bool = False,
          allow_lab: bool = True) -> tuple[bool, str, dict | None]:
    """The full verdict. Lab hosts pass when allow_lab is true."""
    try:
        scope = load_scope(file)
    except ScopeError as e:
        return False, str(e), None
    if allow_lab and is_lab(value) \
            and (scope is None or scope.get("rules", {}).get("allow_lab", True) is not False):
        reason = "lab target (localhost is always lab-legal)"
        if audit:
            _audit(value, True, reason, scope, file)
        return True, reason, scope
    if scope is None:
        ok, reason = (False, "no scope authority (default-deny with --strict)") if strict \
            else (False, "no scope authority")
        if audit:
            _audit(value, ok, reason, None, file)
        return ok, reason, None
    ok, reason = match(scope, value)
    if audit:
        _audit(value, ok, reason, scope, file)
    return ok, reason, scope


def gate(value: str, file: str | os.PathLike | None = None,
         quiet: bool = True) -> bool:
    """Boolean gate used by live-probing code paths."""
    ok, reason, _ = check(value, file=file, strict=True, audit=not quiet,
                          allow_lab=True)
    if not ok and not quiet:
        import sys
        print(f"✗ LIVE-FIRE REFUSED — {value}: {reason}", file=sys.stderr)
        print("  init one: spydermonkey scope init --engagement E --in-scope <host,CIDR>",
              file=sys.stderr)
    return ok


def rate_wait(file: str | os.PathLike | None = None) -> None:
    """Honor rules.max_rate_rps between live requests (process-wide)."""
    try:
        scope = load_scope(file)
    except ScopeError:
        return
    if not scope:
        return
    try:
        rps = float(scope.get("rules", {}).get("max_rate_rps", 0) or 0)
    except (TypeError, ValueError):
        return
    if rps <= 0:
        return
    interval = 1.0 / rps
    with _LOCK:
        import time
        delta = time.time() - _LAST["at"]
        if delta < interval:
            time.sleep(interval - delta)
        _LAST["at"] = time.time()


# ── audit ────────────────────────────────────────────────────────────────────

def _audit(value: str, ok: bool, reason: str, scope: dict | None,
           file: str | os.PathLike | None) -> None:
    f = audit_path(file)
    row = {
        "at": now_iso(),
        "engagement": (scope or {}).get("engagement", "none"),
        "value": value[:500],
        "verdict": "IN" if ok else "OUT",
        "reason": reason[:300],
    }
    try:
        f.parent.mkdir(parents=True, exist_ok=True)
        with _AUDIT_LOCK:
            with f.open("a") as fh:
                fh.write(json.dumps(row) + "\n")
        os.chmod(f, 0o600)
    except OSError:
        pass


def history(limit: int = 40, file: str | os.PathLike | None = None) -> list[dict]:
    f = audit_path(file)
    if not f.exists():
        return []
    rows = []
    for line in f.read_text(errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    return rows[-limit:]


# ── presentation helpers ─────────────────────────────────────────────────────

def summary(scope: dict) -> dict:
    allow_all = any(str(e).strip().lower() in ("*", "all")
                    for e in scope.get("in_scope", []))
    return {
        "schema": scope.get("schema", 1),
        "engagement": scope.get("engagement", "?"),
        "in_scope": len(scope.get("in_scope", [])),
        "out_of_scope": len(scope.get("out_of_scope", [])),
        "rules": scope.get("rules", {}),
        "expires": scope.get("expires"),
        "expired": _expired(scope),
        "allow_all": allow_all,
        "created": scope.get("created"),
        "updated": scope.get("updated"),
    }
