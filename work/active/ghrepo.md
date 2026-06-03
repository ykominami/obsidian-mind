---
date: 2026-04-10
description: Githubリポジトリ管理システム-Pythonパッケージ
project: ghrepo
status: active
quarter: Q2-2026
tags:
  - work-note
---

# ghrepo

## Context

GitHub リポジトリ管理 CLI。`gh repo list` でリポジトリ一覧を取得・スナップショット管理する。

## Architecture

```
CLIエントリーポイント (main)
    └─ Clix (引数定義)
    └─ Ghrepo (ディスパッチ + 実行)
           ├─ CommandSetup  → setup サブコマンド
           ├─ CommandList   → list / fix サブコマンド
           └─ CommandSearch → search サブコマンド
```

**レイヤー構成**

| レイヤー | クラス/ファイル | 役割 |
|----------|----------------|------|
| エントリーポイント | `ghrepo.py` / `Ghrepo` | Clix で引数パース → クラスメソッドへディスパッチ（インスタンス化なし） |
| CLI定義 | `clix.py` / `Clix` | argparse サブパーサー定義のみ、ロジックなし |
| コマンド実行 | `CommandList` / `CommandSearch` / `CommandSetup` | `yklibpy.command.Command` を継承、クラスメソッドで実装 |
| 設定・ストレージ | `AppConfigx` + `yklibpy.AppStore/Storex` | YAML読み書きは yklibpy に委譲（snapshot.yaml のみ直書き） |

**データフロー（list サブコマンド）**

```
gh repo list (外部コマンド) → JSON
→ CommandList.get_all_repos() ← management fields付与
→ CommandList.save_snapshot()
    ├─ snapshots/<id>/snapshot.yaml
    ├─ snapshots.yaml（追記）
    └─ repos.yaml（マージ更新）
→ --output JSON ファイル出力
```

**主要な型**: `RepoItem = dict[str, Any]` / `RepoAssoc = dict[str, RepoItem]`（command_list.py と command_search.py に意図的重複定義）

**yklibpy 依存**: AppStore・Storex・AppConfig・Cli・Command・CommandGhUser・Loggerx

## Notes

## Action Items
- [ ]

## Related
- [[North Star]]
- [[yklibpy]]
