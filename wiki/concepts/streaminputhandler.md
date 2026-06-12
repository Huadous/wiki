---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [standard]
aliases:
  - "流输入处理接口"
  - "Stream 输入处理器"
---


# StreamInputHandler

## 定义

StreamInputHandler 是 brpc 中用于处理 Streaming RPC 消息接收、空闲超时和流关闭事件的抽象回调接口。用户通过实现其三个纯虚函数来定义应用层对 Stream 事件的处理逻辑，是构建流式 RPC 应用的核心组件。

## 关键特征

- **抽象基类**：作为纯虚接口定义，强制子类实现所有回调方法
- **Stream 事件覆盖**：包含三种关键回调：消息到达、空闲超时、流关闭
- **回调时机明确**：`on_received_messages` 首次调用时机有明确定义——客户端在同步 RPC 返回后或异步 `done->Run()` 后；服务端在 `done->Run()` 后
- **批量消息处理**：`on_received_messages` 接收 `butil::IOBuf *const messages[]` 数组和大小参数，支持批量处理
- **连接生命周期管理**：通过 `on_closed` 回调通知对端关闭事件，便于资源清理

## 应用

- **流式 RPC 应用开发**：通过继承 StreamInputHandler 实现自定义数据处理逻辑
- **实时数据推送**：服务端接收客户端订阅后通过 Stream 持续推送数据
- **双向流通信**：客户端和服务端同时实现回调处理双向消息流
- **超时重连**：利用 `on_idle_timeout` 检测空闲连接并触发重连策略

## 相关概念

- [[concepts/stream|Stream]]
- [[concepts/streamoptions|StreamOptions]]
- [[concepts/streaming-rpc|Streaming RPC]]

## 相关实体

- [[entities/brpc|brpc]]
- [[entities/iobuf|IOBuf]]

## 来源提及

- "class StreamInputHandler { public: // Callback when stream receives data virtual int on_received_messages(StreamId id, butil::IOBuf *const messages[], size_t size) = 0; // Callback when there is no data for a long time on the stream virtual void on_idle_timeout(StreamId id) = 0; // Callback when stream is closed by the other end virtual void on_closed(StreamId id) = 0; };" — [[sources/en_streaming_rpc|en_streaming_rpc]]
- "on_received_messages 首次调用的时机：在客户端同步 RPC 返回后或异步 RPC done->Run() 后，在服务端 done->Run() 后" — [[sources/en_streaming_rpc|en_streaming_rpc]]