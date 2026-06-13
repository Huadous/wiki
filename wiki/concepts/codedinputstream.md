---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/techniques]]"
  - "[[brpc/en_iobuf.md]]"
tags:
  - "term"
aliases:
  - "CodedInputStream 类"
  - "编码输入流"
---

## Related Concepts
- [[concepts/streaming-multiple-messages|streaming-multiple-messages]]
- [[concepts/iobuf|IOBuf]]
- [[concepts/iobufaszero-copy-input-stream|IOBufAsZeroCopyInputStream]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/grpc|grpc]]
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/techniques|techniques]]**
> - "(If you want to avoid copying bytes to a separate buffer, check out the CodedInputStream class (in both C++ and Java) which can be told to limit reads to a certain number of bytes.)"

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "Parse IOBuf in user-defined formats
>
> ```c++
> IOBufAsZeroCopyInputStream wrapper(&iobuf);
> CodedInputStream coded_stream(&wrapper);
> coded_stream.ReadLittleEndian32(&value);
> ...
> ```"