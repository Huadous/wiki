---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_http_service]]"]
tags: [method]
aliases:
  - "URL路由类型"
  - "brpc URL类型"
---


# URL types

## 定义
URL types 是 brpc HTTP 服务中用于定义 URL 路由匹配模式的一种机制。brpc 支持三种 URL 路由类型：以 `/ServiceName/MethodName` 为前缀、以 `/ServiceName` 为前缀、以及 RESTful URL。每种类型适用于不同的服务场景，提供从简单到高度灵活的 URL 映射能力。

## 关键特征
- **三种路由类型**：提供从默认到高度可定制的 URL 匹配模式。
- **以 `/ServiceName/MethodName` 为前缀**：这是 brpc 的默认路由方式，URL 路径严格映射到服务名和方法名，适合标准 RPC 风格的 HTTP 服务。
- **以 `/ServiceName` 为前缀**：URL 仅匹配服务名，方法名通过其他方式（如 HTTP Header 或 Body 内容）指定，适合资源管理类服务。
- **RESTful URL**：允许使用正则表达式、路径参数等灵活定义 URL 映射关系，适合构建符合 REST 风格的 API。

## 应用
- **标准 RPC 服务**：使用 `/ServiceName/MethodName` 类型，适合需要明确方法调用语义的微服务。
- **资源管理服务**：使用 `/ServiceName` 类型，适合对同一资源集合（如 `/user`）执行不同操作（GET、POST、DELETE）的服务。
- **RESTful API 服务器**：使用 RESTful URL 类型，支持路径参数（如 `/users/{id}`）和复杂路由规则，适合构建 Web API。

## 相关概念
[[concepts/restful-url|RESTful URL]]

## 相关实体
[[entities/brpc|brpc]]

## 来源提及
- "URL types — [[sources/en_http_service|en_http_service]]"
- "/ServiceName/MethodName as the prefix — [[sources/en_http_service|en_http_service]]"
- "/ServiceName as the prefix — [[sources/en_http_service|en_http_service]]"
- "Restful URL — [[sources/en_http_service|en_http_service]]"