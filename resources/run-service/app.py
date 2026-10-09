#!/usr/bin/env python3
"""run-service — Level-3 "Run" API for the OSDev tutorials.

Accepts an edited C kernel source, compiles + boots it inside a locked-down
Docker sandbox (non-root, no network, cpu/mem/time limits), and returns the
QEMU serial output ("Hello World!").

Endpoints:
    GET  /health          -> {"ok": true}
    POST /run             -> {"ok": bool, "output": str, "duration_ms": int}

Security (guests allowed):
  - runs in a disposable container: --rm, --network none, --read-only root
  - --memory 256m --cpus 1 --pids-limit 64
  - hard wall-clock timeout (SANDBOX_TIMEOUT) on the container
  - per-IP rate limiting (token bucket)
  - only the C kernel is compiled; source size capped
"""
import json
import os
import shutil
import subprocess
import tempfile
import time
import threading
from collections import defaultdict, deque

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, "template")   # boot.s, linker.ld, Makefile
RUNNER_SCRIPT = os.path.join(APP_DIR, "run_kernel.sh")
IMAGE = os.environ.get("RUNNER_IMAGE", "osdev-runner:latest")

SANDBOX_TIMEOUT = int(os.environ.get("SANDBOX_TIMEOUT", "20"))   # seconds (compile+boot)
MAX_SOURCE_BYTES = int(os.environ.get("MAX_SOURCE_BYTES", "65536"))  # 64 KB
RATE_LIMIT = int(os.environ.get("RATE_LIMIT", "10"))     # requests
RATE_WINDOW = int(os.environ.get("RATE_WINDOW", "60"))   # per N seconds
MAX_CONCURRENT = int(os.environ.get("MAX_CONCURRENT", "3"))

app = FastAPI(title="osdev-run-service")

# --- rate limiting (in-memory token bucket per IP) ---
_hits = defaultdict(deque)
_lock = threading.Lock()
_sem = threading.Semaphore(MAX_CONCURRENT)

def rate_ok(ip: str) -> bool:
    now = time.time()
    with _lock:
        q = _hits[ip]
        while q and now - q[0] > RATE_WINDOW:
            q.popleft()
        if len(q) >= RATE_LIMIT:
            return False
        q.append(now)
        return True


@app.get("/health")
def health():
    return {"ok": True, "image": IMAGE}


@app.post("/run")
async def run(req: Request):
    ip = req.client.host if req.client else "unknown"
    if not rate_ok(ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded — slow down.")

    body = await req.json()
    source = body.get("source", "")
    filename = os.path.basename(body.get("filename", "kernel.c")) or "kernel.c"

    if not isinstance(source, str) or not source.strip():
        raise HTTPException(status_code=400, detail="No source provided.")
    if len(source.encode("utf-8")) > MAX_SOURCE_BYTES:
        raise HTTPException(status_code=413, detail="Source too large (max 64 KB).")
    if not filename.endswith((".c", ".h", ".c++", ".cpp")):
        filename = "kernel.c"

    if not _sem.acquire(blocking=False):
        raise HTTPException(status_code=503, detail="Server busy — try again shortly.")

    workdir = tempfile.mkdtemp(prefix="run-")
    t0 = time.time()
    try:
        # 1. lay down the template (boot.s, linker.ld, Makefile) + the user's source
        for f in ("boot.s", "linker.ld", "Makefile"):
            src = os.path.join(TEMPLATE_DIR, f)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(workdir, f))
        with open(os.path.join(workdir, filename), "w", encoding="utf-8") as fh:
            fh.write(source)
        # The template Makefile expects kernel.c; if the user used another name, alias it.
        if filename != "kernel.c":
            shutil.copy2(os.path.join(workdir, filename), os.path.join(workdir, "kernel.c"))

        # The container runs as non-root 'runner' (uid 1000); make the mount writable.
        os.chmod(workdir, 0o777)
        for f in os.listdir(workdir):
            try:
                os.chmod(os.path.join(workdir, f), 0o666)
            except OSError:
                pass

        # 2. run the sandbox container
        cmd = [
            "docker", "run", "--rm",
            "--network", "none",
            "--memory", "256m",
            "--cpus", "1",
            "--pids-limit", "64",
            "--read-only",
            "--tmpfs", "/tmp:size=32m",
            "-v", f"{workdir}:/work:rw",
            "-v", f"{RUNNER_SCRIPT}:/run_kernel.sh:ro",
            "--entrypoint", "/bin/bash",
            IMAGE, "/run_kernel.sh",
        ]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True,
                                  timeout=SANDBOX_TIMEOUT)
            output = (proc.stdout or "") + (proc.stderr or "")
        except subprocess.TimeoutExpired as e:
            output = (e.stdout or "") if isinstance(e.stdout, str) else ""
            output += "\n=== SANDBOX TIMEOUT (killed after %ds) ===" % SANDBOX_TIMEOUT
            return JSONResponse({"ok": False, "output": output.strip(),
                                 "duration_ms": int((time.time()-t0)*1000)})

        # 3. keep only the interesting part (from COMPILE onward), cap size
        out = output.strip()
        if len(out) > 20000:
            out = out[:10000] + "\n... [truncated] ...\n" + out[-8000:]
        return {"ok": proc.returncode == 0, "output": out,
                "duration_ms": int((time.time()-t0)*1000)}
    finally:
        _sem.release()
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get("HOST", "127.0.0.1"),
                port=int(os.environ.get("PORT", "8099")))
