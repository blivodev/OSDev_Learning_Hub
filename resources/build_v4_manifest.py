import json, re
from pathlib import Path

ROOT = Path(r"D:/Projects/OSDev_Learning_Hub/resources")
v4 = json.loads((ROOT / 'books_v4.json').read_text(encoding='utf-8'))
fixmap = json.loads((ROOT / 'archive_fix_map_v4.json').read_text(encoding='utf-8'))
print("v4 books:", len(v4))


def classify(title):
    t = title.lower()
    ELEC = re.compile(r'(arduino|esp|raspberry|microcontroller|circuit|electronics|electrical|embedded|robot|sensor|mcu|avr|fpga|pcb|iot|wireless|power|oscilloscope|radio|transistor|integrated circuit|digital logic|microprocessor|signal|vhdl|verilog|stm32|pico|motor|op.?amp|telecommunication|automation|control|converter|induction|voltage|electric|amplifier|semiconductor|logic|analog)', re.I)
    return 'Electronics' if ELEC.search(t) else 'OSDev'


def diff(t):
    t = t.lower()
    if re.search(r'(introduction|intro|beginner|basics|fundamentals|first|101|guide|getting started|overview|what you need|easy|simple|tutorial)', t): return 'Beginner'
    if re.search(r'(advanced|expert|internals|design|implementation|from scratch|under the hood|deep|professional|optimiz|research|proceedings|conference|international|theoretical|studies|super)', t): return 'Advanced'
    if re.search(r'(kernel|compiler|architecture|systems|programming|embedded|microcontroller|network|security|concurrent|database|real.?time|parallel|distributed|maintenance|administration|technical|circuit|device|semiconductor|firmware|parsing|graphics|vision|robotics|control|sensor|protocol)', t): return 'Hard'
    return 'Intermediate'


def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


# title -> good_url from fixmap
title_to_url = {}
for iid, info in fixmap.items():
    if iid == 'en':
        continue
    t = (info.get('title') or '').lower().strip()
    if t:
        title_to_url[t] = info.get('good_url') or f'https://archive.org/details/{iid}'

SHELF_OS = "OS Development"
SHELF_EL = "Electronics & Microcontrollers"
manifest = []
for b in v4:
    iid = b['id']
    title = b['title']
    shelf = SHELF_OS if classify(title) == 'OSDev' else SHELF_EL
    d = diff(title)
    url = title_to_url.get(title.lower().strip(), f'https://archive.org/details/{iid}')
    html = f"<h2>{esc(title)}</h2>"
    html += f'<p><img src="{esc(b["cover"])}" alt="Cover" style="max-width:220px;border-radius:8px"></p>'
    html += "<p><strong>Read it here:</strong></p>"
    html += f'<p><a href="{esc(url)}" target="_blank" rel="noopener" class="button">📖 Open the book</a></p>'
    html += f'<p><em>Added to the sektor9.dev learning library · difficulty: {esc(d)} · <strong>{shelf}</strong>.</em></p>'
    manifest.append({'shelf': shelf, 'book': title, 'difficulty': d, 'cover': b['cover'],
                     'pages': [{'name': 'Overview & access', 'html': html}]})

Path(ROOT / 'v4_import_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
from collections import Counter
print("v4 import manifest:", len(manifest))
print("shelves:", dict(Counter(m['shelf'] for m in manifest)))
print("difficulty:", dict(Counter(m['difficulty'] for m in manifest)))
print("with fixed URL:", sum(1 for m in manifest if 'archive.org/details' not in m['pages'][0]['html']))
