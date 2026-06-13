---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]"]
tags: [term]
aliases:
  - "Serialized Descriptor Sets"
  - "序列化描述符集"
---


# Serialized Descriptors

## 定义
Serialized Descriptors（序列化描述符）是指将 [[entities/descriptor.proto|descriptor.proto]] 序列化为二进制格式后得到的描述符集（descriptor sets）。在 Protocol Buffers 生态系统中，存在大量此类预先序列化的二进制快照，它们已被发布、存储并被各种工具和运行时广泛消费。它们构成了 Protobuf Editions 演进过程中的重要兼容性约束。

## 关键特征
- 以二进制形式存在的 descriptor.proto 序列化产物，独立于原始的 `.proto` 源文件
- 在生态系统中广泛分布，已被工具链和运行时长期依赖
- 需要在较长的时间窗口内（数月级别）继续保持可用
- 对 Protobuf Editions 的功能解析机制构成兼容性约束
- 是判断是否可以移除回退机制（fallback）的关键时间基准

## 应用
- 在 [[concepts/legacy-syntax-editions|Legacy Syntax Editions]] 提案中，Serialized Descriptors 是讨论 edition zero 发布时间表时的核心考量因素：由于大量已发布的序列化描述符需要在未来数月内继续工作，因此不能过早地要求它们支持新的功能解析机制
- 为避免长时间阻塞 edition zero 的发布，protoc 需在功能解析失败时提供回退机制——对 proto2/proto3 文件回退到现有的硬编码默认值
- 作为兼容性决策的时间锚点：只有在确认不再需要支持早于本次文档变更的过期 descriptor.proto 快照时，才能移除上述回退机制

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]

## 相关实体
- [[entities/descriptor.proto|descriptor.proto]]

## 来源提及
- "As we now know, there are a lot of serialized `descriptor.proto` descriptor sets out there that need to continue working for O(months)." — [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]
- "In order to avoid blocking edition zero for that long, we may need fallbacks in protoc for the case where feature resolution *fails*." — [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]