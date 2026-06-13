---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_streaming_rpc]]"
  - "[[brpc/streaming_rpc.md]]"
tags:
  - "standard"
aliases:
  - "流选项"
  - "Stream 配置结构体"
---

## 相关概念
- [[concepts/stream|stream]]
- [[concepts/streaming-rpc|streaming-rpc]]
- [[concepts/滑动窗口流控|滑动窗口流控]]
- [[concepts/流控|流控]]
- [[concepts/streaminputhandler|StreamInputHandler]]
- [[concepts/streamcreate|StreamCreate]]
- [[concepts/streamaccept|StreamAccept]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
> **Source: [[sources/en_streaming_rpc|en_streaming_rpc]]**
> - "struct StreamOptions
    // The max size of unconsumed data allowed at remote side.
    // If |max_buf_size| <= 0, there's no limit of buf size
    // default: 2097152 (2M)
    int max_buf_size;
 
    // Notify user when there's no data for at least |idle_timeout_ms|
    // milliseconds since the last time that on_received_messages or on_idle_timeout
    // finished.
    // default: -1
    long idle_timeout_ms;
     
    // Maximum messages in batch..."

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - "struct StreamOptions // The max size of unconsumed data allowed at remote side. If |max_buf_size| <= 0, there's no limit of buf size default: 2097152 (2M)"
> - "Create a Stream at client-side along with the |cntl|, which will be connected when receiving the response with a Stream from server-side. If |options| is NULL, the Stream will be created with default options"