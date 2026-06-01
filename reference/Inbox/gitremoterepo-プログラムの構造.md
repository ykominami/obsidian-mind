● プログラム構造

  全体像

  CLI コマンド
      │
      ▼
  main.py (コアロジック)
      │
      ├── find_git_dirs()     ← ファイルシステム走査
      ├── run_git_remote_v()  ← git コマンド実行
      ├── parse_remote_v()    ← 出力テキストのパース
      ├── build_report()      ← レポート構築
      └── write_yaml()        ← YAML 出力

  ---
  エントリーポイント（CLI → 関数）

  ┌────────────────┬──────────────────┬─────────────────────────────────────────┐
  │    コマンド    │       関数       │                  役割                   │
  ├────────────────┼──────────────────┼─────────────────────────────────────────┤
  │ gitrepo        │ mainx()          │ ディレクトリ走査 → YAML出力             │
  ├────────────────┼──────────────────┼─────────────────────────────────────────┤
  │ gitrepoanalyze │ main_analyze()   │ 既存YAMLを to_dict() で正規化して再出力 │
  ├────────────────┼──────────────────┼─────────────────────────────────────────┤
  │ grr_load_yaml  │ load_yaml_main() │ yklibpy経由でYAMLをロード               │
  ├────────────────┼──────────────────┼─────────────────────────────────────────┤
  │ xt2, xt3       │ xt2() / xt3()    │ 開発用スタブ（本番では不使用）          │
  └────────────────┴──────────────────┴─────────────────────────────────────────┘

  ---
  データフロー（メインパス）

  ファイルシステム
      └── find_git_dirs()
              │ リポジトリルート一覧
              ▼
          git -C <root> remote -v  (サブプロセス)
              │ テキスト出力
              ▼
          parse_remote_v()
              │ { "origin": { "fetch": url, "push": url } }
              ▼
          build_report()
              │ { base_dir, repo_count, repos: [...] }
              ▼
          write_yaml()  →  report.yaml

  ---
  モジュール間の依存関係

  __init__.py
      ├── main.py          (スタンドアロン、外部依存なし)
      ├── analyzer.py
      │       ├── remotedef.py  (RemoteDef + RemoteDef.Item)
      │       └── repodef.py    (RepoDef)
      └── x.py             (yklibpy への薄いラッパー)

  filex.py（Filex）は実装済みだが、現在どのエントリーポイントからも呼ばれていない。

  ---
  データモデル（Analyzerパス専用）

  Analyzer はCLIには繋がっておらず、プログラム的にのみ使用：

  Analyzer.analyze(yaml_text)
      └── RepoDef (path + remotes[])
              └── RemoteDef (remote名 + children[])
                      └── RemoteDef.Item (kind: fetch/push/other/root)

  Item.kind の意味：
  - other — remote名ノード（origin など）、value は空
  - fetch / push — URLリーフノード
  - root — Item.create_root() で生成する仮想ルート

  ---
  重要な設計上の注意点

  Analyzer は壊れやすい
  YAMLライブラリを使わず、"repo_count:" "  - path:"
  などの文字列でテキストを分割する。YAMLのインデントやキー名が変わると動作しなくなる。

  gitrepoanalyze は Analyzer を使わない
  yaml.safe_load() → to_dict() の正規化ルートを使う。Analyzer は別設計の実験的実装。

  to_dict() の正規化ルール（main.py）
  Path → str、tuple/set → list、カスタムクラスは .to_dict() を優先、フォールバックは __dict__（_
  プレフィックスを除外）、最終手段は str(obj)。

