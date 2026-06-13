---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_rpc]]"
  - "[[brpc/flatmap.md]]"
  - "[[brpc/en_streaming_log.md]]"
  - "[[brpc/en_iobuf.md]]"
tags:
  - "product"
aliases:
  - "baidu utility"
  - "baidu util"
  - "butil 工具库"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/flatmap|FlatMap]]
- [[entities/streaming_log|streaming_log]]
- [[entities/logsink|LogSink]]

## Related Concepts
- [[concepts/流式日志|流式日志]]
- [[concepts/check宏|CHECK宏]]
- [[concepts/哈希表|哈希表]]
- [[concepts/iobuf|IOBuf]]
- [[concepts/butil|butil 基础工具库]]

## Mentions in Source

> **Source: [[sources/flatmap|flatmap]]**
> - `#include <butil/logging.h>` — [[sources/flatmap|flatmap]]
> - `#include <butil/containers/flat_map.h>` — [[sources/flatmap|flatmap]]
> - `https://github.com/apache/brpc/blob/master/src/butil/containers/flat_map.h` — [[sources/flatmap|flatmap]]
> - `#0 0x000000afaa23 butil::debug::StackTrace::StackTrace()` — [[entities/streaming_log|streaming_log]]

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - `#include <butil/logging.h>` — [[sources/en_streaming_log|en_streaming_log]]
> - `Streaming log is the best choice for printing complex objects or template objects.` — [[sources/en_streaming_log|en_streaming_log]]
> - `butil（Baidu Utility Library）为 brpc 框架的运行提供日志、线程管理、字符串处理等通用基础设施。` — [[sources/en_streaming_log|en_streaming_log]]
> - `streaming_log 通过 butil/logging.h 暴露给用户，是 brpc 应用层日志输出的核心接口之一。` — [[sources/en_streaming_log|en_streaming_log]]

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - `brpc uses butil::IOBuf as data structure for attachment in some protocols and HTTP body.` — [[sources/en_iobuf|en_iobuf]]
> - `It's a non-contiguous zero-copied buffer, proved in previous projects, and good at performance.` — [[sources/en_iobuf|en_iobuf]]