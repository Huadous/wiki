---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_streaming_rpc]]"
  - "[[brpc/streaming_rpc.md]]"
tags:
  - "term"
aliases:
  - "流"
  - "用户空间连接"
  - "Stream API"
  - "流"
  - "用户空间连接"
---

## Related Concepts
- [[concepts/streaming-rpc|Streaming RPC]] — 流式 RPC 的父概念，Stream 是其核心抽象
- [[concepts/streamid|StreamId]] — Stream 的唯一标识，所有读写、关闭操作都通过该 Id 进行
- [[concepts/streamoptions|StreamOptions]] — Stream 的配置结构体，用于设置 Stream 创建时的参数
- [[concepts/streaminputhandler|StreamInputHandler]] — 服务端用于接收 Stream 消息的处理器接口
- [[concepts/io多路复用|io多路复用]] — 底层 TCP 连接复用技术的核心机制，多个 Stream 可共享同一连接
- [[concepts/握手|握手]] — Stream 建立过程中的连接协商阶段
- [[concepts/流控|流控]] — Stream 的流控制机制，决定了写入是否阻塞（通过 `StreamWait` 管理）

## Related Entities
- [[entities/brpc|brpc]] — 实现 Stream 抽象的核心框架，Stream API 是 BRPC 的一部分
- [[entities/iobuf|iobuf]] — BRPC 的缓冲区类型，用于 `StreamWrite` 中传递消息数据

## Mentions in Source
> **Source: [[sources/en_streaming_rpc]]**
> - "Streaming RPC enables users to establish Stream which is a user-space connection between client and service."
> - "Multiple Streams can share the same TCP connection at the same time."
> - "In the code we use StreamId to represent a Stream, which is the key ID to pass when reading, writing, closing the Stream."
> - "int StreamCreate(StreamId* request_stream, Controller &cntl, const StreamOptions* options);"
> - "int StreamAccept(StreamId* response_stream, Controller &cntl, const StreamOptions* options);"
> - "int StreamWrite(StreamId stream_id, const butil::IOBuf &message);"
> - "int StreamWait(StreamId stream_id, const timespec* due_time);"

> **Source: [[sources/streaming_rpc]]**
> - "Streaming RPC让用户能够在client/service之间建立用户态连接，称为Stream, 同一个TCP连接之上能同时存在多个Stream。"
> - "程序中我们用StreamId代表一个Stream，对Stream的读写，关闭操作都将作用在这个Id上。"
> - "目前Stream都由Client端建立。"