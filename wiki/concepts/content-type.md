---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "term"
aliases:
  - "内容类型"
  - "MIME类型"
  - "Content-Type (in brpc)"
  - "内容类型"
  - "MIME类型"
---

## Related Concepts
- [[concepts/http-headers|HTTP headers]]
- [[concepts/status-code|Status Code]]
- [[concepts/http|HTTP]]
- [[concepts/http-2|HTTP/2]]
- [[concepts/accept-header|Accept Header]]
- [[concepts/gzip-compression|gzip compression]]
- [[concepts/mime-type|MIME type]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]
- [[entities/http_parser|http_parser]]

## Mentions in Source
> Content-type is a frequently used header for storing type of the HTTP body, and specially processed in brpc and accessible by cntl->http_request().content_type(). — [[sources/en_http_service|en_http_service]]

> if (cntl->http_request().content_type() == "application/json") { ... } — [[sources/en_http_service|en_http_service]]

> cntl->http_response().set_content_type("text/html"); — [[sources/en_http_service|en_http_service]]