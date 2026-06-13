---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-README.md]]"
tags:
  - "Stricter Schemas with Editions"
  - "Protobuf Editions"
  - "Feature gating"
  - "Identifier naming conventions"
  - "Reserved keywords"
  - "Name resolution in Protobuf"
  - "Nonempty package"
  - "Enum value uniqueness"
  - "Field number reservation"
  - "Implicit string concatenation"
  - "#optional escape syntax"
  - "Strict boolean options"
  - "Decimal field numbers"
  - "Package declaration position"
  - "Go-style name resolution"
  - "Unused imports"
  - "Contextual keywords"
aliases:
  - "Stricter Schemas with Editions"
  - "Editions 收紧 Schema 备忘录"
---

## 来源
- Original file: [[protobuf/editions-stricter-schemas-with-editions.md]]
- Ingested: 2026-06-13
- Additional source: [[protobuf/editions-README]] — 未提供直接相关信息

## 核心内容
本文档由 [[entities/mcy|mcy]] 撰写,于 2022-11-28 获批准,主要探讨如何利用 [[concepts/protobuf-editions|Protobuf Editions]] 机制系统性地收紧 [[entities/protobuf|Protobuf]] 语言中长期存在的宽松语法角落。作者指出,Protobuf 在标识符命名、关键字复用、package 声明、名称解析、枚举值、import、字段号、字符串拼接等多个位置允许的语法过于宽松,虽很少被实际使用,却显著增加了后端与运行时的实现复杂度。文档的核心方法论——[[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]],即通过 [[concepts/feature-gating|Feature gating]] 为每条 lint 引入一个布尔 feature,默认从 true 起步,并在未来 edition 中切换为 false,从而形成 ratchet(棘轮)式演化,实现语言的逐步收紧。

## 关键实体
- [[entities/mcy|mcy]] — 文档作者,Protobuf 社区贡献者
- [[entities/protobuf|Protobuf]] (Protocol Buffers) — 文档讨论的对象语言

## 关键概念
- [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]] — 文档核心议题,提议性方法论
- [[concepts/protobuf-editions|Protobuf Editions]] — 语言版本演进机制,本文的收紧载体
- [[concepts/feature-gating|Feature gating]] — feature 翻转的迁移机制
- [[concepts/identifier-naming-conventions|Identifier naming conventions]] — 强制 PascalCase/snake_case/SHOUTY_CASE 三类命名规范
- [[concepts/reserved-keywords|Reserved keywords]] — 关键字将彻底保留,不再允许作标识符
- [[concepts/name-resolution-in-protobuf|Name resolution in Protobuf]] — 名称解析的现状与改进方向
- [[concepts/nonempty-package|Nonempty package]] — 要求每个文件必须声明 package
- [[concepts/enum-value-uniqueness|Enum value uniqueness]] — 禁止枚举值别名
- [[concepts/field-number-reservation|Field number reservation]] — 以 `reserved N to max;` 声明下一可用字段号
- [[concepts/implicit-string-concatenation|Implicit string concatenation]] — 禁止相邻字符串隐式拼接
- [[concepts/#optional-escape-syntax|#optional escape syntax]] — 用于将关键字转义为标识符的语法
- [[concepts/strict-boolean-options|Strict boolean options]] — 布尔选项严格限制为 true/false
- [[concepts/decimal-field-numbers|Decimal field numbers]] — 字段号仅允许十进制字面量
- [[concepts/package-declaration-position|Package declaration position]] — package 声明应置于文件开头
- [[concepts/go-style-name-resolution|Go-style name resolution]] — 以 Go 风格替代 C++ 风格名称解析
- [[concepts/unused-imports|Unused imports]] — 禁止未使用的 import(沿用 Go 规则)
- [[concepts/contextual-keywords|Contextual keywords]] — 引入新关键字的渐进策略,参考 Rust editions

## 要点
- Protobuf 在标识符命名、关键字复用、package、名称解析、枚举值、import、字段号、字符串拼接等多个角落存在宽松语法,增加后端与运行时的实现成本。
- 文档建议通过 Editions 机制为每条 lint 引入一个布尔 feature,默认 true,在未来 edition 中切换为 false,形成 ratchet 式收紧。
- 标识符命名被收紧为 Message/Enum/Service/Method 使用 PascalCase、Field/package 组件使用 snake_case、Enum value 使用 SHOUTY_CASE,且仅支持 ASCII。
- 关键字将彻底保留,不再允许作标识符;同时引入 `[[concepts/#optional-escape-syntax|#optional]]` 转义语法;新关键字的引入参照 Rust 的 [[concepts/contextual-keywords|contextual keyword]] → reserved 升级路径。
- 名称解析方案建议从 C++ 风格转向 [[concepts/go-style-name-resolution|Go-style name resolution]],要求名称要么是单标识符要么是完整限定名。
- Package 声明应强制非空,且应作为文件中 syntax/edition 之后的第一条声明;import 应遵循 Go 规则,要求每个非 public import 至少被使用一次。
- 枚举值应禁止别名(共享数值);message 应以 `reserved N to max;` 作为第一个 production 声明下一可用字段号。
- 布尔选项严格限制为 true/false;字段号仅允许十进制字面量;相邻字符串的隐式拼接应被禁止。
- 文档明确说明这是关于 Editions 用例的备忘录,并非正式的设计文档。