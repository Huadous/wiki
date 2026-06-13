---
type: source
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "features.default_symbol_visibility"
  - "features.enforce_naming_style"
  - "features.enum_type"
  - "features.field_presence"
  - "Protobuf Editions"
  - "Feature setting scope"
  - "Edition 2024"
  - "Edition 2023"
  - "proto2"
  - "proto3"
  - "export keyword"
  - "local keyword"
aliases:
  - "Protocol Buffers Editions 特性设置文档"
  - "Protobuf Features 文档"
---

## Feature Settings for Editions (Protocol Buffers 文档) - Summary

### 来源
- Original file: [[protobuf/features.md]]
- New source: [[protobuf/editions-what-are-protobuf-editions]]
- Ingested: 2026-06-12

### 核心内容
本文档是 [[concepts/protobuf-editions|Protobuf Editions]] 的官方特性配置指南，详细介绍了如何通过特性设置（Feature Settings）在 Editions 中保留 [[concepts/proto2|proto2]] 或 [[concepts/proto3|proto3]] 的行为。文档重点阐述了四个核心特性：[[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]（控制符号导出可见性）、[[concepts/features-enforce_naming_style|features-enforce_naming_style]]（强制命名规范）、[[concepts/enum-type|enum-type]]（枚举类型行为、开闭枚举）以及 [[concepts/features-field_presence|features-field_presence]]（字段存在性跟踪）。每个特性均详细说明了可选值、适用范围及默认变化。此外还介绍了 [[concepts/feature-setting-scope|feature-setting-scope]] 的层级结构以及 [[entities/prototiller|Prototiller]] 工具（尚未发布）在迁移中的作用。文档旨在帮助用户理解 [[concepts/edition-2024|edition-2024]] 和 [[concepts/edition-2023|edition-2023]] 的默认行为差异，并正确配置特性以避免盲目复制。

### 关键实体
- [[entities/prototiller|Prototiller]] — 用于语法版本与 Editions 之间转换的命令行工具（尚未正式发布），文档中用于演示迁移后的等效代码。

### 关键概念
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]] — 控制消息和枚举在导入时的可见性，值包括 EXPORT_ALL、EXPORT_TOP_LEVEL、LOCAL_ALL、STRICT
- [[concepts/features-enforce_naming_style|features-enforce_naming_style]] — 强制命名规范以确保往返兼容性，值包括 STYLE2024、STYLE_LEGACY
- [[concepts/enum-type|enum-type]] — 处理未定义枚举值的行为，值包括 CLOSED（闭枚举）、OPEN（开枚举）
- [[concepts/features-field_presence|features-field_presence]] — 字段存在性跟踪，值包括 LEGACY_REQUIRED、EXPLICIT、IMPLICIT
- [[concepts/feature-setting-scope|feature-setting-scope]] — 特性应用层级：文件级、非嵌套级、嵌套级、最低级
- [[concepts/edition-2024|edition-2024]] — 引入 EXPORT_TOP_LEVEL 默认可见性与 STYLE2024 严格命名风格
- [[concepts/edition-2023|edition-2023]] — 保持 legacy 命名风格与 EXPORT_ALL 默认导出
- [[concepts/proto2|proto2]] — 默认 CLOSED 枚举、EXPLICIT 字段存在性
- [[concepts/proto3|proto3]] — 默认 OPEN 枚举、IMPLICIT 字段存在性
- [[concepts/export-关键字|export 关键字]] — 在定义前使用的符号导出关键字，覆盖文件级可见性
- [[concepts/local-keyword|local-keyword]] — 限制符号私有的关键字，与 export 配合使用

### 要点
- Protobuf Editions 提供了可配置的特性来覆盖默认行为，以保留 [[concepts/proto2|proto2]] 或 [[concepts/proto3|proto3]] 的兼容性
- 四个核心特性均具有明确的可选值和适用范围，可在不同层级上覆盖设置
- [[concepts/edition-2024|edition-2024]] 相比 [[concepts/edition-2023|edition-2023]] 改变了默认符号可见性和命名风格
- 特性设置按层级生效：文件级 < 非嵌套级 < 嵌套级 < 最低级（字段等），下级覆盖上级
- [[entities/prototiller|Prototiller]] 工具尚未发布，但展示了从旧语法向 Editions 的自动化迁移路径
- export 和 local 关键字提供了对符号可见性的细粒度控制，无需修改文件级别的默认设置

### 补充信息（来自 editions-what-are-protobuf-editions 文档）
- Protobuf Editions 的核心目的是统一 proto2 和 proto3 的语法差异，通过特性设置实现向后兼容性，同时为新功能（如可选字段、开闭枚举、自定义选项等）提供统一的语法基础。
- 特性设置不仅限于文档中列举的四个核心特性，还包括其他功能（如 map 类型、分组字段等）的配置，但文档重点覆盖了 Edition 2023 和 Edition 2024 之间默认值有变化的特性。
- 特性设置可在多个层级上配置，包括文件级、消息级、字段级和枚举值级，这种层级结构允许用户精确控制每个元素的特定行为，而无需全局修改。