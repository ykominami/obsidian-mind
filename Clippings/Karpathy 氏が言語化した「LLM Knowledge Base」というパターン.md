---
title: "Karpathy 氏が言語化した「LLM Knowledge Base」というパターン"
source: "https://dev.classmethod.jp/articles/karpathy-llm-knowledge-base/"
author:
  - "[[森茂洋]]"
published: 2026-04-05
created: 2026-04-23
description:
tags:
  - "clippings"
---
## はじめに

こんにちは、クラスメソッド製造ビジネステクノロジー部の森茂です。

2026 年 4 月 3 日、AI 研究者で「バイブコーディング（vibe coding）」の名付け親としても知られる Andrej Karpathy 氏が [Xのポスト](https://x.com/karpathy/status/2039805659525644595) で「LLM Knowledge Bases」と題した投稿をしました。1,300 万回以上の閲覧を集め、翌日には詳細なアイデアファイルが gist として公開されています。

<iframe src="https://embed.zenn.studio/card#zenn-embedded__fc90a8ab480248" frameborder="0" height="122"></iframe>

このポストに反応が大きかった理由は、多くの人がすでに似たようなことを試みていたからだと思います。Claude Code の CLAUDE.md、各 AI エージェント のルールファイル、あるいは Notion や Obsidian に自分なりのナレッジ構造を作っている人。X や Reddit、Hacker News でも「LLM にナレッジを整理させる」系の話題は以前から繰り返し盛り上がっていました。Karpathy 氏のポストは、そういった散発的な試みに名前と構造を与えてくれたように感じます。自分もそのひとりで、「ああ、自分がやっていたのはこういうことだったのか」と輪郭がはっきりした感覚がありました。

以前「 [Claude Code と暮らす](https://dev.classmethod.jp/articles/living-with-claude-code/) 」という記事でワークスペースの全体像を紹介しましたが、あれから数ヶ月でだいぶ構成は変わりました。今回はその中のナレッジ管理の部分を、Karpathy 氏のコンセプトに照らし合わせながら見直してみます。

## Karpathy の「LLM Knowledge Base」とは

まず、Karpathy 氏が何を言っているのかを整理してみます。

### LLM にナレッジの「保守」を任せる

端的に言えば、 **生のドキュメントを LLM に渡して、構造化された Markdown の wiki を「コンパイル」してもらう** というアイデアです。

RAG（Retrieval-Augmented Generation）は「質問されたときにドキュメントの断片を検索して回答する」アプローチですが、Karpathy 氏の提案はそれとは方向が異なります。質問のたびに情報を探し直すのではなく、 **あらかじめ LLM が情報を読み込んで、整理されたナレッジとして永続化しておく** 。wiki は使うたびに育っていくので、知識が複利的に蓄積されていきます。

Karpathy 氏はこれを 3 つの層で捉えています。

### 3 層アーキテクチャ

<iframe src="https://embed.zenn.studio/mermaid#zenn-embedded__e3b1411fb81a38" frameborder="0" height="760"></iframe>

**Raw sources** は、記事、論文、リポジトリ、画像など、不変の精選ドキュメントです。自分が集めてきた「生の素材」がここに入ります。Web 記事は Obsidian Web Clipper で Markdown に変換し、関連画像もローカルに落としておくと LLM が参照しやすくなるとのことです。

**Schema** は、wiki の構造や規約を定義する設定ドキュメントです。どんなカテゴリで整理するか、ファイルの命名規則はどうするか、といったルールを記述します。いわば wiki の「設計図」です。

**Wiki** は、LLM が生成した Markdown ファイル群です。Raw sources のサマリー、概念ごとのエンティティページ、それらを繋ぐバックリンクで構成されます。重要なのは、 **人間が直接書くことはほとんどない** という点。wiki は LLM の領域であり、人間はキュレーションや方向づけに集中します。

### 3 つの操作

wiki に対する操作として、Karpathy 氏は 3 つを挙げています。

**Ingest（取り込み）** は、新しいソースを処理して wiki に統合する操作です。LLM がドキュメントを読み、サマリーを書き、関連するエンティティページを更新し、index.md を改訂します。単なるインデックス化ではなく「統合」であることがポイントで、既存の知識と矛盾があればそれも解消されます。

**Query（質問）** は、wiki に対して質問を投げ、回答を得る操作です。ここが面白いところで、 **回答を新たなページとして wiki に「filing back」する** ことで、自分の探索や質問がそのまま知識として蓄積されます。使えば使うほど wiki が充実していく、というわけです。

**Lint（健全性チェック）** は、wiki 全体に対するヘルスチェックです。矛盾するデータ、古くなった主張、孤立したページ、欠落したリンクなどを LLM が検出し、修正を提案します。Karpathy 氏は「LLM は人間が退屈に感じる保守タスク——相互参照、一貫性チェック、統合の更新——を放棄しない」と書いています。ここが人間と LLM の役割分担として絶妙だなと感じます。

### 意図的な「抽象さ」

gist を読んで印象的だったのは、Karpathy 氏自身がこれを **「hacky collection of scripts」** と呼んでいることです。完成されたプロダクトでも、確立された方法論でもなく、「こういう方向性がありそうだ」という探索段階の共有。gist にも「intentionally kept a little bit abstract/vague because there are so many directions to take this in（意図的に少し抽象的/曖昧にしている。方向性がたくさんあるから）」と書かれています。

概念としては、Vannevar Bush が 1945 年に提唱した Memex（ドキュメント間の連想トレイルを辿る装置）を思い出します。80 年越しに、LLM がそれを Markdown ファイルの中で実現しつつあるのかもしれません。

## RAG とどう違うのか

Karpathy 氏のアプローチをもう少し掘り下げるために、RAG との違いを考えてみます。

RAG は、質問されるたびにドキュメントの断片を検索して LLM に渡すアプローチです。情報はクエリごとに再構成されるので、wiki のような永続的な構造は持ちません。一方、LLM Knowledge Base は、LLM が事前に情報を読み込んで構造化し、永続的な wiki として保持します。wiki はクエリごとに捨てられるのではなく、回答を filing back することで成長し続けます。

Karpathy 氏自身もこう書いています。

> I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.  
> （高度な RAG に手を伸ばす必要があると思っていたが、この程度の規模なら LLM は index ファイルとサマリーの自動維持がかなり上手で、関連データもわりと簡単に読んでくれた）

ただし、これは規模が ~100 記事、~400K words（約 40 万語）という比較的小さなスケールでの話です。ドキュメントが数千件、数百万語になると話は変わってくるかもしれません。

個人的には、「RAG か wiki か」は二択ではないと思っています。実際に両方を運用してみると、 **アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利** という使い分けに落ち着いてきました。Karpathy 氏のポストもどちらかを否定するものではなく、「RAG に飛びつく前に、シンプルな wiki でどこまでいけるか試してみたら意外といけた」という実感の共有だと受け取っています。

## 自分は Claude Code でこう組み込んでいる

ここからは自分の話です。以前の「Claude Code と暮らす」記事から数ヶ月が経ち、ワークスペースの中身はだいぶ入れ替わりましたが、「母艦ワークスペース」という骨格は変わっていません。

<iframe src="https://embed.zenn.studio/card#zenn-embedded__90fdd2bad4ed58" frameborder="0" height="122"></iframe>

Karpathy 氏の投稿を読む前から、セッション間の知識を永続化する仕組みは持っていました。Mem0 による fact 抽出やベクターDB へのドキュメント蓄積、古くなった知識を整理する監査コマンドなど。ただ、それらはあくまで LLM が検索で参照するためのもので、 **人間が読める形で構造化されたドキュメント** としては十分に整備できていませんでした。

Karpathy 氏のポストを読んで、「LLM にコンパイルさせて wiki にする」という発想がストンと腑に落ちました。既存のメモリ基盤の上に wiki 層を載せる形で `/kb-compile` というカスタムコマンドを作り、いま試しているところです。

<iframe src="https://embed.zenn.studio/mermaid#zenn-embedded__dd6db75c423ac8" frameborder="0" height="24"></iframe>

ディレクトリ構成はこんな感じです。

```
workspace/
├── knowledge/    # Raw — 日報、リサーチ、セッションログ
├── wiki/         # Compiled Wiki — LLM がコンパイルした成果物
│   ├── _index.md
│   ├── _recent.md
│   └── projects/
└── ...           # 他のワークスペース（blog、scratchpad 等）
```

Karpathy 氏のコンセプトと対応づけると、 `workspace/knowledge/` が Raw sources、各ディレクトリに置いた `CLAUDE.md` が Schema、 `workspace/wiki/` が Compiled Wiki に相当します。さらに自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて、RAG 的な検索と wiki の両方を使い分けています。

wiki の更新は `/kb-compile` というカスタムコマンドで行っています。実行すると Claude Code がプロジェクト情報を集めてきて、wiki を生成・更新します。 `/kb-compile blog` のように特定のプロジェクトだけをコンパイルすることも、 `/kb-compile --all` で全体を一括更新することもできます。Karpathy 氏の Lint に相当する `--lint` オプションもあって、矛盾検出やリンク切れチェック、古い記事の検出ができるようにしています。

実際にコンパイルされた `_index.md` の一部を見ると、こんな形です。

```markdown
## Active Projects (30)

### Infrastructure & AI Platform

| Project                 | Description                                    | Last Updated |
| ----------------------- | ---------------------------------------------- | ------------ |
| [[second-brain-server]] | Claude Code 統合メモリ基盤（Mem0 + HybridRAG） | 2026-03-31   |
| [[claude-code-hub]]     | Agent Hub（v1 運用中 + v2 Phase 1）            | 2026-02-16   |
| [[magi]]                | Multi-Agent Governance Intelligence            | 2026-03-19   |

### Edge AI & Robotics

...
```

30 プロジェクトの全体地図がひとつのファイルにまとまっていて、新しいセッションを始めるときにまずこれを見ると「いま何がどうなっているか」がすぐ掴めます。個々のプロジェクト記事にも frontmatter やバックリンクがあり、Obsidian で開けばグラフビューも使えます。

もちろん、これが正解というわけではありません。手動でコマンドを叩かないと更新されない、プロジェクト横断のトピック記事にはまだ手をつけていない、Lint の自動実行も仕組み化できていない。Karpathy 氏と同じく「hacky collection of scripts」の域を出ていないのが正直なところです。

それでも、「LLM に wiki の保守を任せる」というコンセプト自体は、実際に運用してみると思った以上に実用的でした。人間が退屈に感じるインデックス更新や相互参照の管理を LLM がやってくれるので、自分はプロジェクトの方向づけや意思決定に集中できます。

## まとめ

Karpathy 氏のポストの核心は、「LLM をコンパイラとして使う」という発想の転換だと思います。コードを書かせるだけでなく、知識の整理・構造化・保守を任せる。人間は退屈な保守タスクから解放されて、キュレーションと方向づけに集中する。

自分の場合は、セッション間の知識永続化に Mem0 + pgvector を使っていたところに、Karpathy 氏の「wiki にコンパイルする」という発想を載せてみました。まだ始めたばかりで正解かはわかりません。ただ、LLM に「このフォルダをまとめて」と頼んでみたときの「あ、これでいいのか」という感覚は、試してみないと得られないものでした。

Karpathy 氏は gist の中でこう書いています。

> I think there is room here for an incredible new product instead of a hacky collection of scripts.  
> （hacky なスクリプトの寄せ集めではなく、ここには素晴らしいプロダクトが生まれる余地がある）