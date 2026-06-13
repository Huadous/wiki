---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "method"
aliases:
  - "Edition 全序比较"
  - "edition_less_than"
  - "Edition Total Order"
  - "Total Ordering of Editions"
  - "Edition 全序比较"
  - "edition_less_than"
  - "Edition Total Order"
---

## Description
Edition Total Order 定义于《Life of an Edition》文档，是 Protobuf Editions 体系中跨 edition 进行大小比较的标准化规则。其算法为：将 edition 字符串按 `.` 切分为若干分量，对各分量依次按「长度优先、再按字典序」的复合方式排序（例如 `9 < 10`），从而在任意两个 edition 之间得到唯一确定的全序关系。引入该总序的动机在于最小化后端的同步成本：protobuf-team 仅负责宣告（proclaim）editions，并不直接定义它们，各第三方后端需要自行跨 edition 调整默认值；有了全序之后，后端只需判断某个 proto 文件是否比引入新默认值的 edition 更晚（例如通过 `file.EditionIsLaterThan("2023")` 或 `file.EditionIsBetween("2023", "2023.1")`），而无需跟踪所有可能的 edition 组合。该全序进一步被 [[sources/editions-minimum-required-edition|editions-minimum-required-edition]] 直接复用，作为判断运行时所支持的 edition 是否小于描述符所要求的最低必需 edition 的判定基础，从而支撑运行时与编辑器之间的兼容性判定。

## Related Concepts
- [[concepts/edition|Edition]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-proclamation|Edition Proclamation]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]

## Mentions in Source
> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "Less than" is defined per the edition total order given in [Life of an Edition](life-of-an-edition.md). To restate it, it is the following algorithm:

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - However, protobuf-team does not define editions, it only proclaims them. Third-party backends are responsible for changing defaults across editions. To minimize the amount of synchronization, we introduce a total order on editions.
> - The total order is thus: the edition string is split on '.'. Each component is then ordered by a.len < b.len && a < b. This ensures that 9 < 10, for example.