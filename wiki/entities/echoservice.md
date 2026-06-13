---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "other"
aliases:
  - "EchoService"
  - "Echo RPC 服务"
  - "brpc Echo 服务示例"
---

## 相关实体
- [[entities/brpc|brpc]] — 托管 EchoService 示例的 RPC 框架
- [[entities/protocol-buffers|Protocol Buffers]] — 用于定义 EchoService 接口的序列化协议
- [[entities/protoc|protoc]] — Protocol Buffers 编译器，用于从 `.proto` 文件生成服务桩代码
- [[entities/myechoservice|MyEchoService]] — 实现 EchoService 接口的具体类
- [[entities/closureguard|ClosureGuard]] — 用于异步服务中管理回调生命周期的工具（页面未创建）

## 相关概念
- [[concepts/baidu_std-protocol|baidu_std-protocol]] — brpc 默认使用的通信协议
- [[concepts/streaming-rpc|流式 RPC]] — brpc 支持的流式 RPC 概念
- [[concepts/head-of-line-blocking|HOL blocking]] — 队头阻塞问题及其在 brpc 中的处理
- [[concepts/流控|流控]] — 流量控制机制
- [[concepts/空闲超时|空闲超时]] — 连接空闲超时处理
- [[concepts/同步服务|同步服务]] — 同步处理 RPC 请求的服务实现模式
- [[concepts/异步服务|异步服务]] — 异步处理 RPC 请求的服务实现模式