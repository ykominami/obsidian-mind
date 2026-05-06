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

TOPPERSプロジェクト TECS WG での開発作業全体の進捗管理ノート。

## Context

- TECS (TOPPERS Embedded Component System) のコンポーネント記述言語・ツールチェーン開発
- tecsgen（コンポーネント記述コンパイラ）、TECSCDE（設計環境）、関連ツール群を並行開発
- 参照資料: [[03-Resources/my-topic/CLAUDE|TECS Wiki]]

**状態凡例:** `-` 未着手 / `進行中` / `完了` / `保留`

## tecsgen

コンポーネント記述言語のコンパイラ。Ruby 実装。

| 作業 | 状態 | メモ |
|------|------|------|
| 外部仕様作成 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| 内部仕様作成 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| リファクタリング | - | |
| 新機能追加 | - | |
| テスト仕様・テストプログラム作成 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| ユーザ向けドキュメント作成 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |

## TECSCDE

TECS コンポーネント設計環境（Component Diagram Editor）。

| 作業 | 状態 | メモ |
|------|------|------|
| 外部仕様・内部仕様 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| JS版（フレームワーク非依存）外部仕様 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| JS版（フレームワーク依存）外部仕様 | - | |
| JS版（フレームワーク依存）内部仕様 | - | |
| JS版（フレームワーク依存）実装 | - | |
| JS版（フレームワーク依存）テスト仕様・テストプログラム | - | |

## ツール群

| ツール | 作業 | 状態 | メモ |
|--------|------|------|------|
| tecsmerge | 実装・仕様 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| RubyScriptAnalyzer | 実装・仕様 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |
| TECS向け LSP サーバ | 実装・仕様 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |

## ドキュメント

| ドキュメント | 状態 | メモ |
|------------|------|------|
| TECS仕様書 | 進行中 | 既存 wiki ベース仕様書を llm-wiki で更新する方法調査中 |
| ツール仕様書 | 進行中 | 既存 wiki ベース仕様書を llm-wiki で更新する方法調査中 |

## mkspec（テスト管理）

| 作業 | 状態 | メモ |
|------|------|------|
| テスト管理システム整備 | 進行中 | コードベースからドキュメント生成方法調査中（NotebookLM 等） |

## Action Items

- [ ]

## Open Questions

-

## Related

- [[North Star]]
- [[03-Resources/my-topic/CLAUDE|TECS Wiki]]
