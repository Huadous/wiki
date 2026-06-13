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
> - No directly relevant information.