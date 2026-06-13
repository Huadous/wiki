---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_rpc.md]]"]
tags: [method]
aliases:
  - "创建Stream"
  - "StreamCreate API"
---


# StreamCreate

## 定义
StreamCreate 是 brpc Streaming RPC 中客户端用于创建 Stream 的 API。它在 Client 本地预先创建一个或多个 Stream，然后通过一次使用 baidu_std 协议的 RPC 将这些 Stream 发送到对端 Service。如果 Service 接受了这批 Stream，response 返回后 Stream 即建立成功。返回值为 0 表示成功，-1 表示失败。

## 关键特征
- **客户端预创建模式**：Stream 先在 Client 本地创建，再通过 RPC 与远端 Service 建立连接，类似 Linux 中先创建 socket 再 connect 的流程。
- **批量创建能力**：支持单 Stream 和多 Stream 两个重载版本，对应不同的 StreamOptions 配置，可一次发送一批 Stream 给对端。
- **同步建立机制**：通过一次 baidu_std 协议的 RPC 调用完成 Stream 建立，response 返回即表示对端 Service 是否接受。
- **明确的返回值语义**：返回 0 表示成功（Service 接受了这批 Stream），返回 -1 表示失败。

## 应用
- brpc 流式 RPC 客户端在发起流式通信前调用 StreamCreate 来初始化 Stream 对象。
- 适用于需要长期双向数据流传输的场景，如流式 Echo、消息推送、日志流等。
- 在已知对端 Service 接受 Stream 的前提下，可通过 StreamOptions 配置单 Stream 或多 Stream 模式以满足不同的并发流需求。

## 相关概念
- [[concepts/streamaccept|StreamAccept]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/stream|Stream]]

## 相关实体
- [[entities/streamid|StreamId]]
- [[entities/streamoptions|StreamOptions]]
- [[entities/controller|Controller]]

## 来源提及
- "Called at the client side // Create a Stream at client-side along with the |cntl|, which will be connected when receiving the response with a Stream from server-side." — [[sources/streaming_rpc|streaming_rpc]]
- "Return 0 on success, -1 otherwise int StreamCreate(StreamId* request_stream, Controller &cntl, const StreamOptions* options);" — [[sources/streaming_rpc|streaming_rpc]]
- "用linux下建立连接的过程打比方，Client先创建socket（创建Stream），再调用connect尝试与远端建立连接（通过RPC建立Stream）" — [[sources/streaming_rpc|streaming_rpc]]