---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-java-lite-for-editions.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "term"
aliases:
  - "string_field_validation"
  - "kUtf8CheckBit"
  - "isEnforceUtf8"
---

## Description
`features.string_field_validation` 作为 Protobuf Editions Zero 阶段定义的字符串校验开关，决定运行时是否对字符串字段执行 UTF-8 合法性验证。该特性是三态枚举（tristate），包含三种取值：MANDATORY（默认值，运行时 MUST 验证 UTF-8 合法性）、HINT（运行时可以拒绝无效 UTF-8，也可以为了性能跳过检查）以及 NONE（类似 bytes 字段，解析器可以以未指定方式处理无效 UTF-8）。文档明确警告该特性在 _Editions Zero Feature: utf8_validation_ 中正被重新考虑，因为 UTF-8 验证的实际情况比最初认为的更为复杂；长期来看，团队希望移除该特性并强制所有 string 字段进行 UTF-8 验证。在 Java Lite 实现中，该特性由现有的 `kUtf8CheckBit`（0x200）位承载，且由于 HINT 验证级别不适用于 Java 平台——其行为与 MANDATORY 或 NONE 完全一致——该位足以覆盖所有 Editions Zero 字符串验证场景，因此提案建议保持原位对应关系不变（Keep as-is），无需为 HINT 引入额外位表达。提案同时建议引入类似 `isEnforceUtf8` 的辅助函数以封装位判断语义，提升代码可读性并降低位掩码直接使用的维护成本。该特性将 UTF-8 校验与其他字段存在性、编码特性解耦，使各特性位可独立开启或关闭，从而在跨语言实现之间维持行为对齐，并通过 Java Lite MessageInfo 字段编码机制在运行时正确生效。

## Related Concepts
- [[concepts/kUtf8CheckBit|kUtf8CheckBit]]
- [[concepts/Editions Zero Features|Editions Zero Features]]
- [[concepts/isEnforceUtf8|isEnforceUtf8]]
- [[concepts/Java Lite MessageInfo Field Encoding|Java Lite MessageInfo Field Encoding]]
- [[concepts/HINT 验证级别不适用于 Java|HINT 验证级别不适用于 Java]]
- [[concepts/utf8_validation|utf8_validation]]
- [[concepts/features.string_field_validation|features.string_field_validation]]（自身引用入口）

## Related Entities
- [[entities/java-lite|Java Lite]]
- [[entities/edition-zero|Edition Zero]]

## Mentions in Source

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - `features.string_field_validation` — `kUtf8CheckBit (0x200)`. Keep as-is.
> - HINT does not apply to Java and will have the same behavior as MANDATORY or NONE.

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - This feature is a tristate: MANDATORY - this means that a runtime MUST verify UTF-8.
> - The default will be `MANDATORY`.
> - **WARNING:** UTF8 validation is actually messier than originally believed.