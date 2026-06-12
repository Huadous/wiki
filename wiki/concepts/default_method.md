---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "method"
aliases:
  - "默认方法"
  - "Default Method"
---

## 使用方式

在 proto 文件中將服務名稱設為 `FileService`，並將方法宣告為 `default_method`，然後在實現類中重寫該方法即可。註冊服務後，客戶端可通過形如 `/FileService/your_path` 的 URL 進行訪問，其中 `your_path` 部分可透過 `cntl->http_request().unresolved_path()` 獲取。

## 相關概念

- [[concepts/URL映射規則|URL映射規則]]
- [[concepts/RESTful API|RESTful API]]
- [[concepts/HTTP服務|HTTP/h2服務]]
- [[concepts/未解析路徑|未解析路徑（unresolved_path）]]

## 相關實體

- [[entities/brpc|brpc]]
- [[entities/protobuf-protobuf|Protocol Buffers]]

## 來源提及

> **來源: [[sources/en_http_service|en_http_service]]**
> - "Use `FileService` as the service name and `default_method` as the method name in the proto file."
> - "service FileService { rpc default_method(HttpRequest) returns (HttpResponse); }"
> - "virtual void default_method(google::protobuf::RpcController* cntl_base, const HttpRequest* /*request*/, HttpResponse* /*response*/, google::protobuf::Closure* done) { ... }"
> - "After adding the implemented instance into the server, the service is accessible via following URLs (the path after /FileService is filled in cntl->http_request().unresolved_path(), which is always normalized)"