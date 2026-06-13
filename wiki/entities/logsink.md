---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "other"
aliases:
  - "logging::LogSink"
  - "LogSink 抽象类"
---

## Description
LogSink 是 [[sources/streaming_log|streaming_log]] 中负责日志输出目标的抽象类，位于 [[entities/butil|butil]] 工具库提供的日志体系中。用户可以通过 `logging::SetLogSink` 函数修改日志刷入的目标，实现日志输出行为的灵活替换。默认情况下日志输出到屏幕，但用户可以继承 LogSink 实现自定义的日志打印逻辑，例如写入文件、发送到远程日志收集系统等。LogSink 机制是 streaming_log 灵活适配不同日志消费场景的关键扩展点，常与 [[entities/streaming_log|streaming_log]] 配合使用。文档示例展示了通过 `SetLogSink(old_sink)` 恢复原始 sink 的典型用法。[[entities/StringSink|StringSink]] 是 LogSink 的一个典型示例实现，它同时继承 LogSink 和 `std::string`，将日志内容存入字符串，主要用于单元测试中验证日志输出（如通过 `log_str.find` 断言包含特定文件:行号）。

## Related Entities
- [[entities/streaming_log|streaming_log]]
- [[entities/StringSink|StringSink]]
- [[entities/butil|butil]]

## Related Concepts
- [[concepts/流式日志|流式日志]]
- [[concepts/LOG macro|LOG macro]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - streaming log通过logging::SetLogSink修改日志刷入的目标，默认是屏幕。
> - 在完成一条日志后会被刷入屏幕或logging::LogSink
> - `::logging::LogSink* old_sink = ::logging::SetLogSink(&log_str);`

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - The default destination of streaming log is the screen. You can change it through logging::SetLogSink.
> - Users can inherit LogSink and implement their own output logic.
> - StringSink Inherit both LogSink and string. Store log content inside string and mainly aim for unit test.