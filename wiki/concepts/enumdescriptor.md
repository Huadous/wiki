---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]"]
tags: [term]
aliases:
  - "EnumDescriptor class"
  - "EnumDescriptor 类"
---


# EnumDescriptor

## 定义
EnumDescriptor 是 Protocol Buffers API 中的一个类,用于表示一个 protobuf 枚举。它暴露了与枚举元数据相关的属性(例如 `is_closed()`),后者用于返回该枚举是否被当作封闭(closed)处理。一致性(conformant)行为应基于枚举本身来确定其封闭性,并可通过 `EnumDescriptor::is_closed()` 进行查询。

## 关键特征
- 属于 Protocol Buffers 描述符(descriptor)API 的一部分,用于在运行时反映 `.proto` 文件中定义的枚举类型。
- 暴露 `is_closed()` 等属性,允许查询枚举的封闭性(closedness)状态。
- 存在一个悬而未决的设计问题:是否应将 `is_closed` 从 `EnumDescriptor` 迁移到 `FieldDescriptor`,原因在于对某些语言而言,枚举的开放性不仅取决于其定义,还取决于其使用位置(包含该枚举值的字段)。
- 一致性行为将封闭性的判定锚定在枚举定义上,并以 `EnumDescriptor::is_closed()` 作为统一查询入口。

## 应用
- 在 protobuf 运行时中根据枚举类型的封闭性决定允许的取值集合,例如在封闭枚举中拒绝未声明的未知值。
- 作为 Edition Zero 中"枚举字段封闭性"特性设计的一部分,为一致性运行时(conformant runtime)提供标准的封闭性查询接口。
- 在支持描述符反射(reflection)的语言绑定中,用于在运行时检查枚举定义并据此调整序列化/反序列化行为。

## 相关概念
- [[concepts/FieldDescriptor|FieldDescriptor]]
- [[concepts/Enum Field Closedness|Enum Field Closedness]]
- [[concepts/Open Enum|Open Enum]]
- [[concepts/FileDescriptor|FileDescriptor]]

## 相关实体
- [[entities/Protocol Buffers|Protocol Buffers]]

## 来源提及
- "An open (lol) question is whether we should move is_closed from EnumDescriptor to FieldDescriptor." — [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]
- "Conformant behavior determines closedness based on the enum and can be queried using EnumDescriptor::is_closed()." — [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]