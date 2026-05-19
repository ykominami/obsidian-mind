---
date: 2026-05-19
description: "tecsgen（TECS コンポーネント記述コンパイラ）内部仕様書。処理フロー・クラス設計・意味解析・最適化・コード生成の実装を対象とする。"
project: TECS
quarter: Q2-2026
status: active
tags:
  - work-note
  - tecs
  - tecsgen
  - spec
---

# tecsgen 内部仕様

> [!info] 文書状態
> **ドラフト（2026-05-19）** — ソースコード（`trunk/tecsgen/`、v1.9.0）を直接読んで作成。

## 1. 概要

### 1.1 目的

本文書は tecsgen の実装内部を記述する。tecsgen のコード読解・改修・テスト仕様作成を行う TECS WG メンバを対象読者とする。

### 1.2 対象バージョン

`tecslib/version.rb` で管理。現在のトランクバージョン: **1.9.0**。

### 1.3 関連文書

| 文書 | 内容 |
|------|------|
| [[tecsgen外部仕様]] | CLI・入出力・エラー形式 |
| TECS CDL リファレンスマニュアル | CDL 言語仕様 |
| TECS コンポーネント実装モデルリファレンスマニュアル | 生成コードの仕様 |

---

## 2. ソースファイル構成

```
trunk/tecsgen/
├── tecsgen.rb              # エントリポイント（TECSGEN クラス定義・起動）
├── tecsmerge.rb            # tecsmerge コマンド本体
├── tecsflow.rb             # tecsflow コマンド本体
├── tecscde.rb              # TECSCDE 起動スクリプト
├── tecslib/
│   ├── version.rb          # バージョン定義（$version, $package）
│   ├── core/
│   │   ├── tecs_lang.rb    # 字句解析器（Lexer）・文字コード処理
│   │   ├── bnf.y.rb        # YACC 文法定義（Parser + Generator クラス）
│   │   ├── bnf.tab.rb      # racc 生成パーサテーブル（同梱済み）
│   │   ├── C_parser.y.rb   # C 言語パーサ文法定義（import_C 用）
│   │   ├── C_parser.tab.rb # C パーサテーブル（同梱済み）
│   │   ├── tecsgen.rb      # TECSGEN クラス（パス管理・処理制御）
│   │   ├── generate.rb     # コード生成（最大ファイル、5400行）
│   │   ├── optimize.rb     # 最適化処理
│   │   ├── plugin.rb       # Plugin 基底クラス
│   │   ├── pluginModule.rb # PluginModule モジュール（ポストコード生成）
│   │   ├── messages.rb     # ローカライズ済みメッセージ定義
│   │   ├── types.rb        # 型システム（CDL 型クラス群）
│   │   ├── value.rb        # 値クラス群
│   │   ├── expression.rb   # 式クラス群（42KB）
│   │   ├── location.rb     # ソースコード位置（locale）管理
│   │   ├── gen_xml.rb      # XML 出力（tecsflow 用）
│   │   ├── tecsinfo.rb     # TECSInfo 実行時情報（30KB）
│   │   ├── tool_info.rb    # TOOL_INFO 機能
│   │   ├── unjoin_plugin.rb# unjoin プラグイン
│   │   ├── syntaxobj.rb    # syntaxobj/ ディレクトリのロード
│   │   ├── componentobj.rb # componentobj/ ディレクトリのロード
│   │   ├── syntaxobj/      # 構文オブジェクト（CDL パースツリーノード）
│   │   │   ├── node.rb         # Node 基底クラス（locale 管理・エラー出力）
│   │   │   ├── decl.rb         # 型・属性・変数宣言
│   │   │   ├── funchead.rb     # 関数ヘッダ（シグニチャ関数）
│   │   │   ├── paramdecl.rb    # パラメータ宣言
│   │   │   ├── paramlist.rb    # パラメータリスト
│   │   │   ├── typedef.rb      # typedef 宣言
│   │   │   ├── namedlist.rb    # 名前→オブジェクト マップ（NamedList）
│   │   │   ├── cdlinitializer.rb # CDL 初期化子
│   │   │   ├── cdlstring.rb    # CDL 文字列
│   │   │   └── namespacepath.rb # 名前空間パス
│   │   └── componentobj/   # コンポーネントモデルオブジェクト
│   │       ├── namespace.rb    # Namespace（名前空間）
│   │       ├── region.rb       # Region（リンクルート・ドメイン）
│   │       ├── signature.rb    # Signature（シグニチャ）
│   │       ├── celltype.rb     # Celltype（セルタイプ）
│   │       ├── compositecelltype.rb # CompositeCelltype（複合セルタイプ）
│   │       ├── compositecelltypejoin.rb # 複合セルタイプの結合処理
│   │       ├── cell.rb         # Cell（セルインスタンス、1930行）
│   │       ├── port.rb         # Port（呼び口・受け口）
│   │       ├── join.rb         # Join（結合記述、1363行）
│   │       ├── reversejoin.rb  # ReverseJoin（逆 require 結合）
│   │       ├── factory.rb      # Factory（ファクトリ記述）
│   │       ├── import.rb       # Import ディレクティブ処理
│   │       ├── import_c.rb     # import_C ディレクティブ処理（C ヘッダ解析）
│   │       ├── importable.rb   # Importable モジュール
│   │       ├── domaintype.rb   # DomainType（ドメイン）
│   │       ├── classtype.rb    # ClassType（クラス）
│   │       └── celltypeModule.rb # CelltypeModule モジュール
│   └── plugin/             # 標準付属プラグイン群（70+ ファイル）
```

