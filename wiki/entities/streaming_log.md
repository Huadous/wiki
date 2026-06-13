---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/brpc/streaming_log|brpc/streaming_log]]"]
tags: [product]
aliases:
  - "流式日志"
  - "streaming_log 系统"
---


# streaming_log

## 基本信息
- Type: product
- Source: [[sources/brpc/streaming_log|streaming_log]]

## 描述
streaming_log 是 [[entities/butil|butil]] 库提供的流式日志系统，是本文档的核心主题。它通过继承 `std::ostream` 并利用 C++ `operator<<` 的 chaining 机制，让用户可以将复杂对象链式送入日志，避免了 printf 风格需要先转 string 的不便和大量临时内存分配。streaming_log 接口与 [[entities/glog|Google glog]] 保持高度兼容，但在 [[concepts/thread-local缓冲|thread-local 缓冲]]、节流日志线程安全保证和 noflush 批量输出机制等方面有所改进。其日志默认输出到屏幕，也可通过 [[entities/logsink|LogSink]] 接口（如 [[entities/stringsink|StringSink]]）重定向。整体上，它是 [[entities/brpc|brpc]] 生态中日志记录的推荐方式之一。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/butil|butil]]
- [[entities/glog|glog]]
- [[entities/logsink|LogSink]]
- [[entities/stringsink|StringSink]]

## 相关概念
- [[concepts/流式日志|流式日志]]
- [[concepts/log宏|LOG宏]]
- [[concepts/thread-local缓冲|thread-local缓冲]]
- [[concepts/operator-chaining|operator chaining]]

## 来源提及
- "streaming_log - Print log to std::ostreams" — [[sources/brpc/streaming_log|brpc/streaming_log]]
- "流式日志正是通过继承std::ostream，把对象打入日志的，在目前的实现中，送入日志流的日志被记录在thread-local的缓冲中，在完成一条日志后会被刷入屏幕或logging::LogSink，这个实现是线程安全的。" — [[sources/brpc/streaming_log|brpc/streaming_log]]