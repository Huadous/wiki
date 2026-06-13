---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "other"
aliases:
  - "logging::StringSink"
  - "StringSink 类"
---

## Description
StringSink 是 [[brpc/streaming_log|streaming_log]] 默认提供的一个 LogSink 实现，它同时继承自 [[entities/butil|butil]] 中 [[entities/socketuniqueptr|socketuniqueptr]] 体系所引用的日志接收接口 LogSink 以及 C++ 标准库的 std::string，将日志内容直接存放到字符串缓冲区中。该类主要用于单元测试场景，使原本会写入屏幕的日志被重定向到字符串对象中，从而让测试代码能够以编程方式获取并断言日志输出内容。其典型使用模式为：声明一个 `::logging::StringSink` 局部变量 `log_str`，通过 `::logging::SetLogSink(&log_str)` 将其设置为当前 sink 并保存原 sink 指针，然后执行待测代码，最后调用 `log_str.find(...)` 验证日志内容是否包含预期字符串（如 `ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"))`），并通过 `SetLogSink(old_sink)` 恢复原来的 sink。这种设计使得对日志内容的断言测试变得简单直接，无需解析屏幕输出或文件。

## Related Entities
- [[entities/butil|butil]]（提供 LogSink 接口所在的工具库）
- LogSink（日志接收接口，StringSink 的基类之一）（来源：[[sources/en_streaming_log|en_streaming_log]]）

## Related Concepts
- [[concepts/流式日志|流式日志]]
- 单元测试（unit test）（来源：[[sources/en_streaming_log|en_streaming_log]]）
- LOG_AT（来源：[[sources/en_streaming_log|en_streaming_log]]）

## Mentions in Source
- 同时继承了LogSink和string，把日志内容存放在string中，主要用于单测 — [[brpc/streaming_log|streaming_log]]
- ::logging::StringSink log_str; — [[brpc/streaming_log|streaming_log]]
- ::logging::LogSink* old_sink = ::logging::SetLogSink(&log_str); — [[brpc/streaming_log|streaming_log]]

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "Inherit both LogSink and string. Store log content inside string and mainly aim for unit test."
> - "::logging::StringSink log_str;"
> - "ASSERT_NE(std::string::npos, log_str.find(\"specified_file.cc:12345\"));"