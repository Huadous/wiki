---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "method"
aliases:
  - "SSE"
  - "服务器推送事件"
  - "Server-Sent Events"
  - "Server-Sent Events (SSE)"
  - "SSE"
  - "服务器推送事件"
  - "Server-Sent Events"
  - "Server-Sent Events (SSE) (in brpc)"
  - "SSE"
  - "服务器推送事件"
  - "Server-Sent Events"
  - "Server-Sent Events (SSE)"
  - "SSE"
  - "服务器推送事件"
  - "Server-Sent Events"
---

## Related Concepts
- [[concepts/progressive-attachment|ProgressiveAttachment]]
- [[concepts/http-chunked-transfer-encoding|HTTP chunked transfer encoding]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/http_parser|http_parser]]
- [[entities/curl|curl]]
- [[entities/progressiveattachment|ProgressiveAttachment]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "In addition, we can easily implement Server-Sent Events(SSE) with this feature, which enables a client to receive automatic updates from a server via a HTTP connection."
> - "SSE could be used to build real-time applications such as chatGPT."
> - "Please refer to HttpSSEServiceImpl in http_server.cpp for more details."

> **Source: [[sources/http_service|http_service]]**
> - "利用该特性可以轻松实现Server-Sent Events(SSE)服务，从而使客户端能够通过 HTTP 连接从服务器自动接收更新。"
> - "非常适合构建诸如chatGPT这类实时应用程序，应用例子详见[http_server.cpp](https://github.com/apache/brpc/blob/master/example/http_c++/http_server.cpp)中的HttpSSEServiceImpl。"