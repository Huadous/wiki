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
  - "HTTP headers"
  - "HTTP请求头"
  - "HTTP响应头"
  - "HTTP headers (in brpc)"
  - "HTTP headers"
  - "HTTP请求头"
  - "HTTP响应头"
---

## Related Concepts

- [[concepts/Content-Type|Content-Type]]
- [[concepts/状态码|状态码]]
- [[concepts/查询字符串|查询字符串]]
- [[concepts/HTTP-H2服务|HTTP/H2服务]]

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/curl|curl]]

## Mentions in Source

> **Source: [[sources/http_service|http_service]]**
> - "http header是一系列key/value对，有些由HTTP协议规定有特殊含义，其余则由用户自由设定。"
> - "const std::string* user_agent_str = cntl->http_request().GetHeader(\"User-Agent\");"
> - "在header中增加\"Accept-encoding: gzip\"，大小写不敏感。"