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
  - "CHECK_XX"
  - "CHECK()"
  - "CHECK_EQ"
  - "CHECK_GT"
  - "CHECK macro"
  - "CHECK()"
  - "CHECK_EQ"
  - "CHECK_GT"
---

## Description
CHECK_XX 是 brpc streaming_log 中 CHECK 宏族的算术比较特化变体，涵盖 CHECK_EQ、CHECK_NE、CHECK_LT、CHECK_LE、CHECK_GT、CHECK_LE 等共六种二元关系。该组宏的设计动机是提供比通用 CHECK(expression) 更丰富的诊断输出：当断言失败时，除了打印表达式的源码文本外，还会同时输出左右两侧操作数的实际取值，例如 `CHECK_GT(x, y);` 失败时会输出 `Check failed: x > y (1 vs 2)`，使调试者无需借助调试器即可立即看到具体数值。源码对此给出了明确的最佳实践建议——**应当**使用具体的 CHECK_XX 来表达算术条件，而非退化为裸 CHECK。延续 DLOG/DCHECK 的设计传统，CHECK_XX 也存在对应的调试版本 DCHECK_XX，在 NDEBUG 宏被定义（即 Release 构建）时其参数表达式完全不会被求值，因此与 DCHECK 一样，**不应**在 DCHECK_XX 中放置具有副作用的代码。CHECK_XX 的语义与 gtest 中的 ASSERT_EQ/ASSERT_LT 等宏族直接对应，反映了 brpc 在 API 设计上对 gtest 测试断言风格的借鉴。

## Related Concepts
- [[concepts/log宏|LOG宏]]
- [[concepts/dlog宏|DLOG宏]]
- [[concepts/check宏|CHECK宏]]
- [[concepts/dcheck宏|DCHECK宏]]
- [[concepts/ndebug|NDEBUG]]

## Related Entities
- [[entities/butil|butil]]
- [[entities/streaming_log|streaming_log]]
- [[entities/gtest|gtest]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - "日志另一个重要变种是CHECK(expression)，当expression为false时，会打印一条FATAL日志。类似gtest中的ASSERT，也有CHECK_EQ, CHECK_GT等变种。"
> - "你**应该**根据比较关系使用具体的CHECK_XX，这样当出现错误时，你可以看到更详细的信息"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "Another import variation of logging is CHECK(expression). When expression evaluates to false, it will print a fatal log."
> - "You should use CHECK_XX for arithmetic condition so that you can see more detailed information when check failed."
> - "Like DLOG, you should NOT include important side effects inside DCHECK."
> - "has other form such as CHECK_EQ, CHECK_GT, and so on."
> - "You **should** use `CHECK_XX` for arithmetic condition so that you can see more detailed information when check failed."
> - "`CHECK_GT(x, y);  // Check failed: x > y (1 vs 2).`"