---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/rdma]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/rdma.md]]"
tags:
  - "product"
aliases:
  - "IOBuf 缓冲区"
  - "输入输出缓冲区"
  - "butil::IOBuf"
  - "IOBuf 缓冲区"
  - "输入输出缓冲区"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]
- [[entities/blockpool|BlockPool]]
- [[entities/examplestreaming_echo_c++|examplestreaming_echo_c++]]（Streaming RPC 中使用 IOBuf 的示例）

## Related Concepts
- [[concepts/零拷贝|零拷贝]]
- [[concepts/内存注册|内存注册]]
- [[concepts/内存池|内存池]]
- [[concepts/streamingrpc|Streaming RPC]]

## Mentions in Source

> **Source: [[sources/en_rdma|en_rdma]]**
> - "All data which need to transmit is in the Blocks of IOBuf." — [[sources/en_rdma|en_rdma]]
> - "In order to realize receiving zero copy, the receive side must post receive buffers in Blocks of IOBuf, which are stored in RdmaEndpoint::_rbuf." — [[sources/en_rdma|en_rdma]]
> - "the memory used by IOBuf is taken over by the RDMA memory pool (see src/brpc/rdma/block_pool.cpp)." — [[sources/en_rdma|en_rdma]]

> **Source: [[sources/rdma|rdma]]**
> - "要发送的所有数据默认都存放在IOBuf的Block中，因此所发送的Block需要等到对端确认接收完成后才可以释放，这些Block的引用被存放于RdmaEndpoint::_sbuf中。" — [[sources/rdma|rdma]]
> - "而要实现接收零拷贝，则需要确保接受端所预提交的接收缓冲区必须直接在IOBuf的Block里面，被存放于RdmaEndpoint::_rbuf。" — [[sources/rdma|rdma]]
> - "brpc内部的数据收发都使用IOBuf，为了在兼容IOBuf的情况下实现完全零拷贝，整个IOBuf所使用的内存空间整体由统一内存池接管(参见src/brpc/rdma/block_pool.cpp)。" — [[sources/rdma|rdma]]
> - "应用程序可以自己管理内存，然后通过IOBuf::append_user_data_with_meta把数据发送出去。在这种情况下，应用程序应该自己使用rdma::RegisterMemoryForRdma注册内存（参见src/brpc/rdma/rdma_helper.h）。" — [[sources/rdma|rdma]]
> - "应用程序可以自己管理内存，然后通过IOBuf::append_user_data_with_meta把数据发送出去。" — [[sources/rdma|rdma]]

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - "Write |message| into |stream_id|. The remote-side handler will received the message by the written order" — [[sources/streaming_rpc|streaming_rpc]]
> - "virtual int on_received_messages(StreamId id, butil::IOBuf *const messages[], size_t size) = 0;" — [[sources/streaming_rpc|streaming_rpc]]