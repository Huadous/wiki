---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/brpc/streaming_log|brpc/streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "product"
aliases:
  - "流式日志"
  - "streaming_log 系统"
---

## Description
streaming_log 是 [[entities/butil|butil]] 库提供的流式日志系统，定义于 `<butil/logging.h>` 头文件中，是 [[entities/brpc|brpc]] 生态中日志记录的推荐方式之一。它通过继承 `std::ostream` 并利用 C++ 流式操作符 `<<` 的 chaining 机制，让用户可以将复杂对象或模板对象直接链式送入日志，无需预先转换为字符串，大幅简化了代码并避免了 printf 风格日志中大量临时内存分配的开销。该组件采用线程本地缓冲机制，在完成一条日志后会被统一刷入屏幕或 [[entities/logsink|logging::LogSink]]，具备线程安全特性。streaming_log 接口与 [[entities/glog|Google glog]] 保持高度兼容，并通过 [[concepts/noflus日志|noflus 日志]] 等机制进一步优化了批量输出场景。它是处理复杂对象、模板对象打印的最优选择，同时支持通过 [[entities/stringsink|StringSink]] 等 [[entities/logsink|LogSink]] 实现重定向。

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/butil|butil]]
- [[entities/glog|glog]]
- [[entities/logsink|LogSink]]
- [[entities/stringsink|StringSink]]

## Related Concepts
- [[concepts/流式日志|流式日志]]
- [[concepts/log宏|LOG宏]]
- [[concepts/plog宏|PLOG宏]]
- [[concepts/vlog宏|VLOG宏]]
- [[concepts/dlog宏|DLOG宏]]
- [[concepts/check宏|CHECK宏]]
- [[concepts/noflus日志|noflus日志]]
- [[concepts/thread-local缓冲|thread-local缓冲]]
- [[concepts/operator-chaining|operator chaining]]

## Mentions in Source
> **Source: [[sources/brpc/streaming_log|brpc/streaming_log]]**
> - "streaming_log - Print log to std::ostreams"
> - "流式日志正是通过继承std::ostream，把对象打入日志的，在目前的实现中，送入日志流的日志被记录在thread-local的缓冲中，在完成一条日志后会被刷入屏幕或logging::LogSink，这个实现是线程安全的。"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "Streaming log is the best choice for printing complex objects or template objects."
> - "Streaming log is such a log stream that inherits std::ostream to send the object into the log."
> - "In the current implementation, the logs are recorded in a thread-local buffer, which will be flushed into screen or logging::LogSink after a complete log record."