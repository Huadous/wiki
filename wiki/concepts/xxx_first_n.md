---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_streaming_log]]"]
tags: [method]
aliases:
  - "LOG_FIRST_N"
  - "前 N 次日志宏"
---


# XXX_FIRST_N

## 定义
XXX_FIRST_N 是一族限制日志最多输出 N 次的日志宏（例如 `LOG_FIRST_N(INFO, 20)` 最多打印 20 条日志），其中 `XXX` 代表 `LOG`、`LOG_IF`、`PLOG`、`SYSLOG`、`VLOG`、`DLOG` 等多种日志宏前缀。达到上限后，即使继续调用也不再输出。

## 关键特征
- 通过计数器限制日志输出次数，超过 N 次后自动停止输出
- 在累计达到 N 次之前，相比普通 `LOG` 多一次原子操作（relaxed order）
- 达到 N 次之后为零开销（不再递增计数器，也不进行输出）
- 是宏族形式，覆盖多种日志宏前缀（LOG、LOG_IF、PLOG、SYSLOG、VLOG、DLOG 等）
- 计数器以原子方式更新，可安全用于多线程并发场景

## 应用
- 初始化阶段只关心"前几次"出现的日志信息，避免重复噪音淹没关键输出
- 异常检测场景：仅记录前 N 次异常，防止异常风暴时日志被刷屏
- 资源路径或配置加载等一次性事件的有限次追踪
- 调试时希望看到早期样本但又不想持续打印的中间状态

## 相关概念
- [[concepts/xxx_every_n|XXX_EVERY_N]]
- [[concepts/xxx_once|XXX_ONCE]]
- [[concepts/xxx_every_second|XXX_EVERY_SECOND]]

## 相关实体
- [[entities/log|LOG]]

## 来源提及
- "XXX represents for LOG, LOG_IF, PLOG, SYSLOG, VLOG, DLOG, and so on." — [[sources/en_streaming_log]]
- "These logging macros print log at most N times." — [[sources/en_streaming_log]]
- "It costs an additional atomic operation (relaxed order) compared to normal LOG before N, and zero cost after." — [[sources/en_streaming_log]]