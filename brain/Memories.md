---
date: 2026-05-07
description: "Index of memory topics — key decisions, patterns, gotchas, people context"
tags:
  - brain
  - index
---

# Memories

Persistent context and knowledge retained across sessions. Each topic lives in its own note — follow the links.

- [[Key Decisions]] — architectural and workflow decisions worth recalling
- [[Patterns]] — recurring patterns and conventions discovered across work
- [[Gotchas]] — things that have bitten before and will bite again
- [[People & Context]] — org structure, teams, review history, dynamics
- [[North Star]] — living goals document, read at session start
- [[Skills]] — custom slash commands and workflows

## Recent Context

- 2026-06-09: TECS wiki クエリ（呼び口配列・受け口配列の書き方 — tecs/tecs-0 両wiki）。wiki log更新のみ、vault ノート未作成。⚠️未解消: TECS仕様書(tecs wiki版)-受け口配列の書き方を教えて.md 未作成・TECS仕様書 22件 untracked（未コミット）・TECS-MEMO/_inbox フォルダ untracked・命名衝突フォルダ4件継続。
- 2026-06-08: TECS wiki クエリ集中セッション（tecs + tecs-0 両wiki）。コンポーネント・セル・セルタイプ・受け口・呼び口・シグニチャを体系的にクエリ。CDL シグニチャ記述例を両wiki ingest + compile + lint。vault: TECS仕様書(tecs wiki版)/シグニチャ ファイル名余分スペース修正。⚠️未解消: `_inbox/TECS仕様書-シグニチャとは何か.md`（既存ファイルの改善版）処理待ち・deleted files未コミット継続・命名衝突フォルダ4件継続。
- 2026-06-07: セッション内作業なし（wrap-up + standup のみ）。Obsidian経由でユーザが大規模再編成: Note/ 85件 → reference/Note/ 移動。⚠️ 命名衝突フォルダ4件残存（Kindle 1/SHIFT-AI 1/VCS-PROJECT-PKGMGR 1/YouTube 1）— 次セッションで手動マージ要。claudianプラグイン削除。templates/読書.md追加。reference/Inbox/ 3件追加。
- 2026-06-06: wrap-up — 2026-06-04/05セッション。①vault大規模再編成: reference/ 77件 → Note/ 13サブフォルダに再分類（4e795e2）。②ghrepo/gistx/gitreporemote の3ワークノートにArchitecture詳細追記（c452e02）。③Patterns.md に2パターン追加（vault再分類ワークフロー・ghrepo型Python CLIパターン）。④LLM-wiki MEMO大幅拡張。⑤Copilotプラグイン+カスタムプロンプト14件統合。⑥htmlparser命名調査ノート整理・Kindle clipping 3件追加。brag 3件追加。未解消（継続）: Collaboration/Feedbackコンピテンシーエビデンス未記録。
- 2026-05-31: standup後作業 — ①Inbox 6件処理（nlm-CLI/Obsidian-AI連携昇格・NotebookLMワークフロー追記・3件削除）、②Clippings 4件コミット、③.obsidian/daily-notes.json を.gitignore追加。④TECS wiki — tecsgen/trunk内部ドキュメント6件ingest・compile_wiki.py実行（source-summary 6件新規・concept 45件更新・backlink 43件修正・ソース88→94件）。git `2e28259`。未解消（継続）: Collaboration/Deliveryコンピテンシーノート未作成（12+セッション）。
- 2026-05-29: wrap-up — 2026-05-28/29セッション。TECS wiki RST 9件ingest完了（ソース57件に拡張）。Inbox 1件処理（NotebookLM活用術→reference/Note/昇格）。templates/from-NotebookLM.md を正規テンプレートとして追跡開始。.gitignore に 2hop-links-plus 追加。brag追記3件（Inbox15件処理・TECS wiki 9件ingest・Patterns.md 2パターン）。未解消（継続）: ①Collaboration/Deliveryコンピテンシーノート未作成（10+セッション）、②TECS wiki コンパイル未実施（9件以上未コンパイルソース）
- 2026-05-27: wrap-up — セッション内作業なし（即wrap-up）。未追跡ファイル: Clippings 2件（Karpathy LLM wiki記事・ベクトルDB不要記事）、reference/Inbox 2件（AIAU-雑談・llm-wiki に必要なもの）、デザイン系3ディレクトリ（テンプレートサンプル、.gitignore推奨）。brag-spotter: semantic search CLIリファレンス・YouTube Bases 3本・LLM wikiメモリ研究の3件未記録→Q2 brag追記。未解消（継続10セッション以上）: ①Collaboration/Deliveryコンピテンシーノート未作成、②work/1-1/空、③デザイン系ディレクトリ・プロジェクト/ 未追跡。
- 2026-05-26: wrap-up — Inbox4件処理（Claudeの7つの組み込み機能→reference/Note/・TECSコンポーネント仕様書目次案→reference/Note/・KarpathyのCLAUDE.md拡張ルールを既存ノートに統合・無題のファイル→Clippings/重複のため削除）。templates/Untitled.md削除（Daily Note Template重複）。未解消（継続9セッション以上）: ①Collaboration/Deliveryコンピテンシーノート未作成、②Note/ディレクトリ未追跡（Kindle/SHIFT-AI/VCS/YouTube）、③work/1-1/空、④デザイン系ディレクトリ・プロジェクト/ 未追跡。
- 2026-05-25: wrap-up — reference/Note/ABC.md・DEF.md の削除コミット、reference/Inbox/ 10件追加コミット・プッシュ完了。新規Inbox5件出現（10分でわかるObsidian・dataview・karpathy-CLAUDE.md・ベクトルDB活用・今日のタスク）・Note/ディレクトリ未追跡継続。未解消（継続）: ①Collaboration/Deliveryコンピテンシーノート未作成（7セッション以上）、②work/1-1/・デザイン系ディレクトリ・プロジェクト/ 未追跡。
- 2026-05-23: wrap-up — `reference/Claude Code スキルのモデル指定.md` を新規作成（work/archive のフロントマターなし raw 出力を整形）。`.claude/**/settings.local.json` を .gitignore に追加。コミット・プッシュ完了。未解消（継続）: ①Collaboration/Delivery コンピテンシーノート未作成（5セッション以上）。
- 2026-05-22: wrap-up — vault-audit全修正・celltype概念ページ昇格の2件をQ2ブラグに追記。claudian plugin・設定ファイル同期をコミット・プッシュ完了。未解消（4セッション継続）: ①21件の削除ファイル未コミット（Clippings/・Note/・ARCHITECTURE.md 等）、②ルート直下の生出力ノート4件（要削除/移動）、③AI toolsディレクトリの.gitignore未追加、④Collaboration/Deliveryコンピテンシーノート未作成。
- 2026-05-20: wrap-up — tecsgen外部仕様（17KB）・内部仕様（25KB）の未コミット成果物をコミット・プッシュ。brag docに仕様書2件エントリ追加。TECSブロッカー「ドキュメント生成方法未決定」は**解決済み**（llm-wiki + Claude Code直読に決定、2026-05-19）。未解消: 多数の未追跡ファイル（日次ノート・root散在ノート）、Collaboration/Deliveryコンピテンシーノート未作成。
- 2026-05-19: wrap-up — brag docに3エントリ追加（North Star見出し修正・Memories継続ログ運用確立・icon-file-group-managerアーカイブ完了）。未解消: 77件の未追跡ファイル（日次ノート20件・root散在ノート多数）、「ドキュメント生成方法未決定」TECSブロッカー、Collaboration/Deliveryコンピテンシーノート未作成。claudian plugin main.js未コミット（要確認）。
- 2026-05-15: wrap-up — North Star見出し階層バグを修正（`#`・`##` が `## Current Focus` 内に混在 → `###`/`####` に統一）。brag-spotter結果: Gotchas.md運用開始・TECS知識ベース動作検証・個人開発11件可視化の3件が未記載。Collaboration/Deliveryコンピテンシーノート未作成。未解消: 34件の未追跡ファイル（日次ノート11件・Kindle 7件・rootノート等）、「ドキュメント生成方法未決定」TECSブロッカー（3週間以上）
- 2026-05-14: wrap-up — brag docにコンピテンシーフレームワーク設計エントリ追加。未解消問題: 34件の未追跡ファイル積み残し（日次ノート11件がvault root・Kindle 7件・画像3件・Claude Codeノート等がroot）、「ドキュメント生成方法未決定」TECSブロッカー3週間未解消、North Star heading階層崩れ（# が ## の中に混在）
- 2026-05-12: wrap-up + weekly synthesis — 読み取り専用セッション。ファイル変更なし。主な所見: 34件の未追跡ファイル積み残し（空の日次ノート11件・Kindle読書ノート7件・画像3件・ルートノート2件）、未コミット変更14件、「ドキュメント生成方法未決定」ブロッカーが2週間未解消でTECS全タスク停滞中。brag doc未追記3件（コンピテンシーフレームワーク設計・North Star証跡リンク・TECS共通ブロッカー可視化）
- 2026-05-09: wrap-up — Slack MCP server を .mcp.json に追加（トークン未設定）、North Star `## Goals` 書式バグ修正、未コミットの散在ノート群（Claude Codeのproject knowledge.md・タスク管理ノート.md・Kindle 6冊・WSL2・Python notes）を確認・整理待ち
- 2026-05-07: TECS wiki index 修復（stale indexes — 8記事が未登録、0→10に修正）、North Star の「ドキュメント作成」に "to be written" 項目（プラグイン16種・TECS仕様書2件・拡張コンポーネント2件）を追加、validate-write vault境界チェック追加、Gotchas文書化
