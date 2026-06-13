---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_rpc]]"]
tags: [term]
aliases:
  - "StreamId"
  - "Stream Id"
  - "流标识"
---


# StreamId

## 定义
StreamId 是 brpc 中用于标识一个 [[concepts/Stream|Stream]] 的对象。程序中对 Stream 的读写、关闭操作都作用在这个 Id 上。StreamId 通过 [[concepts/StreamCreate|StreamCreate]]（Client 端）或 [[concepts/StreamAccept|StreamAccept]]（Server 端）创建得到，在建立成功后即可用于 [[concepts/StreamWrite|StreamWrite]]、[[concepts/StreamWait|StreamWait]]、[[concepts/StreamClose|StreamClose]] 等 API 调用。文档还提供了 StreamIds 类型用于同时表示多个 Stream 的集合，配合批量创建和接受 API 使用。

## 关键特征
- 作为 Stream 的标识符，所有 Stream 相关操作的句柄
- 由 `StreamCreate`（Client 端）或 `StreamAccept`（Server 端）创建产生
- 创建成功后即可作为参数传入 `StreamWrite`、`StreamWait`、`StreamClose` 等 API
- 提供 StreamIds 集合类型，用于表示多个 Stream 的批量操作
- 与 [[entities/socket|socket]] 系统解耦，是 brpc 流式 RPC 体系中的独立抽象

## 应用
- **Client 端流式 RPC**：通过 `StreamCreate` 获取 StreamId，进而向服务端发送流式数据或接收流式响应
- **Server 端流式 RPC**：通过 `StreamAccept` 获取客户端发起的 Stream 的 StreamId，用于处理双向流通信
- **批量流管理**：使用 StreamIds 集合类型，配合批量创建或接受 API，一次性管理多个 Stream
- **流的生命周期控制**：通过 StreamId 完成流的读写等待与关闭操作

## 相关概念
- [[concepts/Stream|Stream]]
- [[concepts/StreamCreate|StreamCreate]]
- [[concepts/StreamAccept|StreamAccept]]
- [[concepts/StreamWrite|StreamWrite]]
- [[concepts/StreamClose|StreamClose]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "程序中我们用StreamId代表一个Stream，对Stream的读写，关闭操作都将作用在这个Id上。" — [[sources/streaming_rpc|streaming_rpc]]
- "int StreamCreate(StreamId* request_stream, Controller &cntl, const StreamOptions* options);" — [[sources/streaming_rpc|streaming_rpc]]