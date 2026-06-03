---
date: 2026-04-25
description: "AIエージェント設計パターン・ツール・論文メモ — 六色思考帽、Agent Skills、メモリ評価"
tags:
  - reference
  - ai
  - agents
---

# AI エージェント

## 六色思考帽フレームワーク（Edward de Bono）

AIエージェントチームへの応用:

| 帽子 | 役割 | 担当 |
|------|------|------|
| 白（データ） | 事実調査 | 市場データ・数値のみ報告 |
| 赤（感情） | ユーザー代弁者 | ユーザーがどう感じるか分析 |
| 黒（批判） | リスク担当 | 何が失敗しうるか徹底追及 |
| 黄（楽観） | チャンス担当 | うまくいく理由を提示 |
| 緑（創造） | アイデア担当 | 型破りな発想を5つ生成 |
| 青（統制） | まとめ役 | 全視点を統合して結論 |

### CLAUDE.md でのエージェントチーム設定 Tips
1. 手順を明確にする
2. 進捗状況をメモさせる（progress.md）

## Agent Skills（DeepMind 論文）

- 論文: "Closing the Knowledge Gap with Agent Skills" — Google DeepMind
- エージェントにスキルを持たせることで知識ギャップを埋めるアプローチ

## メモリ評価（Supermemory / MemoryBench）

- **MemoryBench**: AIメモリシステムの標準ベンチマーク
- **MemScore**: Quality・Latency・Tokens の3指標で評価

## 関連

- [[Claude-Code-教科書]] — マルチエージェント構成・タスク設計の実践
- [[AI-開発-2026-02]] — エージェントフレームワーク・ツール一覧
