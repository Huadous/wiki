---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|Protobuf Editions 设计文档索引]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "standard"
aliases:
  - "Edition 命名规范"
  - "Edition Naming Rules"
---

## Description
Edition 命名是 Edition 生命周期管理的核心组成部分，决定了 Edition 在各语言中如何被识别、比较和发布。早期《Life of an Edition》文档提出了一种宽松的命名方案：使用「年份+可选修订号」的字符串形式，并通过拆分 `.` 后按「长度优先、字典序次之」的规则实现全序比较（例如 `9 < 10`）。然而，这种字符串方案在跨语言实现中存在解析复杂、可读性不一致等问题。新的命名方案转向使用 **Edition 枚举类型**，其设计目标包括：离散可控的合法值集合、简单可比较、跨语言一致、数量较少（约 100 个）且缓慢增长（约每年一个）。该决策涉及在可读性、解析复杂度与跨语言一致性之间的多维度权衡，并借鉴了 Calver（基于日历的版本命名）的思路，同时考虑了 Hyrum's Law 对版本标识稳定性的影响。文档明确指出，Edition 应当可以按数值方式比较，以便推导 Edition 之间的时间先后顺序。

## Related Concepts
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]
- [[concepts/edition-proclamation|Edition Proclamation]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/edition-enum|Edition Enum]]
- [[concepts/calver|Calver]]
- [[concepts/hyrums-law|Hyrum's Law]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/prototiller|Prototiller]]

## Mentions in Source
> **Source: [[sources/editions-readme|Protobuf Editions 设计文档索引]]**
> - "The following topics are in this repository:"
> - "[Edition Naming](edition-naming.md)"
> - "This directory contains historical design documents that describe plans for implementing Protobuf Editions."

> **Source: [[sources/editions-life-of-an-edition|Life of an Edition]]**
> - "(**Note:** The above edition ordering is updated in [Edition Naming](edition-naming.md).)"
> - "The total order is thus: the edition string is split on `'.'`. Each component is then ordered by `a.len < b.len && a < b`. This ensures that `9 < 10`, for example."

> **Source: [[sources/editions-life-of-an-edition|Life of an Edition]]**
> - No directly relevant information

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "One of the things Life of an Edition lays out is a very loose scheme for naming editions."
> - "We will document that these are intended to be comparable numerically for finding the time ordering of editions."