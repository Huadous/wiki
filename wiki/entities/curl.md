---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_http_service]]"
tags:
  - "product"
aliases:
  - "cURL"
  - "curl命令行工具"
  - "libcurl"
  - "cURL"
  - "curl命令行工具"
---

## Related Concepts
- [[concepts/内置服务|内置服务]] — 提供HTTP接口供curl测试
- [[concepts/JSON to PB Conversion|JSON to PB Conversion]] — curl支持的序列化格式转换
- [[concepts/HTTP/2|HTTP/2]] — brpc的h2协议比libcurl更友好
- [[concepts/json2pb|json2pb]] — brpc中JSON与Protobuf的相互转换机制
- [[concepts/序列化|序列化]] — curl可通过Content-Type切换JSON与protobuf序列化
- [[concepts/HTTP|HTTP]] — curl和libcurl支持的核心协议之一
- [[concepts/Gzip压缩|Gzip压缩]] — curl需加--compressed选项才能启用压缩支持；若没有该选项，则服务器始终返回未压缩的结果
- [[concepts/Accept-encoding|Accept-encoding]] — curl若不添加--compressed选项则不会发送此HTTP头部，导致服务器不压缩响应