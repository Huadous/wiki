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

## Description
protobuf 服务定义是 brpc 框架中构建 RPC 与 HTTP/H2 服务的统一接口描述手段。其核心思想是以 `.proto` 文件作为接口契约的单一来源：用户在该文件中启用通用服务选项（如 C++ 场景下的 `option cc_generic_services = true;`），使用 `message` 声明请求/响应的强类型数据结构，并使用 `service` 与 `rpc` 关键字声明方法集合。`protoc` 编译器据此自动生成 C++/Java/Python 等多语言的 Service 基类与桩代码，开发者只需继承基类并覆写方法即可完成服务端实现，典型示例为 `EchoService`。

该机制不仅限于基于 protobuf 消息的 RPC，也同样适用于 HTTP/H2 服务。brpc 中的 HTTP/H2 服务接口虽然不使用 pb 消息，但仍必须在 proto 文件中定义，且 request 和 response 都使用空结构体（如 `message HttpRequest {};` 与 `message HttpResponse {};`）。这一设计确保了所有服务声明集中在 proto 文件中，而不是散列在 proto 文件、程序、配置等多个地方，从而为服务的发现、注册和文档化提供一致入口。

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