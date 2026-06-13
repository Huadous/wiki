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

**Source: [[sources/en_http_service|en_http_service]]**
> Content-type is a frequently used header for storing type of the HTTP body, and specially processed in brpc and accessible by cntl->http_request().content_type().

> if (cntl->http_request().content_type() == "application/json") { ... }

> cntl->http_response().set_content_type("text/html");

**Source: [[sources/http_service|http_service]]**
> Content-type记录body的类型，是一个使用频率较高的header。它在brpc中被特殊处理，需要通过cntl->http_request().content_type()来访问，cntl->GetHeader("Content-Type")是获取不到的。

> 如果RPC失败(Controller被SetFailed), Content-Type会框架强制设为text/plain，而response body设为Controller::ErrorText()。