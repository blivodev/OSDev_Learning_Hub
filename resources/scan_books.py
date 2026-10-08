import json, concurrent.futures, urllib.request, os, sys

PROG = r"D:/Projects/OSDev_Learning_Hub/resources/scan_results.json"
URLS = r"D:/Projects/OSDev_Learning_Hub/resources/dl_urls.json"

done = json.load(open(PROG, encoding='utf-8')) if os.path.exists(PROG) else {}
with open(URLS, encoding='utf-8') as f:
    urls = json.load(f)

todo = [u for u in urls if u not in done]
print(f"resume: done={len(done)} todo={len(todo)}", flush=True)

def check(url):
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            clen = r.headers.get('Content-Length')
            return (url, 'ok', int(clen) if clen else 0)
    except urllib.error.HTTPError as e:
        return (url, f'http{e.code}', 0)
    except Exception:
        return (url, 'err', 0)

# Process in chunks of 300, saving after each chunk so progress survives
for i in range(0, len(todo), 300):
    chunk = todo[i:i+300]
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        for r in ex.map(check, chunk):
            results.append(r)
    for u, st, sz in results:
        done[u] = {"s": st, "b": sz}
    with open(PROG, 'w', encoding='utf-8') as f:
        json.dump(done, f)
    ok = [v for v in done.values() if v["s"]=="ok"]
    print(f"progress {len(done)}/{len(urls)} ok={len(ok)} ok_gb={sum(v['b'] for v in ok)/1e9:.2f}", flush=True)

print("SCAN COMPLETE", flush=True)
