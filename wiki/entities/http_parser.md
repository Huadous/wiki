---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "product"
aliases:
  - "http-parser"
  - "Node.js HTTP parser"
  - "node.js http_parser"
  - "http-parser"
  - "Node.js HTTP parser"
  - "node.js http parser"
  - "http-parser"
  - "Node.js HTTP parser"
  - "node.js http_parser"
  - "http-parser"
  - "Node.js HTTP parser"
---

## Related Entities

- [[entities/brpc|brpc]] — brpc 框架，http_parser 在其 HTTP 服务中被用作核心解析引擎
- [[entities/curl|curl]] — 另一个广泛使用的 HTTP 工具链，提供 libcurl 库
- [[entities/baidu|baidu]] — brpc 的维护组织
- [[entities/rapidjson|rapidjson]] — brpc 生态中用于 JSON 解析的相关库

## Related Concepts

- [[concepts/http-2|HTTP/2]] — 下一代 HTTP 协议，与 http_parser 解析的 HTTP/1.x 消息不同
- [[concepts/http-chunked-mode|HTTP chunked mode]] — 分块传输编码，http_parser 支持解析的传输方式
- [[concepts/gzip-response-body-compression|gzip 响应体压缩]] — brpc HTTP 实现中与 http_parser 配合使用的响应压缩技术
- [[concepts/h2|HTTP/H2服务]] — brpc 的 HTTP/H2 服务整体设计，http_parser 在其中负责 HTTP/1.x 消息的解析

## Mentions in Source

> **Source: [[sources/http_service|http_service]]**
> - 使用了node.js的[http parser](https://github.com/apache/brpc/blob/master/src/brpc/details/http_parser.h)解析http消息，这是一个轻量、优秀、被广泛使用的实现。
> - 在最差情况下解析http请求的时间复杂度也是O(N)，其中N是请求的字节数。