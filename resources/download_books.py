#!/usr/bin/env python3
"""Download the book library to cPanel. Resumable, parallel, robust.
Run on server: python3 download_books.py /home/USER/books/download_manifest.txt <workers> <logfile>
"""
import os, sys, subprocess, concurrent.futures, time

MANIFEST = sys.argv[1] if len(sys.argv) > 1 else "/home/USER/books/download_manifest.txt"
WORKERS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
LOGFILE = sys.argv[3] if len(sys.argv) > 3 else "/home/USER/books/download.log"
DL = sys.argv[4] if len(sys.argv) > 4 else "/home/USER/books/downloads"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"

os.makedirs(DL, exist_ok=True)

def load_manifest(path):
    items = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                items.append((parts[0].strip(), parts[1].strip()))
    return items

def download_one(item):
    file, url = item
    dest = os.path.join(DL, file)
    if os.path.isfile(dest) and os.path.getsize(dest) > 0:
        return f"SKIP {file}"
    tmp = dest + ".tmp"
    cmd = ["wget", "-q", "-c", "-L", "-T", "90", "-t", "5", "-U", UA, "-O", tmp, url]
    try:
        r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
        if r.returncode == 0 and os.path.isfile(tmp) and os.path.getsize(tmp) > 0:
            os.replace(tmp, dest)
            return f"OK {file}"
        if os.path.exists(tmp):
            os.remove(tmp)
        return f"FAIL {file}"
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        return f"FAIL {file}"

def main():
    items = load_manifest(MANIFEST)
    total = len(items)
    print(f"Starting download of {total} files with {WORKERS} workers -> {LOGFILE}", flush=True)
    start = time.time()
    with open(LOGFILE, "a") as lf:
        lf.write(f"\n--- run started {time.strftime('%Y-%m-%d %H:%M:%S')} files={total} workers={WORKERS}\n")
    ok = skip = fail = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for res in ex.map(download_one, items):
            with open(LOGFILE, "a") as lf:
                lf.write(res + "\n")
            if res.startswith("OK"): ok += 1
            elif res.startswith("SKIP"): skip += 1
            else: fail += 1
            if (ok + skip + fail) % 100 == 0:
                print(f"  progress {ok+skip+fail}/{total} ok={ok} skip={skip} fail={fail} elapsed={int(time.time()-start)}s", flush=True)
    with open(LOGFILE, "a") as lf:
        lf.write(f"DONE ok={ok} skip={skip} fail={fail} total={total}\n")
    print(f"DONE ok={ok} skip={skip} fail={fail} total={total}", flush=True)

if __name__ == "__main__":
    main()
