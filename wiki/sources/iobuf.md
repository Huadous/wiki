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

## 关键概念
- [[concepts/零拷贝缓冲|零拷贝缓冲]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobuf-与-protobuf-互操作|IOBuf 与 Protobuf 互操作]]
- [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]
- [[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]]
- [[concepts/bufhandle|BufHandle]]

## 要点
- IOBuf 是 brpc 框架采用的非连续零拷贝缓冲数据结构，定义于 `src/butil/iobuf.h`，接口与 `std::string` 类似但不完全相同。
- 支持轻量拷贝（仅拷贝管理结构）、零拷贝 append、fd 读写、protobuf 互操作以及通过 [[concepts/iobufbuilder|IOBufBuilder]] 当作 `std::ostream` 使用。
- IOBuf 不应作为程序内通用存储结构，应保持较短生命周期以避免单个 IOBuf 锁定过多 8K block。
- 解析使用 [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]，序列化使用 [[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]]，可与 protobuf 的 ZeroCopy API 或 `CodedInputStream` 配合实现零拷贝。
- 性能基准：在文件读入→12+1024 字节切割→合并→写出场景下可达 1519.99MB/s 吞吐与 1467171 QPS。
- 相比 Kylin 的 [[concepts/bufhandle|BufHandle]]，IOBuf 封装了内部结构并自动管理引用计数，使用更安全。
- 来源文件 [[entities/en-client|en_client]] 未提供与 IOBuf 直接相关的信息。
- 来源文件 [[entities/client|client]] 未提供与 IOBuf 直接相关的信息。