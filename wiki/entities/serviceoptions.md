---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [other]
aliases:
  - "ServiceOptions结构体"
  - "brpc服务选项"
---


# ServiceOptions

## 基本信息
- Type: other
- Source: [[sources/en_server|brpc Server Programming Guide]]

## 描述

ServiceOptions 是 brpc 框架中用于配置单个服务添加选项的结构体。当通过 `server.AddService()` 方法向服务器注册服务时，可以传入该对象以精细控制服务的行为。该结构体包含三个关键字段：`ownership`（控制服务器是否拥有服务实例的所有权）、`restful_mappings`（定义 RESTful 路径与 Protobuf 方法的映射关系）、以及 `allow_http_body_to_pb`（控制是否允许 HTTP 请求体自动转换为 Protobuf 请求）。特别地，`allow_http_body_to_pb` 字段对于需要以非典型方式处理 HTTP 请求的传统服务至关重要，设置为 `false` 可关闭默认的从 HTTP/h2 请求体到 Protobuf 请求的转换行为。ServiceOptions 与 [[entities/brpc|brpc]] 的服务框架紧密集成，是定制服务端行为的基础配置单元。

## 相关实体

- [[entities/brpc|brpc]] — brpc 框架，ServiceOptions 是该框架的一部分
- [[entities/ServerOptions|ServerOptions]] — brpc 中用于配置服务器全局选项的结构体
- [[entities/Controller|Controller]] — brpc 中用于控制 RPC 调用的对象

## 相关概念

无相关概念。

## 来源提及

- "brpc::ServiceOptions svc_opt;
svc_opt.ownership = ...;
svc_opt.restful_mappings = ...;
svc_opt.allow_http_body_to_pb = false; // turn off conversion from http/h2 body to pb request
server.AddService(service, svc_opt);" — [[sources/en_server|brpc Server Programming Guide]]

- "This behavior is unaffected by setting allow_http_body_to_pb or not." — [[sources/en_server|brpc Server Programming Guide]]