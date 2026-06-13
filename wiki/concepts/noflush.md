---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "logging::noflush"
  - "noflush 哨兵对象"
---

## Description
noflush 是 brpc 流式日志（streaming_log）机制中的一个特殊哨兵对象，由 [[entities/brpc|brpc]] 提供。当通过 `LOG(...)` 宏追加 noflush 后，该条日志不会立即刷入屏幕，而是保留在线程局部（thread-local）缓冲中等待后续合并。下一次不附带 `noflush` 的普通 LOG 输出时，缓冲中的累积内容会随该次日志一并刷入屏幕，从而避免每条日志单独占一行的碎片化输出。典型的循环用法为：`LOG(TRACE) << "Items:" << noflush; for (...) LOG(TRACE) << *it << noflush; LOG(TRACE);`，最终只产生单行 TRACE 输出。noflush 同时支持 bthread，可让各协程累积日志而在 RPC 结束时统一刷新，实现类 UB pushnotice 的批量输出效果。需要注意的是，文档明确警告：异步方法中不得使用 noflush，因其底层会切换 bthread 上下文，可能导致累积日志丢失或行为错乱。此外，如果编译时开启了 glog 选项，则不支持 noflush。

## Related Concepts
- [[concepts/thread-local缓冲|thread-local 缓冲]]
- [[concepts/LOG宏|LOG 宏]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/streaming_log|streaming_log]]

## Mentions in Source
> **Source: [[sources/streaming_log|streaming_log]]**
> - "如果你暂时不希望刷到屏幕，加上noflush。这一般会用在打印循环中"
> - "前两次TRACE日志都没有刷到屏幕，而是还记录在thread-local缓冲中，第三次TRACE日志则把缓冲都刷入了屏幕。"
> - "> 注意：如果编译时开启了glog选项，则不支持noflush。"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "If you don't want to flush the log at once, append noflush. It's commonly used inside a loop:"
> - "The noflush feature also support bthread so that we can push lots of logs from the server's bthreads without actually print them (using noflush), and flush the whole log at the end of RPC."