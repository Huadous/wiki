---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions]]"
  - "[[protobuf/editions.md]]"
tags:
  - "method"
aliases:
  - "扩展声明语法"
  - "extension declarations syntax"
  - "扩展字段预留"
  - "Extension Declarations"
  - "扩展声明语法"
  - "extension declarations syntax"
  - "扩展字段预留"
---

## Description
扩展声明是 Protocol Buffers Editions 版本中引入的语法机制，用于在消息类型中明确声明扩展字段的编号范围。其设计动机源于一个长期存在的实践痛点：扩展字段是开发者最容易犯编号重用错误的地方之一，历史上由此引发的向前/向后兼容性问题屡见不鲜。该机制通过声明式语法预留出一段扩展字段编号，使其他开发者能够清楚地识别该消息已声明的扩展范围，从而避免意外冲突。在语义上，扩展声明与消息内部用于保留字段的 `reserved` 关键字相似，但作用对象专门限定为扩展字段，使用场景更为聚焦。作为 Protocol Buffers 防止字段编号被误用、保障消息兼容性工具集的重要组成部分，扩展声明常用于版本迁移、多团队协作以及基础框架消息类型的扩展规划中。

## Related Concepts
- [[concepts/field-number|field number]]
- [[concepts/reserved-field|reserved field]]
- [[concepts/Message-type|Message type]]
- [[concepts/wire-format|wire format]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source
> **Source: [[sources/editions|editions]]**
> - "Extension Declarations provide a mechanism for reserving extension fields."
> - "This has been a very easy mistake to make with extension fields for several reasons. Extension Declarations provide a mechanism for reserving extension fields."