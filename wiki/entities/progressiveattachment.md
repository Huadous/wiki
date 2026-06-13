---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "other"
aliases:
  - "渐进附件"
  - "ProgressiveAttachment"
---

## Related Entities
- [[entities/brpc|brpc]]

## Related Concepts
- 渐进发送
- [[concepts/server-sent-events|Server-Sent Events]]
- 分块传输
- chunked模式
- [[concepts/intrusive-ptr|intrusive_ptr]]
- [[concepts/chunked-transfer-encoding|Chunked Transfer Encoding]]
- HTTP/H2服务
- 实时流式响应

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
- "Call `Controller::CreateProgressiveAttachment()` to create a body that can be written progressively. The returned `ProgressiveAttachment` object should be managed by `intrusive_ptr`"
- "If the write occurs before running of the server-side done, the sent data is cached until the done is called."
- "Call `Controller::CreateProgressiveAttachment()` to create a body that can be written progressively."
- "We can easily implement Server-Sent Events(SSE) with this feature"

> **Source: [[sources/http_service|http_service]]**
- "brpc server支持发送超大或无限长的body。"
- "调用Controller::CreateProgressiveAttachment()创建可持续发送的body。"
- "利用该特性可以轻松实现Server-Sent Events(SSE)服务，从而使客户端能够通过 HTTP 连接从服务器自动接收更新。"