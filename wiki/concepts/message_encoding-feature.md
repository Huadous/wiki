---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/style]]"]
tags: [term]
aliases:
  - "消息编码特性"
  - "delimited representation"
  - "message_encoding 特性"
---


# message_encoding 特性

## 定义
message_encoding 特性是 Protocol Buffers editions 2023 中提供的一个特性，用于替代已废弃的 groups 语法。通过将该特性设置为 `delimited`，可以在保持有线格式兼容的前提下，使用嵌套消息定义和字段类型来替代 groups，实现从旧语法到新版语法（edition 2023）的平滑迁移。

## 关键特征
- **替代 groups**: message_encoding 特性专为替代已废弃的 groups 语法而设计。
- **有线格式兼容**: 通过设置 `delimited`，生成的有线格式与原有的 groups 保持兼容，不会破坏已有的序列化数据。
- **声明式语法**: 使用该特性时，开发者只需在字段上声明 `message_encoding = DELIMITED`，而无需修改消息的内部结构。
- **迁移桥梁**: 它是从 proto2/proto3 过渡到 edition 2023 的关键特性之一，允许团队逐步迁移代码。
- **与 Field presence 特性配合**: 在需要时，可以与其他特性（如 LEGACY_REQUIRED）结合使用，以处理更复杂的迁移场景。

## 应用
- **groups 语法迁移**: 当项目需要从 proto2（groups 已废弃）或 proto3（groups 已移除）迁移到 edition 2023 时，可以使用 message_encoding 特性来保持有线格式兼容。
- **样式指南推荐**: [[concepts/groups|groups]] 被官方样式指南列为不推荐使用的语法，推荐使用嵌套消息和 message_encoding 特性作为替代方案。
- **代码重构**: 在重构遗留的 Protocol Buffers 定义时，可以使用该特性逐步替换旧的 groups 定义，而无需一次性修改所有依赖的代码和数据。

## 相关概念
- [[concepts/groups|groups]]
- [[concepts/Field presence feature (LEGACY_REQUIRED)|Field presence feature (LEGACY_REQUIRED)]]
- [[concepts/required fields|required fields]]

## 相关实体
- [[entities/Protocol Buffers|Protocol Buffers]]

## 来源提及
- "Groups is an alternate syntax and wire format for nested messages. Groups are considered deprecated in proto2, were removed from proto3, and are converted to a delimited representation in edition 2023." — [[sources/style|style]]
- "You can use a nested message definition and field of that type instead of using the group syntax, using the message_encoding feature for wire-compatibility." — [[sources/style|style]]