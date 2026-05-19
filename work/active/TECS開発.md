---
date: 2026-04-26
description: "TOPPERSプロジェクト TECS WG — tecsgen・TECSCDE・ツール群・仕様書・mkspec の開発進捗概要"
project: TECS
quarter: Q2-2026
status: active
tags:
  - work-note
---

# TECS 開発

TECS WG の開発作業全体の進捗管理ノート。

## Context

- TECS (TOPPERS Embedded Component System) のコンポーネント記述言語・ツールチェーン開発
- tecsgen（コンポーネント記述コンパイラ）、TECSCDE（設計環境）、関連ツール群を並行開発
- 参照資料: [[reference/03-Resources/my-topic/CLAUDE|TECS Wiki]]
- tecsgenの最新コード  E:\Crepo\ykominami-svn-2\tecsgen\trunk

**状態凡例:** `-` 未着手 / `進行中` / `完了` / `保留`

> [!success] 共通ブロッカー解決済み（2026-05-19）
> ~~コードベースからのドキュメント生成方法（NotebookLM 等）が未決定。~~
> **決定**: NotebookLM は採用せず。RST ソースは llm-wiki（Claude Code 直接 ingest）で知識ベース化し、仕様書執筆は Claude Code がコードベースを直接読んで行う。tecs-docs の ASP3+TECS RST 32件を llm-wiki TECS トピックに取り込み済み（raw 48件、記事 13件）。

## tecsgen

コンポーネント記述言語のコンパイラ。Ruby 実装。

| 作業 | 状態 | メモ |
|------|------|------|
| 外部仕様作成 | 進行中 | [[tecsgen外部仕様]] ドラフト作成済み |
| 内部仕様作成 | 進行中 | [[tecsgen内部仕様]] ドラフト着手（2026-05-19） |
| リファクタリング | - | |
| 新機能追加 | - | |
| テスト仕様・テストプログラム作成 | 進行中 | |
| ユーザ向けドキュメント作成 | 進行中 | |

## TECSCDE

TECS コンポーネント設計環境（Component Diagram Editor）。

| 作業 | 状態 | メモ |
|------|------|------|
| 外部仕様・内部仕様 | 進行中 | |
| JS版（フレームワーク非依存）外部仕様 | 進行中 | |
| JS版（フレームワーク依存）外部仕様 | - | |
| JS版（フレームワーク依存）内部仕様 | - | |
| JS版（フレームワーク依存）実装 | - | |
| JS版（フレームワーク依存）テスト仕様・テストプログラム | - | |

## ツール群

| ツール | 作業 | 状態 | メモ |
|--------|------|------|------|
| tecsmerge | 実装・仕様 | 進行中 | |
| RubyScriptAnalyzer | 実装・仕様 | 進行中 | |
| TECS向け LSP サーバ | 実装・仕様 | 進行中 | |

## ドキュメント

llm-wiki に TECS RST ドキュメントを ingest 済み（2026-05-19）。仕様書執筆は Claude Code + llm-wiki の組み合わせで進める。

| ドキュメント | 状態 | メモ |
|------------|------|------|
| TECS仕様書 | 進行中 | |
| ツール仕様書 | 進行中 | |

## mkspec（テスト管理）

| 作業 | 状態 | メモ |
|------|------|------|
| テスト管理システム整備 | 進行中 | |

## Action Items

- [x] ドキュメント生成方法を決定する（NotebookLM / llm-wiki / 他）→ **llm-wiki + Claude Code に決定（2026-05-19）**
- [x] tecsgen 外部仕様の骨子を作成する → **[[tecsgen外部仕様]] 作成済み（2026-05-19）**
- [ ] llm-wiki TECS トピックをベースに仕様書ドラフトを開始する

## Open Questions

## Related

- [[North Star]]
- [[reference/03-Resources/my-topic/CLAUDE|TECS Wiki]]
- [[perf/competencies/技術文書化|技術文書化]] — 仕様書作成の competency 証拠
- [[perf/competencies/ソフトウェアアーキテクチャ|ソフトウェアアーキテクチャ]] — CDL・tecsgen 設計判断の competency 証拠
