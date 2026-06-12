---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/rdma]]"]
tags: [other]
aliases:
  - "BlockPool内存池"
  - "RDMA内存池"
  - "brpc BlockPool"
---


# BlockPool

## 基本信息
- Type: other
- Source: [[sources/rdma|rdma]]

## 描述
BlockPool是[[entities/brpc|brpc]]中为[[entities/iobuf|IOBuf]]管理内存的统一内存池，其实现位于`src/brpc/rdma/block_pool.cpp`。由于[[entities/rdmaendpoint|RDMA]]要求使用注册内存，BlockPool预先注册大块内存并划分为固定大小的Block，供IOBuf使用，从而实现[[concepts/零拷贝|零拷贝]]。该内存池支持动态增长，并可通过参数配置初始大小、增长大小、最大区域数、桶数和线程本地缓存数。BlockPool的设计避免了频繁的[[concepts/内存注册|内存注册]]操作，显著提升了性能。此外，应用程序也可以自行注册内存，并通过`IOBuf::append_user_data_with_meta`发送数据。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/iobuf|IOBuf]]
- [[entities/rdmaendpoint|RdmaEndpoint]]

## 相关概念
- [[concepts/内存注册|内存注册]]
- [[concepts/零拷贝|零拷贝]]
- [[concepts/内存池|内存池]]

## 来源提及
- 整个IOBuf所使用的内存空间整体由统一内存池接管(参见src/brpc/rdma/block_pool.cpp)。 — [[sources/rdma|rdma]]
- RDMA要求数据收发所使用的内存空间必须被注册（memory register），把对应的页表映射注册给网卡，这一操作非常耗时，所以通常都会使用内存池方案来加速。 — [[sources/rdma|rdma]]
- 注意，由于IOBuf内存池不由用户直接控制，因此实际使用中需要注意IOBuf所消耗的总内存，建议根据实际业务需求，一次性注册足够的内存池以实现性能最大化。 — [[sources/rdma|rdma]]