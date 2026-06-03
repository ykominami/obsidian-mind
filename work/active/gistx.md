---
date: 2026-04-10
description: Gist管理システム-Pythonパッケージ
project: gistx
status: active
quarter: Q2-2026
tags:
  - work-note
---

# gistx

## Context

GitHub Gist 管理 CLI。`gh gist list` でGistをクローン・管理する。

## Architecture

```
gistx (CLI)
  └─ mainx() [gistx.py]
       └─ Clix.parse_args() [clix.py]
            └─ args.func(args) → Gistx クラスメソッドへ委譲

mainx()
  ├─ Gistx.setup(args)    → CommandSetup(appstore).run()
  ├─ Gistx.clone(args)    → CommandClone(appstore).run(args, repo_kind)
  └─ Gistx.fix(args)      → CommandFix(appstore).run(args)
```

**レイヤー構成**

| レイヤー | クラス/ファイル | 役割 |
|----------|----------------|------|
| CLI | `Clix` | argparse サブコマンド定義 |
| オーケストレーター | `Gistx` | 引数検証・AppStore 初期化・コマンド委譲 |
| コマンド | `CommandClone` / `CommandFix` / `CommandSetup` | 各サブコマンドのビジネスロジック |
| データモデル | `GistInfo` | gist 1件を表す値オブジェクト |
| 設定定義 | `AppConfigx` | ファイル名・ディレクトリ名・設定キーの定数 |
| 外部依存 | `yklibpy` | AppStore / Loggerx / Timex 等の共通ライブラリ |

**データフロー（clone コマンド）**

```
gh gist list (subprocess)
→ _parse_gh_gist_list_output() → GistInfo[]
→ gists.yaml（workspaces/<ID>/gists.yaml）
→ _filter_gists() でpublic/private/all に絞り込み
→ gh gist clone (subprocess) × gist数
→ progress.yaml・workspaces.yaml に記録
```

**永続化パス**: `%APPDATA%/gistx/config.yaml`、`%LOCALAPPDATA%/gistx/<user>/workspaces/`

**設計上の注意点**:
- `CommandFix` は旧来の `gistlist/` + `fetch.yaml` を操作するレガシーコード（現行アーキと不整合）
- `_get_workspace_path()` と YAML ヘルパーが CommandClone/CommandFix で重複（未リファクタリング）
- `check` サブコマンドは定義のみ、`NotImplementedError` を送出

## Notes

## Action Items
- [ ]

## Related
- [[North Star]]
- [[yklibpy]]
- [[ghrepo]]
