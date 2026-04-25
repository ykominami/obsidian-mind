---
date: 2026-04-25
description: "Vault-specific workflows and slash commands — reusable patterns for review prep, project tracking, and vault maintenance"
tags:
  - brain
  - index
---

# Skills

Custom slash commands, subagents, and reusable workflows. Defined in `.claude/commands/` and `.claude/agents/`.

## Slash Commands

### Daily Workflow

| Command | Purpose |
|---------|---------|
| `/standup` | Morning kickoff — load context, review yesterday, surface tasks, identify priorities |
| `/dump` | Freeform capture — dump anything, gets routed to the right notes automatically |
| `/wrap-up` | Full session review — verify notes, indexes, links, suggest improvements. Auto-triggered on "wrap up". |

### Editing & Synthesis

| Command | Purpose |
|---------|---------|
| `/humanize` | Voice-calibrated editing — makes Claude-drafted text sound like you wrote it |
| `/weekly` | Weekly synthesis — cross-session patterns, North Star alignment, uncaptured wins |

### Capture & Documentation

| Command | Purpose |
|---------|---------|
| `/capture-1on1` | Capture 1:1 meeting transcript into structured vault note with quotes, action items, DM context |
| `/incident-capture` | Capture incident from Slack channels/DMs into structured vault notes — timeline, people, analysis, brag entry |
| `/slack-scan` | Deep scan Slack channels/DMs for evidence — extracts timestamped touchpoints, organizes by context |

### Performance & Review

| Command | Purpose |
|---------|---------|
| `/peer-scan` | Deep scan a peer's GitHub PRs for review prep — produces structured analysis saved to `perf/evidence/` |
| `/review-brief` | Generate review brief (manager or peer version) from vault data |
| `/self-review` | Write self-assessment for review tool — projects, competencies, principles |
| `/review-peer` | Write peer review — projects, principles, performance summary |

### Vault Maintenance

| Command | Purpose |
|---------|---------|
| `/vault-audit` | Deep structural audit — indexes, frontmatter, links, Bases, folder placement, stale context |
| `/vault-upgrade` | Import content from an existing vault — detects version, classifies notes, transforms frontmatter, rebuilds indexes |
| `/project-archive` | Move completed project from `work/active/` to `work/archive/YYYY/`, update all indexes |

## Usage Notes

**Daily:**
- `/standup` replaces the manual session start — reads North Star, active work, tasks, git log
- `/dump` processes freeform text and routes each piece to the correct note type and folder
- `/wrap-up` is auto-triggered when you say "wrap up" — runs full session review

**Editing & Synthesis:**
- `/humanize` calibrates against your actual writing samples, not a word blacklist. Detects context from frontmatter (review → corporate-confident, incident → precise, 1:1 → conversational). Run after drafting any note to make it sound human.
- `/weekly` bridges standup and review brief — run at end of week for cross-session patterns, North Star drift, and uncaptured wins. Output is transient by default; offer to promote findings to brag doc or North Star.

**Capture:**
- `/capture-1on1` handles transcripts, raw notes, or summaries
- `/incident-capture` takes Slack URLs and produces structured incident documentation
- `/slack-scan` should be run AFTER `/peer-scan` to add context beyond code (leadership, communication, collaboration evidence)

**Performance:**
- `/peer-scan` works best when launched as parallel agents (one per person)
- `/review-brief` needs the private brief to exist first — it generates filtered versions from it

**Maintenance:**
- `/vault-audit` should be run at the end of substantial sessions — catches stale indexes and mixed context
- `/vault-upgrade` imports content from an existing vault (older obsidian-mind or any Obsidian vault). Detects version, classifies notes, transforms frontmatter, fixes wikilinks, rebuilds indexes. Use `--dry-run` to preview.
- `/project-archive` handles the active/ → archive/ move with index updates

