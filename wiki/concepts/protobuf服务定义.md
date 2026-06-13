---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/server|server]]"]
tags: [method]
aliases:
  - "protobuf service definition"
  - "brpc protobuf 服务定义"
---


# protobuf服务定义

## 定义
protobuf服务定义是在brpc中使用 Protocol Buffers 的 `.proto` 文件定义 RPC 服务接口的方法。用户通过在 `.proto` 文件中设置 `option cc_generic_services = true;`，并定义 `message`（请求/响应数据结构）和 `service`（RPC 方法集合），由 `protoc` 编译器生成对应的 C++ Service 基类。用户继承该基类并实现其方法即可完成服务端逻辑。该方法以 `EchoService` 为典型示例演示完整定义流程。

## 关键特征
- 通过 `.proto` 文件以 IDL（接口描述语言）方式声明 RPC 服务接口
- 需要显式启用 `option cc_generic_services = true;`（C++ 场景），Java/Python 则分别对应 `java_generic_services` 和 `py_generic_services`
- `protoc` 编译 `.proto` 文件后自动生成 Service 基类与消息类的桩代码
- 开发者只需继承生成的 Service 基类并覆写方法，即可实现业务逻辑
- 支持请求/响应消息的强类型定义（`message` 字段类型由 proto schema 约束）
- 与 brpc 框架深度集成，是构建 brpc RPC 服务的标准入口方式

## 应用
- 在 brpc 中定义任何自定义的 RPC 服务接口（典型示例：`EchoService`）
- 跨语言 RPC 接口的标准化描述（C++ 服务端可与 Java、Python 等客户端互通）
- 服务端与客户端共享同一份 `.proto` 文件作为接口契约
- 通过 `protoc` 自动生成的桩代码减少手写序列化/反序列化代码的工作量

## 相关概念
- [[concepts/json-pb-conversion|JSON <=> PB转换]]
- [[concepts/protobuf-arena|protobuf arena]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "告诉protoc要生成C++ Service基类，如果是java或python，则应分别修改为java_generic_services和py_generic_services" — [[sources/server|server]]
- "option cc_generic_services = true;" — [[sources/server|server]]