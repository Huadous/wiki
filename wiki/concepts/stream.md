---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_streaming_rpc]]"
tags:
  - "term"
aliases:
  - "流"
  - "用户空间连接"
  - "Stream API"
  - "流"
  - "用户空间连接"
---

## Description
Stream 是 BRPC 中实现 Streaming RPC 的核心抽象，它在用户空间定义了逻辑连接，与底层 TCP 传输协议解耦。每个 Stream 通过唯一的 `StreamId` 进行标识，客户端可以使用 `StreamCreate()` 发起创建，服务端通过 `StreamAccept()` 接受请求来完成 Stream 的建立。Stream 支持全双工通信，发送方可以连续写入消息，接收方按顺序读取；多个 Stream 可以共享同一个 TCP 连接，提高网络资源利用率。Stream API 提供了完整的函数集合来操作 Stream 的生命周期，包括 `StreamWrite()`（写入消息）、`StreamWait()`（等待缓冲区可写，支持同步和异步版本）和 `StreamClose()`（关闭 Stream）。这些函数返回 0 表示成功，错误时返回 `EAGAIN`、`EINVAL`、`ETIMEDOUT` 等错误码，使得开发者可以利用 Streaming RPC 模型实现高效的数据传输。

## 关键特征
- **用户空间抽象**：Stream 不是操作系统级别的连接，而是在用户态定义的逻辑连接，与底层传输协议解耦
- **唯一标识**：每个 Stream 拥有唯一的 `StreamId`，所有操作（读、写、关闭）都通过该 ID 进行
- **多路复用**：多个 Stream 可以共享同一个 TCP 连接，提高网络资源利用率
- **全双工通信**：客户端和服务端可以同时发送和接收消息，互不阻塞
- **顺序保证**：接收方按发送顺序读取消息，保证消息的有序性
- **生命周期明确**：由客户端主动创建，服务端被动接受，双方均可发起关闭
- **标准 API 接口**：通过 `StreamCreate`、`StreamAccept`、`StreamWrite`、`StreamWait`、`StreamClose` 等函数提供统一的操作接口

## 应用
- **实时消息推送**：服务端可以持续向客户端推送更新，如股票行情、通知等
- **大数据流式处理**：在 Spark、Flink 等场景中传输批量数据，避免频繁建立连接和握手
- **双向流式通信**：如聊天应用中的消息发送与接收、在线游戏中的状态同步
- **事件流订阅**：客户端订阅特定事件，服务端通过 Stream 持续发送事件数据

## 相关概念
- [[concepts/streaming-rpc|Streaming RPC]] — 流式 RPC 的父概念，Stream 是其核心抽象
- [[concepts/streamoptions|StreamOptions]] — Stream 的配置结构体，用于设置 Stream 创建时的参数
- [[concepts/io多路复用|io多路复用]] — 底层 TCP 连接复用技术的核心机制
- [[concepts/握手|握手]] — Stream 建立过程中的连接协商阶段
- [[concepts/流控|流控]] — Stream 的流控制机制，决定了写入是否阻塞（通过 `StreamWait` 管理）

## 相关实体
- [[entities/brpc|brpc]] — 实现 Stream 抽象的核心框架，Stream API 是 BRPC 的一部分
- [[entities/iobuf|iobuf]] — BRPC 的缓冲区类型，用于 `StreamWrite` 中传递消息数据

## 来源提及
> **Source: [[brpc/en_streaming_rpc]]**
> - "Streaming RPC enables users to establish Stream which is a user-space connection between client and service."
> - "Multiple Streams can share the same TCP connection at the same time."
> - "In the code we use StreamId to represent a Stream, which is the key ID to pass when reading, writing, closing the Stream."

> **Source: [[sources/en_streaming_rpc|en_streaming_rpc]]**
> - "int StreamCreate(StreamId* request_stream, Controller &cntl, const StreamOptions* options);"
> - "int StreamAccept(StreamId* response_stream, Controller &cntl, const StreamOptions* options);"
> - "int StreamWrite(StreamId stream_id, const butil::IOBuf &message);"
> - "int StreamWait(StreamId stream_id, const timespec* due_time);"