---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_overview]]"]
tags: [method]
aliases:
  - "并行消息处理"
  - "Parallel request processing"
---


# Parallel Message Processing

## 定义
并行消息处理是brpc在I/O层面的一项核心设计，它允许从同一个TCP连接（fd）中并行解析和处理多个请求，而无需等待前一个请求完全处理完毕。

## 关键特征
- **同连接并行**：来自同一TCP连接的不同消息可以被同时处理，突破传统单连接串行处理的瓶颈
- **事件驱动架构**：基于事件驱动模型和bthread用户态协程实现高效的并发调度
- **无阻塞设计**：处理大消息时不会阻塞同连接中的其他小消息的解析与处理
- **细粒度并发**：不仅在不同fd之间实现并行，在同一fd内的不同消息层面也实现了并行

## 应用
- **高性能RPC框架**：在brpc等框架中显著提升多请求并发处理能力和整体吞吐量
- **微服务架构**：适用于需要同时处理大量RPC调用的微服务网关和API服务器
- **实时通信系统**：在需要低延迟响应的场景下，避免大请求头阻塞后续小请求
- **流量混合场景**：当请求大小差异较大时（如小查询与大批量上传混用），能大幅降低尾部延迟

## 相关概念
- [[concepts/IO-thread-model|IO-thread model]]
- [[concepts/bthread|bthread]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/eventdispatcher|eventdispatcher]]
- [[entities/inputmessenger|inputmessenger]]
- [[entities/socket|socket]]

## 来源提及
- "In brpc, reading from different fds is parallelized and even processing different messages from one fd is parallelized as well." — [[sources/en_overview|en_overview]]
- "Parsing a large message does not block other messages from the same fd, not to mention other fds." — [[sources/en_overview|en_overview]]