---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions]]"]
tags: [term]
aliases:
  - "Enum value uniqueness"
  - "Protobuf 枚举值唯一性"
---


# Enum value uniqueness

## 定义
**Enum value uniqueness**(枚举值唯一性)是指在 Protobuf 中禁止同一个枚举类型内的不同枚举值共享相同数值(也称为 alias)的规则。例如禁止 `enum Foo { BAR = 5; BAZ = 5; }` 这样的写法。该概念主张在未来的 edition 中彻底关闭别名支持,以收紧 schema 约束。

## 关键特征
- **禁止别名**:不允许同一枚举中存在多个成员共享同一数值。
- **影响后端实现复杂度**:别名机制会给 Protobuf 后端实现带来显著复杂度。
- **影响文本与 JSON 编解码**:在 textproto 与 JSON 的编解码过程中会产生诡异(weird)行为。
- **通过 feature gate 平滑迁移**:建议引入 `features.allow_enum_aliases` feature,默认值为 `true`,后续将其切换为 `false`,以达成收紧目标。

## 应用
- 在新的 Protobuf edition 中收紧枚举定义规则,消除别名带来的歧义。
- 引导存量 schema 逐步迁移到无别名模式,从而简化代码生成、运行时反射以及文本/JSON 互操作。
- 为后端实现、序列化与反序列化逻辑提供更明确的语义约束。

## 相关概念
- [[concepts/feature-gating|Feature gating]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## 相关实体
- [[entities/protobuf|Protobuf]]

## 来源提及
- "Right now, we allow aliases in enums: `enum Foo { BAR = 5; BAZ = 5; }` This results in significant complexity in some parts of the backend, and weird behavior in textproto and JSON. We should disallow this." — [[sources/editions-stricter-schemas-with-editions]]