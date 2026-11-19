#!/usr/bin/env python3
"""Regenerate meeting-notes/index.json from the front matter of meeting-notes/*.md.

Each note starts with:
---
title: Weekly sync
date: 2026-11-18
time: 10:00 GMT-08:00   (optional)
attendees: Name, Name
---
Run:  python3 scripts/build-meeting-index.py
"""
import json, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent / "meeting-notes"
items = []
for p in sorted(root.glob("*.md")):
    if p.name.lower() == "readme.md":
        continue
    text = p.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    items.append({
        "file": p.name,
        "title": meta.get("title", p.stem),
        "date": meta.get("date", ""),
        "time": meta.get("time", ""),
        "attendees": meta.get("attendees", ""),
    })
items.sort(key=lambda i: (i["date"], i["time"]), reverse=True)
(root / "index.json").write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8")
print(f"{len(items)} note(s) indexed")
