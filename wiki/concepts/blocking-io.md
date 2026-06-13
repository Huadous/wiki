---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "term"
aliases:
  - "Blocking IO"
  - "阻塞I/O"
  - "同步阻塞IO"
---

## Related Concepts
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/asynchronous-io|Asynchronous IO]]

## Related Entities
- [[entities/tcmalloc|tcmalloc]]
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/en_io|brpc IO设计文档]]**
> - "Blocking IO: once an IO operation is issued, the calling thread is blocked until the IO ends, which is a kind of synchronous IO, such as default actions of posix read and write."
> - "When the IO concurrency is low, non-blocking IO is not necessarily more efficient than blocking IO, which is handled completely by the kernel."

> **Source: en_io**
> - 未提供与阻塞IO直接相关的新增信息。

> **Source: [[sources/io|brpc IO 模型]]**
> - "blocking IO: 发起IO操作后阻塞当前线程直到IO结束，标准的同步IO，如默认行为的posix read和write。"
> - "但当IO并发度愈发提高时，blocking IO阻塞一个线程的弊端便显露出来：内核得不停地在线程间切换才能完成有效的工作，一个cpu core上可能只做了一点点事情，就马上又换成了另一个线程，cpu cache没得到充分利用。"