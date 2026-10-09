#!/usr/bin/env python3
"""sektor9 admin service — central administration page.

Runs on VPS1 (where Caddy lives). Provides:
  GET  /                -> the admin SPA (admin.html)
  GET  /api/overview    -> service health + counts (all hosts)
  GET  /api/users       -> list basic-auth users per service
  POST /api/users/add   -> add a user to a service's auth
  POST /api/users/remove-> remove a user from a service's auth
  GET  /api/logs        -> recent logs (caddy / run-service / etc.)

Auth: the whole site sits behind Caddy basic-auth (osdev). No extra login.
Security: only the whitelisted services below can be modified; user names are
validated; hashes are generated with bcrypt via htpasswd.
"""
import json, os, re, subprocess, time, urllib.request
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
import uvicorn

APP_DIR = os.path.dirname(os.path.abspath(__file__))
CADDYFILE = os.environ.get("CADDYFILE", "/opt/osdev/Caddyfile")

app = FastAPI(title="sektor9-admin")

# ---- service registry: what we can inspect/manage ----
# "auth" = how users are stored for that service.
SERVICES = {
    "wiki":       {"url": "https://wiki.sektor9.dev",       "kind": "caddy",  "desc": "BookStack wiki"},
    "osdev":      {"url": "https://osdev.sektor9.dev",      "kind": "htpasswd","desc": "OS Dev docs"},
    "elecdocs":   {"url": "https://elecdocs.sektor9.dev",   "kind": "htpasswd","desc": "Electronics docs"},
    "electro":    {"url": "https://electro.sektor9.dev",    "kind": "htpasswd","desc": "Electronics hub"},
    "docs":       {"url": "https://docs.sektor9.dev",       "kind": "htpasswd","desc": "Docs portal"},
    "books":      {"url": "https://books.sektor9.dev",      "kind": "htpasswd","desc": "Book library"},
    "ide":        {"url": "https://ide.sektor9.dev",        "kind": "caddy",  "desc": "Browser IDE"},
    "vnc":        {"url": "https://vnc.sektor9.dev",        "kind": "caddy",  "desc": "VGA display"},
    "run":        {"url": "https://run.sektor9.dev",        "kind": "caddy",  "desc": "Kernel run service"},
}

# htpasswd files live on cPanel; we reach them via SSH.
CPANEL_SSH = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8",
              "-p", "22", "-i", os.path.expanduser("~/.ssh/id_rsa"),
              "user@example.com"]
HTPASSWD_PATHS = {
    "osdev":    "/home/USER/os/.htpasswd",
    "elecdocs": "/home/USER/elec/.htpasswd",
    "electro":  "/home/USER/electronhub/.htpasswd",
    "docs":     "/home/USER/public_html/docs/.htpasswd",
    "books":    "/home/USER/books/downloads/.htpasswd",
}


def sh(cmd, timeout=20):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except Exception as e:
        return 1, "", str(e)


def check_http(url, timeout=8):
    """Return (status_code, ms) for a URL, cache-busted."""
    t0 = time.time()
    try:
        req = urllib.request.Request(url + ("&" if "?" in url else "?") + "cb=%d" % int(t0),
                                     method="GET")
        try:
            r = urllib.request.urlopen(req, timeout=timeout)
            code = r.status
        except urllib.error.HTTPError as e:
            code = e.code
        return code, int((time.time()-t0)*1000)
    except Exception:
        return 0, int((time.time()-t0)*1000)


@app.get("/")
def index():
    return FileResponse(os.path.join(APP_DIR, "admin.html"))


@app.get("/api/overview")
def overview():
    svcs = []
    for key, meta in SERVICES.items():
        code, ms = check_http(meta["url"])
        if code in (200, 302, 308):
            health = "up"
        elif code in (401, 403):
            health = "protected"      # auth prompt = up
        elif code == 0:
            health = "down"
        else:
            health = "warn"
        svcs.append({"key": key, "desc": meta["desc"], "url": meta["url"],
                     "code": code, "ms": ms, "health": health})

    # book count from the library API (metadata only)
    books = None
    try:
        r = urllib.request.urlopen("https://books.sektor9.dev/api/books.php", timeout=8)
        books = json.load(r).get("total")
    except Exception:
        pass

    # wiki stats from BookStack API (public metadata via /api/*)
    wiki = None
    try:
        r = urllib.request.urlopen("https://wiki.sektor9.dev/api/docs.json", timeout=8)
        d = json.load(r)
        wiki = len(d.get("docs", []))
    except Exception:
        pass

    return {"services": svcs, "books": books, "wiki_pages": wiki,
            "ts": int(time.time())}


# ---- user management ----
def _caddy_users():
    """Parse basicauth users per site from the Caddyfile."""
    out = {}
    try:
        txt = open(CADDYFILE).read()
    except Exception:
        return out
    # crude but effective: find 'site {  ... basicauth { user "hash" ... } ... }'
    for m in re.finditer(r'([a-z0-9.-]+\.sektor9\.dev)\s*\{', txt):
        site = m.group(1)
        tail = txt[m.end():m.end()+2000]
        bu = re.search(r'basicauth\s*\{([^}]*)\}', tail)
        if bu:
            users = re.findall(r'^\s*([A-Za-z0-9._-]+)\s+"', bu.group(1), re.M)
            out[site] = users
    return out


