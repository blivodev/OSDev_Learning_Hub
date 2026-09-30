#!/usr/bin/env python3
"""Verify all glossary tooltip links in OSDev_Learning_Hub resolve to real pages."""
import os, re

HUB = r"D:/Projects/OSDev_Learning_Hub"
os.chdir(HUB)
GLOSS = os.path.abspath("GLOSSARY")

# glossary term slugs (files directly in GLOSSARY, not underscore/support, not README)
slugs = set(f[:-3] for f in os.listdir(GLOSS)
            if f.endswith(".md") and not f.startswith("_") and f != "README.md")

# gather docs, excluding vendored dirs and glossary support files
docs = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "Cosmos", "blog_os", "node_modules", "target")]
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            base = os.path.basename(p)
            # skip the runtime support/contract files we used internally
            if base in ("_template.md", "_TERMS.md", "_ANNOTATION.md"):
                continue
            docs.append(p)

def resolve(doc, linkpath):
    return os.path.abspath(os.path.join(os.path.dirname(doc), linkpath))

broken = []
total = 0
by_doc = {}
for doc in docs:
    text = open(doc, encoding="utf-8").read()
    for m in re.finditer(r"\[([^\[\]]+)\]\(([^()]+\.md)(?:\s+\"[^\"]*\")?\)", text):
        href = m.group(2).strip()
        if "GLOSSARY" not in href and "/GLOSSARY/" not in href:
            continue
        total += 1
        by_doc.setdefault(os.path.normpath(doc), []).append(href)
        resolved = resolve(doc, href)
        if not os.path.isfile(resolved):
            broken.append((doc, href, resolved))

print("glossary links checked:", total)
print("docs containing glossary links:", len(by_doc))
print("BROKEN (target file missing):", len(broken))
for b in broken:
    print("   ", b[0], "->", b[1], "=>", b[2])

# Which term slugs are never used as links from the 29 content docs?
content_docs = [d for d in docs if not os.path.normpath(d).startswith(os.path.normpath("GLOSSARY"))]
all_text = "\n".join(open(d, encoding="utf-8").read() for d in content_docs)
used_slugs = set(re.findall(r"/?GLOSSARY/([A-Za-z0-9\-]+)\.md", all_text))
unused = sorted(slugs - used_slugs)
print("\nterm pages never linked from content docs:", len(unused))
for u in unused:
    print("   ", u)

# List which content docs have links, for the report
print("\nPer-doc link counts:")
for d in sorted(by_doc):
    print(f"   {d}: {len(by_doc[d])}")
