---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-life-of-an-edition]]"
  - "[[protobuf/editions-edition-evolution.md]]"
tags:
  - "method"
aliases:
  - "EditionIsBetween"
  - "file.EditionIsLaterThan"
  - "Edition Predicates"
  - "EditionIsBetween"
  - "file.EditionIsLaterThan"
---

## Description
`EditionIsLaterThan` 与 `EditionIsBetween` 共同构成 Edition Predicates 谓词方法集合，其设计目的是让后端在 protobuf 核心团队不感知的情况下也能引入或修改特性的默认值。具体的调用形式为 `file.EditionIsLaterThan("2023")`（判断当前 proto 是否晚于某版本）或 `file.EditionIsBetween("2023", "2023.1")`（判断是否介于两个版本之间）。该机制成立的根基在于 Editions 在版本字符串上定义了全序关系（total ordering），从而保证任意两个版本之间的大小关系都是良定义的。借助这一查询式接口，第三方后端可以在版本时间线上灵活地声明特性生效边界——例如决定 `haskell:more_monads` 在 2023 之后为 true、在 2023.1 之后回到 false——而无需维护一份庞大的 edition → 默认值映射表。后端的改动也因此被局部化：只需在确实改变某个默认值的位置修改谓词条件，而不必为每个新宣告的 edition 单独添加 `switch` 分支。

## Related Concepts
- [[concepts/Total Ordering of Editions|Total Ordering of Editions]]
- [[concepts/Language-scoped features|Language-scoped features]]
- [[concepts/Edition Proclamation|Edition Proclamation]]
- [[concepts/Backend Features|Backend Features]]
- [[concepts/Build Horizon|Build Horizon]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/Protobuf Editions|Protobuf Editions]]

## Mentions in Source
> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "This means that a backend can pick the default not by looking at the edition, but by asking 'is this proto older than this edition, where I introduced this default?'"

> **Source: [[sources/editions-edition-evolution|editions-edition-evolution]]**
> - "This means that a backend can pick the default not by looking at the edition, but by asking \"is this proto older than this edition, where I introduced this default?\""
> - "Thus, if I decide that `haskell:more_monads` becomes true in 2023, I simply ask `file.EditionIsLaterThan(\"2023\")`. If it becomes false in 2023.1, a future backend can ask `file.EditionIsBetween(\"2023\", \"2023.1\")`."