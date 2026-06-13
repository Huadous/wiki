---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "google::protobuf::Closure"
  - "回调闭包"
  - "done (protobuf Closure)"
  - "google::protobuf::Closure"
  - "回调闭包"
  - "protobuf::Closure"
  - "google::protobuf::Closure"
  - "回调闭包"
  - "done (protobuf Closure)"
  - "google::protobuf::Closure"
  - "回调闭包"
---

## Description
`google::protobuf::Closure` 是 Protobuf 提供的回调接口，在 brpc 的客户端与服务端共享使用但语义不同。服务端 `done` 由框架创建、用户调用，封装了离开 `CallMethod` 后的所有动作（响应校验、序列化、回传客户端等）；客户端 `done` 则由用户构造并通过 `CallMethod` 传入，RPC 结束后由 brpc 触发。为了避免忘记调用 `done->Run()`，brpc 强烈推荐使用 `ClosureGuard`（RAII）保证其一定被执行。在异步访问场景下，除了使用 `NewCallback` 生成 `done` 外，用户也可以自定义继承 `google::protobuf::Closure`，把 `Response` 和 `Controller` 作为成员变量一起 `new` 出来，从而把响应、控制器、回调三次内存分配合并为一次，以降低分配开销。同步访问中 `Closure` 则配合 `ClosureGuard` 简化同步流程控制。

## Related Concepts
- [[concepts/ClosureGuard|ClosureGuard]]：brpc 提供的 RAII 封装，自动调用 `done->Run()`。
- [[concepts/异步服务|异步服务]]：利用 Closure 实现非阻塞 RPC 处理，提升系统吞吐量。
- [[concepts/同步服务|同步服务]]：同步 RPC 处理中 Closure 配合 ClosureGuard 使用，简化代码。
- [[concepts/异步访问|异步访问]]：异步 RPC 模式下 `done`（Closure）由用户构造并传入 `CallMethod`。
- [[concepts/同步访问|同步访问]]：同步 RPC 模式下 `done->Run()` 由框架在当前调用栈内完成。

## Related Entities
- [[entities/brpc|brpc]]：使用 Closure 作为 RPC 处理回调的框架。
- [[entities/protocol-buffers|protocol-buffers]]：定义 Closure 抽象类的底层序列化库。
- [[entities/brpc|brpc::Controller]]：brpc 控制器，与 Closure 配合管理 RPC 处理流程，可作为 Closure 的成员变量以合并内存分配。
- [[entities/brpc|brpc::Server]]：brpc 服务器，负责创建 `done` Closure 并传递给服务方法。
- [[entities/brpc|brpc::Channel]]：brpc 客户端通道，异步访问时用户通过其发起 `CallMethod` 并传入 `done` Closure。

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "done: Created by brpc and passed to service's CallMethod(), including all actions after leaving CallMethod(): validating response, serialization, sending back to client etc."
> - "No matter the RPC is successful or not, done->Run() must be called by user once and only once when the RPC is done."
> - "Server-side and client-side both use done to represent the continuation code after leaving CallMethod, but they're totally different..."
> - "Server-side done is created by framework, called by user after processing of the request to send back response to client."
> - "We strongly recommending using ClosureGuard to make done->Run() always be called."

> **Source: [[sources/en_server|en_server]]**
> - "No directly relevant information"

> **Source: [[sources/client|client]]**
> - "除了使用NewCallback生成done，也可以把Response和Controller作为done的成员变量，一起new出来。"
> - "使用NewCallback的缺点是要分配三次内存：response, controller, done。如果profiler证明这儿的内存分配有瓶颈，可以考虑自己继承Closure，把response/controller作为成员变量，这样可以把三次new合并为一次。"