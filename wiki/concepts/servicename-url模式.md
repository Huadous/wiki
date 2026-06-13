---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "method"
aliases:
  - "ServicePrefix模式"
  - "资源服务URL模式"
  - "/ServiceName URL pattern"
  - "ServicePrefix模式"
  - "资源服务URL模式"
  - "Service-Prefix URL Pattern"
  - "ServicePrefix模式"
  - "资源服务URL模式"
  - "/ServiceName URL pattern"
  - "ServicePrefix模式"
  - "资源服务URL模式"
---

## Description
/ServiceName URL模式 将整个服务名作为URL前缀，路径的剩余部分直接映射为资源路径。例如，`/FileService/foobar.txt`表示资源`./foobar.txt`，`/FileService/app/data/boot.cfg`表示`./app/data/boot.cfg`。这种设计非常适合需要按目录结构组织资源的服务，如静态文件服务或配置管理系统。使用时需在proto文件中将服务方法定义为`default_method`，服务后所有以`/ServiceName`开头的URL都会触发该默认方法。未解析路径通过`cntl->http_request().unresolved_path()`获取，且总是被规范化为无前后斜杠、无重复斜杠的形式。brpc框架会自动处理路径中的多余斜杠，保持路径整洁，同时确保访问时路径一致。

## Related Concepts
- [[concepts/service-name-method-name-url-pattern|/ServiceName/MethodName URL模式]]
- [[concepts/RESTful-url-mapping|RESTful URL映射]]
- [[concepts/http-h2-service|HTTP/h2服务]]

## Related Entities
- [[entities/baidu|brpc]]

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "http/h2 services for managing resources may need this kind of URL, such as `/FileService/foobar.txt` represents `./foobar.txt` and `/FileService/app/data/boot.cfg` represents `./app/data/boot.cfg`."
> - "Use `FileService` as the service name and `default_method` as the method name in the proto file."
> - "| /FileService | FileService.default_method | "/FileService" | "" |"
> - "http/h2 services for managing resources may need this kind of URL, such as /FileService/foobar.txt represents ./foobar.txt and /FileService/app/data/boot.cfg represents ./app/data/boot.cfg."
> - "Use FileService as the service name and default_method as the method name in the proto file."