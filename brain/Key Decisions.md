---
date: 2026-05-10
description: "Architectural and workflow decisions worth recalling across sessions — each links to its source work note"
tags:
  - brain
---

# Key Decisions

Architectural or workflow decisions worth recalling. Link to the full [[Decision Record]] when one exists.

## 2026-04

- **Kiro仕様書駆動開発を cpiconfiles で採用（2026-04-25）** — 実装前に Kiro で要求定義（実装言語・機能仕様）を先行作成してから実装に入るワークフローを確立。AI駆動開発において「仕様書を先行させる」ことで実装の手戻りを減らす。証跡: git `7ccc716`, [[icon-file-group-manager-要件定義書]]
- **llm-wiki を TECS 仕様書作成の主要ツールに採用（2026-04-24）** — 87 HTML ソースから wiki ページを自動生成する pipeline を確立。NotebookLM / 手動作成より自動化・再現性を優先する判断。証跡: git commit around `87c59c2`, [[reference/03-Resources/my-topic/CLAUDE|TECS Wiki]]
