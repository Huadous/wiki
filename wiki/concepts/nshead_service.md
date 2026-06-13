---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/server|server]]"]
tags: [method]
aliases:
  - "NsheadService"
  - "nshead_service 机制"
  - "实现 NsheadService"
---


# nshead_service

## 定义
nshead_service 是 brpc 中用于实现自定义 nshead 协议服务的机制。用户通过实现 `NsheadService` 接口（特别是 `NovaServiceAdaptor`、`PublicPbrpcServiceAdaptor`、`NsheadMcpackAdaptor` 等适配器），并将其赋值给 `ServerOptions.nshead_service` 字段来启用对应的协议。nshead_mcpack 是其中一种具体协议，其数据包由 `nshead + mcpack` 构成，并使用 mcpack2pb 使得同一份代码可以同时处理 mcpack 和 pb 两种格式。

## 关键特征
- 基于 `NsheadService` 接口实现自定义协议服务
- 通过 `ServerOptions.nshead_service` 字段注册到 brpc Server
- 提供多种内置适配器：`NovaServiceAdaptor`、`PublicPbrpcServiceAdaptor`、`NsheadMcpackAdaptor`
- nshead_mcpack 协议数据包结构为 `nshead + mcpack`，不包含特殊字段
- 通过 mcpack2pb 实现 mcpack 与 pb 双格式统一处理
- 协议中未传递 `ErrorText` 字段，发生错误时 server 只能关闭连接

## 应用
- 在 brpc Server 中支持 nshead 系列自定义二进制协议
- 兼容历史遗留的 nshead-based 协议栈（如百度内部使用的 Nova、Pbrpc、mcpack 协议）
- 允许用户在不修改 brpc 核心代码的前提下扩展私有协议
- 通过 mcpack2pb 同时支持 mcpack 与 Protobuf 序列化格式，降低协议适配成本

## 相关概念
- [[concepts/协议支持|协议支持]]
- [[concepts/JSON-PB转换|JSON <=> PB转换]]

## 相关实体
- [[entities/brpc-server|brpc::Server]]
- [[entities/brpc-serveroptions|brpc::ServerOptions]]

## 来源提及
- "和UB相关的协议请阅读[实现NsheadService](nshead_service.md)。" — [[sources/server|server]]
- "顾名思义，这个协议的数据包由nshead+mcpack构成，mcpack中不包含特殊字段。不同于用户基于NsheadService的实现，这个协议使用了mcpack2pb，使得一份代码可以同时处理mcpack和pb两种格式。" — [[sources/server|server]]