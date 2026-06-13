---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[entities/rdmaendpoint]]"]
tags: [term]
aliases:
  - "轮询完成队列"
  - "PollCq 调用"
---

# PollCq

## 定义
PollCq（轮询完成队列）是 RDMA（远程直接内存访问）编程模型中用于检查发送或接收操作是否完成的核心机制。应用程序通过调用 poll 函数从完成队列（Completion Queue, CQ）中获取已完成的工作请求（Work Completion, WC）状态。

## 关键特征
- **阻塞与非阻塞模式**：支持阻塞等待完成事件或非阻塞轮询检查。
- **批量处理能力**：单次 poll 调用可检索多个完成条目，提升 I/O 效率。
- **完成状态检查**：返回操作成功、错误或部分完成等状态码。
- **CQ 绑定**：每个完成队列与特定 QP（队列对）关联，poll 操作作用于绑定后的 CQ。

## 应用
- **高性能网络 I/O**：在 RDMA 编程中用于异步收发操作的完成确认，是驱动数据流的核心循环。
- **事件驱动模型**：配合 event channel 实现中断驱动的完成通知，平衡低延迟与低 CPU 占用。
- **用户态与内核态**：在 librdmacm 或 ibverbs 库中作为用户态 API，在 kernel bypass 场景下直接访问硬件完成队列。

## 相关概念
- [[concepts/rdma|RDMA (远程直接内存访问)]]：PollCq 是 RDMA 操作完成确认的关键步骤。
- [[concepts/completion-queue|完成队列 (Completion Queue)]]：PollCq 操作的目标数据结构。
- [[concepts/queue-pair|队列对 (Queue Pair)]]：发起 RDMA 操作的通信端点，其完成状态由 PollCq 获取。

## 相关实体
- [[entities/rdmaendpoint|rdmaendpoint]]：在 rdmaendpoint 的实现中，PollCq 被用于异步地检查已提交的 RDMA 操作是否完成。
- [[entities/block-pool|block-pool]]：使用 PollCq 机制管理内存池的释放和回收时机。
- [[entities/brpc|brpc]]：brpc 框架的 RDMA 后端实现中，PollCq 是连接管理和请求处理循环的核心组成部分。

*(No source content available for this page)*