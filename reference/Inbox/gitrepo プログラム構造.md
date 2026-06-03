# ghrepo
 プログラムの構造を説明して

● ghrepo の構造

  全体像

  CLIエントリーポイント (main)
      └─ Clix (引数定義)
      └─ Ghrepo (ディスパッチ + 実行)
             ├─ CommandSetup  → setup サブコマンド
             ├─ CommandList   → list / fix サブコマンド
             └─ CommandSearch → search サブコマンド

  レイヤー構成

  エントリーポイント層
  - ghrepo.py の main() が起点。Clix で引数をパースし、Ghrepo のクラスメソッドへディスパッチする。
  - Ghrepo はインスタンス化せず、すべてクラスメソッド（setup, list_repos, fix_repos, search_repos）。

  CLI定義層
  - clix.py の Clix が argparse のサブパーサーを組み立てる。コマンドと引数の定義のみ担当し、ロジックは持たない。

  コマンド実行層
  - CommandList、CommandSearch、CommandSetup が実際の処理を担う。
  - すべて yklibpy.command.Command
  を継承したクラスメソッド/インスタンスメソッドとして実装（モジュールレベルの関数なし）。

  設定・ストレージ層
  - AppConfigx がフィールド定義・ファイル名定数・file_assoc構造を保持。
  - yklibpy の AppStore / Storex が実際のYAML読み書きを担う（ghrepo側は直接ファイルIOを書かない、ただし snapshot.yaml
  のみ yaml.safe_dump で直書き）。

  データフロー（listサブコマンド）

  gh repo list (外部コマンド)
      ↓ JSON
  CommandList.get_all_repos()  ← management fields付与 (snapshot-id, valid, field_1/2/3)
      ↓ RepoAssoc
  CommandList.save_snapshot()
      ├─ snapshots/<id>/snapshot.yaml  書き込み
      ├─ snapshots.yaml                追記
      └─ repos.yaml                    マージ更新
      ↓
  --output で指定したJSONファイルに出力

  主要な型

  type RepoItem = dict[str, Any]      # 1リポジトリ分のデータ
  type RepoAssoc = dict[str, RepoItem]  # name → RepoItem の辞書

  この2つが command_list.py と command_search.py に重複定義されている（意図的な設計）。

  外部依存

  yklibpy（../yklibpy のローカルパッケージ）が基盤を提供。ghrepo側が使うのは：

  ┌────────────────┬─────────────────────────────────────┐
  │ yklibpy クラス │                役割                 │
  ├────────────────┼─────────────────────────────────────┤
  │ AppStore       │ 設定・DBファイルへの統一アクセス    │
  ├────────────────┼─────────────────────────────────────┤
  │ Storex         │ 個別ファイルのload/output           │
  ├────────────────┼─────────────────────────────────────┤
  │ AppConfig      │ KIND_CONFIG/KIND_DB等の定数         │
  ├────────────────┼─────────────────────────────────────┤
  │ Cli            │ argparse ラッパー                   │
  ├────────────────┼─────────────────────────────────────┤
  │ Command        │ コマンドの基底クラス                │
  ├────────────────┼─────────────────────────────────────┤
  │ CommandGhUser  │ gh auth status からユーザー名を取得 │
  ├────────────────┼─────────────────────────────────────┤
  │ Loggerx        │ ログ出力ユーティリティ              │
  └────────────────┴─────────────────────────────────────┘

✻ Baked for 20s

※ recap: Reviewing and maintaining the ghrepo CLI project. Just explained the program structure. No pending action —
  awaiting the user's next request. (disable recaps in /config)
