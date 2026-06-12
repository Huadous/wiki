---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_streaming_rpc]]"
tags:
  - "phenomenon"
aliases:
  - "队头阻塞"
  - "HOL blocking"
  - "自动分段"
  - "队头阻塞"
  - "HOL blocking"
---

## Description
队头阻塞（Head-of-line blocking）是网络通信中的常见性能问题，根源在于先进先出（FIFO）队列的依赖特性——单个数据包的阻塞会直接影响后续所有包的顺序处理。该现象在多种协议和场景中出现，包括HTTP/1.1流水线、TCP连接中混合大小消息传输、以及流式RPC中的多流共享连接场景。在[[concepts/streaming-rpc|Streaming RPC]]中，自动分段机制是缓解队头阻塞的关键技术：当发送方写入一个很大的消息时，系统会自动将其分割成多个小段进行传输，使得同一连接上的其他流不会被单个大消息阻塞。接收方收到这些段后重新组装成原始消息，并保持[[concepts/消息边界|消息边界]]不变。这种分段策略显著提高了网络利用率和整体吞吐量，尤其是在多个[[concepts/stream|Stream]]共享同一个TCP连接时尤为重要。

## Related Concepts
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/stream|Stream]]
- [[concepts/消息边界|消息边界]]

## Related Entities
- [[entities/brpc|Apache brpc]]

## Mentions in Source
> **Source: [[sources/en_streaming_rpc|en_streaming_rpc]]**
> - "We support segment large messages automatically to avoid Head-of-line blocking problem."
> - "The basic transmission unit on Stream is message."