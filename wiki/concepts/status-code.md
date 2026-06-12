---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
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

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/http_parser|http_parser]]

## Mentions in Source
- Status code is a special field in HTTP response to store processing result of the http request. Possible values are defined in http_status_code.h. — [[sources/en_http_service|en_http_service]]
- if (cntl->http_response().status_code() == brpc::HTTP_STATUS_NOT_FOUND) { ... } — [[sources/en_http_service|en_http_service]]
- cntl->http_response().set_status_code(brpc::HTTP_STATUS_INTERNAL_SERVER_ERROR); — [[sources/en_http_service|en_http_service]]