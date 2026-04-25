[「AIにコードを書かせる」だけじゃない！「AIネイティブ開発」へ移行するためのマインドセットと2つの実践手法 \(3/3\)\|CodeZine（コードジン）](https://codezine.jp/article/detail/22862?p=3)
1.###  Visual-to-Code
2.### Agentic Workflow

[スケッチが5分でReactコードに？ AI時代の新開発「Visual\-to\-Code」の実践と設計を見極めて精度を上げるコツ \(1/3\)\|CodeZine（コードジン）](https://codezine.jp/article/detail/23351)

[Build beautiful frontends with OpenAI Codex](https://www.youtube.com/watch?v=fK_bm84N7bs "Build beautiful frontends with OpenAI Codex")

学術的には「Sketch2Code」や「Design-to-Code」

Visual-to-Codeでは、人間同士のコミュニケーションのように、描いた絵を渡すだけでAIが空間情報を直接読み取ってくれます。

### なぜキーワードが重要なのか
図を簡単に描いても丁寧に描いても構造の再現精度はそれなりに高く、より精緻に制御したい場合には、キーワードの有無が重要になることがわかりました。

画像内テキストの視認性が結果に影響することは、公式も認識しています。

　つまり、私はスケッチを描いているつもりで、実は「視覚的に配置されたテキストプロンプト」を書いていたのです。そう捉えると、これは「プロンプトエンジニアリング」の延長線上にあります

AIプロトタイピングツールにおいて「[プロンプトの具体性が出力品質を左右する](https://www.nngroup.com/articles/vague-prototyping/ "プロンプトの具体性が出力品質を左右する")」
## Visual-to-Codeの精度を向上させるための工夫
### 具体的なキーワードを記述する
**具体的なライブラリ名や機能名を書き込む**
実装したい特定の機能がある場合は、略称でも構わないのでスケッチ内に明記しておくのが良さそう

### 補足のプロンプトを添える
「**画像 + キーワード + 補足プロンプト**」の組み合わせが、現在の開発における基本形

### レイアウトの細部には固執しない




