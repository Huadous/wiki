---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "-minloglevel"
  - "最小日志级别"
  - "Logging Control"
  - "-minloglevel"
  - "最小日志级别"
---

## Description
minloglevel 是 brpc 框架中用于控制日志输出阈值的全局标志，通过简单的整数值映射（0=INFO, 1=NOTICE, 2=WARNING, 3=ERROR, 4=FATAL）实现精确的日志级别过滤。该标志可在运行时动态修改，开发者无需重启服务即可调整日志输出粒度，这在生产环境问题排查时尤为有用。未被打印的日志仅执行一个简单的 `if` 判断，参数不会实际求值（例如，如果日志不打印，参数中的函数调用不会执行），因此即使设置为较高级别也不会造成显著的性能开销。brpc 还提供了其他相关日志控制标志，如 `-crash_on_fatal_log` 用于控制 FATAL 级别日志是否触发崩溃，以及 `-log_hostname` 用于在日志行中输出主机名以辅助聚合日志的溯源。

## Related Concepts
- [[concepts/bthread_concurrency|bthread_concurrency]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bvar|bvar]]
- [[entities/redis|redis]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "Only logs with levels **not less than** the level specified by -minloglevel are printed. This flag can be modified at run-time. Correspondence between values and log levels: 0=INFO 1=NOTICE 2=WARNING 3=ERROR 4=FATAL, default value is 0."
> - "Overhead of unprinted logs is just a 'if' test and parameters are not evaluated (For example a parameter calls a function, if the log is not printed, the function is not called)."
> - "If [-log_hostname](http://brpc.baidu.com:8765/flags/log_hostname) is turned on, each line of log contains the hostname so that users know machines at where each line is generated from aggregated logs."