---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/json2pb.md]]"
  - "[[brpc/http_service.md]]"
tags:
  - "product"
aliases:
  - "RapidJSON"
  - "rapidjson库"
---

## Related Entities
- [[entities/brpc|brpc]] — 在其 HTTP 服务与 json2pb 模块中使用 rapidjson 作为 JSON 解析组件
- [[entities/json2pb|json2pb]] — 使用 rapidjson 作为底层 JSON 解析器，实现 JSON 与 protobuf 的双向转换
- [[entities/http_parser|http_parser]] — 另一个被 brpc 使用的解析库，负责 HTTP 协议解析
- [[entities/carbon|carbon]] — 同样关注性能的编程语言项目
- [[entities/tcmalloc|tcmalloc]] — 高性能内存分配器，与 rapidjson 的性能优化目标一致
- [[entities/jemalloc|jemalloc]] — 高性能内存分配器，与 rapidjson 的性能优化目标一致

## Related Concepts
- [[concepts/JSON|JSON]] — rapidjson 是专门处理 JSON 数据的解析与生成库
- [[concepts/Content-Type|Content-Type]] — HTTP 头字段，用于标识请求/响应体中 JSON 格式数据的媒体类型
- [[concepts/HTTP headers|HTTP headers]] — HTTP 协议头字段集合，决定如何解析请求/响应体中的 JSON 数据
- [[concepts/JSON Parsing|JSON解析]] — rapidjson 的核心功能领域
- [[concepts/Performance Optimization|性能优化]] — rapidjson 的设计核心理念
- [[concepts/JSON-protobuf转换规则|JSON-protobuf转换规则]] — 涉及 rapidjson 的 Object/Array 结构与 protobuf 字段的对应映射
- [[concepts/repeated字段JSON编码|repeated字段JSON编码]] — rapidjson 的 Array 结构与 protobuf 的 repeated 字段相对应

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
> - "Use rapidjson to parse json, which is a json library focuses on performance."
> - "brpc的HTTP实现使用了rapidjson，以提高JSON解析效率"
> - "rapidjson是一个专注于性能的JSON库"

> **Source: [[sources/json2pb|json2pb]]**
> - "json解析使用[rapidjson](https://github.com/miloyip/rapidjson)。"
> - "rapidjson会根据值打上对应的类型标记，比如：对于3，rapidjson中的IsUInt, IsInt, IsUint64, IsInt64等函数均会返回true。"
> - "对应rapidjson Object, 以花括号包围，其中的元素会被递归地解析。"

> **Source: [[sources/http_service|http_service]]**
> - "使用[rapidjson](https://github.com/miloyip/rapidjson)解析json，这是一个主打性能的json库。"