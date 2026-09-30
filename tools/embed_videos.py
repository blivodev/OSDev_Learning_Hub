#!/usr/bin/env python3
"""Embed YouTube videos inline in OSDev_Learning_Hub docs.

Converts `- [Title](https://www.youtube.com/watch?v=ID) — caption` bullets under a
"Watch and learn"/"Video resources" heading into an inline embedded <details> block
using the privacy-enhanced youtube-nocookie.com domain. MkDocs/Material renders the
raw HTML (pymdownx + Material allow it), so the video plays on the page instead of
opening a new tab. Each video is collapsed behind a "▶ Watch & learn" toggle to keep
the page clean.

Run from the HUB root: python embed_videos.py wet
"""
import os, re, sys

YOUTUBE_RE = re.compile(
    r"\[([^\]]+)\]\(https?://(?:www\.)?(?:youtube\.com|youtu\.be)/(?:watch\?v=|embed/|shorts/)?([A-Za-z0-9_-]{6,20})(?:&[^)]*)?\)(?: —\s*([^)\n]*))?"
)
WATCH_HEADER = re.compile(r"^## Watch and learn\s*$", re.M | re.I)
VIDEO_HEADER = re.compile(r"^## Video resources\s*$", re.I)

def embed_video(title, vid, caption):
    cap = (caption or "").strip()
    cc = f"<p class=video-caption>{cap}</p>" if cap else ""
    return (
        "<details class=\"video-embed\">\n"
        f"<summary>▶ Watch: {title}</summary>\n"
        f"<iframe src=\"https://www.youtube-nocookie.com/embed/{vid}\" "
        "title=\"" + title.replace('"', '&quot;') + "\" width=\"100%\" height=\"400\" "
        "style=\"border:0;border-radius:8px;\" allow=\"accelerometer; autoplay; clipboard-write; "
        "encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>\n"
        + ((cc + "\n") if cc else "") +
        "</details>"
    )

def process(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if "youtube-nocookie.com/embed" in text:
        return 0, 0  # already processed
    # Find each video bullet line and replace it with the embed block.
    count = 0
    def repl(m):
        nonlocal count
        count += 1
        return embed_video(m.group(1), m.group(2), m.group(3))
    new, n = YOUTUBE_RE.subn(repl, text)
    if n == 0:
        return 0, 0
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    return n, count

def main(root=None, which="wet"):
    docs = []
    if not root:
        root = r"D:\Projects\OSDev_Learning_Hub"
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "Cosmos", "blog_os", "target", "GLOSSARY")]
        for fn in filenames:
            if fn.endswith(".md"):
                p = os.path.join(dirpath, fn)
                t = open(p, encoding="utf-8").read()
                if YOUTUBE_RE.search(t) and not ("youtube-nocookie.com/embed" in t):
                    p_abs = os.path.abspath(p)
                    docs.append(p_abs)
    total = 0
    changed = []
    for p in docs:
        n, _ = process(p)
        if n:
            changed.append((os.path.relpath(p, root), n))
            total += n
    print(f"Files with embedded videos: {len(changed)}, total video embeds: {total}")
    for rel, n in sorted(changed):
        print(f"  {rel}: {n}")
    return changed

if __name__ == "__main__":
    main()
