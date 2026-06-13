---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log]]"]
tags: [method]
aliases:
  - "CHECK()"
  - "CHECK_EQ"
  - "CHECK_GT"
---


# CHECK宏

## 定义
CHECK 是 streaming_log 中的断言宏，行为类似于 gtest 的 ASSERT 宏。当其表达式求值为 false 时，会打印一条 FATAL 级别的日志，并附带完整的调用栈信息。CHECK 系列包含针对不同比较关系的具体变种，如 CHECK_EQ、CHECK_GT、CHECK_LT 等。

## 关键特征
- **断言语义**：当表达式为 false 时触发 FATAL 日志并打印完整调用栈，类似于 gtest 中的 ASSERT 宏。
- **变种丰富**：提供 CHECK_EQ、CHECK_GT、CHECK_LT 等具体比较关系的变种宏。
- **更详细的错误信息**：使用具体的 CHECK_XX 变种相比通用 CHECK(x > y) 能提供更丰富的诊断信息，例如输出 "1 > 2 (1 vs 2)" 而不仅仅是 "Check failed: x > y"。
- **流式追加行为**：CHECK 失败后其后的日志流内容仍会被打印，行为类似 glog 的流式追加。
- **精确选择原则**：文档明确强调应根据具体比较关系选择最精确的 CHECK_XX 变种。

## 应用
- 在 streaming_log 及其他 brpc 组件中用于运行时条件校验。
- 替代 gtest ASSERT 在生产代码中进行失败即终止式的断言检查。
- 在关键不变量或前置条件不满足时立即终止流程并附带完整堆栈信息，便于问题定位。
- 当使用通用 CHECK 表达比较关系时，建议替换为 CHECK_EQ、CHECK_GT、CHECK_LT 等具体变种以获得更可读的错误信息。

## 相关概念
- [[concepts/log宏|LOG宏]]
- [[concepts/dlog宏|DLOG宏]]

## 相关实体
- [[entities/butil|butil]]

## 来源提及
- "日志另一个重要变种是CHECK(expression)，当expression为false时，会打印一条FATAL日志。类似gtest中的ASSERT，也有CHECK_EQ, CHECK_GT等变种。" — [[brpc/streaming_log|streaming_log]]
- "你**应该**根据比较关系使用具体的CHECK_XX，这样当出现错误时，你可以看到更详细的信息" — [[brpc/streaming_log|streaming_log]]