---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_rpc|streaming_rpc]]"]
tags: [method]
aliases:
  - "StreamWrite API"
  - "Stream 写入接口"
  - "写入Stream"
---


# StreamWrite

## 定义
StreamWrite 是 brpc Streaming RPC 中向 [[concepts/stream|Stream]] 写入消息的 API。调用方将 [[entities/butil-iobuf|butil::IOBuf]] 类型的消息写入 stream_id，接收端 handler 会按照发送顺序收到消息。返回值 0 表示成功，非零表示出错。

## 关键特征
- **消息类型**：接受 [[entities/butil-iobuf|butil::IOBuf]] 类型的消息作为参数。
- **顺序保证**：接收端 handler 按照写入顺序依次接收消息，体现 Streaming RPC 全双工且保证顺序的特性。
- **流式持续写入**：输入端可以源源不断地往 Stream 中写入消息，消息以流式方式持续传输。
- **返回值**：成功返回 0，失败返回 errno。
- **关键错误码**：
  - `EAGAIN`：设置了 `max_buf_size` 且对端未消费的数据已超过限制。
  - `EINVAL`：`stream_id` 无效或已关闭。

## 应用
- 在 brpc Streaming RPC 场景中，由生产者端持续向 Stream 推送消息。
- 适用于需要全双工、消息有序传输的长连接通信，例如日志流、实时数据推送、消息队列桥接等。
- 与 [[concepts/流控|流控]] 配合使用，可通过 `max_buf_size` 限制对端未消费数据量，避免内存积压。

## 相关概念
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/stream|Stream]]
- [[concepts/流控|流控]]

## 相关实体
- [[entities/streamid|StreamId]]
- [[entities/butil-iobuf|butil::IOBuf]]

## 来源提及
- Write |message| into |stream_id|. The remote-side handler will received the
// message by the written order
// Returns 0 on success, errno otherwise — [[sources/streaming_rpc|streaming_rpc]]
- 输入端可以源源不断的往Stream中写入消息， 接收端会按输入端写入顺序收到消息。 — [[sources/streaming_rpc|streaming_rpc]]