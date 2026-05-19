---
date: 2026-05-19
description: "tecsgen（TECS コンポーネント記述コンパイラ）外部仕様書の骨子。CDL 入力・生成コード出力・CLI・プラグイン・エラー処理を対象とする。"
project: TECS
quarter: Q2-2026
status: active
tags:
  - work-note
  - tecs
  - tecsgen
  - spec
---

# tecsgen 外部仕様

> [!info] 文書状態
> **ドラフト（2026-05-19）** — 動作環境・メッセージ形式・最適化内容をコードベース調査済み（`trunk/tecsgen/`）。

## 1. 概要

### 1.1 目的

tecsgen は TECS（TOPPERS Embedded Component System）のコンポーネント記述コンパイラである。CDL（Component Description Language）で記述されたコンポーネント構成を入力として受け取り、C 言語のセルタイプ実装用コードおよびカーネル設定コードを生成する。

### 1.2 ビルドシステムにおける位置付け

```
.cdl ファイル
    ↓ tecsgen
生成コード（_tecsgen.h, _factory.h, tecsgen.cfg, テンプレート .c/.h）
    ↓ tecsmerge（手書きコードへのマージ）
セルタイプ実装コード
    ↓ C コンパイラ
実行ファイル
```

### 1.3 対象読者

- TECS を利用して組込みシステムを開発するアプリケーション開発者
- tecsgen を利用する TECS ユーザー
- TECS カーネルライブラリ（ASP3 等）の組み込み担当者

### 1.4 関連文書

| 文書 | 内容 |
|------|------|
| CDL リファレンスマニュアル | CDL 言語仕様の詳細 |
| TECS コンポーネント実装モデルリファレンスマニュアル | 生成コードの詳細 |
| TECS コンポーネント図（TCD）リファレンスマニュアル | コンポーネント図の記法 |
| tecsmerge コマンドリファレンス | tecsmerge の使い方 |
| tecsflow コマンドリファレンス | tecsflow の使い方 |

---

## 2. 動作環境

| 項目 | 内容 |
|------|------|
| 実装言語 | Ruby |
| 最小 Ruby バージョン | 1.9.2 以降（動作確認済みバージョン: 2.2.2p95） |
| 動作確認 OS | Linux (Ubuntu, Fedora)、macOS X、Windows (Cygwin)、Windows コマンドプロンプト（exerb 版） |
| 依存ライブラリ | 標準ライブラリのみ（`optparse`, `kconv`, `pp`）。構文解析器（`bnf.tab.rb`）は同梱 |
| ツールバージョン（trunk） | 1.9.0 |

---

## 3. 入力

### 3.1 CDL ファイル

- 拡張子: `.cdl`
- 文字エンコーディング: UTF-8（SJIS / EUC も対応）
- 複数ファイルを指定した場合の処理: 指定順に順次 import される（後続ファイルは前ファイルの名前空間を参照可）

#### 3.1.1 CDL 記述要素の対応状況

| CDL 要素 | 対応バージョン | 備考 |
|---------|--------------|------|
| シグニチャ記述 | 〜 V1.3 | callback / context / deviate 指定子 |
| セルタイプ記述 | 〜 V1.3 | active / singleton / generate / idx_is_id |
| 複合セルタイプ（composite） | V1.5.0 | |
| 組上げ記述（セル記述） | 〜 V1.3 | through / prototype 指定子 |
| ネームスペース（namespace） | 〜 V1.3 | |
| リージョン（region） | 〜 V1.3 | node / linkunit / domain / class |
| 呼び口制限（restrict） | V1.4.0 | |
| 動的結合（[dynamic]/[ref_desc]） | V1.4.0 | |
| ファクトリ（factory{}/FACTORY{}） | 〜 V1.3 | |
| アロケータ（send/receive） | 〜 V1.3 | |

### 3.2 C プリプロセッサ連携

`import_C` ディレクティブで C ヘッダを取り込む際、C プリプロセッサ（cpp）を使用する。

- デフォルト cpp コマンド: `gcc -E -DTECSGEN`
- 環境変数 `TECS_CPP` でデフォルトをオーバーライド可能（`-c` オプションも同様）
- `-D` / `-I` でマクロ定義・インクルードパスを指定

---

## 4. 出力

### 4.1 生成ファイル一覧

生成ディレクトリ（デフォルト: `gen/`）に以下のファイルを出力する。

