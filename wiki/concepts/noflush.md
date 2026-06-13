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

## Related Concepts
- [[concepts/thread-local缓冲|thread-local 缓冲]]
- [[concepts/LOG宏|LOG 宏]]
- [[concepts/LOG macro|LOG macro]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/streaming_log|streaming_log]]
- [[entities/bthread|bthread]]

## Mentions in Source
> **Source: [[sources/streaming_log|streaming_log]]**
> - "如果你暂时不希望刷到屏幕，加上noflush。这一般会用在打印循环中"
> - "前两次TRACE日志都没有刷到屏幕，而是还记录在thread-local缓冲中，第三次TRACE日志则把缓冲都刷入了屏幕。"
> - "> 注意：如果编译时开启了glog选项，则不支持noflush。"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "If you don't want to flush the log at once, append noflush. It's commonly used inside a loop:"
> - "The noflush feature also support bthread so that we can push lots of logs from the server's bthreads without actually print them (using noflush), and flush the whole log at the end of RPC."