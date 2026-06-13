---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/iobuf|iobuf]]"
  - "[[brpc/en_iobuf.md]]"
tags:
  - "term"
aliases:
  - "IOBuf 输入流适配器"
  - "ZeroCopyInputStream wrapper"
---

## Description
IOBufAsZeroCopyInputStream 是连接 butil::IOBuf 与 Protobuf 生态的关键桥梁。其核心价值在于 IOBuf 内部由多个非连续内存块（block）组成，借助该适配器，Protobuf 解析器可以直接消费这些非连续的内存块，而无需先将整个缓冲区物化（materialize）为一块连续内存，从而避免了额外的数据拷贝开销。

该适配器主要支持两类使用场景：第一，直接将 IOBuf 解析为 Protobuf 消息，通过 `pb_message.ParseFromZeroCopyStream(&wrapper)` 即可完成反序列化；第二，将 IOBuf 按照用户自定义格式解析，结合 `CodedInputStream` 可以灵活读取 varint、固定长度整数（如 `ReadLittleEndian32`）等数据，适用于非 Protobuf 格式的自定义协议解析。

作为 brpc 在高性能反序列化场景下的关键工具，IOBufAsZeroCopyInputStream 与 [[concepts/iobufbuilder|IOBufBuilder]]（对应的输出方向适配器）、[[concepts/iobuf-protobuf-interop|IOBuf 与 Protobuf 互操作]]模式共同构成了 IOBuf 与 Protobuf 生态之间完整的零拷贝数据通路。

## Related Concepts
- [[concepts/butil-iobuf|butil::IOBuf]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobuf-protobuf-interop|IOBuf 与 Protobuf 与 IOBuf 互操作]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/iobuf|iobuf]]**
> - 解析IOBuf为protobuf message
> - 解析IOBuf为自定义结构
> - `IOBufAsZeroCopyInputStream wrapper(&iobuf);`
>   `pb_message.ParseFromZeroCopyStream(&wrapper);`
> - `IOBufAsZeroCopyInputStream wrapper(&iobuf);`
>   `CodedInputStream coded_stream(&wrapper);`
>   `coded_stream.ReadLittleEndian32(&value);`

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - Parse a protobuf message from the IOBuf 

c++
IOBufAsZeroCopyInputStream wrapper(&iobuf);
pb_message.ParseFromZeroCopyStream(&wrapper);
> - Parse IOBuf in user-defined formats

```c++
IOBufAsZeroCopyInputStream wrapper(&iobuf);
CodedInputStream coded_stream(&wrapper);
coded_stream.ReadLittleEndian32(&value);
...