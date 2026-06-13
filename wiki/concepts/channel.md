---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/http_client]]"
  - "[[brpc/en_backup_request.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "brpc::Channel"
  - "Channel 类"
---

## Related Concepts
- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/url-host-field|URL 与 Host 字段]]
- [[concepts/backup-request|Backup Request]]
- [[concepts/channel-options|ChannelOptions]]
- [[concepts/selective-channel|SelectiveChannel]]
- [[concepts/backup-request-ms|backup_request_ms]]
- [[concepts/naming-service|Naming Service]]
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/controller|Controller]]
- [[concepts/connection-type|Connection Type]]
- [[concepts/health-checking|Health Checking]]
- [[concepts/protocol|协议]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/exampleselective_echo_c++|exampleselective_echo_c++]]

## Mentions in Source

> **Source: [[sources/http_client]]**
> - "brpc::Channel可访问http/h2服务，ChannelOptions.protocol须指定为PROTOCOL_HTTP或PROTOCOL_H2。"
> - "设定好协议后，`Channel::Init`的第一个参数可为任意合法的URL。注意：允许任意URL是为了省去用户取出host和port的麻烦，`Channel::Init`只用其中的host及port，其他部分都会丢弃。"

> **Source: [[sources/en_backup_request]]**
> - "Channel opens backup request. Channel sends the request to one of the servers and when the response is not returned after ChannelOptions.backup_request_ms ms, it sends to another server, taking the response that coming back first."
> - "Define a SelectiveChannel that sets backup request, in which contains two sub channel."

> **Source: [[sources/en_client]]**
> - "Channel.Init() is not thread-safe."
> - "Channel.CallMethod() is thread-safe and a Channel can be used by multiple threads simultaneously."
> - "Client-side of RPC sends requests. It's called Channel rather than \"Client\" in brpc. A channel represents a communication line to one server or multiple servers, which can be used for calling services."

> **Source: [[sources/client]]**
> - "Channel.Init()是线程不安全的。"
> - "Channel.CallMethod()是线程安全的，一个Channel可以被所有线程同时使用。"
> - "Channel可以分配在栈上。"
> - "Channel在发送异步请求后可以析构。"
> - "没有brpc::Client这个类。"
> - "Channel可以**被所有线程共用**，你不需要为每个线程创建独立的Channel，也不需要用锁互斥。"