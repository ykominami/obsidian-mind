---
kindle-bookId: '16875'
kindle-title: ソフトウェア開発にChatGPTは使えるのか？――設計からコーディングまでAIの限界を探る
kindle-author: 小野 哲
kindle-highlightsCount: 13
kindle-asin: B0C9L3DH5S
kindle-lastAnnotatedDate: Invalid date
kindle-bookImageUrl: 'https://m.media-amazon.com/images/I/71Su+FUVGhL._SX1024.jpg'
---
# ソフトウェア開発にChatGPTは使えるのか？――設計からコーディングまでAIの限界を探る
## Metadata
* Author: [小野 哲](https://amazon.co.jp//%E5%B0%8F%E9%87%8E-%E5%93%B2/e/B004LR5RVU/ref=aufs_dp_fta_an_dsk)
* ASIN: B0C9L3DH5S
* Reference: https://amazon.co.jp/dp/B0C9L3DH5S
* [Kindle link](kindle://book?action=open&asin=B0C9L3DH5S)

## Highlights
1つのアテンションメカニズムではなく、複数のアテンションメカニズムを用いることで、各単語が持つ複数の観点からの関連性を同時にとらえることが可能になり、文脈理解がより豊かになります。これがマルチヘッドアテンションの主な目的です。 — location: [515](kindle://book?action=open&asin=B0C9L3DH5S&location=515) ^ref-35079

---
マルチヘッドアテンションでは、入力の単語ベクトルが複数の異なる「ヘッド」（ — location: [517](kindle://book?action=open&asin=B0C9L3DH5S&location=517) ^ref-28726

---
メカニズムの一種）にそれぞれ投入され、各ヘッドが独自に新しいベクトルを生成します。そして、それらを結合して1つのベクトルを作り出し — location: [518](kindle://book?action=open&asin=B0C9L3DH5S&location=518) ^ref-16359

---
Concat（連結：Concatenate）という手法が用いられます。連結されたものを1つの通常のベクトルに変換し、それが最終的な出力となります。 — location: [527](kindle://book?action=open&asin=B0C9L3DH5S&location=527) ^ref-20346

---
単語どうしのリーグ戦の得点表を1冊に閉じた得点 — location: [530](kindle://book?action=open&asin=B0C9L3DH5S&location=530) ^ref-56052

---
デコーダーはエンコーダーと似たような構造をしており、同じようにアテンションメカニズムとマルチヘッドアテンションを利用 — location: [537](kindle://book?action=open&asin=B0C9L3DH5S&location=537) ^ref-6664

---
デコーダーではエンコーダーからの文脈情報とデコーダー自身がこれまでに生成したトークンの情報の2つを参照 — location: [538](kindle://book?action=open&asin=B0C9L3DH5S&location=538) ^ref-20911

---
意味 — location: [539](kindle://book?action=open&asin=B0C9L3DH5S&location=539) ^ref-50726

---
はエンコーダー側から、単語はデコーダー側 — location: [540](kindle://book?action=open&asin=B0C9L3DH5S&location=540) ^ref-46101

---
エンコーダーが各単語の文脈をとらえて生成したベクトル情報をデコーダーへ渡します。デコーダーでは、この情報と自身がこれまでに生成したトークンの情報を合わせて新たなアテンションを計算 — location: [540](kindle://book?action=open&asin=B0C9L3DH5S&location=540) ^ref-61985

---
Attention Is All You Need』 — location: [554](kindle://book?action=open&asin=B0C9L3DH5S&location=554) ^ref-20321

---
GPTはTransformerのデコーダー部分だけを使用 — location: [563](kindle://book?action=open&asin=B0C9L3DH5S&location=563) ^ref-20462

---
GPTの一番の特徴は、そのトランスフォーマーベースのデコーダーアーキテクチャを使用して、一連の単語（またはトークン）が与えられたとき、次に来る最もありそうな単語を予測する能力 — location: [572](kindle://book?action=open&asin=B0C9L3DH5S&location=572) ^ref-18790

---
