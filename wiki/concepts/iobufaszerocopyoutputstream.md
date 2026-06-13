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
  - "IOBuf 输出流适配器"
  - "IOBufAsZeroCopyOutputStream"
  - "ZeroCopyOutputStream wrapper"
---

## Related Concepts
- [[concepts/butil-iobuf|butil::IOBuf]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]
- [[concepts/iobuf-protobuf-interop|IOBuf 与 Protobuf 互操作]]
- [[concepts/zerocopyoutputstream|ZeroCopyOutputStream]]
- [[concepts/protocol-buffers|Protocol Buffers]]
- [[concepts/zero-copy-buffer|Zero-copy buffer]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/iobuf|iobuf]]**
> - "protobuf序列化为IOBuf"
> - "IOBufAsZeroCopyOutputStream wrapper(&iobuf); pb_message.SerializeToZeroCopyStream(&wrapper);"
> - "用可打印数据创建IOBuf"

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "Serialize a protobuf message into the IOBuf"
>
> ```c++
> IOBufAsZeroCopyOutputStream wrapper(&iobuf);
> pb_message.SerializeToZeroCopyStream(&wrapper);
> ```
> - "No directly relevant information"