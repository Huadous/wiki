---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
tags:
  - "method"
aliases:
  - "I/O 线程模型"
  - "IO thread architecture"
  - "IO threads"
  - "I/O 线程模型"
  - "IO thread architecture"
---

## 描述
IO 线程模型是常见的网络编程模型，其中线程专门用于等待和读取文件描述符上的事件。传统 IO 线程的主要问题在于，同一时刻每个线程只能读取一个文件描述符，当一个 IO 线程上的多个 fd 处于忙碌状态时，其他 fd 的读取操作可能会被延迟。在高负载场景下，这种延迟会加剧长尾效应，影响整体系统性能。brpc 采用 [[concepts/eventdispatcher|EventDispatcher]]（EDISP）结合 [[concepts/bthread|bthread]] 的方式避免了此问题——EDISP 并不像常见 IO 线程那样负责实际的读写操作，而是专注于事件分发，真正的读写处理由 bthread 协作完成，从而实现了消息级并行和无头阻塞，大幅提升了系统吞吐量和响应能力。

## 相关概念
- [[concepts/bthread|bthread]]
- [[concepts/parallel-message-processing|parallel-message-processing]]
- [[concepts/eventdispatcher|eventdispatcher]]
- [[concepts/non-blocking-io|non-blocking-io]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/eventdispatcher|eventdispatcher]]

## 来源提及
> **Source: [[sources/en_overview|en_overview]]**
- "Reading and parsing requests from different clients is fully parallelized and users don't need to distinguish between 'IO-threads' and 'Processing-threads'. Other implementations probably have 'IO-threads' and 'Processing-threads' and hash file descriptors(fd) into IO-threads."
- "In brpc, reading from different fds is parallelized and even processing different messages from one fd is parallelized as well."

> **Source: [[sources/en_io|en_io]]**
- "Unlike the common 'IO threads', EDISP is not responsible for reading or writing."
- "The problem of IO threads is that one thread can only read one fd at a given time, other reads may be delayed when many fds in one IO thread are busy."