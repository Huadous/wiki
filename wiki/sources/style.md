---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[protobuf/style.md]]"
tags: [Standard File Formatting, File Structure, Identifier naming styles, Package, Message Names, Field Names, Oneof Names, Enums, Services, Required Fields, Groups, Avoid confusing relative packages on field types, Avoid Field Names and Oneof Names that Could Potentially Cause Collisions, Underscores in Identifiers, Enum Value Prefixing]
aliases: ["Protobuf 样式指南", "Protocol Buffers 编码规范"]
---

# Style Guide | Protocol Buffers Documentation - Summary

## 来源
- Original file: [[protobuf/style.md]]
- Ingested: 2026-06-12

## 核心内容

本文档是 [[entities/protocol-buffers|Protocol Buffers]] 官方发布的样式指南，旨在为开发者编写 `.proto` 文件提供统一的命名和格式规范。指南涵盖标准文件格式（80字符行宽、2空格缩进、双引号字符串）、[[concepts/file-structure|文件结构]]（许可证、概述、语法、包、导入、文件选项以及其余内容）以及完整的命名规范体系。在标识符风格上，文档明确定义了 [[concepts/titlecase|TitleCase]]、[[concepts/lower_snake_case|lower_snake_case]]、[[concepts/upper_snake_case|UPPER_SNAKE_CASE]] 和 [[concepts/camelcase|camelCase]] 四种命名方式，并规定 `.proto` 文件中应使用前三种而非 camelCase。具体规则包括：[[concepts/package-naming|包名]]使用点分隔的 lower_snake_case、[[concepts/message-naming|消息名]]使用 TitleCase、[[concepts/field-naming|字段名]]使用 snake_case（repeated 字段用复数）、[[concepts/enum-naming|枚举类型名]] TitleCase 且[[concepts/enum-value-prefixing|枚举值]] UPPER_SNAKE_CASE（第一个值以 `_UNSPECIFIED` 或 `_UNKNOWN` 结尾）、[[concepts/service-naming|服务名]]和 RPC 方法名使用 TitleCase。此外，指南强烈不推荐使用 [[concepts/required-fields|required 字段]]和 [[concepts/groups|groups 语法]]，指出这些特性不利于长期模式演化。

## 关键实体

- [[entities/protocol-buffers|Protocol Buffers]] — 本指南所规范的序列化框架，文档为其官方样式指南，为开发者编写 `.proto` 文件提供标准和最佳实践。

## 关键概念

- [[concepts/titlecase|TitleCase]] — 大驼峰命名风格，用于消息名、枚举类型名、服务名和方法名。
- [[concepts/lower_snake_case|lower_snake_case]] — 小写下划线命名风格，用于包名、字段名、文件名和 oneof 名。
- [[concepts/upper_snake_case|UPPER_SNAKE_CASE]] — 大写蛇形命名风格，用于枚举值。
- [[concepts/camelcase|camelCase]] — 小驼峰命名风格，明确说明不在 `.proto` 文件中直接使用。
- [[concepts/file-structure|文件结构]] — 标准组织顺序：许可证、概述、语法、包、导入、文件选项、其余内容。
- [[concepts/package-naming|包命名规范]] — 点分隔的 lower_snake_case 序列，不包含大写字母，不耦合目录路径，不使用 Java 风格。
- [[concepts/message-naming|消息命名规范]] — 使用 TitleCase。
- [[concepts/field-naming|字段命名规范]] — 使用 snake_case，repeated 字段复数化。
- [[concepts/enum-naming|枚举命名规范]] — 类型名 TitleCase，值 UPPER_SNAKE_CASE，第一个值以 `_UNSPECIFIED` 或 `_UNKNOWN` 结尾。
- [[concepts/service-naming|服务命名规范]] — 使用 TitleCase。
- [[concepts/required-fields|required 字段]] — 被强烈弃用，不利于模式演化，可在 edition 2023 中通过 LEGACY_REQUIRED 兼容。
- [[concepts/groups|groups 语法]] — 被弃用，推荐使用嵌套消息定义和 `message_encoding` 特性兼容。
- [[concepts/enum-value-prefixing|枚举值前缀]] — 建议对枚举值进行前缀以避免名称冲突。
- [[concepts/relative-package-references|相对包引用]] — 避免使用混淆的相对包引用，推荐明确写出完整包名。
- [[concepts/underscores-in-identifiers|标识符下划线规则]] — 禁止首尾下划线，下划线后必须紧跟字母。
- [[concepts/field-presence-feature-legacy_required|Field Presence 特性 (LEGACY_REQUIRED)]] — 控制字段存在性语义，兼容 proto2 required 字段。
- [[concepts/message_encoding-feature|消息编码特性]] — 替代 groups 语法，通过 delimited 表示保持线格式兼容。
- [[concepts/avoiding-language-keywords-in-protobuf-identifiers|避免语言关键字冲突]] — 避免使用 `has_`、`get_`、`set_`、`clear_` 前缀、`_value` 后缀以及 `descriptor` 名称。

## 要点

- `.proto` 文件应遵循统一格式规范：80字符行宽、2空格缩进、双引号字符串。
- 文件结构有固定顺序：许可证→概述→语法→包→导入（排序）→文件选项→其余内容。
- 标识符命名风格使用 TitleCase、lower_snake_case、UPPER_SNAKE_CASE，避免在 `.proto` 文件中使用 camelCase。
- 消息名使用 TitleCase，字段名使用 snake_case（repeated 用复数），枚举类型名 TitleCase 且值 UPPER_SNAKE_CASE。
- 强烈不推荐使用 required 字段和 groups 语法，因其影响长期模式演化。
- 枚举值应使用前缀以避免跨枚举名称冲突，建议使用枚举类型名转换的 UPPER_SNAKE_CASE 作为前缀。
- 建议在引用其他包的类型时明确写出完整包名，避免使用相对包引用。
- 避免在标识符中使用会导致生成代码冲突的前缀/后缀，如 `has_`、`get_`、`set_`、`clear_`、`_value` 和 `descriptor`。