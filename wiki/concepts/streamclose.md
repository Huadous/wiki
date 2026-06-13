---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_rpc]]"]
tags: [method]
aliases:
  - "StreamClose API"
  - "关闭Stream"
---


# StreamClose

## 定义
StreamClose 是 brpc Streaming RPC 中用于关闭 Stream 的 API。它是 Stream 生命周期的终结操作，与 [[concepts/streamcreate|StreamCreate]] 配对完成 Stream 的完整生命周期。

## 关键特征
- 调用后，后续所有 [[concepts/streamwrite|StreamWrite]] 调用将失败
- 调用后，[[concepts/streamwait|StreamWait]] 会立即唤醒
- 两端的 `on_closed` 回调会在所有待发送缓冲区数据被接收完毕之后被通知
- 具有幂等性：可以被多次重复调用而不会产生副作用，避免因重复关闭导致的异常

## 应用
- 在 brpc Streaming RPC 通信中，由 Stream 的持有方在数据发送完毕后调用，以正常关闭 Stream
- 在错误处理或异常流程中调用，立即终止 Stream 并通知对端
- 用于配合 [[concepts/streamcreate|StreamCreate]] 完成 Stream 的完整生命周期管理

## 相关概念
- [[concepts/streaming_rpc|Streaming RPC]]
- [[concepts/stream|Stream]]
- [[concepts/streamwrite|StreamWrite]]
- [[concepts/streamcreate|StreamCreate]]
- [[concepts/streamwait|StreamWait]]

## 相关实体
- [[entities/streamid|StreamId]]
- [[entities/streaminputhandler|StreamInputHandler]]

## 来源提及
- Close |stream_id|, after this function is called:
//  - All the following |StreamWrite| would fail
//  - |StreamWait| wakes up immediately. — [[sources/streaming_rpc|streaming_rpc]]
- This function could be called multiple times without side-effects
int StreamClose(StreamId stream_id); — [[sources/streaming_rpc|streaming_rpc]]