---

## 3. 処理フロー

### 3.1 トップレベルフロー

```
tecsgen.rb (エントリポイント)
  │
  ├─ TECSGEN.init
  │    ├─ initialize_global_var   # グローバル変数初期化
  │    ├─ analyze_option          # コマンドラインオプション解析 (optparse)
  │    ├─ load_modules            # tecslib/* の require
  │    └─ setup                   # パス調整・gen ディレクトリ作成
  │
  ├─ tecsgen = TECSGEN.new
  ├─ tecsgen.run1                 # 構文解析 + 意味解析フェーズ1・2
  ├─ tecsgen.run2                 # 最適化 + コード生成フェーズ
  └─ tecsgen.dump_tecsgen_rbdmp   # 内部モデルダンプ（tecsgen.rbdmp）
```

### 3.2 run1（構文解析 + 意味解析）

```
run1
  ├─ syntax_analisys(ARGV)
  │    └─ ARGV.each { Import.new(f) }   # 全 CDL ファイルを順次パース
  │         ├─ Lexer(tecs_lang.rb) → トークン列
  │         └─ Parser(bnf.tab.rb)  → AST / コンポーネントオブジェクト構築
  │              ※ パース中にプラグインの gen_cdl_file も逐次呼ばれる
  │
  ├─ semantics_analisys_1
  │    ├─ Generator.end_all_parse         # 全 CDL パース完了通知
  │    ├─ [ポストコード生成]
  │    │    └─ PluginModule.gen_plugin_post_code
  │    │         → tmp_plugin_post_code.cdl 生成 → Import でパース
  │    └─ root_namespace.set_definition_join (1回目)
  │         # 結合の左辺（呼び口/属性名）を Port/Decl に解決
  │
  └─ semantics_analisys_2
       ├─ root_namespace.set_definition_join (2回目・ポストコード分)
       ├─ root_namespace.set_require_join    # 必須呼び口の結合確認
       ├─ Cell.make_cell_list2
       ├─ Cell.create_reverse_require_join   # 逆 require 結合構築
       ├─ root_namespace.set_port_reference_count
       ├─ root_namespace.check_join          # 結合整合性チェック（シグニチャ一致等）
       └─ root_namespace.check_ref_but_undef # 参照されているが未定義のセルチェック
```

### 3.3 run2（最適化 + コード生成）

```
run2（リンクルート Region ごとに繰り返し）
  │
  ├─ optimize_and_generate（$unopt == false の場合）
  │    ├─ root_namespace.reset_optimize      # 最適化フラグリセット
  │    ├─ root_namespace.set_cell_id_and_domain  # セル ID 割付・ドメイン設定
  │    ├─ root_namespace.optimize            # 呼び口最適化 + 受け口最適化
  │    └─ root_namespace.generate            # C コード生成（generate.rb）
  │         ├─ 各 Celltype の _tecsgen.h / _factory.h 生成
  │         ├─ 各 Celltype の _templ.c / _inline_templ.h 生成
  │         └─ tecsgen.cfg 生成（ファクトリ出力）
  │
  └─ finalize
       ├─ AppFile.update   # 変更のあったファイルのみ上書き（不変なら timestamp 保持）
       └─ print_report     # エラー・警告件数出力
```

---

## 4. クラス設計

### 4.1 クラス階層

