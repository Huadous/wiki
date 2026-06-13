---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-naming|editions-edition-naming]]"]
tags: [standard]
aliases:
  - "Edition Enum 方案"
  - "Edition enum 提案"
  - "Protobuf Edition Enum"
---


# Edition enum

## 定义
Edition enum 是本文档推荐的 Edition 表示方案：使用 Protocol Buffers 的 `enum` 类型来定义所有合法的 Edition 值（例如 `EDITION_2023 = 1`、`EDITION_2024 = 2` 等）。在 `.proto` 源文件中，Edition 仍以字符串形式书写（如 `edition = "2023"`），但解析器会迅速将其转换为对应的枚举值，所有后续代码均以枚举形式处理 Edition。

## 关键特征
- **内部使用枚举表示**：所有合法的 Edition 值由 Protocol Buffers 的 `enum` 类型集中定义，源代码层面的字符串会被解析器即时转换为枚举常量。
- **整数比较替代版本号字符串比较**：Edition 之间的比较退化为简单的整数比较，不需要再按年份或字符串解析。
- **自动拒绝未知版本**：由于 `enum` 类型天然封闭，解析器在遇到未声明的 Edition 时即可直接报错，而无需依赖字符串匹配。
- **摆脱 calver 命名风格**：不再使用类似 `2023`、`2024` 这样的公历版本（calendar versioning）来标识 Edition，使得版本生命周期与命名解耦。
- **简化文档表述**：由于 Edition 是有限的、可枚举的集合，不再需要为修订版本维护复杂文档，文档负担显著降低。

## 应用
- 在 Protocol Buffers 编译器内部，用 `enum` 类型定义所有 Edition 标识，使解析器、代码生成器以及运行时代码统一使用枚举值进行分支和比较。
- 用于 [[sources/editions-life-of-an-edition|Life of an Edition]] 流程中：解析 `.proto` 时将字符串 Edition 转换为枚举值，再传递到后续的 FeatureSet 处理管线。
- 为 [[concepts/edition|Edition]]、[[concepts/edition-naming|Edition Naming]] 等概念提供底层的标准化标识机制，是 [[concepts/descriptor.proto|descriptor.proto]] 中 Edition 字段类型的推荐实现方式。
- 在 [[entities/prototiller|Prototiller]] 等 Schema 生产工具链中，将 Edition 表示统一为枚举常量，避免重复解析字符串。

## 相关概念
- [[concepts/edition|Edition]]
- [[concepts/edition-naming|Edition Naming]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/feature-set|FeatureSet]]

## 相关实体
- [[entities/prototiller|Prototiller]]

## 来源提及
- "The simplest solution here is to just make an Edition enum for specifying the edition." — [[sources/editions-edition-naming|editions-edition-naming]]
- "Edition comparison becomes even simpler, as it's just an integer comparison" — [[sources/editions-edition-naming|editions-edition-naming]]