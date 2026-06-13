---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [term]
aliases:
  - "correlation id"
  - "调用关联ID"
  - "bthread_id"
---


# correlation_id

## 定义
correlation_id 是 brpc 客户端在每次发起 RPC 调用时为其创建的唯一标识符，本质上是一个 `bthread_id`。它用于在客户端将已发送的请求与稍后收到的 response 进行关联：当 response 返回时，框架从其中提取 correlation_id，即可在 O(1) 时间内定位到对应的 [[entities/brpc::Controller|brpc::Controller]]，而无需查询全局哈希表。RPC 结束后，correlation_id 会被销毁，并唤醒处于 Join 等待状态的线程。

## 关键特征
- 本质为 `bthread_id`，在客户端发起 RPC 时由框架创建
- 作为本次 RPC 的唯一标识，嵌入到请求与 response 的协议字段中
- 收到 response 后，通过 correlation_id 在 O(1) 时间内找到对应的 Controller，无需全局哈希查找
- 良好的多核扩展性，避免了共享哈希表带来的竞争开销
- RPC 结束后自动销毁，并唤醒正在等待该次调用完成的 Join 线程

## 应用
- 异步访问场景下，客户端需要将多个并发发出的请求与陆续到达的 response 一一对应
- 半同步及同步访问场景中，correlation_id 也用于在响应到达时定位对应的 Controller，并唤醒等待的调用线程
- 任何需要高效、无锁地匹配请求-响应的 brpc 调用路径

## 相关概念
- [[concepts/异步访问|异步访问]]
- [[concepts/半同步|半同步]]
- [[concepts/同步访问|同步访问]]

## 相关实体
- [[entities/brpc::Channel|brpc::Channel]]
- [[entities/brpc::Controller|brpc::Controller]]

## 来源提及
- 创建一个bthread_id作为本次RPC的correlation_id。 — [[sources/client|client]]
- 收到response后，提取出其中的correlation_id，在O(1)时间内找到对应的Controller。这个过程中不需要查找全局哈希表，有良好的多核扩展性。 — [[sources/client|client]]