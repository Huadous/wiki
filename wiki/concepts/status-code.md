---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "standard"
aliases:
  - "HTTP状态码"
  - "状态码"
  - "Status Code (in brpc)"
  - "HTTP状态码"
  - "状态码"
---

## Related Concepts
- [[concepts/content-type|Content-Type]]
- [[concepts/http-2|HTTP/2]]
- [[concepts/restful-url|RESTful URL]]
- [[concepts/http-protocol|HTTP 协议]]
- [[concepts/http-headers|HTTP 头部]]
- [[concepts/reason-phrase|Reason-Phrase]]
- [[concepts/http-h2-service|HTTP/H2 服务]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/http_parser|http_parser]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "Status code is a special field in HTTP response to store processing result of the http request. Possible values are defined in http_status_code.h."
> - "if (cntl->http_response().status_code() == brpc::HTTP_STATUS_NOT_FOUND) { ... }"
> - "cntl->http_response().set_status_code(brpc::HTTP_STATUS_INTERNAL_SERVER_ERROR);"

> **Source: [[sources/http_service|http_service]]**
> - "status code是http response特有的字段，标记http请求的完成情况。可能的值定义在[http_status_code.h](https://github.com/apache/brpc/blob/master/src/brpc/http_status_code.h)中。"
> - "cntl->http_response().set_status_code(brpc::HTTP_STATUS_INTERNAL_SERVER_ERROR);"
> - "比如，以下代码以302错误实现重定向："