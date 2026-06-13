---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [method]
aliases:
  - "No presence discipline"
  - "无存在性模式"
  - "implicit presence"
---


# No presence discipline

## 定义
No presence discipline（无存在性模式）是一种字段存在性跟踪机制，其中生成的 API 仅存储字段值，而不存储字段是否被显式设置的信息。在这种模式下，默认值与"不存在"在序列化时是等价的——未被设置的字段不会被序列化输出。该模式主要应用于 proto3 中未使用 `optional` 标签的字段，是 Protocol Buffers 字段存在性管理的两种基本范式之一。

## 关键特征
- **不追踪显式存在性状态**：生成的代码仅保留字段值，不维护"字段是否被设置"的独立标记
- **默认值与不存在等价**：在序列化层面，默认值等同于字段"未出现"，不会被写入 wire format
- **API 简洁**：数据结构简单，无需额外的 presence bit 或跟踪机制
- **merge 行为受限**：无法通过 merge 操作将默认值合并到目标消息中，因为"未被设置"与"设置为默认值"不可区分
- **依赖字段值做决策**：在（反）序列化时直接依据字段值本身判断是否输出，而非依据显式的存在性状态

## 应用
- **proto3 标量字段的默认行为**：未声明 `optional` 的标量字段默认采用 no presence discipline，是 proto3 最初设计的核心特性之一
- **追求简洁的序列化场景**：对消息体积和编解码性能敏感、且不需要区分"未设置"与"显式默认值"的场景
- **遗留协议兼容**：与 proto2 的 implicit presence 语义保持一致，便于历史数据的反序列化

## 相关概念
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/field-presence|Field presence]]
- [[concepts/wire-format|Wire format]]

## 相关实体
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]

## 来源提及
- "The no presence discipline relies upon the field value itself to make decisions at (de)serialization time, while the explicit presence discipline relies upon the explicit tracking state instead." — [[sources/field_presence|field_presence]]
- "Under the no presence discipline, the default value is synonymous with 'not present' for purposes of serialization." — [[sources/field_presence|field_presence]]