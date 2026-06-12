---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "term"
aliases:
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "Chunked transfer encoding"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP chunked transfer encoding"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "Chunked transfer encoding"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "Chunked transfer encoding (in brpc)"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "Chunked transfer encoding"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP chunked transfer encoding"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "Chunked transfer encoding"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "分块传输"
  - "chunked transfer encoding"
  - "分块传输编码"
  - "HTTP分块传输编码"
  - "chunked transfer encoding"
  - "分块传输编码"
---

## Description
HTTP分块传输编码（Chunked Transfer Encoding）是HTTP/1.1协议中定义的数据传输机制，它解决了服务器在无法预知响应内容大小时的数据传输问题。在brpc框架中，brpc明确支持HTTP chunked模式，通过ProgressiveAttachment（基于chunked编码实现渐进式发送）使得服务器可以在生成数据的同时逐步推送响应内容。客户端借助服务器推送事件（SSE）技术，可以实时接收数据流，而无需等待整个响应体完全生成。这种传输方式适用于流式传输大文件或实时数据，与传统Content-Length机制形成互补——前者适用于动态内容生成场景，后者则更适合已知固定长度的静态资源传输。

## Related Concepts
- [[concepts/progressive-sending|Progressive sending]]
- [[concepts/server-sent-events-sse|Server-Sent Events (SSE)]]
- [[concepts/transfer-encoding|Transfer-Encoding]]
- [[concepts/http-long-connection|HTTP 长连接]]
- [[concepts/http-content-length|Content-Length 机制]]
- [[concepts/progressive-receiving|渐进接收]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/http_parser|http_parser]]
- [[entities/progressiveattachment|ProgressiveAttachment]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "Q: Does brpc support http chunked mode? Yes."
> - "Q: Does brpc support http chunked mode?"
> - "A: Yes."