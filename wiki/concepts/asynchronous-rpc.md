---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_backup_request]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "异步 RPC"
  - "Asynchronous RPC"
  - "Asynchronous call"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "异步访问"
  - "异步 RPC"
  - "Asynchronous RPC"
  - "Asynchronous call"
  - "异步 RPC"
  - "Asynchronous RPC"
---

## Description
异步 RPC 是 brpc 中与同步调用相对的非阻塞调用模式：调用方在 `CallMethod` 时传入一个 `done` 回调（`done->Run`），`CallMethod` 仅在请求发送完成后即返回，而不是等到 RPC 整体完成；真正收到响应或调用失败时，框架会在另一个 bthread 上触发 `done->Run()`，从而避免在同步等待期间持锁导致死锁。由于 `CallMethod` 返回时 RPC 尚未结束，`Response`、`Controller`、`done` 等对象通常必须分配在堆上，并在 `done->Run()` 中删除，否则回调可能访问到已释放的内存。`Channel` 本身在异步 `CallMethod` 返回后即可销毁（除非还有未完成的 RPC 需要访问它），而在 `SelectiveChannel` 场景下，传入的 `Request` 必须等到 RPC 完成之后才能释放。

异步 `done` 回调的常见实现方式有两种：一种是使用 `brpc::NewCallback` 生成的独立 `Closure` 对象（涉及三次内存分配），另一种是继承 `google::protobuf::Closure` 并把 `response`、`controller` 作为成员变量（仅需一次内存分配），后者在内存开销与缓存局部性上更为友好。异步 RPC 还被作为一种「备份请求」的替代实现思路进行讨论：发起两个并行的异步调用，在各自的 done 回调中互相取消，先返回的那个会取消另一个尚未完成的调用，从而实现「谁先成功谁生效」的语义。文档同时指出，这种方式会无条件地向后端发送两次请求，将后端压力翻倍，是一种「在任何维度上都不经济」的实现，因此被明确标记为「不推荐」并建议尽量避免；实际生产中应优先使用 [[concepts/backup-request|Backup Request]] 机制（如 `example/backup_request_c++`）或基于 [[concepts/selective-channel|SelectiveChannel]] 的方案。

## Related Concepts
- [[concepts/backup-request|Backup Request]]
- [[concepts/selective-channel|SelectiveChannel]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/synchronous-call|Synchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/cancel-rpc|Cancel RPC]]
- [[concepts/bthread|bthread]]
- [[concepts/newcallback|NewCallback]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/examplecancel_c++|cancel_c++ 示例]]
- [[entities/examplebackup_request_c++|backup_request_c++ 示例]]
- [[entities/exampleselective_echo_c++|SelectiveChannel 备份请求示例]]

## Mentions in Source

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "[Not Recommended] Issue two asynchronous RPC calls and join them. They cancel each other in their done callback."
> - "The problem of this method is that the program always sends two requests, doubling the pressure to back-end services. It is uneconomical in any sense and should be avoided as much as possible."

> **Source: [[sources/en_client|en_client]]**
> - "Pass a callback `done` to CallMethod, which resumes after sending request, rather than completion of RPC."
> - "Generally they should be allocated on heap and deleted in done->Run(). If they're deleted too early, done->Run() may access invalid memory."
> - "The callback runs in a different bthread, even the RPC fails just after entering CallMethod."

> **Source: [[sources/client|client]]**
> - "异步访问指的是：给CallMethod传递一个额外的回调对象done，CallMethod在发出request后就结束了，而不是在RPC结束后。"
> - "由于CallMethod结束不意味着RPC结束，response/controller仍可能被框架及done->Run()使用，它们一般得创建在堆上，并在done->Run()中删除。"
> - "发起异步请求后Channel可以立刻析构。"