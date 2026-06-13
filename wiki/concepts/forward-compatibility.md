---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "phenomenon"
aliases:
  - "向前兼容"
  - "forward-compatible"
---

## Related Concepts
- [[concepts/backward-compatibility|backward-compatibility]]：向后兼容性，旧代码能够读取新消息的能力；与向前兼容性共同构成 Protocol Buffers 的双向兼容性，但在 Edition Lifetimes 新方案下两者均被打破
- [[concepts/serialization|serialization]]：序列化，Protocol Buffers 的核心数据编码方式，向前兼容性的实现基础
- [[concepts/editions|Editions]]：Protobuf 版本（Edition）体系，向前兼容性假设成立与否取决于 Edition 生命周期方案的选择
- [[concepts/edition-patches|Edition Patches]]：补丁版本，因向前兼容性被打破而被重新引入的修复机制
- [[concepts/feature-lifetimes|Feature Lifetimes]]：特性生命周期，定义单个特性在 Edition 中如何引入、演进和淘汰

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]：Protocol Buffers 是实现向前兼容性的核心框架
- [[entities/editions-edition-lifetimes|editions-edition-lifetimes]]：Edition Lifetimes 提案，重新定义了 Edition 中特性的生命周期，直接改变了向前兼容性的假设

## Mentions in Source
> **Source: [[sources/overview|overview]]**
> - "New code will also transparently read old messages. New fields will not be present in old messages; in these cases protocol buffers provide a reasonable default value."
> - "It's standard for software products to be backward compatible, but it is less common for them to be forward compatible."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "We would only ever need multiple editions in a year if somehow we managed to speed up the rollout process and wanted faster turnaround."
> - "This changes those assumptions though, since now editions are neither forward-compatible (new features don't work in old editions) or backward-compatible (old features may not work in new editions)."
> - "No directly relevant information"