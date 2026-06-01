# gistx
❯ プログラムの構造を説明して

● gistx のプログラム構造

  エントリポイントからの流れ

  gistx (CLI コマンド)
    └─ mainx()  [gistx.py]
         └─ Clix.parse_args()  [clix.py] — argparse でサブコマンドを解析
              └─ args.func(args)  — サブコマンドに対応する Gistx のクラスメソッドを呼び出す

  呼び出し関係

  mainx()
    ├─ Gistx.setup(args)
    │     └─ CommandSetup(appstore).run()
    │
    ├─ Gistx.clone(args)
    │     ├─ init_appstore()  — AppStore 初期化
    │     ├─ _load_config_with_legacy_fallback()  — .yml → .yaml レガシー移行
    │     └─ CommandClone(appstore).run(args, repo_kind)
    │           ├─ _resolve_gist_list()  — キャッシュ判定 or gh gist list 実行
    │           ├─ _filter_gists() / _limit_gists()
    │           └─ _clone_gists()  — gh gist clone を1件ずつ実行
    │
    └─ Gistx.fix(args)
          └─ CommandFix(appstore).run(args)
                ├─ remove_empty_directories()  ← モジュールレベル関数（制約違反）
                └─ _reconcile_fetch_yaml()

  レイヤー構成

  ┌────────────────────┬────────────────────────────────────────┬──────────────────────────────────────────────────┐
  │      レイヤー      │            クラス/ファイル             │                       役割                       │
  ├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────┤
  │ CLI                │ Clix                                   │ argparse のサブコマンド定義                      │
  ├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────┤
  │ オーケストレーター │ Gistx                                  │ 引数検証・AppStore 初期化・コマンド委譲          │
  ├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────┤
  │ コマンド           │ CommandClone, CommandFix, CommandSetup │ 各サブコマンドのビジネスロジック                 │
  ├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────┤
  │ データモデル       │ GistInfo                               │ gist 1件を表す値オブジェクト                     │
  ├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────┤
  │ 設定定義           │ AppConfigx                             │ ファイル名・ディレクトリ名・設定キーの定数置き場 │
  ├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────┤
  │ 外部依存           │ yklibpy                                │ AppStore/Loggerx/Timex 等の共通ライブラリ        │
  └────────────────────┴────────────────────────────────────────┴──────────────────────────────────────────────────┘

  データの流れ（clone コマンド）

  gh gist list (subprocess)
    → _parse_gh_gist_list_output()  — テキストを GistInfo[] に変換
    → gists.yaml に保存（workspaces/<ID>/gists.yaml）
    → _filter_gists() でpublic/private/all に絞り込み
    → gh gist clone (subprocess) を gist ごとに実行
    → progress.yaml に成功/失敗数を記録
    → workspaces.yaml にワークスペースIDを記録

  永続化ファイルの関係

  %APPDATA%/gistx/config.yaml          … 設定（user, url_api, gists）

  %LOCALAPPDATA%/gistx/<user>/
    workspaces.yaml                     … ワークスペースID → [timestamp, 件数]
    workspaces/
      <ワークスペースID>/
        gists.yaml                      … gh gist list の結果スナップショット
        gistrepo/
          progress.yaml                 … クローンID → 実行結果
          <クローンID>/
            public/<gist_id>/           … clone した public gist
            private/<gist_id>/          … clone した private gist

  設計上の注意点

  - CommandFix は workspaces/ ではなく旧来の gistlist/ と fetch.yaml
  を操作するレガシーコード（現行アーキテクチャと不整合）
  - _get_workspace_path() と YAML 読み書きヘルパーが CommandClone と CommandFix で重複している（未リファクタリング）
  - check サブコマンドは定義だけあり NotImplementedError を送出する
