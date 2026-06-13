---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/rdma]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/rdma.md]]"
  - "[[brpc/iobuf.md]]"
tags:
  - "product"
aliases:
  - "IOBuf 缓冲区"
  - "输入输出缓冲区"
  - "butil::IOBuf"
  - "IOBuf 缓冲区"
  - "输入输出缓冲区"
---

## Description
butil::IOBuf 是 brpc 中 butil 模块提供的一种非连续零拷贝缓冲数据结构，定义于 `src/butil/iobuf.h`。它的接口与 `std::string` 类似但不完全相同，是 brpc 在部分协议中传输附件和 HTTP body 的核心数据结构。IOBuf 默认构造不分配内存，拷贝时仅复制管理结构而非底层数据，因此支持轻量级拷贝以及零拷贝 append；同时支持从 fd 读写、与 protobuf 互操作，以及通过 IOBufBuilder 当作 `std::ostream` 使用。文档明确指出 IOBuf 不应作为程序内通用存储结构使用，较长的生命周期可能导致单个 IOBuf 锁定多个 8K 的 block，因此应保持较短的生命周期。在 brpc 内部，所有数据的收发都使用 IOBuf，并通过 RDMA 内存池（见 `src/brpc/rdma/block_pool.cpp`）统一接管其内存空间，从而在兼容 IOBuf 的情况下实现完全零拷贝。应用程序也可自行管理内存，通过 `IOBuf::append_user_data_with_meta` 把数据发送出去，并使用 `rdma::RegisterMemoryForRdma` 注册内存（见 `src/brpc/rdma/rdma_helper.h`）。在 Streaming RPC 中，IOBuf 同时作为消息载体，通过 `Stream::Write` 写入、由 `on_received_messages` 回调按写入顺序接收。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]
- [[entities/blockpool|BlockPool]]
- [[entities/examplestreaming_echo_c++|examplestreaming_echo_c++]]（Streaming RPC 中使用 IOBuf 的示例）

## Related Concepts
- [[concepts/零拷贝|零拷贝]]
- [[concepts/零拷贝缓冲|零拷贝缓冲]]
- [[concepts/内存注册|内存注册]]
- [[concepts/内存池|内存池]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobuf-切割|IOBuf 切割]]
- [[concepts/iobuf-拼接|IOBuf 拼接]]
- [[concepts/streamingrpc|Streaming RPC]]

## Mentions in Source

> **Source: [[sources/iobuf|iobuf]]**
> - "brpc使用butil::IOBuf作为一些协议中的附件或http body的数据结构，它是一种非连续零拷贝缓冲，在其他项目中得到了验证并有出色的性能。IOBuf的接口和std::string类似，但不相同。" — [[sources/iobuf|iobuf]]
> - "可以拷贝，修改拷贝不影响原IOBuf。拷贝的是IOBuf的管理结构而不是数据。" — [[sources/iobuf|iobuf]]
> - "IOBuf应保持较短的生命周期，以避免一个IOBuf锁定了多个block (8K each)。" — [[sources/iobuf|iobuf]]

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