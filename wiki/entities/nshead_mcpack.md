---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "product"
aliases:
  - "nshead+mcpack协议"
  - "nshead_mcpack协议"
---

## Related Entities
- [[entities/brpc|brpc]] — 提供该协议支持的RPC框架
- [[entities/serviceoptions|ServerOptions]] — 通过 `nshead_service` 选项启用此协议
- [[entities/nshead_mcpack|nshead_mcpack]] — 本协议实体

## Related Concepts
- [[concepts/协议自动检测|协议自动检测]] — brpc框架自动识别请求协议类型的机制
- [[concepts/多协议支持|多协议支持]] — brpc同时支持多种RPC协议的架构特性
- [[concepts/mcpack2pb|mcpack2pb]] — 在mcpack和Protocol Buffers格式之间转换的技术
- [[concepts/baidu_std|baidu_std]] — brpc支持的另一种RPC协议
- [[concepts/HTTP/h2 协议访问|HTTP/h2 协议访问]] — brpc支持的HTTP/2访问方式
- [[concepts/JSON <=> Protobuf 转换|JSON <=> Protobuf 转换]] — JSON与Protobuf之间的转换技术
- [[concepts/brpc Server|brpc Server]] — brpc框架服务端组件，负责承载协议处理