```
Node                            # 基底クラス（locale 管理・エラー出力）
  ├── BDNode                    # Born-from-Declaration Node（名前・大域名管理）
  │     ├── NSBDNode            # Namespace/BDNode（ネームスペース文脈）
  │     │     ├── Namespace     # 名前空間ツリーノード
  │     │     │     └── Region  # リンクルート・ドメイン・クラス
  │     │     ├── Signature     # シグニチャ定義
  │     │     ├── Celltype      # セルタイプ定義
  │     │     │     └── CompositeCelltype  # 複合セルタイプ
  │     │     └── Cell          # セルインスタンス
  │     └── Join                # 結合記述（呼び口=セル.受け口 / 属性=値）
  ├── Port                      # 呼び口・受け口定義
  ├── FuncHead                  # シグニチャ関数ヘッダ
  ├── ParamDecl                 # パラメータ宣言
  ├── Decl                      # 型・属性・変数宣言
  ├── Typedef                   # typedef 宣言
  ├── Factory                   # factory{} / FACTORY{} 記述
  └── C_EXP                     # C_EXP(式) ラッパ

Plugin                          # プラグイン基底クラス
  ├── CelltypePlugin             # セルタイププラグイン基底
  ├── SignaturePlugin            # シグニチャプラグイン基底
  ├── ThroughPlugin              # through プラグイン基底
  └── CellPlugin                 # セルプラグイン基底
```

### 4.2 Generator クラス（bnf.y.rb）

`Generator` は Singleton パターン（クラスメソッドのみ）で実装される。

| 機能 | メソッド |
|------|---------|
| エラー出力 | `Generator.error(msg, *arg)` / `error2(locale, msg, *arg)` |
| 警告出力 | `Generator.warning(msg, *arg)` / `warning2(locale, msg, *arg)` |
| 情報出力 | `Generator.info(msg, *arg)` / `info2(locale, msg, *arg)` |
| エラー件数 | `Generator.get_n_error` / `get_n_warning` / `get_n_info` |
| 現在 locale | `Generator.current_locale` → `[@file, @lineno, @col]` |
| 構文解析完了通知 | `Generator.end_all_parse` |

`@@n_error` が 0 でない場合、コード生成フェーズはスキップされる。

### 4.3 Namespace クラス

```ruby
class Namespace < NSBDNode
  @name_list          # NamedList: Signature/Celltype/Cell/Typedef/Namespace
  @struct_tag_list    # NamedList: StructType
  @namespace_list     # Namespace[]
  @signature_list     # Signature[]
  @celltype_list      # Celltype[]
  @compositecelltype_list  # CompositeCelltype[]
  @cell_list          # Cell[]（Region のみ保持）
  @typedef_list       # Typedef[]
  @decl_list          # (Typedef|StructType|EnumType)[] 順序保持
  @const_decl_list    # Decl[]
end
```

ルート名前空間は `Region.new("::")` で生成される（Namespace と Region を兼ねる）。

ネームスペーススタック（`@@namespace_stack`）で現在のパース文脈を管理する。

### 4.4 Cell クラス

```ruby
class Cell < NSBDNode
  @celltype           # Celltype | CompositeCelltype
  @join_list          # NamedList: Join（呼び口結合・属性初期化）
  @reverse_join_list  # NamedList: ReverseJoin
  @b_defined          # Bool: 定義済み（prototype との区別）
  @b_checked          # Bool: set_definition_join 完了フラグ
  @require_joined_list # {cp_name=>true}: set_require_join 済み呼び口
  @generate           # [PluginName, option, Plugin]: generate 指定子
  @generate_list      # [[PluginName, option, Plugin], ...]: 全 generate
  @entry_array_max_subscript  # {Port=>Integer}: 受け口配列の最大添数
  @referenced_port_list       # {Port=>Integer}: 受け口参照カウント
end
```

### 4.5 Join クラス

```ruby
class Join < BDNode
  # 左辺
  @name          # Symbol: 属性名 or 呼び口名
  @subscript     # nil=非配列 / -1=添数未指定 / >=0=添数
  @definition    # Port | Decl: set_definition_join で解決
  # 右辺（ポート結合の場合）
  @cell          # Cell: 右辺のセル
  @port          # Port: 右辺の受け口
  @array_member  # rhs 配列（同名初回のみ）
  @array_member2 # Join[] 配列（同名初回のみ）
  @through_list  # cp_through + region_through + ep_through
end
```

### 4.6 Plugin クラス

