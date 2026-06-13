---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term]
aliases:
  - "local 关键字"
  - "局部符号关键字"
---


# local 关键字

## 定义

`local` 关键字是 Protocol Buffers (Protobuf) 中用于控制符号可见性的关键字，与文件级特性 `features.default_symbol_visibility` 配合使用。在 Edition 2024 中，可在消息或枚举定义前使用 `local` 关键字将其限制为私有（不可导出），从而覆盖文件级别的默认可见性设置。

## 关键特征

- **可见性控制**：将消息、枚举等顶层元素设为私有，不对外导出
- **特性协同**：与 [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]] 特性配合工作
- **覆盖文件级设置**：当文件级 `default_symbol_visibility` 设置为 `EXPORT_TOP_LEVEL` 时，使用 `local` 可使特定元素不导出
- **细粒度控制**：与 `export` 关键字共同提供逐元素的符号可见性精确控制
- **适用于顶层元素**：主要用于消息（message）和枚举（enum）定义前

## 应用

- **隐藏内部消息**：将仅供内部使用的消息类型标记为 `local`，防止被外部模块引用
- **API 封装**：在导出库中隐藏实现细节，只暴露公共接口
- **模块化设计**：配合文件级可见性策略，实现不同模块间的严格符号隔离
- **编译优化**：减少导出符号数量，可降低动态链接开销并提升编译效率

## 相关概念

- [[concepts/export-keyword|export keyword]]
- [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]]
- [[concepts/edition-2024|edition-2024]]
- [[concepts/feature-setting-scope|feature-setting-scope]]

## 相关实体

- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/google|Google]]

## 来源提及

- "use the local export keywords to set per-field behavior. " — [[protobuf/features|features]]
- "applying the local keyword overrides this" — [[protobuf/features|features]]
- "export message LocalMessage { ... }" — [[protobuf/features|features]]
- "The following sample shows how you can apply the feature to elements in your proto schema definition files: " — [[protobuf/features|features]]