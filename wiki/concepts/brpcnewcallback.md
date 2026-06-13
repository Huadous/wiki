---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "NewCallback"
  - "brpc::NewCallback()"
---

## Description
`brpc::NewCallback` 是 brpc 中将自由函数(或成员方法)与其关联的 response 对象、`brpc::Controller` 等运行时对象绑定为 `google::protobuf::Closure` 的标准方式,这些绑定对象在异步模式下通常采用堆分配。在异步 RPC 客户端发起调用时,典型用法为 `stub.some_method(cntl, &request, response, brpc::NewCallback(OnRPCDone, response, cntl));`,框架在 RPC 完成时回调 `Run()` 并在结束时自动释放该 Closure。`brpc::NewCallback` 的一个已知缺点是 response、controller、done 三者各自需要一次内存分配,共三次堆分配;为优化生命周期管理,brpc 文档建议独立 `new` response 与 Controller,再使用 `NewCallback` 装配为 done,或将 response/controller 设计为 done 的成员并一起 `new`(前者更便于控制生命周期)。由于 Protobuf 3 将 `NewCallback` 设为 `private`,brpc 在 r32035 之后将 `NewCallback` 独立到 `src/brpc/callback.h` 中并额外增加了若干重载;若代码因 `NewCallback` 编译失败,可直接用 `brpc::NewCallback` 替换 `google::protobuf::NewCallback` 作为零迁移成本的替代方案。

## Related Concepts
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/channel|Channel]]
- [[concepts/brpcjoin|brpc::Join]]
- [[concepts/protobuf-closure|protobuf::Closure]]

## Related Entities
- [[entities/brpc-controller|brpc::Controller]]
- [[entities/brpc-channel|brpc::Channel]]

## Mentions in Source
> **Source: [[sources/en_client|en_client]]**
> - "You can new these objects individually and create done by NewCallback, or make response/controller be member of done and new them together. Former one is recommended."
> - "Since protobuf 3 changes NewCallback to private, brpc puts NewCallback in src/brpc/callback.h after r32035 (and adds more overloads). If your program has compilation issues with NewCallback, replace google::protobuf::NewCallback with brpc::NewCallback."

> **Source: [[sources/client|client]]**
> - "你可以独立地创建这些对象，并使用[NewCallback](#使用NewCallback)生成done"
> - "stub.some_method(cntl, &request, response, brpc::NewCallback(OnRPCDone, response, cntl));"
> - "由于protobuf 3把NewCallback设置为私有，r32035后brpc把NewCallback独立于[src/brpc/callback.h]"
> - "No directly relevant information"