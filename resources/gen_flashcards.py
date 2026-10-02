#!/usr/bin/env python3
"""Generate SRS flashcards page + data from glossary markdown files.
Usage: python gen_flashcards.py <docs-root> <output-dir>
Reads docs-root/GLOSSARY/*.md (excluding README/_/template), extracts each term's
front title + "short version" first paragraph as the card front/back, and writes:
  <output-dir>/flashcards/index.html   (the interactive SRS page)
  <output-dir>/flashcards/flashcards.json  (the deck data)
"""
import os, re, json, sys, html

def slug_title_from_md(path):
    """Return (title, blurb) — title from first # heading, blurb from first paragraph."""
    text = open(path, encoding='utf-8').read()
    title = None
    m = re.search(r'^#\s+(.+)$', text, re.M)
    if m: title = m.group(1).strip()
    # first non-empty paragraph after the frontmatter/heading (skip the "> Back to glossary")
    lines = text.splitlines()
    para = []
    started = False
    for ln in lines:
        s = ln.strip()
        if s.startswith('#') and not started:
            started = True; continue
        if not started: continue
        if s.startswith('>'): continue
        if s.startswith('<!--'): continue
        if not s:
            if para: break
            continue
        if s.startswith('#') and para: break
        para.append(s)
        if len(' '.join(para)) > 400: break
    return title, ' '.join(para)

def gen(gloss_dir, out_dir):
    cards = []
    for fn in sorted(os.listdir(gloss_dir)):
        if not fn.endswith('.md'): continue
        if fn in ('README.md', '_template.md', '_ANNOTATION.md', '_TERMS.md'): continue
        t, b = slug_title_from_md(os.path.join(gloss_dir, fn))
        if not t or not b: continue
        cards.append({'front': t, 'back': b})
    os.makedirs(os.path.join(out_dir, 'flashcards'), exist_ok=True)
    # write data
    data_path = os.path.join(out_dir, 'flashcards', 'flashcards.json')
    open(data_path, 'w', encoding='utf-8').write(json.dumps(cards, ensure_ascii=False))
    # build the HTML page
    title = os.path.basename(os.path.dirname(out_dir)).replace('-', ' ').title()
    items = '\n'.join(
        f'<div class="card" data-f="{html.escape(c["front"],quote=True)}" data-b="{html.escape(c["back"],quote=True)}"></div>'
        for c in cards
    )
    page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flashcards — {html.escape(title)} · sektor9.dev</title>
<style>
:root{{--fg:#e2e8f0;--muted:#94a3b8;--accent:#6366f1;--card:#1e293b;--bg:#0b1220}}
body{{font-family:Segoe UI,Arial,sans-serif;background:var(--bg);color:var(--fg);margin:0;padding:0}}
.wrap{{max-width:640px;margin:0 auto;padding:40px 20px;text-align:center}}
h1{{font-size:1.8rem;color:#fff;margin:0 0 4px}}
.sub{{color:var(--muted);margin:0 0 24px;font-size:.9rem}}
.stats{{font-size:.8rem;color:var(--muted);margin-bottom:16px}}
.flash{{background:var(--card);border:1px solid #334155;border-radius:16px;min-height:240px;display:flex;align-items:center;justify-content:center;padding:30px;margin:0 0 16px;cursor:pointer;user-select:none;transition:transform .12s;font-size:1.15rem;line-height:1.5}}
.flash:hover{{transform:scale(1.01)}}
.flash .back{{color:#c7d2fe;display:none}}
.flash.show .front{{display:none}}
.flash.show .back{{display:block}}
.btns{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:20px}}
button{{font:inherit;padding:10px 18px;border-radius:10px;border:1px solid #334155;background:#1e293b;color:#e2e8f0;cursor:pointer;transition:background .15s}}
button:hover{{background:#273449}}
button.hard{{background:#7f1d1d;border-color:#991b1b}}
button.good{{background:#14532d;border-color:#166534}}
button.easy{{background:#1e3a8a;border-color:#1d4ed8}}
a.back{{display:inline-block;margin-top:10px;color:var(--accent);font-size:.85rem}}
</style></head><body><div class="wrap">
<h1>🧠 Flashcards — {html.escape(title)}</h1>
<p class="sub">Spaced-repetition review of the glossary terms · click a card to flip · rate yourself</p>
<p class="stats" id="stats"></p>
<div class="flash" id="flash"><div class="front"></div><div class="back"></div></div>
<div class="btns">
  <button class="hard" id="hard">Again</button>
  <button class="good" id="good">Good</button>
  <button class="easy" id="easy">Easy</button>
</div>
<div id="deck"></div>
<p><a class="back" href="/">← Back</a></p>
</div>
<script>
const CARDS = {json.dumps(cards, ensure_ascii=False)};
// spaced-repetition: simple Leitner boxes persisted in localStorage
const LS='sektor9-srs-v1';
let boxes=JSON.parse(localStorage.getItem(LS)||'{{}}');
let idx=0, deck=[];
function buildDeck(){{
  deck=[];
  for(let i=0;i<CARDS.length;i++){{let b=boxes[i]||0; for(let j=0;j<=b;j++) deck.push(i);}}
  shuffle(deck);
}}
function shuffle(a){{for(let i=a.length-1;i>0;i--){{let j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]];}}}}
function render(){{
  if(!deck.length) buildDeck();
  if(idx>=deck.length){{ document.getElementById('flash').innerHTML='<div>🎉 Deck complete! <button onclick="restart()">Review again</button></div>'; document.getElementById('stats').textContent='done'; return; }}
  let ci=deck[idx];
  let f=document.getElementById('flash');
  f.classList.remove('show');
  f.querySelector('.front').textContent=CARDS[ci].front;
  f.querySelector('.back').textContent=CARDS[ci].back;
  let due=Object.values(boxes).reduce((a,b)=>a+Math.min(b,1),0);
  let mastered=Object.values(boxes).filter(b=>b>=5).length;
  document.getElementById('stats').textContent=cardCount+' terms · '+deck.length+' cards · mastered '+mastered;
}}
function rate(step){{if(idx>=deck.length)return; let ci=deck[idx]; boxes[ci]=Math.max(0,Math.min(8,(boxes[ci]||0)+step)); localStorage.setItem(LS,JSON.stringify(boxes)); idx++; render();}}
function restart(){{idx=0; buildDeck(); render();}}
document.getElementById('flash').addEventListener('click',()=>{{document.getElementById('flash').classList.toggle('show');}});
document.getElementById('hard').onclick=()=>rate(-2);
document.getElementById('good').onclick=()=>rate(1);
document.getElementById('easy').onclick=()=>rate(3);
const cardCount=CARDS.length;
buildDeck(); render();
</script></body></html>"""
    open(os.path.join(out_dir, 'flashcards', 'index.html'), 'w', encoding='utf-8').write(page)
    print(f"Wrote {len(cards)} flashcards -> {out_dir}/flashcards/")

if __name__ == '__main__':
    gen(sys.argv[1], sys.argv[2])
