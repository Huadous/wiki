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

## Description
`http_body_compress_threshold` 是 brpc HTTP 服务中的一个配置参数，用于控制 HTTP 响应 body 的 gzip 压缩行为。当响应 body 的字节数小于该阈值时（默认 512 字节），brpc 选择不对 body 进行压缩处理。该参数定义在 `src/brpc/policy/http_rpc_protocol.cpp` 中。其设计依据是 gzip 并非一个非常快速的压缩算法——当 body 较小时，压缩操作本身增加的延时可能反而超过网络传输所节省的时间，因此对小尺寸 body 跳过压缩是一种合理权衡。该参数与 `Controller::set_response_compress_type(brpc::COMPRESS_TYPE_GZIP)` 配合使用，并需要客户端请求中携带 `Accept-encoding: gzip` 头才会真正触发压缩流程。

## Related Concepts
- [[concepts/gzip-compression|Gzip 压缩]]
- [[concepts/http-verbose-flag|http_verbose flag]]
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