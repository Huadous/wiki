---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_backup_request]]"]
tags: [project]
aliases:
  - "example/backup_request_c++"
  - "backup_request_c++ 示例"
  - "brpc backup_request C++ 示例"
---


# example/backup_request_c++

## 基本信息
- Type: project
- Source: [[sources/en_backup_request]]

## 描述
example/backup_request_c++ 是 [[entities/brpc|brpc]] 仓库中的一个 C++ 代码示例项目，专门用于演示如何通过 [[entities/Channel|Channel]] 的 backup_request 机制来提升服务的可用性。示例中，客户端会在主请求发出 2ms 后若仍未收到响应即触发备份请求；服务器端则在收到偶数编号的请求时故意休眠 20ms 以模拟慢响应，从而促使客户端触发备份请求机制。从示例的运行日志可见，最终的请求延迟并不会受到服务器端故意休眠的影响；同时，通过 `/rpcz` 调用链可以清晰观察到备份请求的实际触发过程。该示例是理解 [[entities/Channel|Channel]] 级别 [[concepts/backup_request_ms|backup_request_ms]] 配置行为的参考实现，开发者可参照其代码掌握 backup_request 的接入方式与调优方法。

## 相关实体
- [[entities/brpc]]
- [[entities/Channel]]
- [[entities/ChannelOptions]]

## 相关概念
- [[concepts/backup_request]]
- [[concepts/backup_request_ms]]

## 来源提及
- Read example/backup_request_c++ as example code. — [[sources/en_backup_request|en_backup_request]]
- In this example, client sends backup request after 2ms and server sleeps for 20ms on purpose when the number of requests is even to trigger backup request. — [[sources/en_backup_request|en_backup_request]]
- Seen from the log, the latency is not affected by the server's sleeping. The `/rpcz` shows the call chain of backup request as well. — [[sources/en_backup_request|en_backup_request]]