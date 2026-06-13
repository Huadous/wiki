---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "other"
aliases:
  - "调试标志"
  - "HTTP verbose"
  - "-http_verbose"
---

## Related Concepts
- [[concepts/http-h2服务|HTTP/H2 服务]]
- [[concepts/gzip压缩|gzip 压缩]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/http_service|http_service]]**
> - "打开[-http_verbose](http://brpc.baidu.com:8765/flags/http_verbose)即可看到所有的http/h2 request和response"
> - "注意这应该只用于线下调试，而不是线上程序"