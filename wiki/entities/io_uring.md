---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/rdma.md]]"]
tags: [product]
aliases:
  - "io_uring"
  - "Linux io_uring"
  - "异步I/O接口 io_uring"
---


# io_uring

## 基本信息
- Type: product
- Source: [[brpc/rdma.md]]

## 描述
io_uring 是 Linux 内核提供的一种异步 I/O 接口框架，通过共享的提交队列（Submission Queue）与完成队列（Completion Queue）实现高效的异步系统调用提交与完成事件处理，避免了传统同步 I/O 在用户态与内核态之间频繁切换带来的开销。在 brpc 的 RDMA 轮询模式下，用户可以注册一个回调函数，使得每次 RDMA CQ（Completion Queue）轮询时能够调用 io_uring 相关操作，从而实现 RDMA 网络通信与本地异步 I/O 的协同调度，进一步降低整体 I/O 处理延迟。io_uring 常与 [[entities/spdk|SPDK]] 等高性能 I/O 框架配合使用，以构建低延迟、高吞吐的数据通路。

## 相关实体
- [[entities/spdk|SPDK]]

## 相关概念
- [[concepts/轮询模式|轮询模式]]

## 来源提及
- 轮询模式下还可以设置一个回调函数，在每次轮询时调用，可以配合io_uring/spdk等使用。 — [[brpc/rdma]]