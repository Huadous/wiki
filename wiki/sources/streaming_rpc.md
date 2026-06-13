---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/server.md]]"
  - "[[brpc/io.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
tags:
  - "Streaming RPC"
  - "Stream"
  - "流控"
  - "Head-of-line blocking"
  - "baidu_std协议"
  - "StreamOptions"
  - "StreamInputHandler"
  - "StreamId"
  - "StreamCreate"
  - "StreamAccept"
  - "StreamWrite"
  - "StreamWait"
  - "StreamClose"
aliases:
  - "Streaming RPC"
  - "流式RPC"
---

## 关键概念
- [[concepts/streaming-rpc|streaming-rpc]]：本文档的核心主题，用于传输大块或持续数据的交互模型。
- [[concepts/stream|stream]]：client 和 service 之间的用户态连接抽象，同一 TCP 连接上可存在多个。
- [[concepts/流控|流控]]：通过 max_buf_size 限制对端未消费数据量的机制，配合 StreamWait 使用。
- [[concepts/head-of-line-blocking|head-of-line-blocking]]：Streaming RPC 通过自动切割过大消息避免的队头阻塞问题。
- [[concepts/baidu_std协议|baidu_std协议]]：建立 Streaming RPC 所必需的通信协议。
- [[concepts/协议支持|协议支持]]：brpc Server 支持的多协议协商能力，streaming_rpc 为其中之一，与 http、h2c 等共享同一监听端口。
- [[concepts/streamoptions|streamoptions]]：用于配置 Stream 行为的结构体，包含 max_buf_size、idle_timeout_ms 等字段。
- [[concepts/streaminputhandler|streaminputhandler]]：处理 Stream 接收数据的虚基类，需实现 on_received_messages 等回调。
- [[concepts/streamid|streamid]]：标识一个 Stream 的对象，对 Stream 的读写、关闭操作都作用于该 Id。
- [[concepts/streamcreate|streamcreate]]：客户端用于创建 Stream 的 API。
- [[concepts/streamaccept|streamaccept]]：服务端用于接受 Stream 的 API。
- [[concepts/streamwrite|streamwrite]]：向 Stream 写入消息的 API，按发送顺序到达对端。
- [[concepts/streamwait|streamwait]]：用于流控等待的 API，支持同步和异步两种方式。
- [[concepts/streamclose|streamclose]]：关闭 Stream 的 API，具有幂等性。

## 要点
- Streaming RPC 是 brpc 提供的用于传输大块或持续数据的交互模型，基于用户态连接 Stream 实现流水线式传输。
- 同一 TCP 连接之上能同时存在多个 Stream，数据以消息为单位传输，保证消息边界和顺序一致性。
- Stream 目前只支持由 Client 端建立，建立过程必须使用 baidu_std 协议。
- Streaming RPC 支持全双工、流控、超时提醒，并自动切割过大消息以避免 Head-of-line blocking。
- 核心 API 包括 StreamCreate（客户端建立）、StreamAccept（服务端接受）、StreamWrite（写入）、StreamWait（流控等待）和 StreamClose（关闭）。
- 通过继承 StreamInputHandler 并填入 StreamOptions 的 handler 字段可处理对端写入数据、空闲超时和关闭事件。
- 流控机制在已发送未接收数据超过 max_buf_size 时让 Write 返回 EAGAIN，并提供同步/异步的 StreamWait 等待对端消费。
- streaming_rpc 同时也是 brpc Server 支持的一种协议名称，在协议层中以字符串 "streaming_rpc" 表示，且为默认启用。
- brpc Server 支持的协议包括 baidu_std、streaming_rpc、http、h2c 等，这些协议共用同一个 listen 端口，由 server 自动协商使用，无需为不同协议分配不同端口。