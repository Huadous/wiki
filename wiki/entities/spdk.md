---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/rdma|brpc RDMA实现与配置]]"]
tags: [product]
aliases:
  - "Storage Performance Development Kit"
  - "SPDK 存储性能开发套件"
---


# SPDK

## 基本信息
- Type: product
- Source: [[sources/rdma|brpc RDMA实现与配置]]

## 描述
SPDK（Storage Performance Development Kit）是一套用户态存储驱动框架，仅支持轮询模式（polling mode），且只能在单线程（Run To Completion）模式下执行任务，任务执行期间不允许被调度到其他线程。在 [[sources/rdma|brpc RDMA]] 的实现中，RDMA 轮询模式可以与 SPDK 配合使用，通过设置回调函数，在每次 RDMA 轮询时联动 SPDK 操作，从而在用户态完成高性能的数据存取。这种组合要求将 `rdma_edisp_unsched` 设置为 `true`，使 RDMA 事件驱动线程独占一个 [[sources/单线程反应器|bthread worker]]，不能调度其他任务，从而避免与 SPDK 的 Run To Completion 执行模型产生冲突。SPDK 通常与 [[entities/io_uring|io_uring]] 一起作为 brpc RDMA 轮询回调中的用户态驱动选项。

## 相关实体
- [[entities/io_uring|io_uring]]

## 相关概念
- 轮询模式
- verbs API

## 来源提及
- "轮询模式下还可以设置一个回调函数，在每次轮询时调用，可以配合io_uring/spdk等使用。" — [[sources/rdma|brpc RDMA实现与配置]]
- "在配合使用spdk等驱动的时候，因为spdk只支持轮询模式，并且只能在单线程使用（或者叫Run To Completion模式上使用）执行一个任务过程中不允许被调度到别的线程上，所以这时候需要设置（rdma_edisp_unsched）为true，使事件驱动程序一直占用一个worker线程，不能调度别的任务。" — [[sources/rdma|brpc RDMA实现与配置]]
---