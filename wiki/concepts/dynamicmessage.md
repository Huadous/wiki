---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/techniques]]"]
tags: [term]
aliases:
  - "DynamicMessage 类"
  - "Protocol Buffers 动态消息"
---


# DynamicMessage

## 定义

**DynamicMessage** 是 Protocol Buffers 库中提供的一个关键类（支持 C++ 和 Java），用于在 **运行时** 动态解析和处理 protobuf 消息，而无需在编译时预先生成特定消息类型的 C++/Java 代码。它通过利用描述符（`FileDescriptorSet`）来理解消息的结构和字段定义，从而实现对任意 protobuf 消息类型的通用操作。在自描述消息（Self-Describing Messages）机制中，DynamicMessage 是核心工具。

## 关键特征

- **运行时动态性**：无需预编译 `.proto` 文件或依赖静态生成的代码，即可在运行时处理任意 protobuf 消息。
- **依赖描述符**：必须基于 `FileDescriptorSet` 或 `Descriptor` 对象来构建，通过描述符获取字段名称、类型、标签号等信息。
- **通用性**：可以作为处理未知消息类型的统一接口，适用于需要支持动态协议扩展的场景。
- **性能权衡**：相比静态生成的代码（如 `MessageLite` 子类），DynamicMessage 在序列化/反序列化时性能较低，因为需要额外的反射和类型检查开销。
- **跨语言支持**：在 C++ 和 Java 两种主流语言实现中均提供。

## 应用

- **自描述消息系统**：是实现 Self-Describing Messages 的核心组件，允许消息携带自身类型的 `.proto` 定义（`FileDescriptorSet`），从而实现无需预知消息结构的通信。
- **动态协议适配器**：在微服务网关、协议中转服务中，用于动态处理多种未知或频繁变动的消息格式。
- **调试与通用工具**：构建通用的 protobuf 消息查看器、编辑器或调试工具，可与任何 protobuf 消息交互。
- **动态 RPC 调用**：与 gRPC 动态服务配合，在运行时根据服务描述合约调用任意 RPC 方法。

## 相关概念

- [[concepts/self-describing-messages|Self-Describing Messages]]
- [[concepts/scalar-value-types|标量类型]]
- [[concepts/extensions|扩展]]
- [[concepts/oneof-type|oneof 联合类型]]
- [[concepts/map-type|Map 类型]]
- [[concepts/message-type|消息类型]]

## 相关实体

- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc 编译器]]
- [[entities/grpc|gRPC 框架]]

## 来源提及

- “By using classes like DynamicMessage (available in C++ and Java), you can then write tools which can manipulate SelfDescribingMessage.” — [[protobuf/techniques|techniques]]