---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/rdma]]"
  - "[[brpc/rdma.md]]"
tags:
  - "other"
aliases:
  - "BlockPool内存池"
  - "RDMA内存池"
  - "brpc BlockPool"
  - "block_pool"
  - "BlockPool内存池"
  - "RDMA内存池"
  - "brpc BlockPool"
---

## Description
BlockPool 是 [[entities/brpc|brpc]] 中为 [[entities/iobuf|IOBuf]] 管理内存的统一内存池，其实现位于 `src/brpc/rdma/block_pool.cpp`。由于 [[entities/rdmaendpoint|RDMA]] 要求数据收发所使用的内存必须被注册（memory register），把对应的页表映射注册给网卡，这一操作非常耗时，因此 brpc 将整个 IOBuf 所使用的内存空间整体交给 BlockPool 统一接管，通过预注册大块内存并划分为固定大小的 Block 供 IOBuf 使用，从而在兼容 IOBuf 的情况下实现完全 [[concepts/零拷贝|零拷贝]]，避免重复的注册开销。该内存池支持动态增长，并可通过 `rdma_memory_pool_initial_size_mb`、`rdma_memory_pool_increase_size_mb`、`rdma_memory_pool_max_regions` 等参数灵活配置初始大小、增长步长和最大块数，同时支持桶数和线程本地缓存数的配置。需要注意的是，由于 IOBuf 内存池不由用户直接控制，实际使用中应根据业务需求一次性注册足够的内存池以实现性能最大化；此外，应用程序也可以自行注册内存，并通过 `IOBuf::append_user_data_with_meta` 发送数据。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/iobuf|IOBuf]]
- [[entities/rdmaendpoint|RdmaEndpoint]]

## Related Concepts
- [[concepts/内存注册|内存注册]]
- [[concepts/零拷贝|零拷贝]]
- [[concepts/内存池|内存池]]

## Mentions in Source

> **Source: [[sources/rdma|rdma]]**
> - 整个IOBuf所使用的内存空间整体由统一内存池接管(参见src/brpc/rdma/block_pool.cpp)。
> - RDMA要求数据收发所使用的内存空间必须被注册（memory register），把对应的页表映射注册给网卡，这一操作非常耗时，所以通常都会使用内存池方案来加速。
> - 注意，由于IOBuf内存池不由用户直接控制，因此实际使用中需要注意IOBuf所消耗的总内存，建议根据实际业务需求，一次性注册足够的内存池以实现性能最大化。
> - rdma_memory_pool_initial_size_mb: 内存池的初始大小，单位MB，默认1024