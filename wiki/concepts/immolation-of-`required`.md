---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "method"
aliases:
  - "required 字段移除方案"
  - "LEGACY_REQUIRED 迁移模板"
  - "ImmoLation of required"
  - "required field label"
  - "required 字段移除方案"
  - "LEGACY_REQUIRED 迁移模板"
  - "ImmoLation of required"
---

## Description
ImmoLation of `required` 是 Protobuf Editions 体系下处理 `required` 字段语义现代化的一套标准化迁移范式。它建立在对 `required` 本质的精确刻画之上：`required` 仅仅是一项"初始化检查约束"（constraint on initialization checking），用于在初始化阶段强制要求字段必须被赋值，而并非序列化层面的存在性标记。因此，迁移的核心思路不是"硬切换"（hard cutover），而是通过 Edition 特性 [[concepts/Feature|Feature]]（特别是 `features.field_presence`）将字段分阶段重新映射到新的存在性语义上。该方案引入了一个新的中间存在性选项 `ALWAYS_SERIALIZE`：其语义与目标态 `EXPLICIT_PRESENCE` 类似，但当 has-bit 未设置时，仍会序列化该字段的默认值（default value），从而保证旧版本读者在反序列化时总能拿到一个有意义、有类型的值。由于旧读者总能获得某个值，迁移的安全性在语义层面得到了严格保证。完整的迁移路径分为两步：第一步，将所有 `LEGACY_REQUIRED` 字段迁移到 `ALWAYS_SERIALIZE`；第二步，经过一个完整的构建周期（build cycle）后，再将所有 `ALWAYS_SERIALIZE` 字段迁移到 `EXPLICIT_PRESENCE`。两步迁移全部完成后，`LEGACY_REQUIRED` 与 `ALWAYS_SERIALIZE` 这两个变体本身也将被作为破坏性变更（breaking change）一并移除。该模板作为大规模变更（Large-scale Change）的范例，示范了在大型 protobuf 代码库中兼顾二进制兼容性、跨语言运行时与多团队协作的工程范式。

## Related Concepts
- [[concepts/Feature|Feature]]
- [[concepts/Large-scale Change|Large-scale Change]]
- [[concepts/Edition|Edition]]
- [[concepts/field-presence|field presence]]（field_presence 字段存在性概念）
- [[concepts/LEGACY-REQUIRED|LEGACY_REQUIRED]]（Edition 中对 proto2 `required` 的重命名）
- [[concepts/EXPLICIT-PRESENCE|EXPLICIT_PRESENCE]]（字段显式存在性语义）
- [[concepts/ALWAYS-SERIALIZE|ALWAYS_SERIALIZE]]（迁移中间态，has-bit 未设置时序列化默认值）

## Related Entities
- [[entities/Protobuf Editions|Protobuf Editions]]

## Mentions in Source

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "We can use features to move fields off of `features.field_presence = LEGACY_REQUIRED` (the edition's spelling of `required`) and onto `features.field_presence = EXPLICIT_PRESENCE`."
> - "It is always safe to turn a proto from `LEGACY_REQUIRED` to `ALWAYS_SERIALIZE`, because `required` is a constraint on initialization checking, i.e., that the value was present."