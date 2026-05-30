---
date: 2026-05-31
tags: [tecs, plugin]
type: concept
status: active
description: "tecsgenの機能を拡張するプラグイン群。カーネル対応・[[mruby-tecs]]ブリッジ・RPC・トレース等。"
---

# TECS プラグイン

TECSプラグインは、[[tecsgen]]の機能を拡張するモジュールです。

## 種類

### カーネル対応プラグイン

- [[plugin-notifier]] ([[asp3-tecs]])
- ATK1Plugin, HRP2Plugin（未作成）

### mrubyブリッジプラグイン

- [[plugin-mruby-bridge]] — MrubyBridgePlugin
- [[plugin-mruby-info-bridge]] — MrubyInfoBridgePlugin

### RPCプラグイン

- TransparentRPCPlugin, OpaqueRPCPlugin, SharedRPCPlugin（未作成）

### その他

- [[plugin-repeat-cell]] — RepeatCellPlugin
- [[plugin-c2tecs]] — C2TECSBridgePlugin
- TracePlugin, TLVTracePlugin（未作成）

## See Also

- [[tecsgen]]
- [[tecs-overview]]

## Counter-Arguments and Gaps

多くのプラグインリファレンスが未作成 (to be written)。
