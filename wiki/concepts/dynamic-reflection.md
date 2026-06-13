---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [method]
aliases:
  - "Dynamic Reflection"
  - "reflection API"
---


# Dynamic reflection

## 定义
Dynamic reflection 是 Protocol Buffers 提供的一种 API 机制，允许在运行时动态地访问和操作消息字段。与静态生成的代码 API（generated APIs）相对，dynamic reflection 提供了对字段元数据的运行时访问能力，包括字段是否存在（has presence）等信息。这一机制扩展了 Protocol Buffers 在动态场景中的可用性，使开发者无需依赖编译期生成的代码即可查询和操作 protobuf 消息。

## 关键特征
- 运行时访问：允许在程序运行期间动态获取和操作消息字段，无需依赖编译时生成的访问器代码
- 字段元数据查询：可查询字段的描述信息（descriptor），包括字段名称、类型、编号等
- Presence 跟踪支持：在 proto2 和 proto3 中均支持通过 dynamic reflection 检查字段是否存在（has presence）
- 与 generated APIs 并存：与静态生成的代码 API 互补，为不同的使用场景提供灵活的访问方式
- 跨语言一致性：在多种 Protocol Buffers 实现语言中均可使用

## 应用
- 通用编解码工具：开发不依赖特定消息类型的通用序列化/反序列化工具
- 动态消息处理：在运行时根据 schema 描述符（descriptor）处理未知类型的消息
- 字段验证：通过 reflection 检查字段 presence 状态，实现动态字段验证逻辑
- 调试与诊断：在调试过程中动态检查消息字段的值和存在性
- 插件与中间件开发：实现需要动态操作 protobuf 消息的通用插件或中间件

## 相关概念
- [[concepts/field-presence|Field presence]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]

## 相关实体
- [[entities/proto2|proto2]]
- [[entities/proto3|proto3]]
- [[entities/descriptor|google::protobuf::Descriptor]]
- [[entities/descriptorpool|google::protobuf::DescriptorPool]]

## 来源提及
- "This table outlines whether presence is tracked for fields in proto2 APIs (both for generated APIs and using dynamic reflection):" — [[sources/field_presence|field_presence]]
- "This table outlines whether presence is tracked for fields in proto3 APIs (both for generated APIs and using dynamic reflection):" — [[sources/field_presence|field_presence]]