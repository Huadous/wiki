---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/features]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "term"
aliases:
  - "LEGACY_REQUIRED"
  - "Required Field (LEGACY_REQUIRED)"
---

## Description
LEGACY_REQUIRED 属于 Protobuf Editions 中字段存在性（field presence）语义族的一员，其核心特征是"线缆必需、API 可选"：在序列化层面，该字段必须出现在 wire 数据中；而在 API 使用层面，调用方仍可将其视为可选字段进行处理。这一规约主要面向从 proto2 平滑迁移至 Editions 的场景——proto2 的 `required` 关键字长期存在已知缺陷（容易破坏前向/后向兼容性），但出于向后兼容的考虑，Edition Zero 不得不保留相应的语义入口。

为了避免滥用，所有声明为 LEGACY_REQUIRED 的字段必须显式列入 `required` allowlist，否则将触发语法错误。这是一种"显式准入"的约束机制，确保开发者是有意识地引入 wire-required 语义。文档同时提到，任何通过 LEGACY_REQUIRED 显式设置的值都会被序列化到 wire 上，即使该值与默认值相同，这一点与普通 optional 字段的行为存在差异。

从长远来看，社区计划通过一次大规模变更（Large-Scale Change）逐步淘汰 LEGACY_REQUIRED，方案包括：引入 `ALWAYS_SERIALIZE` 枚举值，或新增 `features.always_serialize` 特性，从而把现有的 LEGACY_REQUIRED 字段统一迁移为 EXPLICIT_PRESENCE 字段，最终彻底消除对 proto2 `required` 语义的依赖。

## Related Concepts
- [[concepts/field-presence|field presence]]
- [[concepts/explicit-presence|EXPLICIT presence]]
- [[concepts/required-keyword|required keyword]]
- [[concepts/presence-discipline|presence discipline]]
- [[concepts/editions-large-scale-change|Editions 大规模变更（Large-Scale Change）]]

## Related Entities
- [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- [[sources/editions-readme|editions-readme]]
- [[sources/field_presence|field_presence]]

## Mentions in Source

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "`LEGACY_REQUIRED` - the field is wire-required and API-optional. Setting this will require being in the `required` allowlist."
> - "Any explicitly set value will be serialized onto the wire (even if it is the same as the default value)."