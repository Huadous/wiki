---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/techniques]]"]
tags: [method]
aliases:
  - "自描述消息"
  - "Self-Describing Messages"
  - "SelfDescribingMessage"
---


# Self-describing Messages

## 定义
Self-describing Messages（自描述消息）是一种 Protocol Buffers 技术，通过将 `.proto` 文件的描述符序列化为 `FileDescriptorSet`，并与 `Any` 消息结合，使消息本身包含其类型定义信息。这样，即使接收方没有原始 `.proto` 文件，也可以利用 `DynamicMessage` 类动态解析消息内容。

## 关键特征
- **自包含类型信息**：消息载荷中嵌入了其类型的完整描述（通过 `FileDescriptorSet`），无需依赖外部 `.proto` 文件。
- **动态解析能力**：接收方可使用 `DynamicMessage` 类在运行时解析和访问消息字段，无需预先生成静态代码。
- **非核心特性**：Google 内部未使用此功能，因此 Protocol Buffers 核心库默认不包含。使用前需确认目标平台是否支持动态消息。
- **基于标准类型**：依赖于 `google.protobuf.Any` 和 `google.protobuf.FileDescriptorSet` 等标准 Protobuf 消息类型。

## 应用
- **数据存档与交换**：在长期存储或跨系统传输中，确保消息格式可被未来或未知的客户端解析。
- **调试与日志**：捕获并记录任意 Protobuf 消息的完整内容，无需为每种消息类型编写专门的日志代码。
- **动态代理与桥接**：构建通用的消息路由或转换中间件，能够处理不断变化的消息类型。
- **反射式工具**：开发通用的 Protobuf 消息浏览器、编辑器或测试工具。

## 相关概念
- [[concepts/file-descriptor|FileDescriptor]]
- [[concepts/any-type|Any 类型]]
- [[concepts/dynamic-message|dynamic-message]]
- [[concepts/wire-format|Wire Format]]
- [[concepts/message-type|Message type]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/google|Google]]

## 来源提及
- "Protocol Buffers do not contain descriptions of their own types. Thus, given only a raw message without the corresponding .proto file defining its type, it is difficult to extract any useful data." — [[protobuf/techniques|techniques]]
- "The file src/google/protobuf/descriptor.proto in the source code package defines the message types involved." — [[protobuf/techniques|techniques]]