---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/rdma]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/rdma.md]]"
  - "[[brpc/iobuf.md]]"
  - "[[brpc/http_client.md]]"
  - "[[brpc/en_iobuf.md]]"
  - "[[brpc/en_client.md]]"
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
butil::IOBuf 是 brpc 中 butil 模块提供的一种非连续零拷贝缓冲数据结构，定义于 `src/butil/iobuf.h`，其接口与 `std::string` 类似但不完全相同。默认构造不分配内存，拷贝时仅复制管理结构而非底层数据，因此支持轻量级拷贝以及零拷贝 append；IOBuf 还支持从 fd 读写、与 protobuf 互操作，并可借由 IOBufBuilder 当作 `std::ostream` 使用。文档明确指出 IOBuf 不应作为程序内通用存储结构使用，较长的生命周期可能导致单个 IOBuf 锁定多个引用计数的 8K block，因此应保持较短的生命周期。在 brpc 客户端工作流中，IOBuf 是序列化数据的核心载体：Channel 根据协议选择对应的序列化回调将请求序列化写入 IOBuf，然后将 IOBuf 写入 Socket 并发送到网络；接收到的响应同样先存入 IOBuf，再由对应的协议回调进行反序列化解析，这一链路充分体现了 IOBuf 零拷贝特性对 RPC 高吞吐场景的性能贡献。在 brpc 的 RDMA 传输路径中，所有数据均以 IOBuf Block 形式承载，Block 由统一的 RDMA 内存池（见 `src/brpc/rdma/block_pool.cpp`）接管，从而在兼容 IOBuf 的前提下实现完全零拷贝；应用程序也可通过 `IOBuf::append_user_data_with_meta` 自行管理内存并使用 `rdma::RegisterMemoryForRdma`（见 `src/brpc/rdma/rdma_helper.h`）注册。IOBuf 同时是 brpc HTTP/H2 协议栈中请求与响应 body 的核心承载类型：客户端通过 `cntl.request_attachment().append(...)` 写入待 POST 的数据，回复内容则存放于 `cntl.response_attachment()`，类型均为 butil::IOBuf。在 Streaming RPC 中，IOBuf 同样作为消息载体，通过 `Stream::Write` 写入、由 `on_received_messages` 回调按写入顺序接收。需要注意的是，IOBuf 可通过 `to_string()` 转化为 std::string，但这会分配内存并拷贝全部内容，因此对性能敏感的场景应直接基于 IOBuf 处理、避免要求连续内存。此外，IOBuf 支持通过 ZeroCopyStream 接口进行零拷贝读写，进一步强化了其作为高效网络数据传输载体的定位。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]
- [[entities/blockpool|BlockPool]]
- [[entities/examplestreaming_echo_c++|examplestreaming_echo_c++]]（Streaming RPC 中使用 IOBuf 的示例）
- [[entities/butil|butil]]
- [[entities/channel|Channel]]（在客户端工作流中负责将序列化数据写入 IOBuf 并写入 Socket）
- [[entities/controller|Controller]]

## Related Concepts
- [[concepts/零拷贝|零拷贝]]
- [[concepts/零拷贝缓冲|零拷贝缓冲]]
- [[concepts/内存注册|内存注册]]
- [[concepts/内存池|内存池]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobuf-切割|IOBuf 切割]]
- [[concepts/iobuf-拼接|IOBuf 拼接]]
- [[concepts/streamingrpc|Streaming RPC]]
- [[concepts/brpccontroller|brpc::Controller]]（承载 request/response_attachment）
- [[concepts/引用计数|引用计数]]
- [[concepts/zerocopystream|ZeroCopyStream]]
- [[concepts/socketmap|SocketMap]]
- [[concepts/timeout|Timeout]]
- [[concepts/序列化|序列化]]

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

> **Source: [[sources/http_client|http_client]]**
> - "cntl.response_attachment()是回复的body，类型也是butil::IOBuf。IOBuf可通过to_string()转化为std::string，但是需要分配内存并拷贝所有内容，如果关注性能，处理过程应直接支持IOBuf，而不要求连续内存。" — [[sources/http_client|http_client]]
> - "待POST的数据应置入request_attachment()，它(butil::IOBuf)可以直接append std::string或char*。" — [[sources/http_client|http_client]]

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "brpc uses butil::IOBuf as data structure for attachment in some protocols and HTTP body." — [[sources/en_iobuf|en_iobuf]]
> - "It's a non-contiguous zero-copied buffer, proved in previous projects, and good at performance." — [[sources/en_iobuf|en_iobuf]]
> - "The interface of IOBuf is similar to std::string, but not the same." — [[sources/en_iobuf|en_iobuf]]
> - "Lifetime of IOBuf should be short, to prevent the referentially counted blocks(8K each) in IOBuf lock too many memory." — [[sources/en_iobuf|en_iobuf]]

> **Source: [[sources/en_client|en_client]]**
> - "According to protocol of the Channel, choose corresponding serialization callback to serialize request into IOBuf." — [[sources/en_client|en_client]]
> - "Write IOBuf with serialized data into the Socket and add Channel::HandleSocketFailed into id_wait_list of the Socket." — [[sources/en_client|en_client]]