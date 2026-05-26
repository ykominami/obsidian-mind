---
title: "ベクトルDB不要！Pythonで構築する軽量セマンティック検索『concept-file、concept-grep』"
source: "https://zenn.dev/kiyoka/articles/concept-file-1"
author:
published: 2026-03-26
created: 2026-05-26
description:
tags:
  - "clippings"
---
[CLI](https://zenn.dev/topics/cli)
[llm](https://zenn.dev/topics/llm)
[Agent](https://zenn.dev/topics/agent)
[RAG](https://zenn.dev/topics/rag)
[tech](https://zenn.dev/tech-or-idea)

## はじめに

RAG（検索拡張生成）を試そうとすると、多くの場合「ベクトルデータベース」のセットアップが必要になります。

しかし、「プロジェクト単位でサクッと意味検索がしたい」「DockerでDBを立てるほどではない」というケースも多いはず。そんな「重厚なDBはいらないけれど、grepより賢い検索が欲しい」というニーズに応えるため、検索ツール『concept-grep』を開発しました。また、データの保存形式として、concept-fileという仕様を定義しました。

## concept-file とは？

`.concept` ファイルは、テキスト・埋め込みベクトル・来歴情報を1つのプレーンテキストファイルにまとめるフォーマットです。ベクトルDBは不要で、 `cp` でコピーすれば知識が移動し、 `cat` で中身を確認できます。

ファイルはヘッダー行（1行）とJSONボディの2セクションで構成されます。

```
+==============================+
|  ヘッダー行（1行）            |  "CNCP v1 <JSONのバイト長>\n"
+==============================+
|  JSONボディ（複数行）         |  UTF-8 の整形済みJSON
+==============================+
```

concept-fileフォーマットの詳細

JSONボディの主なフィールド：

| フィールド | 説明 |
| --- | --- |
| `concept` | 概念の名前（人間が読める識別子） |
| `version` | コンテンツのバージョン |
| `text` | テキスト本文 |
| `embedding.model` | 埋め込み生成に使ったモデル名 |
| `embedding.dim` | ベクトルの次元数 |
| `embedding.vector` | 浮動小数点数の配列 |
| `provenance` | 来歴情報（ソースURL、パイプライン等） |

実際のファイル例：

```
CNCP v1 1021
{
  "concept": "Japanese AI Startup Trends",
  "version": "1.0",
  "created_at": "2026-03-14T10:00:00Z",
  "text": "Japanese AI startups have surged since 2024...",
  "embedding": {
    "model": "text-embedding-3-small",
    "dim": 1536,
    "vector": [0.0234, -0.1823, 0.0091, ...]
  },
  "provenance": {
    "source_url": "https://example.com/article",
    "pipeline": "fetch | extract_text | summarize | embed"
  }
}
```

典型的なファイルサイズは埋め込みベクトル込みで16〜32 KB程度です。詳細な仕様は [SPEC.md](https://github.com/kiyoka/concept-file/blob/main/SPEC.md) を参照してください。

## concept-grep

一言で言えば、「意味で検索できる grep（Semantic Grep）」です。キーワードの完全一致ではなく、文章の「概念（コンセプト）」を理解して、関連度の高い順にファイルやコード片を抽出します。

### 主な特徴

| 特徴 | 説明 |
| --- | --- |
| Python実装 | 現代のAI開発と親和性が高く、環境構築も容易 |
| ゼロ・コンフィグ | ベクトルDBの構築は不要。プロジェクト内の `.concept/` ディレクトリでインデックスを管理 |
| ポータビリティ | インデックスはただのファイルなので、リポジトリと一緒に持ち運び可能 |
| ローカルLLM対応 | LM StudioなどOpenAI互換APIを利用でき、プライバシーを守りながら実行可能 |

### 使い方

導入はシンプルです。

```
# 1. インストール
pip install concept-file

# 2. インデックス作成：プロジェクト内のファイルを走査し、埋め込みベクトルを生成
concept-grep --index -r .

# 3. セマンティック検索
concept-grep "認証周りのロジック"
```

`auth` という単語がなくても、ログイン処理やトークン検証のコードを賢く探し当てます。

## 開発の動機：AIエージェントの「目」を拡張する

このツールを作った最大の理由は、AIエージェント（Claude Code や Codex など）のコンテキスト節約です。

巨大なプロジェクトをエージェントに解析させる際、全ファイルをコンテキストに放り込むと、一瞬でトークン上限に達し、コストも跳ね上がります。

`concept-grep` を「エージェントが自ら使える道具」として提供することで、以下のサイクルが可能になります。

1. エージェントが自ら `concept-grep` を実行し、関連箇所を特定。
2. 必要なコード片だけを読み込んで修正。

これにより、トークンの節約と、精度の高い回答を両立できました。

## 開発の裏話：ユーザーはエージェント

このツールの後半の機能実装は、AIエージェントにPostgreSQLの巨大ソースツリーやRubyのソースコードを解析してもらって、そこで得られた課題を一つ一つGitHub Issueにしては潰していくという方法で進めていきました。

![concept-fileのGitHub Issue一覧](https://static.zenn.studio/user-upload/deployed-images/299f239eed0f454fa39ce5a8.png?sha=9fcef7766cb3fcdadf63d5464e9a709c6f6a0e75)

- ソースコードはtree-sitterで要約してからembeddingしてはどうか
- ユニットテストのディレクトリを除外したいので、 `--exclude` が欲しい
- `*.c` だけ見たいので `--include` が欲しい
- 意味検索だけではhitしないので、grepコマンドの結果と混ぜてはどうか
- ファイル名に意味があるので、それも考慮してはどうか

といった改善要求が次々とエージェントから提案されました。

私はその指示に従ってコーディングする、いわば「AIエージェントの下僕」状態。  
結果として、人間にとってもAIにとっても使い勝手の良い、非常に合理的なツールへと進化しました。

## おわりに

「ベクトルDBを立てるほどではないけれど、高度な検索が欲しい」という隙間を埋めるツールとして、『concept-grep』はかなり面白いと感じています。

ソースコードはGitHubで公開しています。 `pip install concept-file` ですぐに使えますので、ぜひお手元のプロジェクトで「意味検索」を試してみてください。

<iframe src="https://embed.zenn.studio/card#zenn-embedded__99391f110621a" frameborder="0"></iframe>

36

27