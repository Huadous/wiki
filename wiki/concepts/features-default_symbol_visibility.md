---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/features]]"
tags:
  - "term"
aliases:
  - "符号默认可见性特性"
  - "default-symbol-visibility feature"
  - "export keyword"
  - "符号默认可见性特性"
  - "default-symbol-visibility feature"
---

## Description
`features.default_symbol_visibility` 控制 proto 文件中消息和枚举的默认导出行为，决定哪些符号在跨文件导入时可见。该特性提供四个可选值：`EXPORT_ALL`（导出所有符号，包括嵌套类型）、`EXPORT_TOP_LEVEL`（仅导出顶层符号，Edition 2024 默认值）、`LOCAL_ALL`（所有符号本地化）和 `STRICT`（更严格的本地化，嵌套类型不能导出）。从 Edition 2024 开始，新增了 `export` 关键字，允许在单个消息或枚举定义前覆盖文件级别的默认设置。例如，当文件级设为 `LOCAL_ALL` 时，使用 `export message LocalMessage { ... }` 可使该消息变为可导出。关键字 `export` 提供了从文件级默认到消息级的细粒度符号导出控制，能够减少死符号并缩小二进制体积。该特性在版本间行为有差异：Edition 2024 及之后默认行为为 `EXPORT_TOP_LEVEL`，而 Edition 2023 及之前版本（包括 proto2/proto3）默认导出所有符号。`export` 关键字是 Protobuf 版本中用于控制符号可见性的关键字，与 `features.default_symbol_visibility` 特性配合使用，用于设置每个字段的行为。

## Related Concepts
- [[concepts/features-field_presence|字段存在性特性]]
- [[concepts/features-enforce_naming_style|命名风格强制特性]]
- [[concepts/feature-setting-scope|特性设置作用域]]
- [[concepts/edition-2024|2024 Edition]]
- [[concepts/features-default_symbol_visibility|符号默认可见性特性]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc compiler]]
- [[entities/grpc|gRPC 框架]]

## Mentions in Source
- "This feature enables setting the default visibility for messages and enums, making them available or unavailable when imported by other protos." — [[sources/features|features]]
- "Use of this feature will reduce dead symbols in order to create smaller binaries." — [[sources/features|features]]
- "Values available: EXPORT_ALL, EXPORT_TOP_LEVEL, LOCAL_ALL, STRICT." — [[sources/features|features]]
- "Added in: Edition 2024" — [[sources/features|features]]
- "use the local export keywords to set per-field behavior." — [[sources/features|features]]
- "export message LocalMessage { ... }" — [[sources/features|features]]
- "applying the local keyword overrides this" — [[sources/features|features]]
- "enabling the export keyword overrides the default" — [[sources/features|features]]