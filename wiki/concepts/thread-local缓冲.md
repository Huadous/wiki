---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "term"
aliases:
  - "thread-local buffer"
  - "TLB"
  - "thread-local 缓冲机制"
---

## Related Concepts
- [[concepts/noflush]]
- [[concepts/流式日志]]
- [[concepts/thread-local-storage|thread-local storage]]（隐含的底层机制）

## Related Entities
- [[entities/logsink]]
- [[entities/stringsink]]
- [[entities/bthread]]（thread-local 缓冲在 bthread 场景下同样适用）
- [[entities/streaming_log|streaming_log]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - "在目前的实现中，送入日志流的日志被记录在thread-local的缓冲中，在完成一条日志后会被刷入屏幕或logging::LogSink，这个实现是线程安全的。"
> - "前两次TRACE日志都没有刷到屏幕，而是还记录在thread-local缓冲中，第三次TRACE日志则把缓冲都刷入了屏幕。"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "In the current implementation, the logs are recorded in a thread-local buffer, which will be flushed into screen or ` logging::LogSink` after a complete log record."
> - "Of course, the implementation is thread safe."
> - "The first two LOG(TRACE) doesn't flush the log to the screen. They are recorded inside the thread-local buffer."