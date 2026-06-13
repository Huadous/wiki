---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [term]
aliases:
  - "repeated"
  - "repeated fields"
  - "可重复字段"
---


# Repeated fields

## 定义
Repeated fields 是 Protocol Buffers 中表示可重复出现的字段类型（使用 `repeated` 关键字修饰）。在 proto2 和 proto3 中，repeated fields 都不跟踪显式 presence：空列表和"未设置"的 repeated field 之间没有区别。这是 repeated fields 与 singular fields 在 presence 语义上的关键差异——singular fields 会跟踪显式 presence，而 repeated fields 不会。

## 关键特征
- **不跟踪 presence**：无论 proto2 还是 proto3，repeated fields 都不会跟踪显式存在性；空列表与未设置的 repeated field 在 API 层面是等价的。
- **Wire format 中的追加语义**：重复出现的 repeated field 值通常会被追加到字段的 API 表示中（即列表中），而非覆盖。
- **Packed 编码格式**：序列化 packed 形式的 repeated field 时，会在 tag stream 中产生一个 length-delimited 值，将所有元素打包为一个单一字段。
- **跨版本一致性**：proto2 和 proto3 在 repeated fields 的 presence 行为上保持一致，两者都不引入显式 presence 跟踪。

## 应用
- **列表型数据建模**：用于在 Protocol Buffers 消息中表示一组数量可变但同类型的值，例如消息的标签列表、日志条目集合等。
- **二进制压缩优化**：通过使用 packed wire format，多个 repeated field 值可以在一次序列化操作中高效传输，减少网络开销。
- **API 向后兼容**：由于 repeated fields 不区分空与未设置状态，客户端和服务端在不同版本间演进时，无需担心 presence 状态的破坏性变化。

## 相关概念
- [[concepts/field-presence|Field presence]]
- [[concepts/wire-format|Wire format]]
- [[concepts/default-value|Default value]]

## 相关实体
- [[entities/proto2|proto2]]
- [[entities/proto3|proto3]]

## 来源提及
- "Repeated fields and maps do not track presence: there is no distinction between an _empty_ and a _not-present_ repeated field." — [[sources/field_presence]]
- "Similar to proto2 APIs, proto3 does not track presence explicitly for repeated fields." — [[sources/field_presence]]
- "Duplicate `repeated` fields are typically appended to the field's API representation." — [[sources/field_presence]]