| ファイル | 内容 | 種類 |
|---------|------|------|
| `tCELLTYPE_tecsgen.h` | CELLCB 型・マクロ定義・インライン関数インクルード | 自動生成（上書き） |
| `tCELLTYPE_factory.h` | ファクトリから生成される静的変数・初期化コード | 自動生成（上書き） |
| `tCELLTYPE_templ.c` | 受け口関数テンプレート（tecsmerge のソース） | 自動生成（テンプレート） |
| `tCELLTYPE_inline_templ.h` | インライン関数テンプレート | 自動生成（テンプレート） |
| `tecsgen.cfg` | ファクトリ出力（カーネル静的 API 等） | 自動生成（上書き） |
| `tecsgen.rbdmp` | tecsgen 内部モデルダンプ（tecsflow 用） | 自動生成 |

テンプレートファイル（`_templ.c`, `_templ.h`）は `-f` オプション指定時のみ上書きされる。通常は tecsmerge で既存実装コードに差分マージする。

### 4.2 セルタイプヘッダ（`_tecsgen.h`）の内容

各セルタイプに対して生成される `tCELLTYPE_tecsgen.h` が含む内容:

1. **CELLCB 型定義** — セルの属性・変数を格納する構造体
2. **マクロ定義**
   - `VALID_IDX(idx)` — IDX 正当性チェック
   - `GET_CELLCB(idx)` — CELLCB ポインタ取得
   - `ATTR_属性名` — 属性アクセス（短縮形）
   - `VAR_変数名` — 変数アクセス（短縮形）
   - `cCall_func(...)` — 呼び口関数呼び出し
   - `NCP_cCall` — 呼び口配列サイズ
   - `FOREACH_CELL(i, p_cellcb)` / `END_FOREACH_CELL` — 全セル反復
   - 通常形マクロ（`tCELLTYPE_ATTR_名前(p_cellcb)` 等）
3. **受け口関数プロトタイプ宣言**
4. **インライン関数ヘッダのインクルード**（`tCELLTYPE_inline.h`）

### 4.3 INITIALIZE_TECS() マクロ

V1.3 以降は常に生成される初期化マクロ。アプリケーションの main 関数の先頭で必ず呼び出す必要がある。呼び出しを省略した場合の動作は未定義。

### 4.4 コード生成の最適化

`-U (--unoptimize)` なしの場合（デフォルト）、tecsgen は以下の最適化を適用する:

**呼び口最適化（optimize_call）**

呼び口が参照するすべてのセルの結合先が同一ポートである場合、以下を組み合わせて適用する:

| 最適化名 | 条件 | 効果 |
|---------|------|------|
| cell_unique | 全セルが同一セル・同一ポートに結合 | CELLCB ポインタを CB に格納しない（直接アドレス） |
| VMT_useless | 全セルが同一ポートに結合 | 関数テーブル（VMT）を生成せず受け口関数を直接呼び出す |
| skeleton_useless | VMT 不要かつ cell_unique | スケルトン関数を生成しない |
| omit（省略） | `optional` で未結合 | CB から呼び口フィールドを省略 |

動的結合（`[dynamic]` / `[ref_desc]`）が適用された呼び口は最適化対象外。

**受け口最適化（optimize_entry）**

呼び口最適化の結果を使用して受け口側のスケルトン関数を省略する。`--unoptimize-entry` オプションで受け口最適化のみを個別に無効化できる。

---

## 5. コマンドラインインターフェース

### 5.1 書式

```
tecsgen [OPTION...] CDL-File
ruby PATH_TO_TECSGEN/tecsgen.rb [OPTION...] CDL-File
```

### 5.2 オプション一覧

#### ファイル処理

| オプション | デフォルト | 説明 |
|---|---|---|
| `-g, --gen=dir` | `gen` | 生成ファイルの出力ディレクトリ |
| `-f, --force-overwrite` | — | テンプレートファイルを強制上書き |

#### C プリプロセッサ

| オプション | 説明 |
|---|---|
| `-c, --cpp=cpp_cmd` | 使用する C プリプロセッサコマンド |
| `-D, --define=def` | プリプロセッサマクロ定義（複数指定可） |
| `-I, --import-path=path` | インクルードパス追加（複数指定可） |
| `-L, --library-path=path` | Ruby ライブラリパス追加 |

#### コード生成

| オプション | 説明 |
|---|---|
| `-R, --RAM-initializer` | RAM 初期化コードを生成する（`INITIALIZE_TECS()` の呼び出しが必要） |
| `-r, --ram` | RAM のみで動作するコードを生成する（ROM サポート無効） |
| `-G, --generate-region=path` | 指定リージョンのコードのみ生成 |
| `-U, --unoptimize` | 呼び口・受け口の最適化を無効化する |
| `--unoptimize-entry` | 受け口最適化のみを無効化する |
| `--c-suffix=c` | 生成 C ファイルの拡張子を指定（デフォルト: `c`） |
| `--h-suffix=h` | 生成ヘッダファイルの拡張子を指定（デフォルト: `h`） |
| `--generate-all-template` | セルが存在しないセルタイプのテンプレートも生成する |
| `--generate-no-template` | テンプレートを一切生成しない |
| `--no-default-import-path` | デフォルトのインポートパス（`TECSPATH` 配下）を追加しない |

