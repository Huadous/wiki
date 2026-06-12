---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_io]]"
  - "[[sources/en_http_service]]"
tags:
  - "term"
aliases:
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
  - "brpc::Controller"
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
  - "remote_side"
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
  - "brpc::Controller"
  - "Controller"
  - "RPC Controller"
  - "brpc控制器"
---

## Related Concepts
- [[concepts/http-parameters|HTTP参数]]
- [[concepts/progressive-attachment|ProgressiveAttachment]]
- [[concepts/http-h2-service|HTTP/h2服务]]
- [[concepts/bthread|bthread]]
- [[concepts/socket-management|Socket管理]]
- [[concepts/race-condition|竞态条件]]
- [[concepts/aba-problem|ABA问题]]
- [[concepts/uri|URI]]
- [[concepts/query-string|Query String]]
- [[concepts/status-code|Status Code]]
- [[concepts/gzip-compression|gzip压缩]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc-server|brpc::Server]]
- [[entities/iobuf|iobuf]]
- [[entities/datafactory|datafactory]]
- [[entities/certinfo|certinfo]]
- [[entities/nginx|nginx]]
- [[entities/closurguard|ClosureGuard]]
- [[entities/authcontext|AuthContext]]
- [[entities/socket|Socket]]
- [[entities/socketuniqueptr|SocketUniquePtr]]
- [[entities/bthread|bthread]]
- [[entities/progressiveattachment|progressiveattachment]]
- [[entities/google-protobuf|Google Protobuf]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "Header of the http/h2 request is in Controller.http_request() and the body is in Controller.request_attachment()."
> - "Header of the http/h2 response is in Controller.http_response() and the body is in Controller.response_attachment()."
> - "brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);"

> **Source: [[sources/en_http_service|en_http_service]]**
> 该源文件未提供与Controller直接相关的新信息。