プラグインは `gen_cdl_file` メソッドで CDL コードを生成し、その後 import で再解析される。コード生成段階では `gen_ep_func_body` でセルタイプの受け口関数本体を生成できる。

| メソッド | 呼び出し段階 | 説明 |
|---------|------------|------|
| `initialize(plugin_arg_str, next_cell, next_cell_opt)` | 構文解析時 | インスタンス生成・引数パース |
| `set_locale(locale)` | 構文解析完了後 | エラー locale の設定 |
| `gen_cdl_file(file)` | 意味解析後（ポストコード） | CDL コードを生成 |
| `gen_ep_func_body(...)` | コード生成 | 受け口関数本体を C で生成 |
| `gen_preamble(file, ...)` | コード生成 | preamble コードを出力 |
| `gen_postamble(file, ...)` | コード生成 | postamble コードを出力 |
| `new_cell(cell)` | ポストコードパース後 | 新しいセルが生成されたとき |

---

## 5. 字句解析・構文解析

### 5.1 字句解析（tecs_lang.rb）

- `kconv` ライブラリを使用して文字コード変換（EUC / SJIS / UTF-8 / NONE）
- 環境変数 `LANG`, `TECSGEN_LANG`, `TECSGEN_FILE_LANG`, `-k` オプションで文字コードを決定
- CDL キーワードテーブル・演算子・リテラル（整数・浮動小数・文字列・文字）を処理
- `$KCODE_CDL` / `$KCONV_CDL`：CDL ファイルの文字コード
- `$KCODE_TECSGEN` / `$KCONV_TECSGEN`：tecsgen ソース自身の文字コード（UTF-8 固定）

### 5.2 構文解析（bnf.y.rb / bnf.tab.rb）

- `racc` で生成されたパーサ（LALR(1)）
- `bnf.tab.rb` はリポジトリに同梱済み（`racc` インストール不要）
- パース中にコンポーネントオブジェクトを直接インスタンス化（AST を経由しない）
- `bnf-deb.tab.rb`：デバッグ用パーサ（`-y` オプションで使用）

### 5.3 C 言語パーサ（C_parser.y.rb）

`import_C` ディレクティブで取り込む C ヘッダを解析するためのサブパーサ。

1. `cpp` コマンドを子プロセスで実行してプリプロセス済みテキストを取得
2. C_parser で型宣言・typedef・マクロ定義を CDL の型システムに変換
3. 変換結果を Namespace に登録

---

## 6. 意味解析

### 6.1 set_definition_join（結合定義解決）

CDL パース時は呼び口名・属性名が文字列のまま Join に格納されている。

`set_definition_join` は再帰的に Namespace ツリーを走査し、各 Cell の Join の左辺を解決する:
- `@name` がセルタイプのポート名 → `@definition = Port`
- `@name` がセルタイプの属性/変数名 → `@definition = Decl`
- 解決できない場合 → エラー

2回呼ばれる理由: プラグインのポストコード（`tmp_plugin_post_code.cdl`）が1回目のパース後に生成されるため、そのセルの結合解決に2回目が必要。

### 6.2 set_require_join（必須結合確認）

`optional` 指定のない呼び口で Join が存在しないものをエラーとして報告する。

### 6.3 check_join（結合整合性チェック）

結合の右辺（受け口）と左辺（呼び口）のシグニチャが一致するか検証する:
- 呼び口シグニチャ ≠ 受け口シグニチャ → エラー
- 呼び口配列サイズと受け口の対応確認
- `restrict` 指定によるリージョン間アクセス制御のチェック
- `Descriptor` 型パラメータの整合性チェック（動的結合）

### 6.4 ポストコード処理（PluginModule）

プラグインが意味解析段階で必要な追加 CDL コードを生成する仕組み。

1. `Generator.end_all_parse` 呼び出し後、各プラグインの `gen_cdl_file` を呼ぶ
2. 生成された CDL を `gen/tmp_plugin_post_code.cdl` に書き出し
3. その CDL を `Import.new` で再パース
4. 再パース後に `set_definition_join` / `check_join` を再度実行

---

## 7. 最適化（optimize.rb）

### 7.1 最適化フラグ

各 Port オブジェクトに以下のフラグが設定される:

| フラグ | 意味 |
|--------|------|
| `@b_cp_optimized` | 呼び口最適化実施済み |
| `@b_cell_unique` | 呼び先セルが1つ（CBに格納不要） |
| `@b_VMT_useless` | VMT（関数テーブル）不要 |
| `@b_skelton_useless` | スケルトン関数不要 |

