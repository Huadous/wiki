---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/features]]"]
tags: [term]
aliases:
  - "LEGACY_REQUIRED"
  - "Required Field (LEGACY_REQUIRED)"
---


# Required Field

## 定义
Required Field 是 Protocol Buffers Editions 中 `features.field_presence` 的一个取值（`LEGACY_REQUIRED`），表示字段在解析和序列化时都是必需的（The field is required for parsing and serialization）。在该模式下，任何显式设置的值都会被序列化到 wire，即使该值与默认值相同。Required Field 是 proto2 语法的特征，文档展示了 proto2 中 `required` 字段经 Prototiller 转换后会映射为设置 `features.field_presence = LEGACY_REQUIRED` 的 Edition 2024 代码。

## 关键特征
- 字段存在性的一种取值（field presence value），是 Field Presence 三种取值之一，另外两种是 EXPLICIT 和 IMPLICIT。
- 解析阶段强制要求字段必须出现，否则消息无法成功反序列化。
- 序列化阶段会写入所有显式设置过的值，即使该值与默认值相同，因此默认值的显式赋值也会出现在 wire 上。
- 对应 proto2 语法中的 `required` 关键字；通过 Prototiller 从 proto2 转换为 Editions 时，`required` 字段会被翻译为 `features.field_presence = LEGACY_REQUIRED`。
- 由于语义过于严格（破坏前后向兼容性），Editions 推荐使用 EXPLICIT 字段存在性作为替代。

## 应用
- 维护旧版 proto2 schema：现有 proto2 文件中的 `required` 字段迁移到 Editions 时，会自动呈现为 `features.field_presence = LEGACY_REQUIRED`。
- 需要强制保证关键字段在序列化产物中始终出现（即便其值等于默认值）的场景。
- 解析时检测缺失字段：LEGACY_REQUIRED 字段若未出现，解析过程应报错，从而提供比 EXPLICIT/IMPLICIT 更强的缺失检测能力。

## 相关概念
- [[concepts/field-presence|Field Presence]]
- [[concepts/features-field-presence|features.field_presence]]
- [[concepts/proto2|proto2]]
- [[concepts/explicit|EXPLICIT]]
- [[concepts/implicit|IMPLICIT]]

## 相关实体
- [[entities/prototiller|Prototiller]]

## 来源提及
- "LEGACY_REQUIRED: The field is required for parsing and serialization. Any explicitly-set value is serialized onto the wire (even if it is the same as the default value)." — [[sources/features|features]]
- "Option features.field_presence = LEGACY_REQUIRED" — [[sources/features|features]]
- "The following code sample shows a proto2 file: syntax = \"proto2\" ... required int32 bar = 1; optional int32 baz = 2; repeated int32 qux = 3;" — [[sources/features|features]]