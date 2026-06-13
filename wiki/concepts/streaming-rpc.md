---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_streaming_rpc]]"
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/io.md]]"
tags:
  - "method"
aliases:
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "streaming_rpc"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "流式RPC (Streaming RPC)"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "streaming_rpc"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "流式RPC"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "streaming_rpc"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "流式RPC (Streaming RPC)"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "streaming_rpc"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
  - "全双工"
  - "流式 RPC"
  - "Streaming RPC"
  - "Streaming Remote Procedure Call"
---

## Description
Streaming RPC 是 brpc 默认启用的流式 RPC 协议，显示为字符串 "streaming_rpc"，与 [[concepts/baidu_std协议|baidu_std]]、[[concepts/协议支持|http、h2c]] 等协议并列作为 brpc 的核心协议之一；它通过统一的 listen 端口监听，由 server 自动进行协议协商，因此用户无需为不同协议配置不同端口。该协议的核心思想是在 client 与 service 之间建立用户态连接——称为 [[concepts/Stream|Stream]]，同一个 TCP 连接之上能同时存在多个 Stream，从而实现高效复用。

Streaming RPC 提供以下关键保证：消息边界清晰、接收消息顺序与发送消息顺序严格一致、全双工通信、内置 [[concepts/流控|流控]] 机制、提供超时提醒、支持自动切割过大的消息以避免 [[concepts/Head-of-line blocking|Head-of-line blocking]] 问题。在 IO 层面，它与 [[entities/Socket|Socket]] 配合，**复用了 Socket 的 wait-free 写出机制以降低工程复杂度并提升并发性能**，这一点在 [[sources/io|io]] 与 [[sources/en_io|en_io]] 中均被明确提及。

然而，Streaming RPC 的多连接、长消息与多 Stream 共存特性也使其在传统单线程 IO 模型下更容易暴露问题。[[sources/io|io]] 文档指出："多租户、复杂分流算法，Streaming RPC 等功能会加重这个问题。" 在 brpc 传统的"一个 IO 线程同时只能读一个 fd"的模型下，繁忙 fd 的积压会延迟同 IO 线程上其他 fd 的读取，而 Streaming RPC 场景下单个 fd 上往往承载更大的消息流与更多 Stream，这一问题会被显著放大。brpc 通过 [[entities/EventDispatcher|EventDispatcher]]（EDISP）+ [[entities/bthread|bthread]] 的设计让 fd 间和 fd 内的消息都能并发处理，从而在 Streaming RPC 等大消息、长连接场景下及时处理不同来源的消息并减少长尾延迟。

## Related Concepts
- [[concepts/流控|流控]]
- [[concepts/Head-of-line blocking|Head-of-line blocking]]
- [[concepts/baidu_std协议|baidu_std协议]]
- [[concepts/StreamOptions|StreamOptions]]
- [[concepts/StreamInputHandler|StreamInputHandler]]
- [[concepts/Stream|Stream]]
- [[concepts/wait-free|wait-free write]]
- [[concepts/协议支持|协议支持]]
- [[concepts/单线程反应器|单线程反应器]]
- [[concepts/Wait-free MPSC 链表|Wait-free MPSC 链表]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/bthread|bthread]]
- [[entities/hulu_pbrpc|hulu_pbrpc]]
- [[entities/grpc|grpc]]
- [[entities/RTMP|RTMP]]
- [[entities/baidu|baidu]]
- [[entities/sofa_pbrpc|sofa_pbrpc]]
- [[entities/nova_pbrpc|nova_pbrpc]]
- [[entities/public_pbrpc|public_pbrpc]]
- [[entities/ub|ub]]
- [[entities/http_client|http_client]]
- [[entities/socket|Socket]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/inputmessenger|InputMessenger]]
- [[entities/examplestreaming_echo_c++|examplestreaming_echo_c++]]

## Mentions in Source

> **Source: [[sources/en_streaming_rpc|en_streaming_rpc]]**
> - [具体引用内容待补充]

> **Source: [[sources/en_io|en_io]]**
> - "Multi-tenancy, complicated load balancing and Streaming RPC worsen the problem."
> - "Streaming RPC also uses Socket to reuse the code on wait-free write."
> - "Under high workloads, regular long delays on one fd may slow down all fds in the IO thread, causing more long tails."
> - "Streaming RPC also uses Socket to reuse the code on wait-free write."
> - "Multi-tenancy, complicated load balancing and Streaming RPC worsen the problem."

> **Source: [[sources/en_io|en_io]]**
> - 该来源中未找到与Streaming RPC直接相关的额外信息。

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - "Streaming RPC让用户能够在client/service之间建立用户态连接，称为Stream, 同一个TCP连接之上能同时存在多个Stream。"
> - "Streaming RPC保证：- 有消息边界。 - 接收消息的顺序和发送消息的顺序严格一致。 - 全双工。 - 支持流控。 - 提供超时提醒 - 支持自动切割过大的消息，避免Head-of-line blocking问题"

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - 该来源中未找到与Streaming RPC直接相关的额外信息。

> **Source: [[sources/server|server]]**
> - "流式RPC协议，显示为\"streaming_rpc\", 默认启用。"
> - "支持的协议有：-百度标准协议... -流式RPC协议，显示为\"streaming_rpc\", 默认启用。"

> **Source: [[sources/io|io]]**
> - "多租户、复杂分流算法，Streaming RPC等功能会加重这个问题。"
> - "Streaming RPC也使用了Socket以复用wait-free的写出过程。"