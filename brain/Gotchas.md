---
date: 2026-05-06
description: "Things that have bitten before and will bite again — pitfalls, edge cases, and testing traps"
tags:
  - brain
---

# Gotchas

Things that have bitten before and will bite again.

## PostToolUse フックが vault 外の `.md` 編集にも発火する

`validate-write` フックはパスの制限なしに全 `.md` 編集を監視する。`C:/Users/ykomi/wiki/` などの Obsidian vault 外のファイルを編集すると「フロントマター欠損」の偽陽性警告が出る。

**対処**: フックの validate-write スクリプトにパスフィルタを追加し、vault ルート外の編集はスキップする（または `.claude/settings.json` の allowlist で対象ファイルパスを限定する）。詳細は [[Skills]] 参照。
