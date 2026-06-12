---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_streaming_rpc]]"]
tags: [standard]
aliases:
  - "流选项"
  - "Stream 配置结构体"
---


# StreamOptions

## 定义
StreamOptions 是一个 C++ 结构体，用于配置 brpc 框架中 Stream 的行为。它通过定义缓冲区大小、空闲超时、批处理大小和消息处理器等参数，控制数据流在远程端和本地端之间的传输策略。

## 关键特征
- **配置性高**：包含 `max_buf_size`、`idle_timeout_ms`、`messages_in_batch` 和 `handler` 四个可配置字段，涵盖流控、超时、批处理和消息处理的核心行为。
- **流量控制**：`max_buf_size` 为正数时，限制远程端未消费数据的最大大小，触发流控机制。
- **空闲检测**：`idle_timeout_ms` 设置空闲超时阈值，用于检测连接空闲并通知用户。
- **批处理优化**：`messages_in_batch` 控制每次回调传递给 `on_received_messages` 的最大消息数，优化批量处理性能。
- **安全性**：当 `handler` 为 NULL 时，远程端不允许写入消息，提供防护机制。

## 应用
- **流式 RPC 配置**：在创建或接受 Stream 时，通过 StreamOptions 实例化具体的流行为参数。
- **资源保护**：通过设置 `max_buf_size` 限制未消费数据量，防止内存溢出。
- **超时处理**：利用 `idle_timeout_ms` 实现空闲通知，用于资源回收或重连逻辑。
- **性能调优**：调整 `messages_in_batch` 优化消息批处理的吞吐量和延迟。

## 相关概念
- [[concepts/stream|stream]]
- [[concepts/streaming-rpc|streaming-rpc]]
- [[concepts/滑动窗口流控|滑动窗口流控]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "struct StreamOptions
    // The max size of unconsumed data allowed at remote side.
    // If |max_buf_size| <= 0, there's no limit of buf size
    // default: 2097152 (2M)
    int max_buf_size;
 
    // Notify user when there's no data for at least |idle_timeout_ms|
    // milliseconds since the last time that on_received_messages or on_idle_timeout
    // finished.
    // default: -1
    long idle_timeout_ms;
     
    // Maximum messages in batch..." — [[sources/en_streaming_rpc|en_streaming_rpc]]