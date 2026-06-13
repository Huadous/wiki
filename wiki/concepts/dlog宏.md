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
---

## Description
DLOG宏是 brpc 日志体系中 LOG 宏的 debug 版本，所有 LOG/PLOG/VLOG/CHECK 系列宏都对应有以 `D` 前缀的 debug 变种（如 DLOG、DPLOG、DVLOG、DCHECK），形成完整的 debug 变种体系。其核心机制基于条件编译：当编译时定义了 `NDEBUG` 宏后，D 系列日志宏会被预处理器/编译器完全消除，不仅是消息不会打印，连参数表达式都不会被评估，因此参数中的副作用（如函数调用、自增等）也不会执行。官方文档明确警告"千万别在D开头的日志流上有重要的副作用"，例如 `DLOG(FATAL) << foo()` 在 release 构建中 `foo()` 不会被调用，可能导致逻辑错误；如果代码中的副作用必须执行，应改用普通的 LOG 宏而非 DLOG。该机制使其非常适合作为仅在 debug 构建中生效的诊断日志，发布版本（Release）会自动剥离，适合高频调用路径与临时性调试输出场景。

## Related Concepts
- [[concepts/log宏|LOG宏]]
- [[concepts/check宏|CHECK宏]]

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
> - No printing means that even the parameters are not evaluated.