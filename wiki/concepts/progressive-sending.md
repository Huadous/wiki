---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "method"
aliases:
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "Progressive receiving"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "Progressive attachment"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "Progressive receiving"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "ProgressiveAttachment (brpc)"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "Progressive receiving"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "Progressive attachment"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "Progressive receiving"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
  - "渐进发送"
  - "progressive attachment"
  - "渐进式发送"
  - "分块发送"
---

## Related Concepts
- [[concepts/server-sent-events|Server-Sent Events (SSE)]]
- [[concepts/http-chunked-mode|HTTP chunked mode]]
- [[concepts/http-long-polling|HTTP 长轮询]]
- [[concepts/streaming-rpc|流式 RPC]]
- [[concepts/gzip响应体压缩|gzip响应体压缩]]
- [[concepts/h2协议|h2协议]]
- [[concepts/progressive-sending|Progressive Sending]]
- [[concepts/progressive-receiving|Progressive Receiving]]
- [[concepts/progressive-attachment|Progressive Attachment]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/controller|Controller]]
- [[entities/progressiveattachment|ProgressiveAttachment]]
- [[entities/socket|Socket]]

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
- "brpc server is capable of sending large or infinite sized body, in following steps:" — [[sources/en_http_service|en_http_service]]
- "Call `Controller::CreateProgressiveAttachment()` to create a body that can be written progressively." — [[sources/en_http_service|en_http_service]]
- "The returned `ProgressiveAttachment` object should be managed by `intrusive_ptr`" — [[sources/en_http_service|en_http_service]]
- "We can easily implement Server-Sent Events(SSE) with this feature, which enables a client to receive automatic updates from a server via a HTTP connection." — [[sources/en_http_service|en_http_service]]
- "Currently brpc server doesn't support calling the service callback once header part in the http request is parsed." — [[sources/en_http_service|en_http_service]]
- "In other words, brpc server is not suitable for receiving large or infinite sized body." — [[sources/en_http_service|en_http_service]]
- "brpc server is capable of sending large or infinite sized body, in following steps:" — [[sources/en_http_service|en_http_service]]
- "Call Controller::CreateProgressiveAttachment() to create a body that can be written progressively." — [[sources/en_http_service|en_http_service]]
- "ProgressiveAttachment::Write() to send the data." — [[sources/en_http_service|en_http_service"]