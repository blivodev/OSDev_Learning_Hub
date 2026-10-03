import json, re
from pathlib import Path

ROOT = Path(r"D:/Projects/OSDev_Learning_Hub/resources")
v5 = json.loads((ROOT / 'books_v5.json').read_text(encoding='utf-8'))
print("v5 books:", len(v5))


def classify(title):
    t = title.lower()
    ELEC = re.compile(r'(arduino|esp|raspberry|microcontroller|circuit|electronics|electrical|embedded|robot|sensor|mcu|avr|fpga|pcb|iot|wireless|power|oscilloscope|radio|transistor|integrated circuit|digital logic|microprocessor|signal|vhdl|verilog|stm32|pico|motor|op.?amp|telecommunication|automation|control|converter|induction|voltage|electric|amplifier|semiconductor|logic|analog|antenna|microwave|instrumentation|mechatronics)', re.I)
    return 'Electronics' if ELEC.search(t) else 'OSDev'


def diff(t):
    t = t.lower()
    if re.search(r'(introduction|intro|beginner|basics|fundamentals|first|101|guide|getting started|overview|what you need|easy|simple|tutorial|dummies|made simple|just the steps|teach yourself)', t): return 'Beginner'
    if re.search(r'(advanced|expert|internals|design|implementation|from scratch|under the hood|deep|professional|optimiz|research|proceedings|conference|international|theoretical|studies|super|reference manual|complete)', t): return 'Advanced'
    if re.search(r'(kernel|compiler|architecture|systems|programming|embedded|microcontroller|network|security|concurrent|database|real.?time|parallel|distributed|maintenance|administration|technical|circuit|device|semiconductor|firmware|parsing|graphics|vision|robotics|control|sensor|protocol|registry|mastering)', t): return 'Hard'
    return 'Intermediate'


def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


SHELF_OS = "OS Development"
SHELF_EL = "Electronics & Microcontrollers"
manifest = []
for b in v5:
    iid = b['id']
    title = b['title']
    shelf = SHELF_OS if classify(title) == 'OSDev' else SHELF_EL
    d = diff(title)
    url = f"https://archive.org/details/{iid}"  # details page default; checker will improve
    html = f"<h2>{esc(title)}</h2>"
    html += f'<p><img src="{esc(b["cover"])}" alt="Cover" style="max-width:220px;border-radius:8px"></p>'
    html += "<p><strong>Read it here:</strong></p>"
    html += f'<p><a href="{esc(url)}" target="_blank" rel="noopener" class="button">📖 Open on archive.org</a></p>'
    html += f'<p><em>Added to the sektor9.dev learning library · difficulty: {esc(d)} · <strong>{shelf}</strong>.</em></p>'
    manifest.append({'shelf': shelf, 'book': title, 'difficulty': d, 'cover': b['cover'],
                     'pages': [{'name': 'Overview & access', 'html': html}]})

Path(ROOT / 'v5_import_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
from collections import Counter
print("v5 import manifest:", len(manifest))
print("shelves:", dict(Counter(m['shelf'] for m in manifest)))
print("difficulty:", dict(Counter(m['difficulty'] for m in manifest)))