### 7.2 optimize_call（呼び口最適化）

各 Celltype の呼び口について、そのセルタイプの全セルを走査して呼び先を収集する。

```
呼び先ポートが1種類のみ？
  Yes → VMT_useless = true
        呼び先セルも1つのみ？
          Yes → cell_unique = true、skeleton_useless = true
          No  → (singleton でなければ) skeleton_useless = true
  No  → 最適化なし
```

例外:
- `[dynamic]` / `[ref_desc]` 指定の呼び口 → 最適化スキップ
- 呼び口配列サイズが `[]`（可変長）→ 最適化スキップ
- `omit` (optional 未結合) → CB から省略

### 7.3 optimize_entry（受け口最適化）

呼び口最適化の結果（VMT_useless/skeleton_useless フラグ）を参照して、受け口側のスケルトン関数の要否を決定する。`--unoptimize-entry` で独立して無効化可能。

---

## 8. コード生成（generate.rb）

### 8.1 生成の起点

`root_namespace.generate` → Namespace ツリーを再帰走査 → Celltype/Cell ごとにファイルを生成。

### 8.2 ファイル出力制御（AppFile / CFile）

- `CFile`: テンポラリファイルに生成内容を書き出す
- `AppFile.update`: 生成完了後に `CFile` と既存ファイルを比較し、差分がある場合のみ上書き（タイムスタンプを不必要に更新しないことでビルドの差分を最小化）
- テンプレートファイル（`_templ.c`, `_inline_templ.h`）は `-f` オプション指定時のみ上書き

### 8.3 `_tecsgen.h` の生成

各セルタイプに対して以下の順序でコードを出力:

1. インクルードガード
2. CELLCB 型定義（属性・変数・呼び口ポインタ）
3. セルの宣言（extern）・初期化子
4. VALID_IDX / GET_CELLCB マクロ
5. 属性・変数アクセスマクロ（短縮形・通常形）
6. 呼び口関数マクロ（最適化結果により VMT 経由 or 直接呼び出し）
7. 受け口関数プロトタイプ
8. FOREACH_CELL / END_FOREACH_CELL マクロ
9. `#include "tCELLTYPE_inline.h"` のインクルード行

### 8.4 `_factory.h` の生成

- `factory{}` / `FACTORY{}` 記述から静的変数・初期化コードを生成
- `$id$` はセル名に展開（composite 内では複合セルタイプのセル名）

### 8.5 `tecsgen.cfg` の生成

- ファクトリ記述のうちカーネル設定向け出力（`TOPPERS/ASP3` の静的 API 等）
- `FACTORY{}` 記述（セルタイプ単位）と `factory{}` 記述（セル単位）の両方を処理

### 8.6 INITIALIZE_TECS() の生成

V1.3 以降常に生成される初期化マクロ。全セルタイプの CB 初期化コードを呼び出す。

---

## 9. プラグイン機構（plugin.rb / pluginModule.rb）

### 9.1 プラグインの種類

| 基底クラス | 用途 | CDL での指定位置 |
|-----------|------|----------------|
| `CelltypePlugin` | セルタイプ全体へのコード生成 | `[generate(Name, ...)]` を celltype の前 |
| `SignaturePlugin` | シグニチャへの処理 | `[generate(Name, ...)]` を signature の前 |
| `ThroughPlugin` | through 結合の透過的挿入 | セルタイプの through 指定 |
| `CellPlugin` | セル単位の処理 | セルの `[generate(Name, ...)]` |

### 9.2 プラグインのロード

`require_tecsgen_lib` が `-L` オプション→ `$RUBYLIB` → システムパスの順にサーチ。プラグインは `tecslib/plugin/` にも自動サーチされる。見つからなければ警告のみ（`b_fatal = false`）。

### 9.3 PluginModule

`PluginModule` モジュールは `Signature`, `Celltype`, `Cell` に include される。

- `@generate` / `@generate_list`：CDL の `[generate(...)]` で登録されたプラグイン情報
- `gen_plugin_post_code(file)`: 全プラグインの `gen_cdl_file` を呼んでポストコードを出力

### 9.4 プラグイン引数パース（Plugin#parse_plugin_arg）

`"key1=val1, key2=val2"` 形式をパース。値は `"..."`, `%...%`, `!...!`, `'...'` 等の複数の囲み記法に対応。`PluginArgProc` ハッシュで識別子ごとの処理を登録。

---

## 10. ファイル入出力

### 10.1 Import / import_C

