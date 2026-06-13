---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "CHECK()"
  - "CHECK_EQ"
  - "CHECK_GT"
  - "CHECK macro"
  - "CHECK()"
  - "CHECK_EQ"
  - "CHECK_GT"
---

## Description
CHECK(expression) 是 brpc streaming_log 中用于运行时断言的宏族，当表达式求值为 false 时会打印 FATAL 级别日志并附带完整调用栈，从而立即终止流程。该宏族的设计借鉴了 gtest 的 ASSERT 语义，但在错误信息输出上更进一步：对于算术比较场景，应优先选用具体的 CHECK_XX 变种（如 CHECK_EQ、CHECK_GT、CHECK_LT），因为这些变种会输出类似 "Check failed: x > y (1 vs 2)" 这样同时展示表达式文本和两侧实际值的诊断信息，远比通用 CHECK(x > y) 仅输出 "Check failed: x > y" 更为丰富。文档明确强调开发者应当遵循精确选择原则，根据比较关系使用最合适的 CHECK_XX 变种。与 DLOG 类似，CHECK 也存在调试版本 DCHECK，遵循 NDEBUG 下的特殊语义：其参数表达式在 NDEBUG 编译下不会被求值，因此与 DLOG 一样，**不应**在 DCHECK 中放置具有重要副作用的代码。

## Related Concepts
- [[concepts/log宏|LOG宏]]
- [[concepts/dlog宏|DLOG宏]]

## Related Entities
- [[entities/butil|butil]]
- [[entities/streaming_log|streaming_log]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - "日志另一个重要变种是CHECK(expression)，当expression为false时，会打印一条FATAL日志。类似gtest中的ASSERT，也有CHECK_EQ, CHECK_GT等变种。"
> - "你**应该**根据比较关系使用具体的CHECK_XX，这样当出现错误时，你可以看到更详细的信息"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "Another import variation of logging is CHECK(expression). When expression evaluates to false, it will print a fatal log."
> - "You should use CHECK_XX for arithmetic condition so that you can see more detailed information when check failed."
> - "Like DLOG, you should NOT include important side effects inside DCHECK."