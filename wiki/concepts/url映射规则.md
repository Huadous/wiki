---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "method"
aliases:
  - "path mapping"
  - "URL 路径映射"
  - "HTTP URL 映射规则"
  - "RESTful URL mapping"
  - "path mapping"
  - "URL 路径映射"
  - "HTTP URL 映射规则"
---

## Description
URL映射规则是 brpc 框架的核心路由机制，负责将 HTTP 请求正确分发到对应的服务处理方法。默认情况下，每个服务方法会暴露在 `/ServiceName/MethodName` 路径下，但开发者可以通过 `restful_mappings` 参数为特定方法定义更为灵活和语义化的 URL 路径，例如 `/user/{id}/info` 这样的 RESTful 风格路径。映射规则支持通配符 `*` 匹配路径中的任意段，匹配后的剩余路径可通过 `cntl.http_request().unresolved_path()` 获取，且该方法返回的路径始终是经过归一化处理的。系统会自动对路径中多余的斜杠进行压缩（如 `//a//b` → `/a/b`），确保路由一致性。一个重要的行为是，一旦方法被 `restful_mappings` 映射到自定义路径，它将不再通过默认的 `/ServiceName/MethodName` 路径访问，这有助于实现严格的 URL 设计规范。多条不同的 URL 路径可以映射到同一个服务方法，这在需要支持多种 URL 格式的遗留系统迁移场景中非常有用。

## Related Concepts
- [[concepts/http-h2-service|HTTP/h2 服务]]
- [[concepts/restful-url|RESTful URL]]

## Related Entities
- [[entities/bns|bns]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
- "the service will provide http/h2 service on `/ServiceName/MethodName` by default."
- "The path after asterisk can be obtained by `cntl.http_request().unresolved_path()`, which is always normalized"
- "brpc supports specifying a URL for each method in a service."
- "If `restful_mappings` is non-empty, the method in service can be accessed by the specified URL rather than /ServiceName/MethodName."
- "Multiple paths can be mapped to a same method."
- "Mapped methods are **not** accessible via `/ServiceName/MethodName` anymore."