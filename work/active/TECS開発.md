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
- 参照資料: [[03-Resources/my-topic/CLAUDE|TECS Wiki]]

**状態凡例:** `-` 未着手 / `進行中` / `完了` / `保留`

> [!warning] 共通ブロッカー
> コードベースからのドキュメント生成方法（NotebookLM 等）が未決定。これが決まるまで「進行中」タスクは全部止まってる。

## tecsgen

コンポーネント記述言語のコンパイラ。Ruby 実装。

| 作業 | 状態 | メモ |
|------|------|------|
| 外部仕様作成 | 進行中 | |
| 内部仕様作成 | 進行中 | |
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

llm-wiki で既存 wiki ベース仕様書を更新する方法を調査中。

| ドキュメント | 状態 | メモ |
|------------|------|------|
| TECS仕様書 | 進行中 | |
| ツール仕様書 | 進行中 | |

## mkspec（テスト管理）

| 作業 | 状態 | メモ |
|------|------|------|
| テスト管理システム整備 | 進行中 | |

## Action Items

- [ ] ドキュメント生成方法を決定する（NotebookLM / llm-wiki / 他）

## Open Questions

- どのツールでコードベースからドキュメントを生成するか

## Related

- [[North Star]]
- [[03-Resources/my-topic/CLAUDE|TECS Wiki]]
