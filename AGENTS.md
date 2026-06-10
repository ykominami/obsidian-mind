# Obsidian Mind

This vault is built for [Claude Code](https://claude.ai/code) with a full operating manual in `CLAUDE.md`.

**Read `CLAUDE.md` for all vault conventions** — structure, note types, linking rules, frontmatter schemas, indexes, and workflows. Most of the content is agent-agnostic.

## Hooks

The hook scripts in `.claude/scripts/` are agent-agnostic TypeScript and shell, executed natively by Node via `--experimental-strip-types` — no build step, no runtime dependencies, no Claude SDK. Hook configs are provided for three agents:

| Agent | Config | Status |
|-------|--------|--------|
| Claude Code | `.claude/settings.json` | Full support |
| Codex CLI | `.codex/hooks.json` | Shared hook scripts |
| Gemini CLI | `.gemini/settings.json` | Shared hook scripts |

| Script | Purpose | Claude event | Codex event | Gemini event |
|--------|---------|--------------|-------------|--------------|
| `session-start.ts` | Inject vault context at startup | SessionStart | SessionStart | SessionStart |
| `classify-message.ts` | Classify messages, inject routing hints | UserPromptSubmit | UserPromptSubmit | BeforeAgent |
| `validate-write.ts` | Validate frontmatter and wikilinks | PostToolUse | PostToolUse | AfterTool |
| `pre-compact.ts` | Back up transcript before compaction | PreCompact | — | PreCompress |

## Commands

18 commands in `.claude/commands/` — agent-agnostic markdown with YAML frontmatter.

- **Claude Code / Gemini CLI**: invoke as `/om-standup`, `/om-dump`, etc.
- **Codex CLI**: type the command name as a regular prompt without the `/` prefix (e.g. `om-standup`). Codex will find and execute the command file.

## Memory

The vault's memory lives in `brain/` — `Memories.md`, `Patterns.md`, `Key Decisions.md`, `Gotchas.md`. These are plain markdown files that any agent can read and write. When you learn something worth remembering, write it to the relevant `brain/` topic note with a wikilink to context.

The `~/.claude/` auto-loaded memory index is Claude Code-specific — skip that section in `CLAUDE.md`. The vault-side `brain/` notes are the source of truth.

## Subagents

9 subagents in `.claude/agents/` handle isolated tasks (brag spotting, vault auditing, cross-linking, etc.). The prompt content is agent-agnostic markdown. Codex CLI (`.codex/agents/`) and Gemini CLI (`.gemini/agents/`) support the same pattern — copy the files and adapt the YAML frontmatter fields to your agent's schema.

## What's Claude Code-specific

Only the `~/.claude/` auto-memory loader is truly Claude Code-specific. Everything else — hooks, commands, subagent prompts, vault memory — is portable.

## Setup

**Codex CLI**: Reads `AGENTS.md` natively. For direct access to `CLAUDE.md`, add to `~/.codex/config.toml`:
```toml
project_doc_fallback_filenames = ["CLAUDE.md"]
```

**Gemini CLI**: Reads `GEMINI.md` natively. For direct access to `CLAUDE.md`, add to `~/.gemini/settings.json`:
```json
{ "context": { "fileName": ["GEMINI.md", "CLAUDE.md"] } }
```

**Other agents** (Cursor, Windsurf, Copilot): Read `AGENTS.md` for vault conventions. Hook support varies by agent.

For more information, see the [README](README.md).

<!-- BEGIN BEADS INTEGRATION v:1 profile:full hash:0a1bbe8a -->
## Issue Tracking with bd (beads)

**IMPORTANT**: This project uses **bd (beads)** for ALL issue tracking. Do NOT use markdown TODOs, task lists, or other tracking methods.

### Why bd?

- Dependency-aware: Track blockers and relationships between issues
- Git-friendly: Dolt-powered version control with native sync
- Agent-optimized: JSON output, ready work detection, discovered-from links
- Prevents duplicate tracking systems and confusion

### Quick Start

**Check for ready work:**

```bash
bd ready --json
```

**Create new issues:**

```bash
bd create "Issue title" --description="Detailed context" -t bug|feature|task -p 0-4 --json
bd create "Issue title" --description="What this issue is about" -p 1 --deps discovered-from:bd-123 --json
```

**Claim and update:**

```bash
bd update <id> --claim --json
bd update bd-42 --priority 1 --json
```

**Complete work:**

```bash
bd close bd-42 --reason "Completed" --json
```

### Issue Types

- `bug` - Something broken
- `feature` - New functionality
- `task` - Work item (tests, docs, refactoring)
- `epic` - Large feature with subtasks
- `chore` - Maintenance (dependencies, tooling)

### Priorities

- `0` - Critical (security, data loss, broken builds)
- `1` - High (major features, important bugs)
- `2` - Medium (default, nice-to-have)
- `3` - Low (polish, optimization)
- `4` - Backlog (future ideas)

### Workflow for AI Agents

1. **Check ready work**: `bd ready` shows unblocked issues
2. **Claim your task atomically**: `bd update <id> --claim`
3. **Work on it**: Implement, test, document
4. **Discover new work?** Create linked issue:
   - `bd create "Found bug" --description="Details about what was found" -p 1 --deps discovered-from:<parent-id>`
5. **Complete**: `bd close <id> --reason "Done"`

### Quality
- Use `--acceptance` and `--design` fields when creating issues
- Use `--validate` to check description completeness

### Lifecycle
- `bd defer <id>` / `bd supersede <id>` for issue management
- `bd stale` / `bd orphans` / `bd lint` for hygiene
- `bd human <id>` to flag for human decisions
- `bd formula list` / `bd mol pour <name>` for structured workflows

### Auto-Sync

bd automatically syncs via Dolt:

- Each write auto-commits to Dolt history
- No manual export/import needed!

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

### Important Rules

- ✅ Use bd for ALL task tracking
- ✅ Always use `--json` flag for programmatic use
- ✅ Link discovered work with `discovered-from` dependencies
- ✅ Check `bd ready` before asking "what should I work on?"
- ❌ Do NOT create markdown TODO lists
- ❌ Do NOT use external issue trackers
- ❌ Do NOT duplicate tracking systems

For more details, see README.md and docs/QUICKSTART.md.

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds

<!-- END BEADS INTEGRATION -->

<!-- BEGIN BEADS CODEX SETUP: generated by bd setup codex -->
## Beads Issue Tracker

Use Beads (`bd`) for durable task tracking in repositories that include it. Use the `beads` skill at `.agents/skills/beads/SKILL.md` (project install) or `~/.agents/skills/beads/SKILL.md` (global install) for Beads workflow guidance, then use the `bd` CLI for issue operations.

### Quick Reference

```bash
bd ready                # Find available work
bd show <id>            # View issue details
bd update <id> --claim  # Claim work
bd close <id>           # Complete work
bd prime                # Refresh Beads context
```

### Rules

- Use `bd` for all task tracking; do not create markdown TODO lists.
- Run `bd prime` when Beads context is missing or stale.
- Keep persistent project memory in Beads via `bd remember`; do not create ad hoc memory files.
<!-- END BEADS CODEX SETUP -->


<!-- headroom:rtk-instructions -->
# RTK (Rust Token Killer) - Token-Optimized Commands

When running shell commands, **always prefix with `rtk`**. This reduces context
usage by 60-90% with zero behavior change. If rtk has no filter for a command,
it passes through unchanged — so it is always safe to use.

## Key Commands
```bash
# Git (59-80% savings)
rtk git status          rtk git diff            rtk git log

# Files & Search (60-75% savings)
rtk ls <path>           rtk read <file>         rtk grep <pattern>
rtk find <pattern>      rtk diff <file>

# Test (90-99% savings) — shows failures only
rtk pytest tests/       rtk cargo test          rtk test <cmd>

# Build & Lint (80-90% savings) — shows errors only
rtk tsc                 rtk lint                rtk cargo build
rtk prettier --check    rtk mypy                rtk ruff check

# Analysis (70-90% savings)
rtk err <cmd>           rtk log <file>          rtk json <file>
rtk summary <cmd>       rtk deps                rtk env

# GitHub (26-87% savings)
rtk gh pr view <n>      rtk gh run list         rtk gh issue list

# Infrastructure (85% savings)
rtk docker ps           rtk kubectl get         rtk docker logs <c>

# Package managers (70-90% savings)
rtk pip list            rtk pnpm install        rtk npm run <script>
```

## Rules
- In command chains, prefix each segment: `rtk git add . && rtk git commit -m "msg"`
- For debugging, use raw command without rtk prefix
- `rtk proxy <cmd>` runs command without filtering but tracks usage
<!-- /headroom:rtk-instructions -->
