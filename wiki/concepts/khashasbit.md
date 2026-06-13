---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [term]
aliases:
  - "kHasHasBit (0x1000)"
  - "0x1000"
  - "Has Has Bit"
---


# kHasHasBit

## 定义
kHasHasBit 是 Java Lite 中 `RawMessageInfo` 字段条目编码已有的一个标志位，十六进制值为 `0x1000`。该位用于编码 Editions Zero 特性 `features.field_presence`，即表示字段是否带有显式的 "has" 位来追踪其存在性。在 Java Lite 向 Editions 迁移的推荐方案中，该位被明确建议保持原样（Keep as-is），因为它已经正确地编码了对应的 Editions 特性。

## 关键特征
- 位值：`0x1000`
- 用途：编码 `features.field_presence` 特性，对应字段是否拥有显式的 "has" 位
- 来源位置：Java Lite 中 `RawMessageInfo` 字段条目编码
- 迁移策略：在 Editions 迁移方案中被建议 **Keep as-is**（保持原样），无需修改
- 属于 Java Lite MessageInfo 编码中已经存在的 Editions 特性位集合，与 [[concepts/kUtf8CheckBit|kUtf8CheckBit]]、[[concepts/kLegacyEnumIsClosedBit|kLegacyEnumIsClosedBit]] 等位并列

## 应用
- 在 Java Lite 运行时中用于在 `RawMessageInfo` 编码层面追踪字段的存在性（field presence）信息
- 作为 Java Lite 向 Editions 迁移的兼容性基础：已有位已经正确映射到 Editions 特性，无需新增或修改编码逻辑
- 与 `GetExperimentalJavaFieldType` 中的 Editions Zero 特性解析对应，使迁移过程可以保持向后兼容

## 相关概念
- [[concepts/features.field_presence|features.field_presence]]
- [[concepts/GetExperimentalJavaFieldType|GetExperimentalJavaFieldType]]
- [[concepts/RawMessageInfo|RawMessageInfo]]
- [[concepts/kUtf8CheckBit|kUtf8CheckBit]]
- [[concepts/kLegacyEnumIsClosedBit|kLegacyEnumIsClosedBit]]

## 相关实体
- [[entities/Java Lite|Java Lite]]

## 来源提及
- "Field entries in `RawMessageInfo` already encode bits corresponding to most ***resolved*** Editions Zero features in `GetExperimentalJavaFieldType`." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- "features.field_presence | `kHasHasBit (0x1000)` | Keep as-is." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]