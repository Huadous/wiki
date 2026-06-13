---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "other"
aliases:
  - "InputMessenger"
  - "输入消息切割器"
---

## Related Entities
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/socket|Socket]]
- [[entities/brpc|brpc]]

## Related Concepts
- [[concepts/bthread|bthread]]
- [[concepts/work-stealing|work stealing]]
- [[concepts/message|Message]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/edge-triggered-mode|Edge triggered 模式]]

## Mentions in Source

> **Source: [[sources/en_io|en_io]]**
> - "InputMessenger负责从fd上切割和处理消息，它通过用户回调函数理解不同的格式。"
> - "Parse一般是把消息从二进制流上切割下来，运行时间较固定；Process则是进一步解析消息(比如反序列化为protobuf)后调用用户回调，时间不确定。"

> **Source: [[sources/io|io]]**
> - "InputMessenger负责从fd上切割和处理消息，它通过用户回调函数理解不同的格式。"
> - "Parse一般是把消息从二进制流上切割下来，运行时间较固定；Process则是进一步解析消息(比如反序列化为protobuf)后调用用户回调，时间不确定。"
> - "InputMessenger会逐一尝试多种协议，由于一个连接上往往只有一种消息格式，InputMessenger会记录下上次的选择，而避免每次都重复尝试。"