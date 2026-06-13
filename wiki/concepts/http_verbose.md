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

## Description
http_verbose 是 brpc 中的一个调试标志（gflag），用于打印所有 HTTP/H2 请求和响应的内容。开启后，服务端会输出详细的 HTTP/H2 报文信息，是排查 HTTP/H2 协议层面问题（如 header 解析、body 处理、响应构造等）时的重要工具。该标志可通过 brpc 的内置 flags 页面 `http://brpc.baidu.com:8765/flags/http_verbose` 进行在线查看和配置，也可以通过命令行参数（如 `-http_verbose`）启用。文档明确强调该功能应仅用于线下调试环境，不应在生产环境中开启，以免产生大量日志影响服务性能。

## Related Concepts
- [[concepts/http-h2服务|HTTP/H2 服务]]
- [[concepts/gzip压缩|gzip 压缩]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/http_service|http_service]]**
> - "打开[-http_verbose](http://brpc.baidu.com:8765/flags/http_verbose)即可看到所有的http/h2 request和response"
> - "注意这应该只用于线下调试，而不是线上程序"