---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_log]]"]
tags: [method]
aliases:
  - "DLOG()"
  - "debug log"
---


# DLOG宏

## 定义
DLOG宏是 brpc 中 LOG 宏的 debug 版本，所有日志宏都有以 `D` 开头的 debug 变种（如 DLOG、DVLOG、DPLOG）。当编译时定义了 **NDEBUG** 宏后，这些以 `D` 开头的日志宏会完全跳过——不仅不会打印日志，连参数都不会被评估，因此参数中的副作用也不会执行。

## 关键特征
- **条件编译生效**：在编译时定义了 `NDEBUG` 后，DLOG 等 D 系列日志宏完全失效，被预处理器/编译器消除。
- **参数不求值**：在 `NDEBUG` 模式下，不仅不会打印日志，连参数表达式都不会被评估，意味着参数中的副作用（如函数调用、自增等）也不会执行。
- **副作用风险**：官方文档明确警告"千万别在D开头的日志流上有重要的副作用"。如果代码中的副作用必须执行，应改用普通的 LOG 宏而非 DLOG。
- **诊断用途**：用于只在 debug 模式下生效的诊断日志，发布版本（Release）会自动剥离。
- **与 LOG 系列对应**：DLOG 对应 LOG，DVLOG 对应 VLOG，DPLOG 对应 PLOG，形成完整的 debug 变种体系。

## 应用
- **开发调试阶段**：在代码中添加仅在 debug 构建中生效的诊断日志，便于排查问题而无需在发布版本中手动删除。
- **性能敏感路径**：在 release 构建中通过 `NDEBUG` 完全消除调试日志的运行时开销（包括参数求值），适合高频调用路径。
- **临时性调试输出**：开发者临时插入 DLOG 用于观察变量状态或程序流程，确认无误后再决定是否升级为正式的 LOG。

## 相关概念
- [[concepts/log宏|LOG宏]]
- [[concepts/check宏|CHECK宏]]

## 相关实体
（无相关实体）

## 来源提及
- 所有的日志宏都有debug版本，以D开头，比如DLOG，DVLOG，当定义了**NDEBUG**后，这些日志不会打印。 — [[sources/streaming_log|streaming_log]]
- **千万别在D开头的日志流上有重要的副作用。** — [[sources/streaming_log|streaming_log]]
- "不会打印"指的是连参数都不会评估。 — [[sources/streaming_log|streaming_log]]