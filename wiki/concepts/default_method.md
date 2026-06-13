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
  - "默认方法"
  - "Default Method"
---

## Related Concepts
- [[concepts/URL映射規則|URL映射規則]]
- [[concepts/RESTful URL映射|Restful URL映射]]
- [[concepts/RESTful API|RESTful API]]
- [[concepts/HTTP服務|HTTP/H2服務]]
- [[concepts/HTTP/h2服務|HTTP/h2服務]]
- [[concepts/未解析路徑|未解析路徑（unresolved_path）]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protobuf-protobuf|Protocol Buffers]]

## Mentions in Source
> **來源: [[sources/en_http_service|en_http_service]]**
> - "Use `FileService` as the service name and `default_method` as the method name in the proto file."
> - "service FileService { rpc default_method(HttpRequest) returns (HttpResponse); }"
> - "virtual void default_method(google::protobuf::RpcController* cntl_base, const HttpRequest* /*request*/, HttpResponse* /*response*/, google::protobuf::Closure* done) { ... }"
> - "After adding the implemented instance into the server, the service is accessible via following URLs (the path after /FileService is filled in cntl->http_request().unresolved_path(), which is always normalized)"

> **來源: [[sources/http_service|http_service]]**
> - "资源类的http/h2服务可能需要这样的URL，ServiceName后均为动态内容。"
> - "proto文件中应以FileService为服务名，以default_method为方法名。"
> - "/FileService之后的路径在cntl->http_request().unresolved_path()中i。"