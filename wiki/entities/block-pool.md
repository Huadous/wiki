---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "RDMA Memory Pool"
---


# Block Pool

## 基本信息
- Type: product
- Source: [[sources/en_rdma|en_rdma]]

## 描述
Block Pool是brpc为RDMA专门实现的固定大小内存池，位于`src/brpc/rdma/block_pool.cpp`。它接管了[[entities/iobuf|IOBuf]]使用的内存，避免了频繁的RDMA内存注册，从而实现真正的零拷贝。Block Pool采用多区域、多桶结构以减少并发竞争，并提供了线程局部缓存来提升性能。用户可通过多个`rdma_memory_pool_*`参数调整初始大小、增加步长、最大区域数、桶数和线程本地缓存数量。建议应用程序根据需求一次性注册足够内存。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/iobuf|IOBuf]]
- [[entities/rdmaendpoint|RdmaEndpoint]]

## 相关概念
- [[concepts/延迟|延迟]]
- [[concepts/零拷贝|零拷贝]]

## 来源提及
- "the memory used by IOBuf is taken over by the RDMA memory pool (see src/brpc/rdma/block_pool.cpp)." — [[sources/en_rdma|en_rdma]]
- "rdma_memory_pool_initial_size_mb: the initial region size of RDMA memory pool (in MB)，default is 1024" — [[sources/en_rdma|en_rdma]]
- "rdma_memory_pool_buckets: the number of buckets for avoiding mutex contention in RDMA memory pool，default is 4" — [[sources/en_rdma|en_rdma]]

## 相关页面
- RDMA 内存池为 CQ 轮询操作提供稳定内存支持，保障低延迟通信 [[concepts/cq]]