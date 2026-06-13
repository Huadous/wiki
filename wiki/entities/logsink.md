---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_log|streaming_log]]"]
tags: [other]
aliases:
  - "logging::LogSink"
  - "LogSink 抽象类"
---


# LogSink

## 基本信息
- Type: other
- Source: [[sources/streaming_log|streaming_log]]

## 描述
LogSink 是 [[sources/streaming_log|streaming_log]] 中负责日志输出目标的抽象类，位于 [[entities/butil|butil]] 工具库提供的日志体系中。用户可以通过 `logging::SetLogSink` 函数修改日志刷入的目标，实现日志输出行为的灵活替换。默认情况下日志输出到屏幕，但用户可以继承 LogSink 实现自定义的日志打印逻辑，例如写入文件、发送到远程日志收集系统等。LogSink 机制是 streaming_log 灵活适配不同日志消费场景的关键扩展点，常与 [[entities/streaming_log|streaming_log]] 配合使用。文档示例展示了通过 `SetLogSink(old_sink)` 恢复原始 sink 的典型用法。

## 相关实体
- [[entities/streaming_log|streaming_log]]
- [[entities/StringSink|StringSink]]
- [[entities/butil|butil]]

## 相关概念
- [[concepts/流式日志|流式日志]]

## 来源提及
- streaming log通过logging::SetLogSink修改日志刷入的目标，默认是屏幕。 — [[sources/streaming_log|streaming_log]]
- 在完成一条日志后会被刷入屏幕或logging::LogSink — [[sources/streaming_log|streaming_log]]
- `::logging::LogSink* old_sink = ::logging::SetLogSink(&log_str);` — [[sources/streaming_log|streaming_log]]