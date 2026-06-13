---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [product]
aliases:
  - "upb"
  - "micro protobuf"
  - "upb C runtime"
---


# upb

## 基本信息
- Type: product
- Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]

## 描述
upb 是一个用 C 语言编写的轻量级 Protocol Buffers 实现，常被多个语言运行时（包括 [[sources/json2pb|json2pb]] 生态中的 Ruby、Rust 等）作为底层基础设施使用。在代码生成方面，upb 使用字段名（field name）来生成 API，例如对 proto2 group `MyGroup` 会生成 `Foo_mygroup()` 这样的方法。upb 的行为与 C++、Python、Go 等语言一致，都使用小写的字段名而非消息名。由于 edition 2023 移除了同步合成消息的生成，upb 作为底层运行时受到了 group 字段问题的影响，需要进行协调修改，以适配 [[concepts/edition-2023|Edition 2023]] 的语义。

## 相关实体
无相关实体

## 相关概念
- [[concepts/codegen|Codegen]]
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/edition-2023|Edition 2023]]

## 来源提及
- ** This includes all upb-based runtimes as well (e.g. Ruby, Rust, etc.) — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- While using the field name for generated APIs required less special-casing in the generators, the field name ends up producing slightly-less-readable APIs for multi-word camelcased groups. — [[sources/editions-group-migration-issues|editions-group-migration-issues]]