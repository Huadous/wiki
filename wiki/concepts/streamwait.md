---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_rpc|streaming_rpc]]"]
tags: [method]
aliases:
  - "StreamWait API"
  - "等待Stream可写"
---


# StreamWait

## 定义
StreamWait 是 brpc [[sources/streaming_rpc|Streaming RPC]] 中用于流控等待的 API。当 [[concepts/streamwrite|StreamWrite]] 因为发送缓冲区已满而返回 `EAGAIN` 时，调用方可通过 StreamWait 阻塞（同步）或注册回调（异步）等待对端消费已发送但尚未接收的数据，直到待发送的缓冲区大小低于 `max_buf_size` 或发生错误为止。

## 关键特征
- **触发场景**：仅在 [[concepts/streamwrite|StreamWrite]] 因缓冲区满返回 `EAGAIN` 时调用，用于实现生产者-消费者背压机制。
- **同步版本**：阻塞当前线程直到缓冲区低于阈值，支持 `due_time` 参数进行超时控制；超时返回 `ETIMEDOUT`；等待期间若 Stream 被关闭，立即唤醒并返回 `EINVAL`。
- **异步版本**：通过 `on_writable` 回调通知等待结果，避免阻塞调用线程，适合高并发生产者场景。
- **等待条件**：等待对端消费数据，使待发送缓冲区大小低于 `max_buf_size`；任一错误发生也会解除等待。
- **返回码语义**：成功返回 0，否则返回对应的 errno（如 `ETIMEDOUT`、`EINVAL` 等）。

## 应用
- **流式生产者-消费者背压控制**：在流式 RPC 场景下，发送端需要根据对端消费速率调整写入节奏，避免内存无限堆积。
- **同步阻塞式流控**：单线程或低并发生产者可直接同步调用 StreamWait，简化等待逻辑。
- **异步高吞吐写入**：多线程异步生产者通过 `on_writable` 回调继续发送，最大化吞吐量。
- **超时保护**：同步版本通过 `due_time` 参数防止因对端长时间不消费导致生产者永久阻塞。
- **优雅关闭处理**：在等待期间检测到 Stream 关闭时立即唤醒并报错，便于调用方及时清理资源。

## 相关概念
- [[concepts/流控|流控]]
- [[concepts/streamwrite|StreamWrite]]
- [[concepts/streaming-rpc|Streaming RPC]]

## 相关实体
- [[entities/streamid|StreamId]]

## 来源提及
- "// Wait util the pending buffer size is less than |max_buf_size| or error occurs\n// Returns 0 on success, errno otherwise" — [[sources/streaming_rpc|streaming_rpc]]
- "当存在较多已发送但未接收的数据时，发送端的Write操作会立即失败(返回EAGAIN）， 这时候可以通过同步或异步的方式等待对端消费掉数据。" — [[sources/streaming_rpc|streaming_rpc]]