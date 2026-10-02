import json, re
from pathlib import Path

ROOT = Path(r"D:/Projects/OSDev_Learning_Hub/resources")
fixmap = json.loads((ROOT / 'archive_fix_map_v3.json').read_text(encoding='utf-8'))
print('v3 fix map entries:', len(fixmap))

manifest = json.loads((ROOT / 'v3_import_manifest.json').read_text(encoding='utf-8'))

def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

# build title->good_url from fixmap
title_to_url = {}
for iid, info in fixmap.items():
    if iid == 'en':
        continue
    t = (info.get('title') or '').lower().strip()
    if t:
        title_to_url[t] = info.get('good_url') or f'https://archive.org/details/{iid}'

fixed = 0
for m in manifest:
    key = m['book'].lower().strip()
    url = title_to_url.get(key)
    if not url:
        continue
    html = m['pages'][0]['html']
    new_html = re.sub(
        r'<a href="[^"]+"[^>]*>📖 Open on archive.org</a>',
        f'<a href="{esc(url)}" target="_blank" rel="noopener" class="button">📖 Open the book</a>',
        html
    )
    if new_html != html:
        m['pages'][0]['html'] = new_html
        fixed += 1

print('URLs fixed from checker:', fixed)
Path(ROOT / 'v3_import_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
print('saved updated v3 manifest')
