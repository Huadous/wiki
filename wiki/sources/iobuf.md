---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/iobuf.md]]"
  - "[[brpc/http_client.md]]"
  - "[[brpc/en_iobuf.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bvar.md]]"
tags:
  - "零拷贝缓冲"
  - "IOBufBuilder"
  - "IOBuf 与 Protobuf 互操作"
  - "IOBufAsZeroCopyInputStream"
  - "IOBufAsZeroCopyOutputStream"
  - "BufHandle"
aliases:
  - "butil::IOBuf 使用指南"
  - "IOBuf 使用指南"
---

## 要点
- IOBuf 是 brpc 框架采用的非连续零拷贝缓冲数据结构，定义于 `src/butil/iobuf.h`，接口与 `std::string` 类似但不完全相同。
- 支持轻量拷贝（仅拷贝管理结构）、零拷贝 append、fd 读写、protobuf 互操作以及通过 [[concepts/iobufbuilder|IOBufBuilder]] 当作 `std::ostream` 使用。
- IOBuf 不应作为程序内通用存储结构，应保持较短生命周期以避免单个 IOBuf 锁定过多 8K block。
- 解析使用 [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]，序列化使用 [[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]]，可与 protobuf 的 ZeroCopy API 或 `CodedInputStream` 配合实现零拷贝。
- 性能基准：在文件读入→12+1024 字节切割→合并→写出场景下可达 1519.99MB/s 吞吐与 1467171 QPS。
- 相比 Kylin 的 [[concepts/bufhandle|BufHandle]]，IOBuf 封装了内部结构并自动管理引用计数，使用更安全。
- 来源文件 [[entities/en-client|en_client]] 未提供与 IOBuf 直接相关的信息。
- 来源文件 [[entities/client|client]] 未提供与 IOBuf 直接相关的信息。

## bvar 监控指标
- [[entities/bvar|bvar]] 内置了多个与 IOBuf 相关的监控计数器，用于观察其内存分配与回收效率：
  - `iobuf_block_count`：当前 IOBuf 持有的 block 数量，反映内存块占用情况。
  - `iobuf_block_count_hit_tls_threshold`：命中 TLS 阈值的次数，用于评估 TLS 优化机制（与 [[concepts/thread-local存储|thread local 存储]] 相关）的触发频率。
  - `iobuf_block_memory`：所有 block 占用的内存字节数（示例值 729088）。
  - `iobuf_newbigview_second`：大视图（big view）的新建频率（示例值 10）。
- IOBuf 的 TLS 优化机制旨在减少多线程环境下的 [[concepts/cache-bouncing|cache bouncing]]，与 [[entities/bvar|bvar]] 自身降低 cache bouncing 的设计理念一脉相承，从而在高频 RPC 消息序列化与传输场景下兼顾效率与可观测性。