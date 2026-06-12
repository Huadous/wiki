---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "method"
aliases:
  - "/ServiceName/MethodName URL模式"
  - "服务名/方法名URL映射"
  - "Service-Method URL模式"
  - "/ServiceName/MethodName URL pattern"
  - "/ServiceName/MethodName URL模式"
  - "服务名/方法名URL映射"
  - "Service-Method URL模式"
  - "Service-Method URL Pattern"
  - "/ServiceName/MethodName URL模式"
  - "服务名/方法名URL映射"
  - "Service-Method URL模式"
  - "/ServiceName/MethodName URL pattern"
  - "/ServiceName/MethodName URL模式"
  - "服务名/方法名URL映射"
  - "Service-Method URL模式"
---

## Description
`/ServiceName/MethodName` URL模式是brpc框架将Protobuf定义的RPC服务自动暴露为HTTP/h2端点的默认机制。当在`.proto`文件中以服务名`ServiceName`（不含包名）声明一个RPC方法，且其请求和响应消息为空（如`google.protobuf.Empty`）时，brpc会自动将该方法映射到形如`/ServiceName/MethodName`的HTTP路径。请求和响应可以为空的原因是所有数据都通过Controller传递：HTTP/h2请求的头部通过`Controller.http_request()`获取，请求体通过`Controller.request_attachment()`获取；响应头部通过`Controller.http_response()`设置，响应体通过`Controller.response_attachment()`设置。此模式简化了从RPC到HTTP的转换过程，开发者无需编写额外的路由代码即可通过标准HTTP客户端（如cURL）访问服务端点。该模式既支持HTTP/1.1也支持HTTP/2协议，URL路径中`/ServiceName/MethodName`之后的额外路径段可通过`cntl->http_request().unresolved_path()`获取，用于处理动态参数或子资源定位。例如，当访问`/HttpService/Echo`时，`unresolved_path()`返回空字符串，而访问`/HttpService/Echo/extra`时则返回`"extra"`。

## Related Concepts
- [[concepts/服务名URL模式|/ServiceName URL模式]]
- [[concepts/restful-url映射|RESTful URL映射]]
- [[concepts/HTTP服务|HTTP/h2服务]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/curl|curl]]

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
> - "Define a service named `ServiceName`(not including the package name), with a method named `MethodName` and empty request/response, the service will provide http/h2 service on `/ServiceName/MethodName` by default."
> - "| /HttpService/Echo | HttpService.Echo | \"/HttpService/Echo\" | \"\" |"
> - "The reason that request and response can be empty is that all data are in Controller: Header of the http/h2 request is in Controller.http_request() and the body is in Controller.request_attachment(). Header of the http/h2 response is in Controller.http_response() and the body is in Controller.response_attachment()."