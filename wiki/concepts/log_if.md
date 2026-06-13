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

## Description
LOG_IF(log_level, condition) 是 brpc streaming_log 中用于条件日志输出的宏，仅在 `condition` 表达式求值为真时才执行日志打印操作。其语义与 `if (condition) { LOG() << ...; }` 完全等价，但写法上更为简洁，专门用于减少条件日志这种常见模式的样板代码。该宏特别适合"仅在异常分支或特定状态下打印日志"的场景，典型用法如 `LOG_IF(NOTICE, n > 10) << "..."`，其中 NOTICE 级别可用来表达重要但不致命的业务条件。LOG_IF 还提供了完整的变体形式以覆盖不同的调试与日志需求，包括 `PLOG_IF`、`DLOG_IF`、`VLOG_IF`、`VLOG2_IF` 等。需要注意：LOG_IF 仅在条件满足时输出一次，而真正的周期性节流需求应配合节流日志宏（如 `LOG_EVERY_N`）使用。

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