#### 診断・その他

| オプション | 説明 |
|---|---|
| `-d, --dryrun` | 文法チェックのみ（コード生成なし） |
| `-v, --verbose` | 詳細情報を出力 |
| `-k, --kcode=code` | CDL ファイルの文字コードを指定（`euc`/`sjis`/`none`/`utf8`） |
| `-i, --idx_is_id` | 全セルタイプに `idx_is_id` を適用する |
| `-u, --unique-id` | セルタイプをまたいで連番 ID を付与する（デフォルト: セルタイプごとに 1 から） |
| `--version` | バージョンを表示して終了 |
| `--no-banner` | バナー表示を抑制する |

### 5.3 環境変数

| 変数名 | 説明 |
|--------|------|
| `TECS_CPP` | C プリプロセッサコマンドを指定（`-c` オプションより優先度が低い） |
| `TECSPATH` | TECS ライブラリパス（`tecsgen/tecs/` を指定）。mruby / RPC プラグイン使用時に必要 |
| `TECSGEN_DEFAULT_RAM` | 設定した場合、デフォルトコード生成モードを ROM → RAM に変更する |
| `TECSGEN_LANG` | 言語・文字コード指定（例: `C.UTF-8`, `ja_JP.eucJP`） |
| `TECSGEN_FILE_LANG` | CDL ファイルの文字コードのみを指定 |
| `RUBYLIB` | Ruby ライブラリパス（`-L` オプションと同等） |

### 5.4 終了ステータス

| コード | 意味 |
|--------|------|
| `0` | 正常終了 |
| `1` | エラー終了 |

---

## 6. プラグインシステム

### 6.1 概要

CDL の `[generate(PluginName, ...)]` 指定子によりプラグインを呼び出す。セルタイプレベルとセルレベルの両方でプラグインを適用できる。

### 6.2 プラグイン呼び出し規約

```tecs-cdl
// セルタイププラグイン
[generate(PluginName, sSignature, "param1=val1, param2=val2")]
celltype tMyType { ... };

// セルプラグイン（結合に対して）
cell tMyType MyCell {
    [generate(PluginName, "options")]
    cCall = OtherCell.eEntry;
};
```

### 6.3 標準付属プラグイン

| カテゴリ | プラグイン名 | 用途 |
|---------|------------|------|
| カーネル対応 | ATK1Plugin | AUTOSAR OS (ATK1) 対応 |
| カーネル対応 | HRP2Plugin | TOPPERS/HRP2 対応 |
| カーネル対応 | ASP3NotifierPlugin | ASP3 タイムイベント通知 |
| mruby ブリッジ | MrubyBridgePlugin | mruby ↔ TECS ブリッジ |
| mruby ブリッジ | MrubyInfoBridgePlugin | TECSInfo を使った mruby ブリッジ（V1.7.0） |
| トレース | TracePlugin | 通常トレース |
| トレース | TLVTracePlugin | TLV 形式トレース |
| RPC | TransparentRPCPlugin | 透過的 RPC |
| RPC | OpaqueRPCPlugin | 不透過 RPC |
| RPC | SharedRPCPlugin | 共有メモリ RPC |
| RPC | SharedOpaqueRPCPlugin | 共有メモリ不透過 RPC |
| C インタフェース | C2TECSBridgePlugin | C コード → TECS 受け口呼び出し |
| C インタフェース | TECS2CPlugin | TECS セル → C 変換 |
| 繰り返し生成 | RepeatCellPlugin | セルを count=N 回繰り返し生成 |
| 繰り返し生成 | RepeatJoinPlugin | 結合配列を count=N 回繰り返し生成 |

### 6.4 プラグイン引数の文法

プラグイン引数は `param=value` 形式のカンマ区切りリスト。値に特殊文字を含む場合は引用符で囲む。

---

## 7. エラーと警告

### 7.1 メッセージ形式

位置情報がある場合:

```
ファイル名:行番号:列番号: error: メッセージ本文
ファイル名:行番号:列番号: warning: メッセージ本文
ファイル名:行番号:列番号: info: メッセージ本文
```

位置情報がない場合（ジェネレータ内部エラー等）:

```
error: メッセージ本文
warning: メッセージ本文
```

処理終了時にエラー・警告の件数サマリを出力する:

```
N error(s)  M warning(s)
```

### 7.2 主要エラーカテゴリ

