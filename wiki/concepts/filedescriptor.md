---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-feature-enum-field-closedness]]"]
tags: [term]
aliases:
  - "FileDescriptor class"
  - "FileDescriptor 类"
---


# FileDescriptor

## 定义
FileDescriptor 是 Protocol Buffers API 中的一个类,表示一个 `.proto` 文件。它通过类似 `SYNTAX_PROTO2` 的常量提供该文件所使用的语法版本信息。在本文档的上下文中,FileDescriptor 被用来确定一个 `.proto` 文件使用的是 [[concepts/proto2|proto2]] 还是 [[concepts/proto3|proto3]] 语法,这在历史上是判定枚举字段应被当作开放(开放枚举)还是封闭(封闭枚举)处理的依据。文档示例代码使用 `file().syntax() == FileDescriptor::SYNTAX_PROTO2` 来检查枚举字段是否处于遗留封闭语义的上下文中。

## 关键特征
- 属于 Protocol Buffers 描述符(descriptor)API 中的核心类,用于在运行时访问 `.proto` 文件的元信息。
- 提供 `syntax()` 等方法返回文件的语法版本常量(如 `SYNTAX_PROTO2`、`SYNTAX_PROTO3`)。
- 是 [[concepts/FieldDescriptor|FieldDescriptor]] 和 [[concepts/EnumDescriptor|EnumDescriptor]] 的容器,通过 `file()` 接口可获取到对应的 FileDescriptor 实例。
- 在 Editions 演进过程中,被用作判定"是否处于 proto2 遗留封闭语义"的运行时检查手段。
- 与 [[concepts/legacy_treat_enum_as_closed|legacy_treat_enum_as_closed]] 特性强相关:历史上 proto2 文件中的枚举默认被视为封闭集合。

## 应用
- 在运行时判断某个 `.proto` 文件的语法版本,从而决定枚举字段的开放或封闭语义。
- 在 Editions 设计中,作为过渡期向后兼容机制的一部分,用于识别需要保留旧封闭行为的代码路径。
- 示例代码:
  ```cpp
  if (field->file()->syntax() == FileDescriptor::SYNTAX_PROTO2) {
    // 处于 proto2 遗留封闭语义上下文
  }
  ```

## 相关概念
- [[concepts/proto2|proto2]]
- [[concepts/FieldDescriptor|FieldDescriptor]]
- [[concepts/EnumDescriptor|EnumDescriptor]]
- [[concepts/legacy_treat_enum_as_closed|legacy_treat_enum_as_closed]]
- [[concepts/proto3|proto3]]

## 相关实体
- [[entities/Protocol Buffers|Protocol Buffers]]

## 来源提及
- `file().syntax() == FileDescriptor::SYNTAX_PROTO2` — [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]
- An open (lol) question is whether we should move is_closed from EnumDescriptor to FieldDescriptor. — [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]