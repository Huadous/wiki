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
Streaming RPC是brpc默认启用的流式RPC协议，显示为字符串"streaming_rpc"。它与baidu_std、http、h2c等协议并列作为brpc支持的核心协议之一，通过统一的listen端口监听，由server自动进行协议协商，因此用户无需为不同协议配置不同端口。该协议的核心思想是在client与service之间建立用户态连接——称为Stream，同一个TCP连接之上能同时存在多个Stream，从而实现高效的复用。

Streaming RPC提供以下关键保证：消息边界清晰、接收消息顺序与发送消息顺序严格一致、全双工通信、内置流控机制、提供超时提醒、支持自动切割过大的消息以避免[[concepts/Head-of-line blocking|Head-of-line blocking]]问题。在IO层面，它与[[entities/Socket|Socket]]配合，复用wait-free write的相关代码以提升并发性能。然而，多租户、复杂的负载均衡与Streaming RPC本身也会加剧[[concepts/Head-of-line blocking|Head-of-line blocking]]问题——在高负载下，某个fd的常规长延迟可能拖慢IO线程中所有fd的处理速度，导致更多的长尾延迟。

## Related Concepts
- [[concepts/流控|流控]]
- [[concepts/Head-of-line blocking|Head-of-line blocking]]
- [[concepts/baidu_std协议|baidu_std协议]]
- [[concepts/StreamOptions|StreamOptions]]
- [[concepts/StreamInputHandler|StreamInputHandler]]
- [[concepts/Stream|Stream]]
- [[concepts/wait-free|wait-free write]]
- [[concepts/协议支持|协议支持]]

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