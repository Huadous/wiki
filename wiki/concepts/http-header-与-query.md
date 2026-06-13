---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client|http_client]]"]
tags: [term]
aliases:
  - "HTTP Header 与 Query"
  - "HTTP 头部"
  - "Query 参数"
---


# HTTP Header 与 Query

## 定义
HTTP Header 与 Query 是 brpc HTTP/H2 客户端中用于访问和修改 HTTP 请求元数据的接口与数据约定。其中 HTTP Header 通过 `GetHeader` / `SetHeader` 接口进行读写，URL Query 参数通过 `uri().GetQuery` / `SetQuery` 接口进行操作。HTTP header 字段的命名与合并规则遵循 [RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2)；URL query 则遵循标准 URL 编码的分隔约定。

## 关键特征
- **Header 访问接口**：brpc 提供 `GetHeader` / `SetHeader` 接口用于访问与修改 HTTP header。
- **Header field_name 大小写规则**：根据 RFC 2616，HTTP header 的 `field_name` 不区分大小写；brpc 在内部按大小写不敏感方式处理。
- **Header 大小写保留**：brpc 在打印 header 时，会保持用户传入时的大小写形式。
- **同名 Header 合并规则**：若出现相同 `field_name` 的多个 header，按 RFC 2616 规范，应使用逗号（`,`）将多个 value 合并为单个 value。
- **Query 分隔符**：多个 query 之间使用 `&` 分隔。
- **Query 键值分隔符**：单个 query 中，key 与 value 之间使用 `=` 分隔。
- **Query value 可省略**：value 可以省略，例如 `key1=value1&key2&key3=value3` 中 `key2` 是合法的 query，其值为空字符串。
- **查询入口**：query 操作通过 `uri()` 暴露的 `GetQuery` / `SetQuery` 接口进行。

## 应用
- 在 brpc HTTP 客户端构造请求时，通过 `SetHeader` 添加自定义 HTTP header（如鉴权 token、内容类型、追踪 ID 等）。
- 通过 `GetHeader` 读取并解析服务端返回的 HTTP header。
- 通过 `uri().SetQuery` 在 URL 中追加或修改查询参数，例如分页参数 `page=1`、过滤条件 `type=foo` 等。
- 通过 `uri().GetQuery` 提取已有 URL 中的查询参数值。
- 在跨服务调用中构造带有公共 header（如 `User-Agent`、`Authorization`）和复杂 query 串的请求。
- 在需要兼容不同大小写风格的调用方时，确保打印或转发 header 时仍保留原始大小写。

## 相关概念
- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/http-method|HTTP Method]]

## 相关实体
（暂无相关实体）

## 来源提及
- 访问名为Foo的header — [[sources/http_client|http_client]]
- 根据[rfc2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2)，http header的field_name不区分大小写。brpc支持大小写不敏感，同时会在打印时保持用户传入的大小写。 — [[sources/http_client|http_client]]
- query之间用"&"分隔, key和value之间用"="分隔, value可以省略，比如key1=value1&key2&key3=value3中key2是合理的query，值为空字符串。 — [[sources/http_client|http_client]]