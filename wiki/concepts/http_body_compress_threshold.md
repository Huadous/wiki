---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
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
- [[concepts/gzip-compression|Gzip压缩]]
- [[concepts/http-verbose-flag|http_verbose flag]]
- Gzip compression (in brpc)

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **来源: [[sources/en_http_service|en_http_service]]**
> - "Body size is less than the bytes specified by -http_body_compress_threshold (512 by default)."
> - "gzip is not a very fast compression algorithm. When the body is small, the delay added by compression may be larger than the time saved by network transmission."
> - "http_body_compress_threshold | 512 | Not compress http body when it's less than so many bytes."