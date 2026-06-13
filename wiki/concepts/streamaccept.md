---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_rpc|streaming_rpc]]"]
tags: [method]
aliases:
  - "接受Stream"
  - "StreamAccept API"
---


# StreamAccept

## 定义
StreamAccept 是 brpc Streaming RPC 中服务端用于接受 Stream 的 API，对应于 [[concepts/streamcreate|StreamCreate]] 的服务端侧。当 Server 收到带有 Stream 的 RPC 请求后，调用 StreamAccept 即可接受该 Stream。

## 关键特征
- **服务端侧 API**：在 Server 端被调用，用于接受由 Client 通过 [[concepts/streamcreate|StreamCreate]] 创建并随请求发送过来的 Stream
- **前置条件检查**：如果 Client 没有在请求中创建 Stream（即 `cntl.has_remote_stream()` 返回 false），StreamAccept 会失败
- **产生 response_stream**：接受成功后，服务端会产生对应的 `response_stream`，用于向 Client 发送数据
- **多重载版本**：提供单 Stream 和多 Stream 两个重载版本，对应不同的使用场景

## 应用
- **双向流式 RPC**：在 Server 端处理 Client 发起的流式请求时，通过 StreamAccept 接受 Stream 并获取 `response_stream`，随后可主动向 Client 推送数据，实现双向通信
- **服务端主动推送场景**：例如 Server 在收到流式请求后需要持续向 Client 推送通知、日志、监控数据等
- **需要服务端确认 Stream 建立的场景**：当业务逻辑要求 Server 显式确认并接管 Stream 时使用

## 相关概念
- [[concepts/streamcreate|StreamCreate]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/stream|Stream]]

## 相关实体
- [[entities/streamid|StreamId]]
- [[entities/streamoptions|StreamOptions]]
- [[entities/controller|Controller]]

## 来源提及
- [Called at the server side]
// Accept the Stream. If client didn't create a Stream with the request
// (cntl.has_remote_stream() returns false), this method would fail. — [[sources/streaming_rpc|streaming_rpc]]
- service在收到RPC后可以通过调用StreamAccept接受。接受后Server端对应产生的Stream存放在response_stream中，Server可通过这个Stream向Client发送数据。 — [[sources/streaming_rpc|streaming_rpc]]