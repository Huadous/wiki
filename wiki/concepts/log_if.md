---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "LOG_IF()"
  - "Conditional LOG Macro"
  - "条件日志宏"
---

## Related Concepts
- [[concepts/LOG宏|LOG宏]]
- [[concepts/节流日志|节流日志]]
- [[concepts/VLOG宏|VLOG宏]]

## Related Entities
- [[entities/streaming_log|streaming_log]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - `LOG_IF(log_level, condition)`只有当condition成立时才会打印，相当于if (condition) { LOG() << ...; }，但更加简短。
> - LOG_IF(NOTICE, n > 10) << "This log will only be printed when n > 10";

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - `LOG_IF(log_level, condition)` prints only when condition is true.
> - It's the same as `if (condition) { LOG() << ...; }` with shorter code：
> - LOG_IF(NOTICE, n > 10) << "This log will only be printed when n > 10";