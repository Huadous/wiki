---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [term]
aliases:
  - "Reflection API"
  - "Protobuf Reflektion"
---


# Reflection

## 定义
Reflection（反射）是 Protocol Buffers 的一项机制，允许用户在运行时动态检查和操作消息的结构、字段、枚举值和序列化方式，而无需依赖预编译生成的代码。这一机制对于需要通用处理 protobuf 数据的高级用例至关重要。

## 关键特征
- **动态性**：无需编译时的代码绑定，即可在运行时遍历消息的字段和类型信息。
- **自描述性**：允许从 `.proto` 文件描述符（`FileDescriptor`、`Descriptor`、`FieldDescriptor` 等）获取完整的消息结构。
- **特征感知（Feature-aware）**：必须与 [[concepts/protobuf-editions|Protobuf Editions]] 的特征继承（[[concepts/feature-inheritance|Feature Inheritance]]）机制兼容，确保动态操作时特征值正确。
- **透明性**：特征继承对用户应完全透明，反射行为应如同特征已被显式设置在所有位置一样。
- **高级用户导向**：主要服务于存储服务提供商、自定义代码生成器和序列化/验证框架等高级场景。

## 应用
- **动态序列化与反序列化**：在不重新生成代码的情况下，处理不同版本或未知类型的 protobuf 消息。
- **自定义代码生成器**：利用反射分析 `.proto` 文件结构，生成目标语言的绑定代码。
- **数据验证与转换**：在通用中间件或数据管道中，动态验证字段值或转换消息格式。
- **存储服务**：如数据库或缓存服务，通过反射解析和存储任意 protobuf 消息，而无需预知所有消息类型。
- **调试与检查工具**：实现通用 protobuf 消息查看器或日志解析工具。

## 相关概念
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/protobuf-editions|Edition]]
- [[concepts/feature|Feature]]
- [[concepts/language-scoped-feature|Language-scoped Feature]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "We plan to upgrade reflection to be feature-aware in a way that minimizes code we need to change." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "We do not expect anyone to implement feature-inheritance logic themselves; feature inheritance should be fully transparent to users, behaving as if features had been placed explicitly everywhere." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]