- `Import.new(filename)`: CDL ファイルをキューに積んでパース
- `Import_C.new(filename)`: C ヘッダを cpp でプリプロセスして C_parser で解析
- インポート済みファイルは再インポートされない（重複チェックあり）
- `$import_path` の順にファイルを検索

### 10.2 文字コード変換（TECSIO）

`TECSIO.str_code_convert(msg, str)` でエラーメッセージに埋め込む文字列を CDL の文字コードに変換する。

---

## 11. エラー・警告処理

### 11.1 フロー

1. 構文解析中: `Generator.error/warning` → `@@n_error/@@n_warning` をインクリメント → `Console.puts` で出力
2. 意味解析中: `Node#cdl_error(msg)` → `Generator.error2(@locale, msg)` で locale 付き出力
3. プラグイン: `Plugin#cdl_error(msg)` → `@locale` が設定されていれば即出力、未設定なら `@error_backlog` に積んで `set_locale` で後出し
4. コード生成中エラー: `Generator.error("G9999 ...")` → エラーカウントのみ（生成は続行するが最終的に exit 1）

### 11.2 エラー番号体系

メッセージ本体は `"X9999 message $1 $2"` 形式（先頭に英字+数字のエラーコード）。
`TECSMsg.get_error_message` でローカライズされたメッセージに置換される。`$1`, `$2` は引数で置換。

| プレフィックス | 発生源 |
|--------------|--------|
| `G` | ジェネレータ本体（generate.rb, tecsgen.rb） |
| `P` | プラグイン共通（plugin.rb） |
| `W` | 警告（W9999 は汎用） |

---

## 12. グローバル変数一覧

| 変数 | 型 | 初期値 | 説明 |
|------|----|--------|------|
| `$gen_base` | String | `"gen"` | 生成ディレクトリ（ベース） |
| `$gen` | String | `"gen"` | 生成ディレクトリ（リンクルート別） |
| `$import_path` | String[] | `["."]` | CDL サーチパス |
| `$library_path` | String[] | `[tecsgen_base_path]` | Ruby ライブラリサーチパス |
| `$define` | String[] | `[]` | cpp マクロ定義 |
| `$cpp` | String | `"gcc -E -DTECSGEN"` | C プリプロセッサコマンド |
| `$tecspath` | String | `tecsgen_base_path/tecs` | TECS ライブラリパス |
| `$rom` | Bool | `true` | ROM サポート（CB を分離生成） |
| `$unopt` | Bool | `false` | 最適化無効（`-U`） |
| `$unopt_entry` | Bool | `false` | 受け口最適化無効（`--unoptimize-entry`） |
| `$dryrun` | Bool | `false` | ドライラン（コード生成なし） |
| `$verbose` | Bool | `false` | 詳細出力 |
| `$debug` | Bool | `false` | デバッグ出力（`-t`） |
| `$ram_initializer` | Bool | `false` | RAM 初期化コード生成（`-R`） |
| `$idx_is_id` | Bool | `false` | 全セルタイプに idx_is_id 適用 |
| `$unique_id` | Bool | `false` | セルタイプ間で連番 ID |
| `$force_overwrite` | Bool | `false` | テンプレート強制上書き（`-f`） |
| `$region_list` | Hash | `{}` | `-G` で指定したリージョン |
| `$generating_region` | Region | `nil` | 現在生成中のリンクルート |
| `$target` | String | `"tecs"` | CDL ファイル名（拡張子除く） |
| `$c_suffix` | String | `"c"` | 生成ファイルの C 拡張子 |
| `$h_suffix` | String | `"h"` | 生成ファイルのヘッダ拡張子 |
| `$kcode` | String\|nil | `nil` | CDL 文字コード（`-k`） |
| `$KCODE_CDL` | String | `"EUC"` | CDL ファイル文字コード |
| `$KCONV_CDL` | const | `Kconv::EUC` | CDL kconv 定数 |

---

## Related

- [[tecsgen外部仕様]] — CLI・入出力・エラー形式（外部から見た仕様）
- [[TECS開発]] — 開発進捗全体
- [[North Star]]
- [[reference/03-Resources/my-topic/CLAUDE|TECS Wiki]] — llm-wiki 知識ベース
- [[perf/competencies/技術文書化|技術文書化]] — 仕様書作成の competency 証拠
- [[perf/competencies/ソフトウェアアーキテクチャ|ソフトウェアアーキテクチャ]] — CDL・tecsgen 設計判断の competency 証拠
