---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/server|server]]"
  - "[[brpc/http_service.md]]"
tags:
  - "method"
aliases:
  - "protobuf service definition"
  - "brpc protobuf 服务定义"
---

## Related Concepts
- [[concepts/json-pb-conversion|JSON <=> PB转换]]
- [[concepts/protobuf-arena|protobuf arena]]
- [[concepts/http-h2-service|HTTP/H2服务]]
- [[concepts/restful-url-mapping|Restful URL映射]]
- [[concepts/default-method|default_method]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/server|server]]**
> - "告诉protoc要生成C++ Service基类，如果是java或python，则应分别修改为java_generic_services和py_generic_services"
> - "option cc_generic_services = true;"

> **Source: [[sources/http_service|http_service]]**
> - "虽然用不到pb消息，但brpc中的http/h2服务接口也得定义在proto文件中，只是request和response都是空的结构体。"
> - "这确保了所有的服务声明集中在proto文件中，而不是散列在proto文件、程序、配置等多个地方。"
> - "option cc_generic_services = true;"