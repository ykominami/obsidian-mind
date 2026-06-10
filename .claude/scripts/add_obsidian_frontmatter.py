"""
Adds standard Obsidian frontmatter (date, description, tags) to Kindle clipping files.
Preserves existing kindle-* fields unchanged.
"""

import re
import sys
from pathlib import Path

CLIPPINGS_DIR = Path(__file__).parents[2] / "Clippings-Kindle"
DEFAULT_DATE = "2026-06-03"  # bulk import date
MAX_DESC_LEN = 148


def parse_frontmatter(content: str) -> tuple[dict, int]:
    """Return (fields dict, line index of closing ---).
    Returns ({}, -1) if no valid frontmatter found."""
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, -1
    close_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close_idx = i
            break
    if close_idx == -1:
        return {}, -1

    # Parse YAML block (safely — only reads, never writes back with pyyaml)
    import yaml
    yaml_block = "\n".join(lines[1:close_idx])
    try:
        data = yaml.safe_load(yaml_block) or {}
    except yaml.YAMLError:
        data = {}
    return data, close_idx


def build_description(title: str, highlights: int) -> str:
    title = str(title).strip()
    desc = f"Kindle {highlights}件ハイライト: {title}"
    if len(desc) > MAX_DESC_LEN:
        cut = MAX_DESC_LEN - 3
        desc = desc[:cut] + "..."
    return desc


def process_file(path: Path, dry_run: bool = False) -> str:
    content = path.read_text(encoding="utf-8")
    data, close_idx = parse_frontmatter(content)
    if close_idx == -1:
        return f"SKIP (no frontmatter): {path.name}"

    # Already has standard fields?
    if "date" in data and "description" in data:
        return f"SKIP (already updated): {path.name}"

    title = data.get("kindle-title", path.stem)
    highlights = data.get("kindle-highlightsCount", 0)
    raw_date = str(data.get("kindle-lastAnnotatedDate", "Invalid date")).strip()

    # Parse date
    date_str = DEFAULT_DATE
    if raw_date not in ("Invalid date", "", "None", "null"):
        # Try common formats
        import datetime
        for fmt in ("%Y-%m-%d", "%B %d, %Y", "%d/%m/%Y"):
            try:
                date_str = datetime.datetime.strptime(raw_date, fmt).strftime("%Y-%m-%d")
                break
            except ValueError:
                continue

    description = build_description(title, highlights)
    # Escape quotes in description
    description = description.replace('"', '\\"')

    new_fields = (
        f'date: {date_str}\n'
        f'description: "{description}"\n'
        'tags:\n'
        '  - kindle\n'
        '  - clipping'
    )

    # Insert before closing ---
    lines = content.splitlines(keepends=True)
    closing_line = lines[close_idx]
    lines.insert(close_idx, new_fields + "\n")

    new_content = "".join(lines)

    if not dry_run:
        path.write_text(new_content, encoding="utf-8")
    return f"UPDATED: {path.name}"


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== DRY RUN ===")

    files = sorted(CLIPPINGS_DIR.glob("*.md"))
    updated = skipped = errors = 0
    for f in files:
        try:
            result = process_file(f, dry_run=dry_run)
            print(result)
            if result.startswith("UPDATED"):
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"ERROR: {f.name} — {e}")
            errors += 1

    print(f"\n{'DRY RUN ' if dry_run else ''}Done: {updated} updated, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
