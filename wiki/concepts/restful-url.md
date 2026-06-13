---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
  - "[[brpc/baidu_std.md]]"
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
  - "RESTful"
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

## Description
RESTful API 是一种利用 HTTP 协议特性来组织 Web Service 接口的设计风格，通过 URL 路径标识资源，并借助 HTTP 方法表达操作语义。在 brpc 框架中，RESTful 被推荐作为 HTTP/H2 服务的标准接口形式，开发者可以通过 `restful_mappings` 为 service 中的每个方法指定一个 URL，使得方法可通过自定义 URL 而非默认的 `/ServiceName/MethodName` 形式被访问。brpc 的 URL 映射规则采用 `PATH => NAME` 的语法，支持路径中包含通配符星号（一个路径中只能出现一个星号），星号之后的部分可通过 `cntl.http_request().unresolved_path()` 获取，且该路径始终是规范化后的。值得注意的是，baidu_std 协议规范建议使用 RESTful 形式，但明确指出由于 RESTful 本身并非一个严格的规范，因此并不强制要求实现遵循，所有符合标准 HTTP 协议的设计都是被允许的。RESTful 风格与 brpc 的 [[concepts/default-method|default_method]] 共同构成了 HTTP 服务接口的两种主要访问方式。

## Related Concepts
- [[concepts/url-mapping-rules|URL映射规则]]
- [[concepts/restful-api|RESTful API]]
- [[concepts/http-h2-service|HTTP/H2服务]]
- [[concepts/default-method|default_method]]
- [[concepts/http-interface|HTTP接口]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/QueueService|QueueService]]
- [[entities/baidu_std|baidu_std]]

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

> **Source: [[sources/baidu_std|baidu_std]]**
> - "建议使用RESTful形式的Web Service接口。由于RESTful并非一个严格的规范，本规范对此不做强制规定。"