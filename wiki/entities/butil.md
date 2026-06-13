---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_rpc]]"
  - "[[brpc/flatmap.md]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "product"
aliases:
  - "baidu utility"
  - "baidu util"
  - "butil 工具库"
---

## Description
streaming_log 是百度 brpc 项目中 butil 基础工具库所暴露的流式日志接口，定义于头文件 `<butil/logging.h>` 中。butil 为 brpc 框架的运行提供日志、线程管理、字符串处理等通用基础设施，streaming_log 正是其日志子模块的对外入口之一。在 brpc 的文档语境中，streaming_log 适用于打印复杂对象或模板对象等不便直接用格式化字符串输出的场景，是 brpc 应用层日志输出的推荐选择。其典型使用方式是通过 `#include <butil/logging.h>` 引入，调用方式与标准流式输出类似。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/flatmap|FlatMap]]
- [[entities/streaming_log|streaming_log]]
- [[entities/logsink|LogSink]]
- [[sources/flatmap|flatmap]]
- [[sources/en_streaming_log|en_streaming_log]]

## Related Concepts
- [[concepts/流式日志|流式日志]]
- [[concepts/check宏|CHECK宏]]
- [[concepts/哈希表|哈希表]]
- [[concepts/butil|butil 基础工具库]]

## Mentions in Source
- `#include <butil/logging.h>` — [[entities/streaming_log|streaming_log]]

> **Source: [[sources/flatmap|flatmap]]**
> - `#include <butil/logging.h>` — [[sources/flatmap|flatmap]]
> - `#include <butil/containers/flat_map.h>` — [[sources/flatmap|flatmap]]
> - `https://github.com/apache/brpc/blob/master/src/butil/containers/flat_map.h` — [[sources/flatmap|flatmap]]

- `#0 0x000000afaa23 butil::debug::StackTrace::StackTrace()` — [[entities/streaming_log|streaming_log]]

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - `#include <butil/logging.h>` — [[sources/en_streaming_log|en_streaming_log]]
> - `Streaming log is the best choice for printing complex objects or template objects.` — [[sources/en_streaming_log|en_streaming_log]]