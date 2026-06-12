---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/rdma]]"
tags:
  - "product"
aliases:
  - "IOBuf 缓冲区"
  - "输入输出缓冲区"
---

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]
- [[entities/blockpool|BlockPool]]

## 相关概念
- [[concepts/零拷贝|零拷贝]]
- [[concepts/内存注册|内存注册]]
- [[concepts/内存池|内存池]]

## 来源提及
> **Source: [[sources/en_rdma|en_rdma]]**
> - "All data which need to transmit is in the Blocks of IOBuf." — [[sources/en_rdma|en_rdma]]
> - "In order to realize receiving zero copy, the receive side must post receive buffers in Blocks of IOBuf, which are stored in RdmaEndpoint::_rbuf." — [[sources/en_rdma|en_rdma]]
> - "the memory used by IOBuf is taken over by the RDMA memory pool (see src/brpc/rdma/block_pool.cpp)." — [[sources/en_rdma|en_rdma]]

> **Source: [[sources/rdma|rdma]]**
> - "要发送的所有数据默认都存放在IOBuf的Block中，因此所发送的Block需要等到对端确认接收完成后才可以释放，这些Block的引用被存放于RdmaEndpoint::_sbuf中。" — [[sources/rdma|rdma]]
> - "而要实现接收零拷贝，则需要确保接受端所预提交的接收缓冲区必须直接在IOBuf的Block里面，被存放于RdmaEndpoint::_rbuf。" — [[sources/rdma|rdma]]
> - "应用程序可以自己管理内存，然后通过IOBuf::append_user_data_with_meta把数据发送出去。" — [[sources/rdma|rdma]]

> **Source: [[sources/rdma|rdma]]**
> - 未提供与 IOBuf 直接相关的新增信息。