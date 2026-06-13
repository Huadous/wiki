---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log|streaming_log]]"]
tags: [method]
aliases:
  - "LOG_IF()"
  - "Conditional LOG Macro"
  - "条件日志宏"
---


# LOG_IF

## 定义
LOG_IF(log_level, condition) 是 brpc streaming_log 提供的一个条件日志宏。它仅在 condition 表达式求值为真时才会执行日志打印，等价于 `if (condition) { LOG(level) << ...; }`，但语法上更为简洁。该宏的设计目的是减少条件日志这种常见模式的样板代码。

## 关键特征
- **条件求值**：传入的 `condition` 表达式仅在需要时进行求值；当条件为假时，整个日志语句（包括潜在的副作用构造）被跳过
- **语义等价**：与 `if (condition) { LOG(level) << ...; }` 在行为上完全等价，仅作为简写形式存在
- **变体丰富**：LOG_IF 支持所有 LOG 的变种形式，包括但不限于 `LOG_IF_EVERY_N`、`PLOG_IF`、`DLOG_IF`、`VLOG_IF` 等
- **流式接口**：与 LOG 宏一样采用流式 `<<` 语法，可链式拼接任意可流式输出的内容

## 应用
- **限频/触发式日志**：在循环或高频调用路径中，仅在异常或特殊条件（如计数器超过阈值）成立时才记录日志，例如 `LOG_IF(NOTICE, n > 10) << "..."` 仅在 `n > 10` 时打印 NOTICE 级别日志
- **调试辅助**：在不污染正常日志输出的前提下，针对特定分支或状态记录调试信息
- **节流日志替代方案**：对于"满足条件才输出"的场景，相比手动 `if` 包装 LOG 可读性更佳；真正的周期性节流需求应配合 [[concepts/节流日志|节流日志]] 相关宏（如 `LOG_EVERY_N`）使用

## 相关概念
- [[concepts/LOG宏|LOG宏]]
- [[concepts/节流日志|节流日志]]

## 相关实体
*暂无相关实体*

## 来源提及
- `LOG_IF(log_level, condition)`只有当condition成立时才会打印，相当于if (condition) { LOG() << ...; }，但更加简短。 — [[brpc/streaming_log|streaming_log]]
- LOG_IF(NOTICE, n > 10) << "This log will only be printed when n > 10"; — [[brpc/streaming_log|streaming_log]]