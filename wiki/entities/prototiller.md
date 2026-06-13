---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/features]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "product"
aliases:
  - "Prototiller 工具"
  - "prototiller"
---

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]] — Prototiller 是 Protocol Buffers 生态系统中的工具
- [[entities/protoc|protoc]] — 同为 Protocol Buffers 工具链中的命令行工具
- [[entities/google|google]] — Protocol Buffers 的维护者和 Prototiller 的潜在发布方
- [[entities/mkruskal-google|mkruskal-google]] — Legacy Syntax Editions 提案的相关人员/作者
- [[entities/mcy|mcy]] — Edition Zero 枚举字段封闭性特性设计文档的相关人员/作者

## Related Concepts
- [[concepts/google-protobuf-any|google-protobuf-any]] — 特性设置中可能使用到的消息类型
- [[concepts/text-format|text-format]] — 与 proto 文件文本格式相关的概念
- Protocol Buffers Editions — Prototiller 的目标迁移格式
- Edition 2024 — Prototiller 支持的目标版本之一
- Edition 2023 — Prototiller 支持的目标版本之一，Legacy Syntax Editions 提案中明确讨论的转换目标
- [[concepts/minimum-required-edition|Minimum Required Edition]] — Prototiller 升级 edition 的行为在最低必需版本机制下被归类为非破坏性变更
- Legacy Syntax Editions — Prototiller 处理 syntax 向 edition 转换的核心背景提案
- proto2 — Prototiller 迁移的源语法之一，被 Legacy Syntax Editions 提案视为特殊 edition
- proto3 — Prototiller 迁移的源语法之一，被 Legacy Syntax Editions 提案视为特殊 edition
- Feature Inference — 与 Prototiller 默认转换策略相关的概念
- Resolved Features — Prototiller 转换保证不变的运行时行为层面
- Unresolved Features — Prototiller 转换会改变的 proto 内部表示层面
- Large-scale Change — Prototiller 行为保持性所支撑的 Editions 推广策略
- Hyrum's Law — 用户访问 unresolved features 时会引发的兼容性问题
- Aliases — Prototiller 被视为该方案的潜在受益者，可用于通过 proto 语言本身指定旧行为以统一处理
- Delimited encoding — Prototiller 与别名方案的结合被视为长期解决 group 字段 delimited 编码问题的理想途径
- Group-like fields — Prototiller 配合别名方案长期解决的目标之一
- Edition Zero Features — Prototiller 向 Edition Zero 迁移所涉及的特性集合
- legacy_treat_enum_as_closed — Prototiller 在 Edition Zero 迁移中需条件性下发的特性标志
- Enum Field Closedness — Prototiller 在迁移中需要特殊处理的枚举字段封闭性特性
- Edition enum — Prototiller 已被验证可正确实现字符串 Edition 名称到 Edition 枚举类型的解析
- Edition Naming — Prototiller 在该提案中被引用作为解析层实现可行性的证据
- descriptor.proto — Edition 枚举定义所在的 proto 文件，与 Edition 名称解析相关

## Mentions in Source

> **Source: [[sources/features|features]]**
> - "Prototiller is a command-line tool that updates proto schema configuration files between syntax versions and editions."
> - "It hasn't been released yet, but is referenced throughout this topic."
> - "After running Prototiller, the equivalent code might look like this:"
> - "edition = \"2024\"; enum Corge { option features.enum_type = CLOSED; ... }"

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "Upgrading the specified edition of a file via Prototiller."
> - "In particular, the following changes should keep the minimum edition constant, with all other things unchanged:"

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "A separate issue is how Prototiller will support the conversion of syntax to edition 2023."
> - "For features it knows about, we can hardcode defaults into the transforms."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "Fixes all of the problems mentioned above"
> - "Allows us to specify the old behavior using the proto language, which allows it to be handled by Prototiller"
> - "We've discussed aliases a lot mostly in the context of `Any`, but they would be useful for any encoding scheme that locks down field/message names."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "we *expect* that people are only making decisions based on resolved features, and therefore that Prototiller transformations are behavior-preserving (despite changing the unresolved features)."
> - "If people have easy access to unresolved features though, we can expect a lot of Hyrum's law issues slowing down these large-scale changes."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "When migrating from syntax to edition zero, Prototiller will need to know all used languages to make the upgrade a trivial change (this is already the case for other edition upgrades)."
> - "Additionally, we would like to make special dispensation in migration tooling for this field"

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "Might be a bit tricky to implement in the parser (but Prototiller does this just fine)"
> - "No directly relevant information"