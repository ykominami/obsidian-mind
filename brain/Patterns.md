---
date: 2026-04-25
description: "Recurring patterns and conventions discovered across work — architecture, naming, tooling, and implementation patterns"
tags:
  - brain
---

# Patterns

Recurring patterns discovered across work.

## ノート管理フレームワーク（脳のOS）

| ゾーン | 比喩 | 役割 |
|--------|------|------|
| Project | 厨房 | 今、手を動かす場所 |
| Knowledge | 脳 | 自分のOS・判断基準 |
| Reference | 書庫 | 道具箱・資料 |
| Asset | 倉庫 | 素材・材料 |

- **Project**: 今動いているものだけ。終わったら完了フォルダへ → [[work/active/]]
- **Knowledge**: 学びのメモ、個人的な哲学、フレームワーク集 → [[brain/]]
- **Reference**: 道具・資料・コマンドリファレンス → [[reference/]]

## 作業停止・再開パターン（2026-05-04 週次サマリーより）

- **GW等の長期休暇期間** — コミットゼロは正常。週次サマリーで振り返るだけでよい
- **全タスク停止のデバッグ** — 複数タスクが同時に「詰まっている」と感じたときは、共通ブロッカー1点を先に特定する（例: ドキュメント生成方法が未決定のまま全TECSタスクがブロックされていた → 決定後に全タスクが前進）

## スタブノートの機能限界

- `work/active/` にリンクなし・コンテキストなしのスタブノートが多数あっても、グラフ上では孤立ノードであり実質機能しない
- `quarter` フィールドがないと Work Dashboard Base に表示されない
- 最低限 `[[North Star]]` へのリンクを持つこと

## コードベース直読み仕様書作成パターン

- **採用文脈**: NotebookLM・RST変換ツール等の中間ツールなし。Claude Code がソースコードを直接読み、仕様書を生成する
- **適用例**: tecsgen 外部仕様（17KB・420行超）・内部仕様（25KB・530行超）を1日でスクラッチ作成（2026-05-19）
- **利点**: ツール設定コストゼロ・コードと仕様の乖離なし・反復修正が高速
- **適用条件**: コードベースが Claude のコンテキストウィンドウに収まる規模、または対象モジュールを絞れる場合
- **出典**: [[work/active/TECS開発]], [[tecsgen外部仕様]], [[tecsgen内部仕様]], git `0258ec8`

## vault再分類ワークフロー

大量ファイルの `reference/` → サブフォルダへの再分類を行うとき。

- **Obsidian内で移動**: Obsidian のファイルエクスプローラーでフォルダごと移動すると、wikilink が自動更新される（ファイルシステム直操作は wikilink を壊す）
- **コミット前確認**: `git status` でリネーム追跡（`R`）が検出されていれば git が移動を認識している。`D + ??` ペアになっている場合は `git mv` 相当として扱われず履歴が切れるため、`git add -u` と `git add <new>` の両方を実行してステージングする
- **wikilink のパス除去**: 移動後は `[[reference/Note/X]]` → `[[X]]` に正規化（Obsidian は note 名だけで解決するため）。brag doc や competency の Related などに残った旧パス付きリンクを検索して修正する
- **.gitignore 見直し**: 新しいプラグインフォルダ（`.obsidian/plugins/xxx/`）は plugin バイナリなので除外対象。ユーザコンテンツフォルダ（`copilot/` 等）は追跡対象
- **適用例**: `reference/` 77件 → `Note/` 13サブフォルダへ再分類（2026-06-04）。git rename として正しくトラック済み
- **出典**: git `chore: vault再編成`, [[perf/brag/Q2 2026]]

## Claude サブエージェント活用パターン

- **文章チェック用サブエージェント** — コーディング時の linter 的に使う発想。レビュー・校正を並列エージェントに委譲することで品質ゲートを自動化できる（出典: [[reference/Inbox/AIAU-雑談(ai)]]）

## Obsidian タグ運用原則

- タグの目的を明確にし一貫したルールを定める: 種類（`work-note`, `decision`）・テーマ・状態（`active`, `completed`）の3軸
- 階層タグ（`project/auth-refactor` など）で粒度と分類の柔軟性を両立
- リンクだけでは捉えきれない「属性によるグルーピング」にタグを使う

## ghrepo 型 Python CLI パターン（仕様書駆動）

**ghrepo のプログラム構造**を、サブコマンドを持つ Python CLI の canonical パターンとして使う。

```
エントリーポイント層  ghrepo.py / main() — Clix で引数パース → ディスパッチ
CLI定義層           Clix (clix.py)      — argparse 定義のみ、ロジックなし
コマンド実行層      CommandXxx          — yklibpy.command.Command 継承
設定・ストレージ層  AppConfigx + yklibpy.AppStore/Storex
```

**スキル連携（仕様書駆動フロー）**:

```
docs/req/idea/*.md  (アイデアレベルの要件)
    ↓ python-cli-req-to-external-spec スキル
docs/req/detail/*.md (詳細要件)
    ↓ python-cli-external-spec スキル  (ghrepo-external-spec)
外部仕様書 (docs/spec/external.md)
    ↓ python-cli-internal-spec スキル
内部仕様書 (docs/spec/internal.md)
```

- **採用文脈**: ghrepo・gistx・gitreporemote・calibrex・filelist 等、Python CLI プロジェクト全般
- **適用条件**: サブコマンドを持つ CLI、yklibpy を共通基盤として使うプロジェクト
- **出典**: [[ghrepo]], [[gistx]], [[gitreporemote]], `reference/Inbox/仕様書駆動の取り組み.md`（2026-06-04）

## プロジェクト実装言語別分類（2026-04-11 時点）

### Ruby 実装
- [[bookinfor]], [[bookmarkr]], [[cpiconfiles]]

### Python 実装
| 状態 | プロジェクト |
|------|-------------|
| 済 | [[ghrepo]], [[gistx]], [[calibrex]] |
| 未済 | [[filelist]], [[gitreporemote]], [[notebookmlx]] |
