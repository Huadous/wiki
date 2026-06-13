---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_streaming_log]]"]
tags: [method]
aliases:
  - "每秒限频日志宏"
  - "LOG_EVERY_SECOND"
---


# XXX_EVERY_SECOND

## 定义
XXX_EVERY_SECOND 是一族日志限频宏（rate-limited logging macros），其中 XXX 代表 LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等日志宏。它们的语义是同一秒内的多次调用最多只会真正打印一次，常用于热点代码路径中检查运行状态而不至于淹没日志。首次调用会立即打印一条日志，相比普通 LOG 额外增加约 30ns 的开销（由 gettimeofday 引起）。

## 关键特征
- **按秒限频**：同一秒内的多次调用至多打印一次日志
- **首次立即输出**：宏的首次调用会立刻打印日志，不存在首条日志被丢弃的情况
- **极低额外开销**：相比普通 LOG 仅增加约 30ns 的开销，主要由 `gettimeofday` 系统调用引入
- **宏族覆盖完整**：涵盖 LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等多种日志宏的变体
- **基于时间窗口**：使用秒级时间窗口进行频率判定，而非基于调用次数

## 应用
- **热点代码路径状态检查**：在高频执行的代码路径（例如 RPC 处理循环、事件回调）中记录调试信息，避免日志风暴
- **周期性心跳检测**：在后台守护线程或长连接保活逻辑中按秒输出心跳状态
- **频繁路径采样**：对被反复命中的代码分支进行低频采样，便于事后排查问题
- **错误状态观测**：当错误短时间内可能反复发生时，仅记录首次或每秒一次的错误，避免日志被淹没

## 相关概念
- [[concepts/XXX_EVERY_N]]
- [[concepts/XXX_FIRST_N]]
- [[concepts/XXX_ONCE]]

## 相关实体
- [[entities/LOG]]
- [[entities/PLOG]]

## 来源提及
- "XXX represents for LOG, LOG_IF, PLOG, SYSLOG, VLOG, DLOG, and so on." — [[sources/en_streaming_log|en_streaming_log]]
- "These logging macros print log at most once per second." — [[sources/en_streaming_log|en_streaming_log]]
- "The first call to this macro prints the log immediately, and costs additional 30ns (caused by gettimeofday) compared to normal LOG." — [[sources/en_streaming_log|en_streaming_log]]