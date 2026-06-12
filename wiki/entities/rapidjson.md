---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "product"
aliases:
  - "RapidJSON"
  - "rapidjson库"
---

## Related Entities
- [[entities/brpc|brpc]] — brpc使用rapidjson实现高效的JSON解析
- [[entities/http_parser|http_parser]] — 另一个被brpc使用的解析库，负责HTTP协议解析
- [[entities/carbon|carbon]] — 同样关注性能的编程语言项目
- [[entities/tcmalloc|tcmalloc]] — 高性能内存分配器，与rapidjson的性能优化目标一致

## Related Concepts
- [[concepts/JSON|JSON]] — rapidjson是专门处理JSON数据的解析与生成库
- [[concepts/Content-Type|Content-Type]] — HTTP头字段，用于标识请求/响应体中JSON格式数据的媒体类型
- [[concepts/JSON Parsing|JSON解析]] — rapidjson的核心功能领域
- [[concepts/Performance Optimization|性能优化]] — rapidjson的设计核心理念

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
> - "Use rapidjson to parse json, which is a json library focuses on performance."
> - "brpc的HTTP实现使用了rapidjson，以提高JSON解析效率"
> - "rapidjson是一个专注于性能的JSON库"