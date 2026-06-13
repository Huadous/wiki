---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
tags:
  - "method"
aliases:
  - "Feature"
  - "特性"
---

## Description
在 Protobuf Editions 中，Feature 是一种附加在任意语法实体（如文件、消息、字段、枚举）上的选项，用于细粒度控制代码生成和运行时行为。每个 Feature 都具有层级继承机制：下层实体（如字段）默认继承上层实体（如文件或消息）中定义的 Feature 值，除非在本地显式覆盖。这种设计使得大型项目可以在文件级别统一设定默认行为，然后在特定消息或字段级别进行微调。Features 不能引入会直接破坏现有二进制兼容性的更改，但可能支持语言后端定义自己的语言范围 feature。Features 的默认值由所使用的 edition 决定，从而确保版本迁移时的向后兼容性。

从 schema producer 的视角来看，Features 是让 Protobuf 安全随时间演进的核心配置机制。Features 通常不会改变消息的 wire format，因此更改 `.proto` 文件的 edition 不会更改消息的 wire format，这一性质是整个 editions 设计的安全保证基础。需要注意的是，代码生成器特定的 features（如 `features.(pb.cpp).string_field_type`）应仅在单个代码库的上下文中应用，schema producer 不应将此类生成器特定选择强加给消费者。常见的 Features 包括字段的 packed 编码控制、枚举的开放/封闭类型控制等。

在 Editions 的设计提案层面，feature 被进一步形式化为 edition 的组成单元：每个 edition 是一组带有默认值的 features，feature 集合或 feature 的默认值只能在引入新 edition 时才能修改，feature 的具体值则可以在使用方的 `.proto` 文件中针对实体级别进行覆盖。提案早期曾采用字符串形式定义 feature，后来改为使用 custom options 来定义和表示 feature，这种表示方式天然支持通过 extensions 扩展特定语言的特性，并配合继承、目标属性（target attributes）与保留（retention）等机制提供更精细的演进能力。

在具体的 schema 设计层面，Features 自身被定义为一个 Protobuf message 类型，其中声明了可在 `.proto` 文件中应用于实体的若干 feature 字段。例如该消息内部可定义 `EnumType` 枚举（含 `OPEN`、`CLOSED` 两个取值）以及一个标注了 `target = TARGET_TYPE_ENUM` 的 `enum` 字段，以此约束该 feature 只能放置在枚举类型所在的层级。Features 既可声明在文件级别，也可声明在其目标实体上；若放置到不支持的层级，protoc 将产生编译错误。这一设计展示了 `target` 与 `retention` 属性在 editions 中的实际组合用法：通过 `target` 限制 feature 的作用域，通过 `retention` 控制 feature 的可继承与可见范围。

## Related Concepts
- [[concepts/editions|Editions]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/target-attributes|Target Attributes]]
- [[concepts/retention|Retention]]
- [[concepts/custom-options|Custom Options]]
- [[concepts/options-attributes|Options Attributes]]
- [[concepts/backward-compatibility|Backward Compatibility]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/schema-consumer|Schema Consumer]]

## Related Entities
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|Protobuf Editions 介绍文档]]**
> - "Features control the individual codegen and runtime behavior of fields, messages, enums, etc."
> - "Features cannot introduce changes that would directly break existing binaries."
> - "A feature, in the narrow context of Protobuf Editions, is an option on any syntax entity of a .proto file that has the following properties..."
> - "This is primarily accomplished through \"features\"."

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|Protobuf Editions for Schema Producers]]**
> - "This is primarily accomplished through \"features\"."
> - "As a reminder, features will generally not change the wire format of messages and thus changing the edition for a `.proto` will not change the wire format of message."

> **Source: [[sources/editions-protobuf-editions-design-features|Protobuf Editions Features Design]]**
> - "An edition is formally a set of \"features\" with a default value per feature."
> - "Features define the specific points of change and evolution on a per entity basis within a .proto file (entities being files, messages, fields, or any other lexical element in the file)."

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - `option features.enum = OPEN;  // allowed at FILE scope`
> - `option features.enum = CLOSED;  // allowed at ENUM scope`