## Subagents

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `brag-spotter` | Proactively finds uncaptured wins and competency gaps | `/wrap-up`, `/weekly` |
| `context-loader` | Loads all vault context about a person, project, incident, or concept | Direct — "load context on X" |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks across the vault | `/vault-audit` |
| `people-profiler` | Bulk create/update person notes from Slack profiles | `/incident-capture` |
| `review-prep` | Aggregates all performance evidence for a given review period | `/review-brief` |
| `slack-archaeologist` | Full Slack reconstruction — reads every message, thread, profile, produces unified timeline | `/incident-capture` |
| `vault-librarian` | Deep vault maintenance — orphan detection, broken links, frontmatter validation, stale notes | `/vault-audit` |
| `review-fact-checker` | Verify every claim in a review draft against vault sources | `/self-review`, `/review-peer` |
| `vault-migrator` | Classify, transform, and migrate content from a source vault | `/vault-upgrade` |

Subagents run in isolated context windows via `.claude/agents/`. They don't pollute the main conversation.

## Hooks

| Hook | When | What |
|------|------|------|
| SessionStart | On startup/resume | QMD re-index, inject North Star, active work, recent changes, tasks, file listing |
| UserPromptSubmit | Every message | Classify content (decision, incident, 1:1, win, architecture, person, project update) and inject routing hints |
| PreToolUse (Write/Edit) | Before file writes | Validate frontmatter, check for wikilinks, verify folder placement |
| PreCompact | Before context compaction | Back up session transcript to `thinking/session-logs/` |
| Stop | End of session | Checklist: archive, update indexes, check orphans |

## LLM Wiki (`llm-wiki:wiki`)

Obsidian vault 内に永続的な知識ベースを構築・管理するスキル。

| コマンド | 説明 |
|----------|------|
| `init <name>` | 新しい wiki を作成 |
| `ingest <path\|url>` | ソース（ファイルまたは URL）を取り込む |
| `compile [<path>]` | raw ソースから wiki ページを生成 |
| `query <question>` | wiki に対して質問し回答を得る |
| `lint` | wiki の整合性チェックと修正 |

現在 `03-Resources/my-topic/` に TECS wiki を運用中。詳細は [[03-Resources/my-topic/CLAUDE]] 参照。

## Semantic Search (QMD)

If QMD is installed (`npm install -g @tobilu/qmd`), the vault has semantic search:

- `qmd query "..."` — hybrid BM25 + vector + LLM reranking (best quality)
- `qmd search "..."` — fast BM25 keyword search
- `qmd vsearch "..."` — semantic vector search (exploratory)
- `qmd update && qmd embed` — refresh index after bulk changes

SessionStart hook runs `qmd update` automatically. See `.claude/skills/qmd/SKILL.md` for full reference.

## Workflow: Weekly Review

1. **`/weekly`** — synthesize the week's activity, check alignment, find patterns
2. Promote any uncaptured wins to brag doc
3. Update North Star if focus shifted
4. **`/wrap-up`** — close the session cleanly

## Workflow: Full Review Cycle Prep

1. **`/review-brief manager`** — generate the manager context transfer doc
2. **`/review-brief peers`** — generate the peer context transfer doc
3. **`/peer-scan`** (parallel, one per peer) — deep scan each peer's PRs
4. **`/slack-scan`** — scan relevant channels for your own evidence + peer context
5. **`/capture-1on1`** — capture the review 1:1 with your manager
6. **`/vault-audit`** — tidy up after all the new data

## Workflow: Project Ramp-Up

1. **`/slack-scan`** — scan project channels for history and decisions
2. **`/peer-scan`** (if needed) — understand what teammates have already built
3. Create work note from gathered context
4. **`/vault-audit`** — ensure everything links properly

## 関連

- [[North Star]] — 現在のフォーカスと目標
- [[Patterns]] — 繰り返し発見されたワークフローパターン
- [[Memories]] — 記憶トピック一覧
