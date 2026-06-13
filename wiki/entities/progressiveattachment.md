---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "other"
aliases:
  - "渐进附件"
  - "ProgressiveAttachment"
---

## Related Concepts
- 渐进发送
- [[concepts/server-sent-events|Server-Sent Events]]
- 分块传输
- chunked模式
- [[concepts/intrusive-ptr|intrusive_ptr]]
- [[concepts/chunked-transfer-encoding|Chunked Transfer Encoding]]

## Usage
通过调用 `Controller::CreateProgressiveAttachment()` 可以创建一个支持渐进写入的响应体。返回的 `ProgressiveAttachment` 对象需使用 `intrusive_ptr` 进行管理。如果在服务端 done 回调执行之前进行写入操作，发送的数据会被缓存直到 done 被调用。该特性可以方便地实现 Server-Sent Events (SSE)。

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
- "Call `Controller::CreateProgressiveAttachment()` to create a body that can be written progressively. The returned `ProgressiveAttachment` object should be managed by `intrusive_ptr`"
- "If the write occurs before running of the server-side done, the sent data is cached until the done is called."
- "Call `Controller::CreateProgressiveAttachment()` to create a body that can be written progressively."
- "We can easily implement Server-Sent Events(SSE) with this feature"