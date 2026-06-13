---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_streaming_rpc]]"
  - "[[brpc/streaming_rpc.md]]"
tags:
  - "phenomenon"
aliases:
  - "队头阻塞"
  - "HOL blocking"
  - "自动分段"
  - "队头阻塞"
  - "HOL blocking"
---

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

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - "支持自动切割过大的消息，避免Head-of-line blocking问题"
> - "在一些应用场景中， client或server需要向对面发送大量数据，这些数据非常大或者持续地在产生以至于无法放在一个RPC的附件中。"