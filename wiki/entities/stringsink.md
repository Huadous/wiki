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