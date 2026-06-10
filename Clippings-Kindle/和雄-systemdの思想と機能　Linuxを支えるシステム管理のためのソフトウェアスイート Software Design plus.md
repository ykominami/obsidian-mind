---
kindle-bookId: '8140'
kindle-title: systemdの思想と機能　Linuxを支えるシステム管理のためのソフトウェアスイート Software Design plus
kindle-author: 森若 和雄
kindle-highlightsCount: 3
kindle-asin: B0CP741RX8
kindle-lastAnnotatedDate: Invalid date
kindle-bookImageUrl: 'https://m.media-amazon.com/images/I/71qs2MgKWsL._SX1024.jpg'
date: 2026-06-03
description: "Kindle 3件ハイライト: systemdの思想と機能　Linuxを支えるシステム管理のためのソフトウェアスイート Software Design plus"
tags:
  - kindle
  - clipping
---
# systemdの思想と機能　Linuxを支えるシステム管理のためのソフトウェアスイート Software Design plus
## Metadata
* Author: [森若 和雄](https://amazon.co.jp//%E6%A3%AE%E8%8B%A5-%E5%92%8C%E9%9B%84/e/B00IJ6JZT4/ref=aufs_dp_fta_an_dsk)
* ASIN: B0CP741RX8
* Reference: https://amazon.co.jp/dp/B0CP741RX8
* [Kindle link](kindle://book?action=open&asin=B0CP741RX8)

## Highlights
それぞれのディレクトリにunit fileが格納され、同じファイル名のファイルがあれば優先度が高いディレクトリにあるunit fileが使われます。このしくみを利用して、管理者が作成したunit fileでディストリビューションのパッケージが提供するunit fileを置き換えることができます。 — location: [669](kindle://book?action=open&asin=B0CP741RX8&location=669) ^ref-3166

---
unit file全体を置き換えるだけでなく、一部だけを追加するドロップインのしくみがあります。たとえば、foo.serviceに記述されている内容に一部追加するには、foo.service.dというディレクトリを作成し、その中に、追加したい部分だけが含まれた部分的なunit fileを.confという拡張子を付けて配置します。 — location: [678](kindle://book?action=open&asin=B0CP741RX8&location=678) ^ref-61679

---
unit fileですでに値が指定されているものをドロップインでもう一度指定した場合の動作はディレクティブにより異なるので、注意が必要です。 Wants や After のような依存関係／前後関係はドロップインで操作できません。 — location: [684](kindle://book?action=open&asin=B0CP741RX8&location=684) ^ref-19220

---
