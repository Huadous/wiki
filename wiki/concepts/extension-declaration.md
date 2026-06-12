---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions]]"]
tags: [method]
aliases:
  - "扩展声明语法"
  - "extension declarations syntax"
  - "扩展字段预留"
---


# Extension Declaration

## 定义
扩展声明（Extension Declaration）是Protocol Buffers中用于预留扩展字段编号的语法机制，在Editions版本中引入。它允许消息类型在使用扩展字段时明确声明扩展字段的编号范围，从而防止其他开发者误用已预留的字段编号，解决扩展字段编号重用导致的向前/向后兼容性问题。该机制类似于保留字段（reserved）的语义，但专门针对扩展场景设计。

## 关键特征
- **字段编号预留**：通过明确声明扩展字段的范围，为未来的扩展预留字段编号，避免与其他扩展或消息字段冲突。
- **兼容性保障**：解决了扩展字段编号被意外重用导致的版本间不兼容问题。
- **声明式语法**：在消息类型定义中使用专门的声明语法，表达该消息支持扩展及其预留的编号范围。
- **与reserved的区分**：专门针对扩展字段，而非消息内部的保留字段，两者在语义和应用场景上有所区别。

## 应用
- **版本迁移**：在Protocol Buffers消息版本演进中，使用扩展声明确保旧版本消息与新扩展字段兼容。
- **多团队协作**：当不同团队或项目使用同一消息类型的扩展字段时，通过声明协调字段编号分配，避免冲突。
- **框架设计**：在基础框架或基础设施消息类型中预声明扩展范围，允许后续功能模块安全添加扩展字段。

## 相关概念
- [[concepts/field-number|field number]]
- [[concepts/reserved-field|reserved field]]
- [[concepts/Message-type|Message type]]
- [[concepts/wire-format|wire format]]

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/protoc|protoc]]

## 来源提及
- "Extension Declarations provide a mechanism for reserving extension fields." — [[sources/editions|editions]]
- "This has been a very easy mistake to make with extension fields for several reasons. Extension Declarations provide a mechanism for reserving extension fields." — [[sources/editions|editions]]