| カテゴリ | 例 |
|---------|-----|
| 構文エラー | CDL 文法違反 |
| 未解決参照 | 未定義のシグニチャ・セルタイプを参照 |
| 型不整合 | 呼び口のシグニチャと受け口のシグニチャが不一致 |
| 結合エラー | 必須の呼び口が未結合 |
| restrict 違反 | 許可されていないリージョンから受け口を呼び出し |
| プラグインエラー | プラグイン処理中のエラー |

### 7.3 警告カテゴリ

| カテゴリ | 例 |
|---------|-----|
| オプショナル呼び口の未結合 | `optional` 修飾された呼び口が未結合 |
| エラー通知未設定 | タイムイベント通知でエラー通知方法が未指定（ignoreErrors=false 時） |

---

## 8. 制約・制限

### 8.1 CDL に関する制約

| 制約 | 内容 |
|------|------|
| C_EXP の使用 | 独立した初期化子としてのみ使用可（演算式の一部には不可） |
| 動的結合の非タスクコンテキスト | unjoin() の呼び出し制限（要確認） |
| composite 内 $id$ | composite セル名に解決される（内部セルの名前ではない） |
| FOREACH_CELL ネスト | 内側ループでは通常形マクロを使用必須 |

### 8.2 生成コードに関する制約

| 制約 | 内容 |
|------|------|
| INITIALIZE_TECS() | main 先頭で必ず呼び出すこと |
| ファイル名 | セルタイプ名とファイル名を一致させること |
| インクルード順 | `_tecsgen.h` を最初にインクルードすること |

### 8.3 既知の制限

| 制限 | 内容 |
|------|------|
| Windows シンボリックリンク | Cygwin 環境では `TECSPATH` へのシンボリックリンクが動作しない |
| 文字コード | CDL ファイルの文字コードを UTF-8 以外（EUC 等）にすると、プラグインが生成するコメントが文字化けする可能性がある |
| gen ディレクトリの階層 | `-g` で階層ディレクトリを指定する場合、事前に手動でディレクトリを作成する必要がある |
| 可変長呼び口配列の最適化 | 呼び口配列サイズが `[]`（可変長）の場合、呼び口最適化は適用されない |
| `-G` オプションとリンクルート | `-G` で指定したリージョンがリンクルートでない場合、警告が出力され無視される |

---

## 9. 使用例

### 9.1 最小構成

```bash
tecsgen myapp.cdl
```

`gen/` ディレクトリに生成コードを出力する。

### 9.2 ディレクトリ指定

```bash
tecsgen -g build/gen/ myapp.cdl
```

### 9.3 カーネルヘッダを含む場合

```bash
tecsgen -I asp3/include/ -I asp3/kernel/ myapp.cdl
```

### 9.4 ドライラン（文法チェックのみ）

```bash
tecsgen -d myapp.cdl
```

### 9.5 典型的なビルドフロー

```bash
# CDL → C コード生成
tecsgen -g gen/ -I kernel/include/ app.cdl

# テンプレートを既存実装にマージ
tecsmerge -e gen/ src/

# ビルド
make
```

---

## 10. 用語集

| 用語 | 定義 |
|------|------|
| CDL | Component Description Language。TECS のコンポーネント記述言語 |
| セル | コンポーネントのインスタンス |
| セルタイプ | コンポーネントの型定義 |
| 呼び口（Call Port） | 機能を要求するポート |
| 受け口（Entry/Receptacle） | 機能を提供するポート |
| シグニチャ | 呼び口・受け口のインターフェース定義（関数ヘッダ集合） |
| CELLCB | Cell Control Block。セルの属性・変数を格納する構造体 |
| CELLIDX | Cell Index。セルを識別するインデックス |
| ファクトリ | CDL から設定ファイル（tecsgen.cfg）を生成する記述 |
| 複合セルタイプ（composite） | 複数のセルを内包するセルタイプ |
| ネームスペース（namespace） | 名前衝突を防ぐためのスコープ機能 |
| リージョン（region） | セルのレイアウト・アクセス制御単位 |
| restrict 指定子 | 受け口への呼び出しをリージョン単位で制限する |
| 動的結合（Dynamic Join） | 実行時に呼び口の結合先を切り替える機能 |

---

## Related

- [[TECS開発]] — 開発進捗全体
- [[North Star]]
- [[reference/03-Resources/my-topic/CLAUDE|TECS Wiki]] — llm-wiki 知識ベース（tecsgen-commands, cdl-language, implementation-patterns 等）
- [[perf/competencies/技術文書化|技術文書化]] — 仕様書作成の competency 証拠
- [[perf/competencies/ソフトウェアアーキテクチャ|ソフトウェアアーキテクチャ]] — CDL・tecsgen 設計判断の competency 証拠
