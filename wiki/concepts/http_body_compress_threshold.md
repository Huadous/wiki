---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "term"
aliases:
  - "HTTP压缩阈值"
  - "gzip压缩阈值"
  - "http_body_compress_threshold"
  - "HTTP body compress threshold"
  - "HTTP压缩阈值"
  - "gzip压缩阈值"
  - "http_body_compress_threshold"
---

## Related Concepts
- [[concepts/gzip-compression|Gzip 压缩]]
- [[concepts/http-verbose-flag|http_verbose flag]]
- [[concepts/accept-encoding-header|Accept-encoding header]]
- [[concepts/http-headers|HTTP headers]]
- Gzip compression (in brpc)

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **来源: [[sources/en_http_service|en_http_service]]**
> - "Body size is less than the bytes specified by -http_body_compress_threshold (512 by default)."
> - "gzip is not a very fast compression algorithm. When the body is small, the delay added by compression may be larger than the time saved by network transmission."
> - "http_body_compress_threshold | 512 | Not compress http body when it's less than so many bytes."

> **来源: [[sources/http_service|http_service]]**
> - "body尺寸小于-http_body_compress_threshold指定的字节数，默认是512"
> - "gzip并不是一个很快的压缩算法，当body较小时，压缩增加的延时可能比网络传输省下的还多"
> - "Not compress http body when it's less than so many bytes."