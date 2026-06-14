---
date: 2026-05-10
description: "Living document of goals, focus areas, and aspirations — read at session start, updated when direction shifts"
tags:
  - brain
  - north-star
aliases:
  - Goals
  - Focus
---

# North Star

目標とフォーカスの生きたドキュメント。自分と Claude の両方が書く。セッション開始時に Claude が読む。

## Current Focus

### TOPPERSプロジェクトのTECS開発(TECS WG関連)
#### tecsgen
- 外部仕様作成
- 内部仕様作成
- リファクタリング
- 新機能追加
- テスト仕様・テストプログラム作成
- ユーザ向けドキュメント作成
#### TECSCDE
- 外部仕様・内部仕様
- JavaScript版（フレームワーク非依存）外部仕様
- JavaScript版（フレームワーク依存）外部仕様・内部仕様・実装・テスト仕様・テストプログラム
#### 各種関連ツール
- tecsmerge
- RubyScriptAnalyzer
- TECS向けLSPサーバ
#### ドキュメント作成
##### TECS仕様書
- コンポーネントモデルリファレンスマニュアル（開発中・未公開）
- ジェネレータコード出力リファレンスマニュアル（開発中・未公開）
- CDL 未記載事項（CDLref_undoc.html — 内容なし）
##### ツール仕様書
##### プラグインドキュメント（tecsgen — 16/17種が未記載）
###### カーネル対応
- ATK1Plugin
- HRP2Plugin
- ASP3 NotifierPlugin
###### mrubyブリッジ
- MrubyBridgePlugin
- Mruby2CBridgePlugin
###### トレース
- TracePlugin
- TLVTracePlugin
###### RPC
- TransparentRPCPlugin
- OpaqueRPCPlugin
- SharedRPCPlugin
- SharedOpaqueRPCPlugin
###### Cインタフェース
- C2TECSPlugin
- TECS2CPlugin
##### 拡張コンポーネント
- TINET+TECS（開発中・未リリース — ドキュメント詳細なし）
- TLSF+TECS（詳細セクション未記載 — "to be filled in"）
#### mkspec(テスト管理)

### 個人開発環境整備
#### NotebookML管理システム
- NotebookMLソース管理システム([[notebookmlx]])
#### 関連ドキュメント管理システム
- ドキュメント管理システム([[bookinfor]] — 書籍・Kindle・ドキュメント・APIキー管理 Railsアプリ)
- bookmark管理システム([[bookmarkr]] — Google Chromeのブックマーク・OneTab機能拡張)
- bookmark管理拡張機能([[bmx]] — Google Chrome用機能拡張)
- Calibre用documentメタデータ抽出システム([[calibrex]] — calibre DBから)
- Gist管理システム([[gistx]])
- Githubリポジトリ管理システム([[ghrepo]])
- gitリポジトリ管理システム([[gitreporemote]])
- ICONファイル管理システム([[cpiconfiles]])
- ファイル管理システム([[filelist]])
- Google Drive用ファイルアップロードプログラム(gupload)
#### HTMLドキュメント解析システム(htmlparser)
- Amazon注文履歴モジュール(amazonorderscraper)
- Amazonカートモジュール(amazonsavedcartscraper)
- Fanza同人バスケットモジュール(fanzadoujinbasketscraper)
- Fanza同人購入履歴モジュール(fanzadoujinpurchasedscraper)
- Amazon-Kindle Unlimitedリストモジュール(kuscraper)
- Udemyマイラーニングモジュール(udemyscraper)
#### LLM対話システム
- janllm
#### Util関連
- TOMLファイル操作(tomlx)
- TkinterベースTUIプログラム(tkinterx_)
- (xmlkindle)
#### Python共通ライブラリ
- Pythonライブラリ(yklibpy)
- Pythonライブラリ(yklibpyz)
#### Ruby共通ライブラリ
- Rubyライブラリ(ykutils)
- Rubyライブラリ(ykxutils)

### AIツールチェーンコスト最適化
- トークン削減（RTK — Rust Token Killer）
- コンテキスト圧縮（headroom MCP — compress/retrieve/status）
- セッション横断記憶（agentmemory — Docker + iii-engine + Node.js）
- Claude Code コスト運用（モデル選択・CLAUDE.md設計・作業プロセス最適化）

## Goals

### Short-term (This Quarter)

-

### Medium-term (This Half)

- 

### Long-term (This Year+)

-

## Aspirations

-

## Anti-goals

-

## Shifts Log

| Date | Shift              | Reason        |
| ---- | ------------------ | ------------- |
|      | Created North Star | Initial setup |
