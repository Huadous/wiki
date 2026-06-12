---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_http_service]]"]
tags: [method]
aliases:
  - "空请求/空响应模式"
  - "HTTP service with empty messages"
  - "proto file HTTP service declaration"
---


# Empty request/response pattern

## 定义
空请求/空响应模式（Empty request/response pattern）是brpc框架中为HTTP服务定义接口的一种设计方法。该方法要求在`.proto`文件中声明RPC服务时，使用空的`HttpRequest`和`HttpResponse`消息作为请求和响应类型。所有HTTP数据（包括请求头和请求体、响应头和响应体）都通过`brpc::Controller`对象访问，而不是通过protobuf消息字段传递。

## 关键特征
- **统一声明**：所有服务接口定义集中在`.proto`文件中，避免分散在代码、配置和其他文件中
- **通过Controller访问数据**：HTTP请求的头部、体部、查询参数等均通过`Controller`对象的`http_request()`和`http_response()`方法获取和设置
- **原型继承**：服务实现类继承由protoc生成的基类，并在重写的RPC方法中处理Controller中的HTTP数据
- **简化proto定义**：proto消息体为空，无需为HTTP参数定义复杂的字段结构，降低了proto文件的复杂度
- **与protobuf服务模型兼容**：保持了brpc统一的RPC服务声明范式，使HTTP服务与普通RPC服务在声明和使用方式上一致

## 应用
- **声明HTTP API端点**：在proto文件中集成HTTP接口定义，使前后端开发者都能通过一致的方式查看服务接口
- **实现Web服务**：利用brpc的高性能HTTP框架处理RESTful API请求
- **创建内部HTTP/RESTful服务**：为微服务架构中的内部通信提供统一的接口约定
- **支持HTTP/2协议**：通过相同的模式支持HTTP/2的流式传输特性
- **简化多协议共存**：在同一服务中同时支持protobuf RPC和HTTP调用，保持接口声明的一致性

## 相关概念
- [[concepts/controller|Controller]]
- [[concepts/service-method-url-pattern|Service-Method URL Pattern]]
- [[concepts/service-prefix-url-pattern|Service-Prefix URL Pattern]]
- [[concepts/protocol-buffers|Protocol Buffers]]
- [[concepts/rpc-framework|RPC Framework]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/google-protobuf|Google Protobuf]]

## 来源提及
- "http/h2 services in brpc have to declare interfaces with empty request and response in a .proto file." — [[sources/en_http_service|en_http_service]]
- "This requirement keeps all service declarations inside proto files rather than scattering in code, configurations, and proto files." — [[sources/en_http_service|en_http_service]]
- "Add the service declaration in a proto file." — [[sources/en_http_service|en_http_service]]