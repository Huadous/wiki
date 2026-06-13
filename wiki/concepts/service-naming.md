---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/style]]"
  - "[[sources/proto3]]"
tags:
  - "standard"
aliases:
  - "服务命名规范"
  - "Service Naming"
  - "gRPC服务命名"
  - "service"
  - "服务命名规范"
  - "Service Naming"
  - "gRPC服务命名"
---

## 描述

服務命名規範是Protocol Buffers中service定義的核心組成部分。在.proto檔案中，service是一個用於定義RPC（遠端過程呼叫）介面的語言結構，其中包含一組RPC方法，每個方法指定輸入和輸出訊息類型。雖然proto3語法並未強制要求定義服務，但為了與gRPC等RPC框架整合，通常會在.proto檔案中定義service。Service定義可以獨立或與訊息、列舉等其他類型共存於同一個檔案中。統一的服務命名規範有助於多語言團隊（如Go、Java、Python）理解和維護服務介面，並使自動生成的API文件更加清晰。

## 相關概念

- [[concepts/titlecase|TitleCase]]
- [[concepts/message-naming|Message命名]]
- [[concepts/protocol-buffers-conventions|Protocol Buffers約定]]
- [[concepts/proto3|proto3]]
- [[concepts/code-generation|程式碼生成]]

## 相關實體

- [[entities/protocol-buffers|Protocol Buffers]]

## 來源提及

> **Source: [[sources/style|style]]**
> - "Use TitleCase for service names and method names."
> - "service FooService { rpc GetSomething (GetSomethingRequest) returns (GetSomethingResponse); }"

> **Source: [[sources/proto3|proto3]]**
> - "While multiple message types (such as message, enum, and service) can be defined in a single .proto file, it can also lead to dependency bloat..."