@app.get("/api/users")
def list_users():
    caddy = _caddy_users()
    result = {}
    # caddy-backed services
    for key, meta in SERVICES.items():
        if meta["kind"] != "caddy":
            continue
        site = meta["url"].replace("https://", "")
        result[key] = {"kind": "caddy", "users": caddy.get(site, [])}
    # htpasswd-backed services (read via SSH)
    for key, path in HTPASSWD_PATHS.items():
        rc, out, err = sh(CPANEL_SSH + ["cat " + path])
        users = [l.split(":", 1)[0] for l in out.splitlines() if ":" in l]
        result[key] = {"kind": "htpasswd", "users": users, "path": path,
                       "error": None if rc == 0 else err.strip()}
    return result


def _gen_hash(password):
    rc, out, err = sh(["htpasswd", "-nbB", "x", password])
    if rc == 0 and ":" in out:
        return out.split(":", 1)[1].strip()
    # fallback: openssl
    rc, out, err = sh(["openssl", "passwd", "-apr1", password])
    return out.strip() if rc == 0 else None


@app.post("/api/users/add")
async def add_user(req: Request):
    b = await req.json()
    service = b.get("service", "")
    user = (b.get("user") or "").strip()
    password = b.get("password") or ""
    if service not in SERVICES:
        raise HTTPException(400, "Unknown service")
    if not re.fullmatch(r'[A-Za-z0-9._-]{2,32}', user):
        raise HTTPException(400, "Invalid username (2-32 chars: letters, digits, . _ -)")
    if len(password) < 8:
        raise HTTPException(400, "Password must be at least 8 characters")

    h = _gen_hash(password)
    if not h:
        raise HTTPException(500, "Could not generate password hash (htpasswd/openssl missing)")

    kind = SERVICES[service]["kind"]
    if kind == "htpasswd":
        path = HTPASSWD_PATHS.get(service)
        if not path:
            raise HTTPException(400, "No htpasswd path for service")
        # remove any existing line for this user, then append
        cmd = (f"grep -v '^{user}:' {path} > {path}.tmp 2>/dev/null; "
               f"echo '{user}:{h}' >> {path}.tmp && mv {path}.tmp {path} && chmod 644 {path}")
        rc, out, err = sh(CPANEL_SSH + [cmd])
        if rc != 0:
            raise HTTPException(500, "Failed to update htpasswd: " + err)
        return {"ok": True, "service": service, "user": user, "kind": "htpasswd"}

    # caddy: we can't safely rewrite Caddyfile from here without a reload helper;
    # return the hash + instructions (safer than blind edits on a live proxy)
    return {"ok": False, "manual": True, "hash": h,
            "note": "Caddy-backed: add this line to the basicauth block in "
                    "/opt/osdev/Caddyfile, then reload Caddy.",
            "line": f'{user} "{h}"'}


@app.post("/api/users/remove")
async def remove_user(req: Request):
    b = await req.json()
    service = b.get("service", ""); user = (b.get("user") or "").strip()
    if service not in SERVICES:
        raise HTTPException(400, "Unknown service")
    if not re.fullmatch(r'[A-Za-z0-9._-]{2,32}', user):
        raise HTTPException(400, "Invalid username")
    kind = SERVICES[service]["kind"]
    if kind == "htpasswd":
        path = HTPASSWD_PATHS.get(service)
        cmd = f"grep -v '^{user}:' {path} > {path}.tmp 2>/dev/null; mv {path}.tmp {path}; chmod 644 {path}"
        rc, out, err = sh(CPANEL_SSH + [cmd])
        if rc != 0:
            raise HTTPException(500, "Failed: " + err)
        return {"ok": True, "service": service, "user": user}
    raise HTTPException(400, "Removing users from Caddy services must be done in the Caddyfile")


@app.get("/api/logs")
def logs(source: str = "caddy", lines: int = 120):
    lines = max(10, min(int(lines), 500))
    if source == "caddy":
        rc, out, err = sh(["docker", "logs", "--tail", str(lines), "caddy"])
        return {"source": "caddy (VPS1)", "lines": (out + err).splitlines()[-lines:]}
    if source == "run":
        rc, out, err = sh(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "runvps",
                           f"journalctl -u run-service -n {lines} --no-pager"])
        return {"source": "run-service (runvps)", "lines": out.splitlines()}
    if source == "fail2ban":
        rc, out, err = sh(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "runvps",
                           f"fail2ban-client status sshd 2>/dev/null | tail -{lines}"])
        return {"source": "fail2ban (runvps)", "lines": out.splitlines()}
    raise HTTPException(400, "Unknown log source")


if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get("HOST", "127.0.0.1"),
                port=int(os.environ.get("PORT", "8100")))
