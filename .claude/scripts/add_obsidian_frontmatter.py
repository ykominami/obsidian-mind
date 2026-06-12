"""
Adds standard Obsidian frontmatter (date, description, tags) to Kindle clipping files.
Preserves existing kindle-* fields unchanged.

Date format: ISO 8601 with time (YYYY-MM-DDT00:00:00.000Z) — matches Obsidian's
internal representation so Obsidian won't reformat the field on open.
"""

import re
import sys
from pathlib import Path

CLIPPINGS_DIR = Path(__file__).parents[2] / "Clippings-Kindle"
DEFAULT_DATE = "2026-06-03T00:00:00.000Z"
MAX_DESC_LEN = 148

# Matches a plain YYYY-MM-DD date (not already ISO with time)
_DATE_PLAIN_RE = re.compile(r"^(date:\s+)(\d{4}-\d{2}-\d{2})$", re.MULTILINE)


def _to_iso(date_str: str) -> str:
    """'2026-06-03' → '2026-06-03T00:00:00.000Z'"""
    return f"{date_str}T00:00:00.000Z"


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


def _write_lf(path: Path, content: str) -> None:
    """Write with LF line endings to prevent CRLF diffs from Obsidian."""
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def process_file(path: Path, dry_run: bool = False) -> str:
    content = path.read_text(encoding="utf-8")
    # Normalize to LF for consistent processing
    content = content.replace("\r\n", "\n")

    data, close_idx = parse_frontmatter(content)
    if close_idx == -1:
        return f"SKIP (no frontmatter): {path.name}"

    if "date" in data and "description" in data:
        # Already has standard fields — check if date needs ISO upgrade
        date_val = str(data.get("date", ""))
        if "T" in date_val:
            # Already ISO format; still normalize CRLF
            if not dry_run:
                _write_lf(path, content)
            return f"SKIP (already ISO): {path.name}"

        # date is YYYY-MM-DD — upgrade to ISO in-place (first occurrence only)
        new_content = _DATE_PLAIN_RE.sub(
            lambda m: m.group(1) + _to_iso(m.group(2)),
            content,
            count=1,
        )
        if not dry_run:
            _write_lf(path, new_content)
        return f"DATE FIXED: {path.name}"

    # No standard fields yet — insert them
    title = data.get("kindle-title", path.stem)
    highlights = data.get("kindle-highlightsCount", 0)
    raw_date = str(data.get("kindle-lastAnnotatedDate", "Invalid date")).strip()

    date_str = DEFAULT_DATE
    if raw_date not in ("Invalid date", "", "None", "null"):
        import datetime
        for fmt in ("%Y-%m-%d", "%B %d, %Y", "%d/%m/%Y"):
            try:
                parsed = datetime.datetime.strptime(raw_date, fmt)
                date_str = _to_iso(parsed.strftime("%Y-%m-%d"))
                break
            except ValueError:
                continue

    description = build_description(title, highlights)
    description = description.replace('"', '\\"')

    new_fields = (
        f"date: {date_str}\n"
        f'description: "{description}"\n'
        "tags:\n"
        "  - kindle\n"
        "  - clipping"
    )

    lines = content.splitlines(keepends=True)
    lines.insert(close_idx, new_fields + "\n")
    new_content = "".join(lines)

    if not dry_run:
        _write_lf(path, new_content)
    return f"UPDATED: {path.name}"


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== DRY RUN ===")

    files = sorted(CLIPPINGS_DIR.glob("*.md"))
    updated = fixed = skipped = errors = 0
    for f in files:
        try:
            result = process_file(f, dry_run=dry_run)
            print(result)
            if result.startswith("UPDATED"):
                updated += 1
            elif result.startswith("DATE FIXED"):
                fixed += 1
            elif result.startswith("SKIP"):
                skipped += 1
        except Exception as e:
            print(f"ERROR: {f.name} — {e}")
            errors += 1

    prefix = "DRY RUN " if dry_run else ""
    print(
        f"\n{prefix}Done: {updated} inserted, {fixed} date-fixed, "
        f"{skipped} skipped, {errors} errors"
    )


if __name__ == "__main__":
    main()
