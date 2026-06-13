---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_streaming_log]]"]
tags: [method]
aliases:
  - "LOG_EVERY_N"
  - "每 N 次日志宏"
  - "Every N Logging Macro"
---


# XXX_EVERY_N

## 定义
XXX_EVERY_N 是 brpc 中一组按调用次数进行采样限频的日志宏族。其中 XXX 可以代表 LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等多种日志前缀,N 是一个整数参数。例如 `LOG_EVERY_N(ERROR, 10)` 表示在累计调用 10 次时才真正输出一次日志,首次调用会立即打印,从而在保留关键早期日志的前提下降低高频路径上的日志开销。

## 关键特征
- **采样式限频**:仅在累计调用次数达到 N 的整数倍时才输出日志,其余调用被跳过。
- **首次立即输出**:首次调用会无延迟地打印日志,确保不会丢失前若干条关键记录。
- **轻微运行时开销**:相较于普通 LOG,每次调用仅多执行一次原子操作(relaxed memory order)。
- **线程安全**:多线程并发计数依然准确,这一点优于 glog 的同名宏。
- **宏族通用性**:同一限频模式覆盖 LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等多种日志前缀。

## 应用
- 对高频事件(如循环内部、热点回调、流量入口等)进行采样打印,既保留可观测性又显著降低日志量。
- 在调试早期阶段希望看到首批样本,而在生产环境中又希望抑制重复噪声时使用。
- 适用于需要线程安全计数的并发服务,避免类似 glog 在多线程下计数失准带来的漏打或重打问题。

## 相关概念
- [[concepts/XXX_EVERY_SECOND]]
- [[concepts/XXX_FIRST_N]]
- [[concepts/XXX_ONCE]]

## 相关实体
- [[entities/glog]]
- [[entities/LOG]]

## 来源提及
- "XXX represents for LOG, LOG_IF, PLOG, SYSLOG, VLOG, DLOG, and so on." — [[sources/en_streaming_log]]
- "These logging macros print log every N times." — [[sources/en_streaming_log]]
- "This macro is thread safe which means counting from multiple threads is also accurate while glog is not." — [[sources/en_streaming_log]]