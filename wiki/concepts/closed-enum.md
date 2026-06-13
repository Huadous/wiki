---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "term"
aliases:
  - "closed enum"
  - "封闭枚举"
---

## Description
closed enum（封闭枚举）要求在解析时严格校验枚举值是否落在预定义的合法值集合内，任何超出该集合的 `int32` 值都不会被识别为已知枚举值，而是被转移到 unknown field set 中保存。这一行为是 proto2 中的默认枚举语义，与 open enum（开放枚举）形成对比。在涉及并行数组（parallel arrays）的场景下，closed enum 可能引发混淆：来自并行数组中某个元素的未知枚举值会被放入 unknown field set，导致原本保持并行的数据结构被破坏。该概念的一个值得注意的运行时 quirk 在于，Java 和 C++ 等实现依据消息所在文件的 `syntax`（而非枚举本身声明的位置）来判断枚举的封闭性，这一非一致性行为在 Edition Zero 中被刻意保留，以避免引入破坏性语义变更。

## Related Concepts
- [[concepts/open-enum|开放枚举]]
- [[concepts/feature|Feature]]
- [[concepts/proto2-syntax|proto2 语法]]
- [[concepts/enum-type|enum_type]]
- [[concepts/unknown-field-set|未知字段集合]]
- [[concepts/parallel-arrays|并行数组]]

## Related Entities
- [[entities/Protocol Buffers]]

## Mentions in Source

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "A **closed enum** is an enum where parsing requires validating that a parsed `int32` representing a field of this type matches one of the known set of valid values."
> - "*closed* enums will store enum values that are out of range in the unknown field set."