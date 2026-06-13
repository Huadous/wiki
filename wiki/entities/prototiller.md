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
- Aliases — Prototiller 被视为该方案的潜在受益者，可用于通过 proto 语言本身指定旧行为以统一处理
- Delimited encoding — Prototiller 与别名方案的结合被视为长期解决 group 字段 delimited 编码问题的理想途径
- Group-like fields — Prototiller 配合别名方案长期解决的目标之一

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