---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "product"
aliases:
  - "nova-pbrpc"
  - "Baidu ads union协议"
  - "NovaService协议"
---

## Related Entities
- [[entities/brpc|brpc]] — 承载该协议的 RPC 框架
- [[entities/baidu|baidu]] — 协议发源组织
- [[entities/nshead_mcpack|nshead_mcpack]] — 同类 nshead 基础协议
- [[entities/hulu_pbrpc|hulu_pbrpc]] — 对比级同类协议
- [[entities/sofa_pbrpc|sofa_pbrpc]] — 对比级同类协议
- [[entities/public_pbrpc|public_pbrpc]] — 对比级同类协议
- [[entities/serviceoptions|serviceoptions]] — 启用配置涉及 `ServerOptions` 结构体

## Related Concepts
- [[concepts/protobuf|protobuf]] — 协议序列化基础
- [[concepts/协议自动检测|协议自动检测]] — brpc 用于识别协议的机制
- [[concepts/nshead|nshead]] — 协议头部格式
- [[concepts/brpc_server|brpc Server]] — 承载该协议的服务器组件
- [[concepts/serveroptions|ServerOptions]] — 启用该协议的配置选项

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Protocol of Baidu ads union, shown as 'nova_pbrpc', disabled by default."
> - "#include <brpc/policy/nova_pbrpc_protocol.h>"
> - "options.nshead_service = new brpc::policy::NovaServiceAdaptor;"