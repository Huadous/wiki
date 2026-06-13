---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[brpc/en_client.md]]"
tags:
  - "project"
aliases:
  - "gRPC 框架"
---

## Related Entities
- [[entities/baidu|Baidu]]
- [[entities/curl|curl]]
- [[entities/etcd|etcd]]
- [[entities/google|Google]] （待创建，gRPC 框架的开发者）

## Related Concepts
- [[concepts/rpc|RPC]]
- [[concepts/http2|HTTP/2]]
- [[concepts/serialization|Serialization]]
- [[concepts/proto-file|.proto file]]
- [[concepts/streaming-rpc|流式 RPC (Streaming RPC)]]
- 协议自动检测
- HTTP/JSON 访问
- 跨语言服务交互
- HTTP/h2+JSON 协议访问
- 微服务架构
- 双向流
- 流控制
- 认证机制
- 重试机制
- [[concepts/h2c|h2c]]
- [[concepts/h2|h2]]
- baidu_std
- Connection Type（单连接与连接池模式）
- PROTOCOL_H2（h2 协议标识常量）
- 命名服务（Naming Service）
- 负载均衡（Load Balancing）
- 熔断（Circuit Breaking）
- Wire Protocol（gRPC 线缆协议）

## Mentions in Source

> **Source: [[sources/overview|overview]]**
- "Many projects use protocol buffers, including the following: gRPC, Google Cloud, Envoy Proxy." — [[sources/overview|overview]]
- "They are most often used for defining communications protocols (together with gRPC) and for data storage." — [[sources/overview|overview]]

> **Source: [[sources/en_server|en_server]]**
- "http/2 and gRPC, shown as 'h2c'(unencrypted) or 'h2'(encrypted), enabled by default." — [[sources/en_server|en_server]]
- "Server detects supported protocols automatically, without assignment from users." — [[sources/en_server|en_server]]

> **Source: [[sources/en_overview|en_overview]]**
- "restful http/https, [h2](https://http2.github.io/http2-spec)/[gRPC](https://grpc.io). using http/h2 in brpc is much more friendly than [libcurl](https://curl.haxx.se/libcurl/)." — [[sources/en_overview|en_overview]]
- "Access protobuf-based protocols with HTTP/h2+json, probably from another language." — [[sources/en_overview|en_overview]]
- "restful http/https, h2/gRPC" — [[sources/en_overview|en_overview]]

> **Source: [[sources/en_client|en_client]]**
- "\"h2:grpc\", which is the protocol of gRPC and based on h2, using single connection by default, check out h2:grpc for details." — [[sources/en_client|en_client]]