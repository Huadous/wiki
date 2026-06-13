---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/iobuf.md]]"
  - "[[brpc/http_client.md]]"
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

## 补充来源
- Original file: iobuf
- Ingested: 2026-06-13
- 说明：未提供与本页直接相关的新信息。

- Original file: http_client
- Ingested: 2026-06-13
- 说明：未提供与本页直接相关的新信息。

## 核心内容
本文档介绍了 [[entities/brpc|brpc]] 中使用的 [[entities/butiliobuf|butil::IOBuf]] 数据结构。IOBuf 是一种非连续的[[concepts/零拷贝缓冲|零拷贝缓冲]]，主要在部分协议中作为附件或 HTTP body 的数据结构使用，其接口与 `std::string` 类似但不完全相同。文档详细列举了 IOBuf 的能力与限制（可默认构造、轻量拷贝、零拷贝 append、fd 读写、protobuf 互操作、流式构造等；不推荐作为通用存储以免锁定过多 8K block），并给出切割、拼接、解析、序列化、打印等操作的代码示例。性能基准显示在文件读入→12+1024 字节切割→合并→写出场景下可达 1519.99MB/s 吞吐。文档还以 Kylin 的 [[concepts/bufhandle|BufHandle]] 作为对比，说明 IOBuf 在易用性与安全性上的优势。

## 关键实体
- [[entities/brpc|brpc]]
- [[entities/butiliobuf|butil::IOBuf]]

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