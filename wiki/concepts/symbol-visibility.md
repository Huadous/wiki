---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/features.md]]"]
tags: [term]
aliases:
  - "default symbol visibility"
  - "符号可见性"
  - "Symbol Visibility"
---


# Symbol Visibility

## 定义
Symbol Visibility（符号可见性）是指在 Protocol Buffers（Protobuf）模式中，消息（message）和枚举（enum）类型在被其他 `.proto` 文件导入时的可见性控制机制。在 Protobuf Edition 2024 中，符号可见性的默认行为从完全可见（`EXPORT_ALL`）演进为更精细的分层控制：顶层符号默认导出，嵌套符号默认 local（`EXPORT_TOP_LEVEL`）。用户可通过 `features.default_symbol_visibility` 特性设置文件级默认值，也可使用 `local` 和 `export` 关键字在逐元素级别精确控制每个符号的可见性。

## 关键特征
- **默认行为演进**：从 `EXPORT_ALL`（全部可见）演进为 `EXPORT_TOP_LEVEL`（顶层可见），默认情况下不再暴露嵌套符号。
- **文件级默认值**：可通过 `features.default_symbol_visibility` 特性设置整个文件的符号可见性默认值。
- **逐元素控制**：支持在每个消息、枚举或嵌套元素上使用 `local` 和 `export` 关键字进行精细控制。
- **STRICT 模式约束**：`STRICT` 值规定嵌套类型不能被导出（`message { enum {} reserved 1 to max; }` 情况除外），并将在未来版本中成为默认行为。
- **API 稳定性**：属于 Protobuf Editions 体系下的特性设置之一。

## 应用
- **避免意外暴露内部类型**：在大型 Protobuf 工程中防止内部数据结构被外部 `.proto` 文件意外引用，降低耦合度。
- **减小最终二进制体积**：通过隐藏不必要的符号，可缩减生成代码的体积，提升编译和链接效率。
- **API 边界管理**：在多团队协作的项目中，明确划分公共 API 与内部实现的边界。
- **渐进式迁移**：从 proto2/proto3 迁移到 Edition 2024 时，按需调整符号可见性以适配新的语义。

## 相关概念
- [[concepts/features-default-symbol-visibility|features.default_symbol_visibility]]
- [[concepts/protocol-buffers-editions|Protocol Buffers Editions]]
- [[concepts/edition-2024|Edition 2024]]

## 相关实体
无相关实体。

## 来源提及
- "This feature enables setting the default visibility for messages and enums, making them available or unavailable when imported by other protos." — [[protobuf/features|features]]
- "In addition to setting the defaults for the entire file, you can use the local and export keywords to set per-field behavior." — [[protobuf/features|features]]