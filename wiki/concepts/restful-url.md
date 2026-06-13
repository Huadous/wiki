---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "method"
aliases:
  - "RESTful 映射"
  - "RESTful mapping"
  - "RESTful URL 模式"
  - "RESTful URL映射"
  - "RESTful 映射"
  - "RESTful mapping"
  - "RESTful URL 模式"
  - "Restful URL映射"
  - "RESTful 映射"
  - "RESTful mapping"
  - "RESTful URL 模式"
  - "RESTful URL映射"
  - "RESTful 映射"
  - "RESTful mapping"
  - "RESTful URL 模式"
---

## Related Concepts
- [[concepts/url-mapping-rules|URL映射规则]]
- [[concepts/restful-api|RESTful API]]
- [[concepts/http-h2-service|HTTP/H2服务]]
- [[concepts/default-method|default_method]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/QueueService|QueueService]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "brpc supports specifying a URL for each method in a service."
> - "Mapping rules: 'PATH1 => NAME1, PATH2 => NAME2 ...'"
> - "The path after asterisk can be obtained by cntl.http_request().unresolved_path(), which is always normalized."

> **Source: [[sources/http_service|http_service]]**
> - "brpc支持为service中的每个方法指定一个URL。"
> - "如果restful_mappings不为空, service中的方法可通过指定的URL被http/h2协议访问，而不是/ServiceName/MethodName."
> - "一个路径中只能出现一个星号。"
> - "No directly relevant information"