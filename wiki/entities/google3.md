---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-group-migration-issues|editions-group-migration-issues]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "other"
aliases:
  - "Google monorepo"
  - "google3 codebase"
  - "Google3 内部代码库"
---

## Description
google3 是 Google 内部的单一代码仓库（monorepo），容纳了 Google 大部分产品的源代码，在 Protobuf Editions 相关文档中被反复作为迁移执行场所和规模参考基准。在 [[sources/editions-group-migration-issues|editions-group-migration-issues]] 中，google3 的内部统计用于评估 [[concepts/edition-2023|Edition 2023]] 的迁移风险，超过 50% 的 proto 文件会产生 Java 生成代码，group 字段的处理变更因此对 Java 影响最大；而 Dart V1 行为变更仅影响极少数 proto 文件。在 [[sources/editions-edition-zero-features|editions-edition-zero-features]] 中，google3 的迁移规模更加具体：共有 385,236 处使用 `optional` 关键字需要删除，约 12,300 处显式启用 packed 字段，仅 200 处显式禁用。这些大规模数据直接驱动了 Edition Zero 的多项设计决策，例如选择 PACKED 作为 repeated_field_encoding 的默认行为。

## Related Entities
No related entities

## Related Concepts
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/edition-zero|Edition Zero]]

## Mentions in Source

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "It was determined that this only affected a handful of protos in google3, and could probably be manually fixed as-needed."
> - "Java's handling changes the story significantly, since over 50% of protos in google3 produce generated Java code."

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "Migration will require deleting every instance of `optional` in proto files in google3, of which there are 385,236."
> - "Users explicitly enabled packed fields 12.3k times, but only explicitly disable it 200 times."