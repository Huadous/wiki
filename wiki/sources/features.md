---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
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
  - "Feature Settings for Editions"
  - "Protobuf Editions 功能设置"
---

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]] — Google 开发的结构化数据序列化框架，Editions 功能所属的总产品
- [[entities/prototiller|Prototiller]] — 尚未正式发布的命令行工具，用于在不同 proto 语法版本与 Editions 之间自动转换配置文件

## 关键概念
- [[concepts/protocol-buffers-editions|Protocol Buffers Editions]] — 版本化的模式定义系统，通过特性设置替代隐式行为
- [[concepts/edition-2023|Edition 2023]] — Editions 体系的首个主要落地版本
- [[concepts/edition-2024|Edition 2024]] — 最新已发布版本，引入了多项新特性与默认值调整
- [[concepts/feature-scope|Feature Scope]] — 特性设置的四个作用域层级（文件级、非嵌套级、嵌套级、最低级）
- [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]] — 控制消息和枚举的默认导出可见性
- [[concepts/features-enforce_naming_style|features.enforce_naming_style]] — 强制执行 Protobuf 风格指南的命名约定
- [[concepts/features-enum_type|features.enum_type]] — 控制[[concepts/open-enum|开放]]与[[concepts/closed-enum|封闭]]枚举行为
- [[concepts/features-field_presence|features.field_presence]] — 控制[[concepts/field-presence|字段存在性]]跟踪方式
- [[concepts/field-presence|Field Presence]] — 字段存在性跟踪的核心概念
- [[concepts/symbol-visibility|Symbol Visibility]] — 符号可见性控制机制
- [[concepts/naming-style-enforcement|Naming Style Enforcement]] — 命名风格标准化机制
- [[concepts/required-field|Required Field]] — features.field_presence 的 LEGACY_REQUIRED 语义
- [[concepts/open-enum|Open Enum]] — features.enum_type 的 OPEN 取值
- [[concepts/closed-enum|Closed Enum]] — features.enum_type 的 CLOSED 取值
- [[concepts/proto2|proto2]] — 早期语法版本，作为功能对照基准
- [[concepts/proto3|proto3]] — 较新的语法版本，作为功能对照基准

## 要点
- [[concepts/protocol-buffers-editions|Protocol Buffers Editions]] 通过版本化（2023、2024）和特性设置替代 [[concepts/proto2|proto2]] / [[concepts/proto3|proto3]] 语法，提供更灵活、可演进的模式定义方式
- 特性设置可在四个 [[concepts/feature-scope|作用域]]（文件级、非嵌套级、嵌套级、最低级）中应用，低作用域设置可覆盖高作用域设置
- [[concepts/edition-2024|Edition 2024]] 引入了 [[concepts/features-default_symbol_visibility|features.default_symbol_visibility]] 和 [[concepts/features-enforce_naming_style|features.enforce_naming_style]] 两个关键特性，分别将默认值调整为 EXPORT_TOP_LEVEL 和 STYLE2024
- [[concepts/features-field_presence|features.field_presence]] 提供 [[concepts/required-field|LEGACY_REQUIRED]]、EXPLICIT 和 IMPLICIT 三种语义，分别对应 [[concepts/proto2|proto2]] required、proto2/2023+ 可选以及 [[concepts/proto3|proto3]] 默认行为
- [[concepts/features-enum_type|features.enum_type]] 控制 [[concepts/open-enum|开放（OPEN，Edition 默认）]] 与 [[concepts/closed-enum|封闭（CLOSED，proto2 默认）]] 枚举行为，影响超出定义范围值的处理方式
- [[entities/prototiller|Prototiller]] 是尚未发布的命令行工具，可自动将旧语法 proto 文件迁移到新 Edition 及其等价的特性设置