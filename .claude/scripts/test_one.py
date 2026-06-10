import sys, yaml
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

target = Path("Clippings-Kindle/Donovan-Kernighan-Go Programming Language, The.md")
content = target.read_text(encoding="utf-8")
lines = content.splitlines()
close_idx = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
data = yaml.safe_load("\n".join(lines[1:close_idx])) or {}
title = data.get("kindle-title", "")
highlights = data.get("kindle-highlightsCount", 0)
desc = f"Kindle {highlights}件ハイライト: {title}"
if len(desc) > 148:
    desc = desc[:145] + "..."
print("TITLE:", title)
print("HIGHLIGHTS:", highlights)
print("DESC:", desc)
print("LEN:", len(desc))

new_fields = f'date: 2026-06-03\ndescription: "{desc}"\ntags:\n  - kindle\n  - clipping'
lines2 = list(content.splitlines(keepends=True))
lines2.insert(close_idx, new_fields + "\n")
print("\n--- Preview first 18 lines ---")
print("".join(lines2[:18]))
