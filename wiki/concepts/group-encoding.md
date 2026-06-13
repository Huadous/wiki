---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [method]
aliases:
  - "Group wire encoding"
  - "FieldType.GROUP"
  - "Protobuf group encoding"
---


# Group encoding

## 定义
Group 编码是 Protocol Buffers 早期的一种消息字段 wire 编码方式，通过 `start_group` / `end_group` tag 来包裹消息体。在 Java Lite 中，group 类型以 `FieldType.GROUP`（数值 17）表示。该提案建议在处理 `features.message_encoding = DELIMITED` 时，在编译器层面将消息字段改写为 group 类型（field type 17），再写入 `MessageInfo`；运行时则与已有的 group 字段共用 `ImmutableMessageFieldLiteGenerator::GenerateFieldInfo` 与解析逻辑，嵌套消息的 `MessageInfo` 编码无需额外修改。文件同时预留了一种未来破坏性改名方案：可将 `FieldType.GROUP` 重命名为 `FieldType.MESSAGE_DELIMITED`（保持数值与位编码不变）以提升可读性，但 Editions Zero 阶段不实施。

## 关键特征
- 是 protobuf 早期用于消息字段的 wire 编码方式，使用 `start_group` / `end_group` tag 包裹消息体。
- 在 Java Lite 中对应 `FieldType.GROUP`，字段类型数值编号为 17。
- 在编译期可作为消息字段的内部表示：编译器在处理 `features.message_encoding = DELIMITED` 的消息字段时，先在类型层面改写为 group（field type 17），再写入 `MessageInfo`。
- 运行期与历史 group 字段共用同一套代码路径（`ImmutableMessageFieldLiteGenerator::GenerateFieldInfo` 及对应解析逻辑），嵌套消息的 `MessageInfo` 编码无需修改。
- 保留了未来破坏性改名空间：可将 `FieldType.GROUP` 重命名为 `FieldType.MESSAGE_DELIMITED`（保持数值与位编码不变），但 Editions Zero 阶段不实施。

## 应用
- 在 Editions 模式下为消息字段实现 DELIMITED 编码：通过编译器把 `features.message_encoding = DELIMITED` 的消息字段改写为 group 类型，从而复用现有的 group 运行时编解码与 `MessageInfo` 基础设施。
- 作为一种过渡机制，使 Java Lite 在不增加新运行时分支的情况下支持新的 DELIMITED 消息编码语义。
- 为未来的可读性优化提供命名升级路径（例如后续将 `FieldType.GROUP` 改名为 `FieldType.MESSAGE_DELIMITED`）。

## 相关概念
- [[concepts/features.message_encoding|features.message_encoding]]
- [[concepts/DELIMITED-message-encoding|DELIMITED message encoding]]
- [[concepts/ImmutableMessageFieldLiteGenerator|ImmutableMessageFieldLiteGenerator]]
- [[concepts/MessageInfo|MessageInfo]]

## 相关实体
- No related entities

## 来源提及
- "Encode as type group. See below." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- "In the compiler, message fields with `features.message_encoding = DELIMITED` should be treated as a group *before* encoding message info." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]