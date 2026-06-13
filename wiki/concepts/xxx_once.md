---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_streaming_log]]"]
tags: [method]
aliases:
  - "LOG_ONCE"
  - "一次性日志宏"
---


# XXX_ONCE

## 定义
XXX_ONCE 是一族日志宏的统称，XXX 涵盖 LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等所有日志形式。XXX_ONCE 是 [[concepts/xxx_first_n|XXX_FIRST_N(..., 1)]] 的语法糖，表示"在整个进程生命周期内最多只打印一次"的日志输出行为。

## 关键特征
- **仅打印一次**：在整个进程生命周期内，同一条日志最多只被打印一次，后续调用将被静默忽略。
- **语法糖实现**：语义上等价于 [[concepts/xxx_first_n|XXX_FIRST_N(..., 1)]]，使用更简洁直观的命名。
- **覆盖全日志宏族**：XXX 涵盖 LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等所有日志形式，保持命名一致性。
- **进程级状态**：其"已打印"状态基于进程内全局标志位，因此多线程并发场景下也能保证全局只打印一次（首次进入的线程打印）。
- **零依赖、轻量级**：使用方式与普通日志宏完全一致，无需额外配置或状态管理。

## 应用
- **初始化状态报告**：服务启动时一次性打印版本号、配置摘要、监听端口等初始化信息，避免每次启动检查时重复输出。
- **首次异常告警**：对那些在系统运行周期内极少出现但又需要被注意到的异常（如首次发现的不合法输入、首次资源耗尽），用 XXX_ONCE 打印而不会被反复刷屏。
- **噪声控制**：在热路径或高频代码段中，对某些不频繁但确实需要记录的分支事件使用 XXX_ONCE，避免淹没其它关键日志。
- **调试探针**：在排查问题时临时埋点，记录某段代码是否曾被执行或某条路径是否被命中，排查完成后可保留或移除。
- **运行时环境探测**：在多平台/多配置适配代码中，仅在首次进入特定分支时打印当前实际生效的环境信息。

## 相关概念
- [[concepts/xxx_first_n|XXX_FIRST_N]]
- [[concepts/xxx_every_n|XXX_EVERY_N]]

## 相关实体
- [[entities/log|LOG]]

## 来源提及
- "XX represents for LOG, LOG_IF, PLOG, SYSLOG, VLOG, DLOG, and so on." — [[sources/en_streaming_log]]
- "These logging macros print log at most once." — [[sources/en_streaming_log]]
- "It's the same as `XXX_FIRST_N(..., 1)`" — [[sources/en_streaming_log]]