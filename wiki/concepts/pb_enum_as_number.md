---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term]
aliases:
  - "枚举数值化"
  - "protobuf枚举格式"
  - "pb_enum_as_number标志"
---


# pb_enum_as_number

## 定义

`pb_enum_as_number` 是百度 RPC 框架 brpc 中的一个 gflag（全局标志/命令行标志），用于控制 Protocol Buffers (protobuf) 枚举型字段在 JSON 格式序列化或反序列化时的表现方式。默认情况下，该标志处于关闭状态，此时枚举字段会以对应的名称字符串（如 `"Foo"`）形式呈现；当标志开启时，枚举字段会转换为对应的整数值（如 `1`）。

## 关键特征

- **影响 JSON 序列化**：该标志专门控制 protobuf 数据在 JSON 格式下的编码/解码行为，不影响二进制 protobuf 序列化。
- **双向影响**：该标志同时作用于客户端发送的请求（JSON 请求体）和服务器返回的响应（JSON 响应体）。
- **默认关闭**：brpc 默认使用枚举名称表示，以保持更好的前后兼容性（当 proto 文件新增枚举值时，旧客户端/服务器仍能正常工作）。
- **开启影响**：开启后，枚举名称会被其整数定义值替换，这可以兼容无法解析枚举名称的旧代码段或非 protobuf 原生系统。

## 应用

- **调试与日志**：在调试或日志记录时，可临时开启该标志以查看枚举字段的原始整数值，便于与底层协议或数据库存储值做比对。
- **兼容遗留系统**：当对接的旧版客户端或第三方系统（如某些前端或非 protobuf 服务）无法解析 protobuf 枚举名称、只能接受整数时，开启该标志可保持兼容。
- **性能优化**：对于大量包含枚举字段的 JSON 请求/响应，使用整数表示可以减少数据传输量（整数 JSON 通常比字符串名称短）。

## 相关概念

- [[concepts/JSON转protobuf|JSON转protobuf]]
- [[concepts/协议自动检测|协议自动检测]]

## 相关实体

- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/brpc|brpc]]
- [[entities/protoc|protoc]]

## 来源提及

- "When `-pb_enum_as_number` is turned on, enums in pb are converted to values instead of names. For example in `enum MyEnum { Foo = 1; Bar = 2; };`, fields typed `MyEnum` are converted to `"Foo"` or `"Bar"` when the flag is off, `1` or `2` otherwise." — [[sources/en_server|en_server]]