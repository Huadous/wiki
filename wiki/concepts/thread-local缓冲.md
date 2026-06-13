---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log.md]]"]
tags: [term]
aliases:
  - "thread-local buffer"
  - "TLB"
  - "thread-local 缓冲机制"
---


# thread-local 缓冲

## 定义
thread-local 缓冲是 streaming_log（即流式日志）实现线程安全的关键机制。在当前实现中，送入日志流的内容被记录在每个线程独立的 thread-local 缓冲中，在完成一条日志（即 LogMessage 析构时）后才会被刷入屏幕或 [[entities/logsink|LogSink]]。这种设计避免了多线程同时写日志时的锁竞争，每个线程独享自己的缓冲空间。

## 关键特征
- **线程隔离**：每个线程拥有独立的缓冲空间，互不干扰。
- **延迟刷新**：日志内容在 LogMessage 析构时才被刷出，而非写入时立即刷新。
- **无锁设计**：通过 thread-local 存储天然避免多线程写日志时的锁竞争。
- **批量输出基础**：同一线程内的多条日志可以暂存在缓冲中，由 noflush 等机制控制合适的统一刷新时机，实现批量输出。
- **依赖 thread-local 存储**：底层依赖编程语言/运行时的 thread-local storage 机制（如 C++11 的 `thread_local` 关键字）。

## 应用
- **多线程日志输出**：在高并发场景下避免锁竞争，提升日志写入性能。
- **流式日志批量化**：配合 noflush 机制，同一线程内的多条 TRACE / DEBUG 日志可以暂存于缓冲，在合适时机（如第三条日志触发时）一次性刷入屏幕，减少 I/O 次数。
- **调试与诊断**：在保持线程安全的前提下，允许用户控制日志的实际输出时机，便于排查时序问题。

## 相关概念
- [[concepts/noflush]]
- [[concepts/流式日志]]

## 相关实体
- [[entities/logsink]]
- [[entities/stringsink]]

## 来源提及
- "在目前的实现中，送入日志流的日志被记录在thread-local的缓冲中，在完成一条日志后会被刷入屏幕或logging::LogSink，这个实现是线程安全的。" — [[brpc/streaming_log|streaming_log]]
- "前两次TRACE日志都没有刷到屏幕，而是还记录在thread-local缓冲中，第三次TRACE日志则把缓冲都刷入了屏幕。" — [[brpc/streaming_log|streaming_log]]