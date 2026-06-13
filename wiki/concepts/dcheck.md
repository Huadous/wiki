---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log|streaming_log]]"]
tags: [term]
aliases:
  - "DCHECK宏"
  - "debug CHECK"
---


# DCHECK

## 定义
DCHECK 是 [[concepts/check宏|CHECK 宏]] 的 debug 版本，其行为与 [[concepts/dlog宏|DLOG 宏]] / DVLOG 宏一致：当预处理器定义了 `NDEBUG` 后，DCHECK 不会打印日志，等价于被完全移除。文档特别警告，不应在 DCHECK 的日志流中包含重要的副作用，因为当 `NDEBUG` 被定义后，不仅日志不会输出，连参数都不会被求值。

## 关键特征
- **Release 构建中完全消除**：当 `NDEBUG` 被定义时，DCHECK 整体被移除，不产生任何运行时开销。
- **参数不会被求值**：在 release 构建中，不仅日志不会输出，连传递给 DCHECK 的参数表达式都不会被评估。
- **仅适用于纯断言**：不能用于依赖求值顺序或包含副作用的逻辑。
- **与 DLOG/DVLOG 一致**：同属以 `D` 开头的 debug 版本日志/断言宏家族。

## 应用
- 在 release 构建中无开销地保留程序不变式检查。
- 调试模式下对关键前置条件、后置条件进行断言验证。
- 与 [[concepts/dlog宏|DLOG]] 配合使用，统一 release 构建的日志与断言消除策略。

## 相关概念
- [[concepts/check宏|CHECK 宏]]
- [[concepts/dlog宏|DLOG 宏]]

## 相关实体
- [[entities/butil|butil]]

## 来源提及
- 和DLOG类似，你不应该在DCHECK的日志流中包含重要的副作用。 — [[brpc/streaming_log|streaming_log]]
- 所有的日志宏都有debug版本，以D开头，比如DLOG，DVLOG，当定义了NDEBUG后，这些日志不会打印。 — [[brpc/streaming_log|streaming_log]]