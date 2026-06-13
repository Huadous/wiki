---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "legacy_string feature"
  - "features.(proto.cpp)/legacy_string"
---


# features.(proto.cpp).legacy_string

## 定义
`features.(proto.cpp).legacy_string` 是 Protobuf Editions 体系中一个语言作用域（language-scoped）的布尔型特性（boolean feature），仅作用于 C++ 后端。该特性默认值为 `true`，用于控制 `string` 或 `bytes` 类型字段的访问器（accessors）返回值的表示形式：当为 `true` 时保留旧版行为，访问器返回 `const std::string&`；当为 `false` 时，访问器返回表现上不透明（representationally opaque）的类型，例如 `absl::string_view`，从而可能带来被遗漏的优化机会。

## 关键特征
- 作用域限定为语言层面，仅影响 C++ 代码生成，不影响其他语言后端。
- 类型为布尔型，默认值为 `true`（即保持旧版行为）。
- 作用的字段类型为 `string` 或 `bytes`。
- 启用（设为 `false`）后，访问器返回表现上不透明的类型（如 `absl::string_view`），类比 `ctype = STRING_PIECE` 的语义。
- 可以在文件（file）或字段（field）粒度上设置，覆盖范围灵活。
- 迁移代价：用户代码中原先假设访问器结果可直接赋值为 `std::string` 的地方需要相应修改。

## 应用
- 用于在 Protobuf Editions 框架下将 C++ 访问器从返回 `const std::string&` 迁移到返回 `absl::string_view` 等不透明表示。
- 当设 `false` 时，启用此前被遗漏的优化机会（missed optimizations）。
- 作为一项大型变更（Large-scale Change），需要分阶段把现有 schema 和用户代码逐步迁移到新的不透明访问器形式。
- 与 Editions 中其他特性（如 `ctype = STRING_PIECE`）协同，作为字符串/字节字段表示层的演进手段。

## 相关概念
- [[concepts/language-scoped-features|Language-scoped features]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/feature|Feature]]

## 相关实体
No related entities

## 来源提及
- We would like to migrate all of them to return `absl::string_view`, a-la `ctype = STRING_PIECE`. — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- To do this, we introduce `features.(proto.cpp).legacy_string`[^1], a boolean feature by default true. When false on a field of appropriate type, it does the needful and causes accessors to become representationally opaque. — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]