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


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

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
