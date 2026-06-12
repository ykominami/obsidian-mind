---
kindle-bookId: '53870'
kindle-title: 設計から学ぶFirebase実践ガイド
kindle-author: '押野 泰平, 長谷川 健史, and 岡田 菜摘'
kindle-highlightsCount: 47
kindle-asin: B0BZHTJ75M
kindle-lastAnnotatedDate: Invalid date
kindle-bookImageUrl: 'https://m.media-amazon.com/images/I/81Kwap4xelL._SX1024.jpg'
date: 2026-06-03T00:00:00.000Z
description: 'Kindle 47件ハイライト: 設計から学ぶFirebase実践ガイド'
tags:
  - kindle
  - clipping
---
# 設計から学ぶFirebase実践ガイド
## Metadata
* Author: [押野 泰平, 長谷川 健史, and 岡田 菜摘](https://amazon.co.jp/javascript:void(0))
* ASIN: B0BZHTJ75M
* Reference: https://amazon.co.jp/dp/B0BZHTJ75M
* [Kindle link](kindle://book?action=open&asin=B0BZHTJ75M)

## Highlights
もしデータの結合が必要な場合は、フロントエンド側から各コレクションへの問い合わせをそれぞれ実行し、フロントエンド側で結合する必要があります。 — location: [761](kindle://book?action=open&asin=B0BZHTJ75M&location=761) ^ref-41810

---
メッセージドキュメントとユーザードキュメントの集合をそれぞれ取得し、各ドキュメントに含まれるキーとなるフィールド値（今回の例では投稿者のドキュメントID）を比較して一致するものだけを抽出する処理を自前で実装します。 — location: [763](kindle://book?action=open&asin=B0BZHTJ75M&location=763) ^ref-42213

---
ループしながらドキュメントをリクエストしているため、リクエスト回数がデータ件数に比例して膨らんでしまいます。いわゆるN+1問題のような動きとなり、ネットワーク帯域の使用量やオーバーヘッドが大きくなります。データ件数が増えるにつれて計算量も大きくなっていくため、これをフロントエンド側、つまりエンドユーザーのブラウザー上で実行すると、ユーザーマシンのCPUやメモリリソースを逼迫し、画面描画の遅延などUXの低下につながるおそれがあります。 — location: [779](kindle://book?action=open&asin=B0BZHTJ75M&location=779) ^ref-39648

---
クライアントサイドジョインを避けるために、意図的に非正規化することが有効 — location: [791](kindle://book?action=open&asin=B0BZHTJ75M&location=791) ^ref-37267

---
Firestoreのトランザクション機能を用いて、アトミックに複数コレクションを更新する方法です。この方法は、もしメッセージドキュメントへの更新に失敗した場合はユーザードキュメントの更新もロールバックされるため、常に整合性が保証されます。NoSQLはトランザクション機能が弱いと最初に述べましたが、実はFirestoreは強い整合性を担保した読み書きの機能を有しています。複数ドキュメントを同時に更新する際は、このトランザクション機能を用いて整合性を保証することを推奨します。 — location: [809](kindle://book?action=open&asin=B0BZHTJ75M&location=809) ^ref-60326

---
ユーザードキュメントの更新時トリガー（ onUpdate トリガー）を利用してFunctionsを実行し、バックエンドで各メッセージドキュメントとデータ同期をするというものです。 — location: [814](kindle://book?action=open&asin=B0BZHTJ75M&location=814) ^ref-6049

---
トランザクションを利用する場合、各機能がユーザードキュメントを更新する際にメッセージも同時に更新するという開発上のルールを強いることになります。 — location: [818](kindle://book?action=open&asin=B0BZHTJ75M&location=818) ^ref-8436

---
Functionsを使ったバックエンドのデータ同期のデメリットとしては、トリガーを多用すると処理のつながりが見えにくくなるという点があります。また、当然トランザクションが分かれてしまうので、Functionsのデータ同期処理が終わるまでの時間はエンドユーザーから見ると更新前のデータが見えてしまい、一貫性がない状態になります。 — location: [822](kindle://book?action=open&asin=B0BZHTJ75M&location=822) ^ref-64727

---
非正規化を選ぶと読み取り時のシンプルさを手に入れた一方で、更新時のデータ整合性を保つための処理が複雑になります。読み取り頻度に比べて、書き込みの頻度が圧倒的に少ないようなユースケースではメリットを強く活かせるでしょう。 — location: [832](kindle://book?action=open&asin=B0BZHTJ75M&location=832) ^ref-12885

---
もし、データ同期が不要な場合には非正規化がとくに有効な選択肢となります。 — location: [835](kindle://book?action=open&asin=B0BZHTJ75M&location=835) ^ref-48632

---
非正規化を選ばざるを得ないユース — location: [841](kindle://book?action=open&asin=B0BZHTJ75M&location=841) ^ref-33065

---
ケースを紹介します。それは、メッセージドキュメントとユーザードキュメントのアクセス制御の要件が異なる場合です。 — location: [841](kindle://book?action=open&asin=B0BZHTJ75M&location=841) ^ref-53667

---
関係を実現するのに役立つデータモデリング機能を3つ紹介します。 ①参照型 ②サブコレクション ③コレクショングループクエリ — location: [850](kindle://book?action=open&asin=B0BZHTJ75M&location=850) ^ref-9298

---
ドキュメントID値を直接保存したくなった場合は、参照型で代替できないかも検討してみるとよいでしょう。 — location: [866](kindle://book?action=open&asin=B0BZHTJ75M&location=866) ^ref-29858

---
参照型を用いてもFirestoreのデータベース側で結合できるようになるわけではなく、依然としてクライアントサイドジョインが必要です。 — location: [869](kindle://book?action=open&asin=B0BZHTJ75M&location=869) ^ref-20739

---
参照関係の不備といったデータ不整合が発生しないようにするためには、セキュリティルールでバリデーションしたり、別途アプリケーションプログラム側で制御したりするなど、整合性を保証する必要があります。 — location: [875](kindle://book?action=open&asin=B0BZHTJ75M&location=875) ^ref-2923

---
参照型がうまく利用できるかどうかを見分ける1つの基準として、エンティティ間の依存関係の有無に着目する方法があります。 — location: [878](kindle://book?action=open&asin=B0BZHTJ75M&location=878) ^ref-63606

---
参照型は、非依存関係の表現に役立つ場合が多い — location: [888](kindle://book?action=open&asin=B0BZHTJ75M&location=888) ^ref-36422

---
ます。1つのドキュメント内に配列など複雑な構造のフィールドを持つと次のデメリットが生じます。 ・明細の追加や削除のたびに配列操作が必要となり、実装が複雑になる。 ・セキュリティルールで配列内の値に対するバリデーションを書くことが困難。 ・ドキュメントサイズが大きくなり、1度のドキュメント取得の際のオーバーヘッドが大きくなる。 ・ドキュメントサイズが大きくなり、Firestoreのドキュメントサイズ上限の制約に触れてしまうリスクが発生する。 — location: [903](kindle://book?action=open&asin=B0BZHTJ75M&location=903) ^ref-3667

---
Firestoreでは、エンティティ同士を結合させるという発想から離れ、さまざまなエンティティ間の関係をどのように階層構造に落とし込むか、という視点を持つことが重要です。なるべく結合（クライアントサイドジョイン）を選択せずに、サブコレクションをうまく利用する形にできるとFirestoreの特性を活かしやすくなります。 — location: [911](kindle://book?action=open&asin=B0BZHTJ75M&location=911) ^ref-32339

---
同名のサブコレクションを横断してドキュメント検索できる、 コレクショングループクエリ — location: [915](kindle://book?action=open&asin=B0BZHTJ75M&location=915) ^ref-15039

---
コレクショングループクエリは、Firestoreのコレクション名（今回の例だと messages）が同じサブコレクションに対して、横断的にドキュメント検索できる機能 — location: [930](kindle://book?action=open&asin=B0BZHTJ75M&location=930) ^ref-43862

---
コレクショングループクエリの注意点としては、サブコレクションの名前が一致していれば検索対象となってしまうことです。チャンネルドキュメント以下に制限できないため、サブコレクションの名前をつける際には注意が必要です。 — location: [934](kindle://book?action=open&asin=B0BZHTJ75M&location=934) ^ref-14281

---
Firestoreの機能をうまく活用して正規化を目指しつつ、結合の要件やデータアクセスの粒度で問題があれば、非正規化も視野に入れて検討するとよい — location: [943](kindle://book?action=open&asin=B0BZHTJ75M&location=943) ^ref-23757

---
基本的には一対一の場合は正規化するかどうかを決めるだけ — location: [951](kindle://book?action=open&asin=B0BZHTJ75M&location=951) ^ref-41698

---
正規化する場合は参照型を使うとシンプルになり、非正規化する場合は一方のドキュメントのMap型等でもう一方のドキュメントデータのコピーを保存 — location: [952](kindle://book?action=open&asin=B0BZHTJ75M&location=952) ^ref-20623

---
一対一の場合に限り、図2.14の左で示すような共通IDという方式も役立つ — location: [954](kindle://book?action=open&asin=B0BZHTJ75M&location=954) ^ref-53529

---
AコレクションとBコレクションが一対一である場合、Aコレクション内のあるドキュメントa1（ドキュメントIDが a1 とします）に対し、Bコレクション内のただ1つのドキュメントが紐づくことになります。このBコレクション内のドキュメントIDも a1 にそろえてしまうという方法になります。 — location: [955](kindle://book?action=open&asin=B0BZHTJ75M&location=955) ^ref-60533

---
FirestoreのドキュメントIDは、ドキュメント登録時に自動採番せずに明示的に指定することもできます。 — location: [958](kindle://book?action=open&asin=B0BZHTJ75M&location=958) ^ref-22128

---
ドキュメントIDの一意性はそのコレクション内のみで保証されるため、異なるコレクションであれば同じIDを別のドキュメントIDとして使うことができます。 — location: [959](kindle://book?action=open&asin=B0BZHTJ75M&location=959) ^ref-31851

---
同じドキュメントIDを持った異なるドキュメント同士を一対一の対応関係にあると見なせるようになります。これが共通ID方式 — location: [961](kindle://book?action=open&asin=B0BZHTJ75M&location=961) ^ref-25667

---
Firestoreのコレクションにおいては共通ID方式をとるメリットは、次の2点です。 ・一対一という関係を保証できる。 ・それぞれのコレクションに異なるアクセス制御を定義できる。 — location: [965](kindle://book?action=open&asin=B0BZHTJ75M&location=965) ^ref-10477

---
Firestoreのコレクション内にそのIDを持つドキュメントは1つしか存在できないという一意性制約を利用 — location: [969](kindle://book?action=open&asin=B0BZHTJ75M&location=969) ^ref-44181

---
ドキュメントIDはあとから変更できないため、一対一の関係性が固定である場合にのみ採用できます。 — location: [972](kindle://book?action=open&asin=B0BZHTJ75M&location=972) ^ref-19973

---
Firestoreのセキュリティルール上の制約 — location: [974](kindle://book?action=open&asin=B0BZHTJ75M&location=974) ^ref-48645

---
Firestoreのセキュリティルールは、1つのコレクションに対して異なるアクセス制御の条件を適用できません。 — location: [974](kindle://book?action=open&asin=B0BZHTJ75M&location=974) ^ref-23439

---
1つのドキュメントは、セキュリティルールの条件を満たしていれば「読める」、そうでないなら「読めない」のどちらかです。一部のフィールドだけを非公開にするような制御はできません。 — location: [979](kindle://book?action=open&asin=B0BZHTJ75M&location=979) ^ref-39358

---
ユーザー公開情報コレクションと、ユーザー個人情報コレクションに分けつつ、それぞれを別ドキュメントで扱うようにします。こうすると、ユーザー公開情報コレクションには誰でも読めるような緩い条件にしつつ、ユーザー個人情報コレクションのほうだけ厳しい条件で守ることができます。 — location: [981](kindle://book?action=open&asin=B0BZHTJ75M&location=981) ^ref-65101

---
これらの各ドキュメントのドキュメントIDを共通のユーザーIDとしておくことで、別コレクションに分割しながらも容易に結合できるようになります。 — location: [984](kindle://book?action=open&asin=B0BZHTJ75M&location=984) ^ref-29096

---
■一対多 — location: [987](kindle://book?action=open&asin=B0BZHTJ75M&location=987) ^ref-6577

---
Firestoreのもっとも基本的な構造であるサブコレクションを利用する代表的なパターンです。この方法で何か問題があった場合は、参照型や非正規化の選択肢も検討しましょう。 — location: [991](kindle://book?action=open&asin=B0BZHTJ75M&location=991) ^ref-38644

---
多対多 — location: [993](kindle://book?action=open&asin=B0BZHTJ75M&location=993) ^ref-54942

---
ます。1つのエンティティAから見ると複数のエンティティBが紐づき、また1つのエンティティBから見ても複数のエンティティAが紐づく関係です。 — location: [994](kindle://book?action=open&asin=B0BZHTJ75M&location=994) ^ref-41658

---
Firestoreの場合でも同様に、マッピングを保存する結合コレクションという方法が使えます。図の一番左のように、ドキュメント内にそれぞれのマッピングを保存するという方法です。A→Bコレクションという形で、Aコレクションから見たBドキュメントの対応関係を参照型の配列として保存しています。例として、ドキュメントa1の b-refs フィールドに/b/b1 と/b/b2 というBコレクション内の2つのドキュメントb1、b2への参照を保存しています。 — location: [998](kindle://book?action=open&asin=B0BZHTJ75M&location=998) ^ref-8663

---
主となるエンティティが決まっていれば、共通ID方式を使うとシンプルになります。主となるコレクションのドキュメントIDと、結合コレクションのドキュメントIDを同じ値にしておき、 — location: [1003](kindle://book?action=open&asin=B0BZHTJ75M&location=1003) ^ref-11148

---
主となるドキュメントから見て紐づいているエンティティのドキュメントの参照を配列で保存します。 — location: [1005](kindle://book?action=open&asin=B0BZHTJ75M&location=1005) ^ref-5525

---
そのエンティティに紐づく相手エンティティの数が増えると、ドキュメントサイズも比例して大きくなるため注意が必要 — location: [1007](kindle://book?action=open&asin=B0BZHTJ75M&location=1007) ^ref-4889

---

もしデータの結合が必要な場合は、フロントエンド側から各コレクションへの問い合わせをそれぞれ実行し、フロントエンド側で結合する必要があります。 — location: [761](kindle://book?action=open&asin=B0BZHTJ75M&location=761) ^ref-41810

---
メッセージドキュメントとユーザードキュメントの集合をそれぞれ取得し、各ドキュメントに含まれるキーとなるフィールド値（今回の例では投稿者のドキュメントID）を比較して一致するものだけを抽出する処理を自前で実装します。 — location: [763](kindle://book?action=open&asin=B0BZHTJ75M&location=763) ^ref-42213

---
ループしながらドキュメントをリクエストしているため、リクエスト回数がデータ件数に比例して膨らんでしまいます。いわゆるN+1問題のような動きとなり、ネットワーク帯域の使用量やオーバーヘッドが大きくなります。データ件数が増えるにつれて計算量も大きくなっていくため、これをフロントエンド側、つまりエンドユーザーのブラウザー上で実行すると、ユーザーマシンのCPUやメモリリソースを逼迫し、画面描画の遅延などUXの低下につながるおそれがあります。 — location: [779](kindle://book?action=open&asin=B0BZHTJ75M&location=779) ^ref-39648

---
クライアントサイドジョインを避けるために、意図的に非正規化することが有効 — location: [791](kindle://book?action=open&asin=B0BZHTJ75M&location=791) ^ref-37267

---
Firestoreのトランザクション機能を用いて、アトミックに複数コレクションを更新する方法です。この方法は、もしメッセージドキュメントへの更新に失敗した場合はユーザードキュメントの更新もロールバックされるため、常に整合性が保証されます。NoSQLはトランザクション機能が弱いと最初に述べましたが、実はFirestoreは強い整合性を担保した読み書きの機能を有しています。複数ドキュメントを同時に更新する際は、このトランザクション機能を用いて整合性を保証することを推奨します。 — location: [809](kindle://book?action=open&asin=B0BZHTJ75M&location=809) ^ref-60326

---
ユーザードキュメントの更新時トリガー（ onUpdate トリガー）を利用してFunctionsを実行し、バックエンドで各メッセージドキュメントとデータ同期をするというものです。 — location: [814](kindle://book?action=open&asin=B0BZHTJ75M&location=814) ^ref-6049

---
トランザクションを利用する場合、各機能がユーザードキュメントを更新する際にメッセージも同時に更新するという開発上のルールを強いることになります。 — location: [818](kindle://book?action=open&asin=B0BZHTJ75M&location=818) ^ref-8436

---
Functionsを使ったバックエンドのデータ同期のデメリットとしては、トリガーを多用すると処理のつながりが見えにくくなるという点があります。また、当然トランザクションが分かれてしまうので、Functionsのデータ同期処理が終わるまでの時間はエンドユーザーから見ると更新前のデータが見えてしまい、一貫性がない状態になります。 — location: [822](kindle://book?action=open&asin=B0BZHTJ75M&location=822) ^ref-64727

---
非正規化を選ぶと読み取り時のシンプルさを手に入れた一方で、更新時のデータ整合性を保つための処理が複雑になります。読み取り頻度に比べて、書き込みの頻度が圧倒的に少ないようなユースケースではメリットを強く活かせるでしょう。 — location: [832](kindle://book?action=open&asin=B0BZHTJ75M&location=832) ^ref-12885

---
もし、データ同期が不要な場合には非正規化がとくに有効な選択肢となります。 — location: [835](kindle://book?action=open&asin=B0BZHTJ75M&location=835) ^ref-48632

---
非正規化を選ばざるを得ないユース — location: [841](kindle://book?action=open&asin=B0BZHTJ75M&location=841) ^ref-33065

---
ケースを紹介します。それは、メッセージドキュメントとユーザードキュメントのアクセス制御の要件が異なる場合です。 — location: [841](kindle://book?action=open&asin=B0BZHTJ75M&location=841) ^ref-53667

---
関係を実現するのに役立つデータモデリング機能を3つ紹介します。 ①参照型 ②サブコレクション ③コレクショングループクエリ — location: [850](kindle://book?action=open&asin=B0BZHTJ75M&location=850) ^ref-9298

---
ドキュメントID値を直接保存したくなった場合は、参照型で代替できないかも検討してみるとよいでしょう。 — location: [866](kindle://book?action=open&asin=B0BZHTJ75M&location=866) ^ref-29858

---
参照型を用いてもFirestoreのデータベース側で結合できるようになるわけではなく、依然としてクライアントサイドジョインが必要です。 — location: [869](kindle://book?action=open&asin=B0BZHTJ75M&location=869) ^ref-20739

---
参照関係の不備といったデータ不整合が発生しないようにするためには、セキュリティルールでバリデーションしたり、別途アプリケーションプログラム側で制御したりするなど、整合性を保証する必要があります。 — location: [875](kindle://book?action=open&asin=B0BZHTJ75M&location=875) ^ref-2923

---
参照型がうまく利用できるかどうかを見分ける1つの基準として、エンティティ間の依存関係の有無に着目する方法があります。 — location: [878](kindle://book?action=open&asin=B0BZHTJ75M&location=878) ^ref-63606

---
参照型は、非依存関係の表現に役立つ場合が多い — location: [888](kindle://book?action=open&asin=B0BZHTJ75M&location=888) ^ref-36422

---
ます。1つのドキュメント内に配列など複雑な構造のフィールドを持つと次のデメリットが生じます。 ・明細の追加や削除のたびに配列操作が必要となり、実装が複雑になる。 ・セキュリティルールで配列内の値に対するバリデーションを書くことが困難。 ・ドキュメントサイズが大きくなり、1度のドキュメント取得の際のオーバーヘッドが大きくなる。 ・ドキュメントサイズが大きくなり、Firestoreのドキュメントサイズ上限の制約に触れてしまうリスクが発生する。 — location: [903](kindle://book?action=open&asin=B0BZHTJ75M&location=903) ^ref-3667

---
Firestoreでは、エンティティ同士を結合させるという発想から離れ、さまざまなエンティティ間の関係をどのように階層構造に落とし込むか、という視点を持つことが重要です。なるべく結合（クライアントサイドジョイン）を選択せずに、サブコレクションをうまく利用する形にできるとFirestoreの特性を活かしやすくなります。 — location: [911](kindle://book?action=open&asin=B0BZHTJ75M&location=911) ^ref-32339

---
同名のサブコレクションを横断してドキュメント検索できる、 コレクショングループクエリ — location: [915](kindle://book?action=open&asin=B0BZHTJ75M&location=915) ^ref-15039

---
コレクショングループクエリは、Firestoreのコレクション名（今回の例だと messages）が同じサブコレクションに対して、横断的にドキュメント検索できる機能 — location: [930](kindle://book?action=open&asin=B0BZHTJ75M&location=930) ^ref-43862

---
コレクショングループクエリの注意点としては、サブコレクションの名前が一致していれば検索対象となってしまうことです。チャンネルドキュメント以下に制限できないため、サブコレクションの名前をつける際には注意が必要です。 — location: [934](kindle://book?action=open&asin=B0BZHTJ75M&location=934) ^ref-14281

---
Firestoreの機能をうまく活用して正規化を目指しつつ、結合の要件やデータアクセスの粒度で問題があれば、非正規化も視野に入れて検討するとよい — location: [943](kindle://book?action=open&asin=B0BZHTJ75M&location=943) ^ref-23757

---
基本的には一対一の場合は正規化するかどうかを決めるだけ — location: [951](kindle://book?action=open&asin=B0BZHTJ75M&location=951) ^ref-41698

---
正規化する場合は参照型を使うとシンプルになり、非正規化する場合は一方のドキュメントのMap型等でもう一方のドキュメントデータのコピーを保存 — location: [952](kindle://book?action=open&asin=B0BZHTJ75M&location=952) ^ref-20623

---
一対一の場合に限り、図2.14の左で示すような共通IDという方式も役立つ — location: [954](kindle://book?action=open&asin=B0BZHTJ75M&location=954) ^ref-53529

---
AコレクションとBコレクションが一対一である場合、Aコレクション内のあるドキュメントa1（ドキュメントIDが a1 とします）に対し、Bコレクション内のただ1つのドキュメントが紐づくことになります。このBコレクション内のドキュメントIDも a1 にそろえてしまうという方法になります。 — location: [955](kindle://book?action=open&asin=B0BZHTJ75M&location=955) ^ref-60533

---
FirestoreのドキュメントIDは、ドキュメント登録時に自動採番せずに明示的に指定することもできます。 — location: [958](kindle://book?action=open&asin=B0BZHTJ75M&location=958) ^ref-22128

---
ドキュメントIDの一意性はそのコレクション内のみで保証されるため、異なるコレクションであれば同じIDを別のドキュメントIDとして使うことができます。 — location: [959](kindle://book?action=open&asin=B0BZHTJ75M&location=959) ^ref-31851

---
同じドキュメントIDを持った異なるドキュメント同士を一対一の対応関係にあると見なせるようになります。これが共通ID方式 — location: [961](kindle://book?action=open&asin=B0BZHTJ75M&location=961) ^ref-25667

---
Firestoreのコレクションにおいては共通ID方式をとるメリットは、次の2点です。 ・一対一という関係を保証できる。 ・それぞれのコレクションに異なるアクセス制御を定義できる。 — location: [965](kindle://book?action=open&asin=B0BZHTJ75M&location=965) ^ref-10477

---
Firestoreのコレクション内にそのIDを持つドキュメントは1つしか存在できないという一意性制約を利用 — location: [969](kindle://book?action=open&asin=B0BZHTJ75M&location=969) ^ref-44181

---
ドキュメントIDはあとから変更できないため、一対一の関係性が固定である場合にのみ採用できます。 — location: [972](kindle://book?action=open&asin=B0BZHTJ75M&location=972) ^ref-19973

---
Firestoreのセキュリティルール上の制約 — location: [974](kindle://book?action=open&asin=B0BZHTJ75M&location=974) ^ref-48645

---
Firestoreのセキュリティルールは、1つのコレクションに対して異なるアクセス制御の条件を適用できません。 — location: [974](kindle://book?action=open&asin=B0BZHTJ75M&location=974) ^ref-23439

---
1つのドキュメントは、セキュリティルールの条件を満たしていれば「読める」、そうでないなら「読めない」のどちらかです。一部のフィールドだけを非公開にするような制御はできません。 — location: [979](kindle://book?action=open&asin=B0BZHTJ75M&location=979) ^ref-39358

---
ユーザー公開情報コレクションと、ユーザー個人情報コレクションに分けつつ、それぞれを別ドキュメントで扱うようにします。こうすると、ユーザー公開情報コレクションには誰でも読めるような緩い条件にしつつ、ユーザー個人情報コレクションのほうだけ厳しい条件で守ることができます。 — location: [981](kindle://book?action=open&asin=B0BZHTJ75M&location=981) ^ref-65101

---
これらの各ドキュメントのドキュメントIDを共通のユーザーIDとしておくことで、別コレクションに分割しながらも容易に結合できるようになります。 — location: [984](kindle://book?action=open&asin=B0BZHTJ75M&location=984) ^ref-29096

---
■一対多 — location: [987](kindle://book?action=open&asin=B0BZHTJ75M&location=987) ^ref-6577

---
Firestoreのもっとも基本的な構造であるサブコレクションを利用する代表的なパターンです。この方法で何か問題があった場合は、参照型や非正規化の選択肢も検討しましょう。 — location: [991](kindle://book?action=open&asin=B0BZHTJ75M&location=991) ^ref-38644

---
多対多 — location: [993](kindle://book?action=open&asin=B0BZHTJ75M&location=993) ^ref-54942

---
ます。1つのエンティティAから見ると複数のエンティティBが紐づき、また1つのエンティティBから見ても複数のエンティティAが紐づく関係です。 — location: [994](kindle://book?action=open&asin=B0BZHTJ75M&location=994) ^ref-41658

---
Firestoreの場合でも同様に、マッピングを保存する結合コレクションという方法が使えます。図の一番左のように、ドキュメント内にそれぞれのマッピングを保存するという方法です。A→Bコレクションという形で、Aコレクションから見たBドキュメントの対応関係を参照型の配列として保存しています。例として、ドキュメントa1の b-refs フィールドに/b/b1 と/b/b2 というBコレクション内の2つのドキュメントb1、b2への参照を保存しています。 — location: [998](kindle://book?action=open&asin=B0BZHTJ75M&location=998) ^ref-8663

---
主となるエンティティが決まっていれば、共通ID方式を使うとシンプルになります。主となるコレクションのドキュメントIDと、結合コレクションのドキュメントIDを同じ値にしておき、 — location: [1003](kindle://book?action=open&asin=B0BZHTJ75M&location=1003) ^ref-11148

---
主となるドキュメントから見て紐づいているエンティティのドキュメントの参照を配列で保存します。 — location: [1005](kindle://book?action=open&asin=B0BZHTJ75M&location=1005) ^ref-5525

---
そのエンティティに紐づく相手エンティティの数が増えると、ドキュメントサイズも比例して大きくなるため注意が必要 — location: [1007](kindle://book?action=open&asin=B0BZHTJ75M&location=1007) ^ref-4889

---
