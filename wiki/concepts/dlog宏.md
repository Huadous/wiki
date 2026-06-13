---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "DLOG()"
  - "debug log"
  - "DLOG"
  - "DLOG()"
  - "debug log"
  - "DLOG family"
  - "DLOG()"
  - "debug log"
  - "DLOG"
  - "DLOG()"
  - "debug log"
---

## Related Concepts
- [[concepts/log宏|LOG宏]]
- [[concepts/check宏|CHECK宏]]
- [[concepts/vlog宏|VLOG宏]]
- [[concepts/plog宏|PLOG宏]]
- [[concepts/ndebug宏|NDEBUG宏]]

## Related Entities
（无相关实体）

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - 所有的日志宏都有debug版本，以D开头，比如DLOG，DVLOG，当定义了**NDEBUG**后，这些日志不会打印。
> - **千万别在D开头的日志流上有重要的副作用。**
> - "不会打印"指的是连参数都不会评估。

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - All log macros have debug versions, starting with D, such as DLOG, DVLOG. When NDEBUG is defined, these logs will not be printed.
> - Do not put important side effects inside the log streams beginning with D.
> - *No printing* means that even the parameters are not evaluated.