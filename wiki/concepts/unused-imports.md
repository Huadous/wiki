---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]"]
tags: [standard]
aliases:
  - "未使用的导入"
  - "unused import check"
---


# Unused imports

## 定义
Unused imports 是指 Protobuf 中允许导入文件但不在该文件中实际使用任何来自该导入的类型的情况。文档提议采用 Go 语言的规则，要求所有非公开的导入必须被使用（即每个导入至少提供文件中引用的一种类型）。该规则属于导入卫生范畴，目的是保持 `.proto` 文件的整洁性与可维护性，避免出现冗余的导入声明。此限制通过特性 `features.allow_unused_imports` 实现，按惯例从 `true` 切换到 `false`，以便在未来的 edition 中强制生效。

## 关键特征
- 借鉴 Go 语言的导入使用规则：所有非公开导入必须在文件中至少提供一种被引用的类型。
- 属于"导入卫生"（import hygiene）约束，旨在消除无实际用途的 `import` 语句。
- 通过特性开关 `features.allow_unused_imports` 控制，默认值为 `true`，按惯例在后续 edition 中切换为 `false` 以强制启用。
- 属于 Editions 体系下逐步收紧 Schema 的标准之一。

## 应用
- 在 Protobuf Editions 中以特性门控方式启用/禁用未使用导入检查。
- 用于维护大规模 `.proto` 文件集合的整洁度，减少冗余声明带来的理解成本。
- 作为编辑器与 lint 工具提示"死导入"的依据，辅助开发者清理不再需要的依赖。

## 相关概念
- [[concepts/Feature gating]]
- [[concepts/Protobuf Editions]]

## 相关实体
- [[entities/Protocol Buffers|Protobuf]]

## 来源提及
- We should adopt the Go rule that all non-public imports are used (i.e, every import provides at least one type referred to in the file). — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]
- We would introduce a feature like `features.allow_unused_imports`, which would switch from true to false. — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]