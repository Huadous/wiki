---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "google::protobuf::Closure"
  - "回调闭包"
  - "done (protobuf Closure)"
  - "google::protobuf::Closure"
  - "回调闭包"
---

## 相关概念
- [[concepts/ClosureGuard|ClosureGuard]]：brpc 提供的 RAII 封装，自动调用 `done->Run()`。
- [[concepts/异步服务|异步服务]]：利用 Closure 实现非阻塞 RPC 处理，提升系统吞吐量。
- [[concepts/同步服务|同步服务]]：同步 RPC 处理中 Closure 配合 ClosureGuard 使用，简化代码。

## 相关实体
- [[entities/brpc|brpc]]：使用 Closure 作为 RPC 处理回调的框架。
- [[entities/protocol-buffers|protocol-buffers]]：定义 Closure 抽象类的底层序列化库。
- [[entities/brpc|brpc::Controller]]：brpc 控制器，与 Closure 配合管理 RPC 处理流程。
- [[entities/brpc|brpc::Server]]：brpc 服务器，负责创建 `done` Closure 并传递给服务方法。

## 来源提及

> **Source: [[sources/en_server]]**
> - "done: Created by brpc and passed to service's CallMethod(), including all actions after leaving CallMethod(): validating response, serialization, sending back to client etc."
> - "No matter the RPC is successful or not, done->Run() must be called by user once and only once when the RPC is done."
> - "Server-side and client-side both use done to represent the continuation code after leaving CallMethod, but they're totally different..."
> - "Server-side done is created by framework, called by user after processing of the request to send back response to client."
> - "We strongly recommending using ClosureGuard to make done->Run() always be called."

> **Source: [[sources/en_server]]**
> - "No directly relevant information"