---
date: 2026-04-10
description: gitリポジトリ管理システム-Pythonパッケージ
project: gitreporemote
status: active
quarter: Q2-2026
tags:
  - work-note
---

# gitreporemote

## Context

ローカルの git リポジトリを走査し、remote URL 情報を YAML に出力する CLI。

## Architecture

```
CLIコマンド
    └─ main.py (コアロジック)
          ├── find_git_dirs()     ← ファイルシステム走査
          ├── run_git_remote_v()  ← git コマンド実行
          ├── parse_remote_v()    ← 出力テキストのパース
          ├── build_report()      ← レポート構築
          └── write_yaml()        ← YAML 出力 → report.yaml
```

**エントリーポイント一覧**

| コマンド | 関数 | 役割 |
|----------|------|------|
| `gitrepo` | `mainx()` | ディレクトリ走査 → YAML出力 |
| `gitrepoanalyze` | `main_analyze()` | 既存YAMLを `to_dict()` で正規化して再出力 |
| `grr_load_yaml` | `load_yaml_main()` | yklibpy経由でYAMLをロード |
| `xt2`, `xt3` | `xt2()` / `xt3()` | 開発用スタブ（本番不使用） |

**モジュール依存関係**

```
__init__.py
    ├── main.py        (スタンドアロン、外部依存なし)
    ├── analyzer.py
    │       ├── remotedef.py  (RemoteDef + RemoteDef.Item)
    │       └── repodef.py    (RepoDef)
    └── x.py           (yklibpy への薄いラッパー)
```

**設計上の注意点**:
- `Analyzer` は壊れやすい — YAML をライブラリでなく文字列分割でパースするため、キー名やインデントが変わると動作しなくなる
- `gitrepoanalyze` は `Analyzer` を使わず `yaml.safe_load() → to_dict()` のルートを使う（別設計）
- `Filex` クラスは実装済みだがどのエントリーポイントからも呼ばれていない

## Notes

## Action Items
- [ ]

## Related
- [[North Star]]
- [[yklibpy]]
- [[ghrepo]]
