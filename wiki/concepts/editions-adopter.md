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
  - "Editions 升级工具"
  - "editions upgrade tool"
  - "Editions upgrader"
  - "Editions 升级工具"
  - "editions upgrade tool"
---

## Description
Editions adopter 是 protoc 内置的命令行升级工具，专注于处理尚未迁移到 Editions 模式的旧式 proto 文件。当用户对 proto2 或 proto3 文件运行 `protoc --upgrade-edition` 时，该工具会分析原文件与最新 edition 之间的差异，并自动补全 `edition` 字段以及迁移所必需的 `features.*` 选项，确保升级前后文件语义保持一致。在转换过程中，adopter 会隐式调用 Features GC，对冗余 features 进行最小化处理，最终以经过特性最小化的 ProtoChangeSpec 格式输出结果。该工具与 Editions upgrader 形成互补——adopter 负责从 proto2/proto3 跨越到 Editions 模式，而 upgrader 则在已是 Editions 模式的文件之间进行版本迭代。在 Edition Zero 等大规模迁移项目中，adopter 作为关键自动化工具被用于批量处理大量遗留 schema 文件，为 schema 生产者提供了一种平滑、可控且保持行为兼容的过渡机制。

## Related Concepts
- [[concepts/editions-upgrader|Editions upgrader]]
- [[concepts/features-gc|Features GC]]
- [[concepts/protochangespec|ProtoChangeSpec]]
- [[concepts/edition-zero|Edition Zero]]

## Related Entities
- [[entities/protoc|protoc]]

## Mentions in Source
> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "The editions "adopter". Running protoc --upgrade-edition -I... file.proto figure out how to update file.proto from proto2 or proto3 to the latest edition, adding features as necessary."
> - "It will emit this information as a ProtoChangeSpec, implicitly running features GC."