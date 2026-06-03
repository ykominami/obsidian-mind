---
date: 2026-05-28
description: "Gemini API MCP サーバー追加コマンドと Claude Code スキル追加手順"
tags:
  - reference
  - mcp
  - gemini
---

# Gemini API — MCP & スキル設定

## MCP サーバー追加

```bash
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

## スキル追加

```bash
# 基本スキル（ほとんどの Gemini API 開発に対応）
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global

# Google Cloud / Vertex AI 経由で Gemini を使う場合
npx skills add google-gemini/gemini-skills --skill vertex-ai-api-dev --global

# リアルタイム会話アプリ開発を行う場合は追加
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global

# エージェント開発（Interactions API）を行う場合は追加
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

## 関連

- [[brain/Patterns]] — Claude Code 活用パターン
- [[Claude活用-Cherny5段階フレームワーク]]
