---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_backup_request]]"]
tags: [method]
aliases:
  - "异步 RPC"
  - "Asynchronous RPC"
---


# Asynchronous RPC

## 定义
异步 RPC（Asynchronous RPC）是一种通过同时发起两个异步 RPC 调用并在各自的 done 回调中互相取消来实现请求备份效果的实现方式。该方法作为 [[concepts/backup-request|Backup Request]] 的一种替代实现途径，曾在 `example/cancel_c++` 示例中给出参考实现，但由于其会无条件地发出两次请求，文档明确建议尽量避免使用。

## 关键特征
- 通过发起两个并行的异步 RPC 调用来实现备份请求的效果。
- 两个调用在各自的 done 回调中互相取消，即先返回的请求会取消另一个尚未完成的请求。
- 始终会向后端服务发送两次请求，使后端压力翻倍。
- 在任何维度上看都不经济（uneconomical in any sense）。
- 文档将其标记为「不推荐」（Not Recommended），并建议尽量避免。

## 应用
- 作为 [[concepts/backup-request|Backup Request]] 的一种参考性替代实现思路，演示如何利用取消机制实现「谁先成功谁生效」的语义。
- 见 `example/cancel_c++` 示例（[[entities/examplecancel_c++|cancel_c++ 示例]]），用于了解异步取消回调的写法。
- 实际生产中应优先使用 [[concepts/backup-request|Backup Request]] 机制（如 `example/backup_request_c++`）或基于 [[concepts/selective-channel|SelectiveChannel]] 的方案，而非本方法。

## 相关概念
- [[concepts/backup-request|Backup Request]]
- [[concepts/selective-channel|SelectiveChannel]]
- [[concepts/streaming-rpc|Streaming RPC]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/examplecancel_c++|cancel_c++ 示例]]
- [[entities/examplebackup_request_c++|backup_request_c++ 示例]]
- [[entities/exampleselective_echo_c++|SelectiveChannel 备份请求示例]]

## 来源提及
- [Not Recommended] Issue two asynchronous RPC calls and join them. They cancel each other in their done callback. — [[sources/en_backup_request|en_backup_request]]
- The problem of this method is that the program always sends two requests, doubling the pressure to back-end services. It is uneconomical in any sense and should be avoided as much as possible. — [[sources/en_backup_request|en_backup_request]]