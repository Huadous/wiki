---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_http_service]]"
tags:
  - "product"
aliases:
  - "Node"
  - "Node.js运行时"
---

## Related Entities
- [[entities/redis|Redis]] — 同属单线程事件循环架构，但面向数据缓存场景
- [[entities/nginx|Nginx]] — 也使用事件驱动模型处理高并发连接
- [[entities/envoy-proxy|Envoy代理]] — 现代微服务网关，与 Node.js 可配合使用
- [[entities/grpc|gRPC]] — Node.js 支持的高性能 RPC 框架
- [[entities/brpc|brpc]] — 使用了 Node.js 的 HTTP 解析器
- [[entities/rapidjson|RapidJSON]] — 与 Node.js HTTP 解析器同为 brpc 使用的开源组件
- [[entities/http_parser|http_parser]] — Node.js 的 HTTP 解析器，被其他项目广泛复用

## Related Concepts
- [[concepts/单线程反应器|单线程反应器]] — Node.js 核心架构的理论基础
- [[concepts/事件驱动架构|事件驱动架构]] — Node.js 设计采用的事件处理模式
- [[concepts/cpu-idle-paradox|cpu-idle-paradox]] — 单线程事件循环面临低 CPU 使用率下的性能问题
- [[concepts/HTTP解析|HTTP解析]] — Node.js HTTP 解析器的核心功能

## Mentions in Source
> **Source: [[concepts/单线程反应器]]**
> - "Node.js：JavaScript 运行时也基于单线程事件循环，处理高并发 IO 请求。"

> **Source: [[sources/en_http_service|en_http_service]]**
> - "Use http parser of node.js to parse http messages, which is a lightweight, well-written, and extensively used implementation."