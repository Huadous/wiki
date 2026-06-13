---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-java-lite-for-editions.md]]"]
tags: [term]
aliases:
  - "MessageSchema 结构"
  - "Java Lite MessageSchema"
---


# MessageSchema

## 定义
`MessageSchema` 是 Java Lite 在运行时使用的描述符形式（descriptor-like schema），由 [[concepts/RawMessageInfo|RawMessageInfo]] 解码而来。它是 Java Lite 进行消息解析与序列化的核心数据结构，充当消息在运行时的模式描述载体。

## 关键特征
- **解码来源**：由 [[concepts/RawMessageInfo|RawMessageInfo]] 解码生成，作为 Java Lite 内部对消息模式（schema）的运行时描述。
- **解析与序列化核心**：承担消息的解析（parsing）与序列化（serialization）任务，是 Java Lite 数据通路的关键数据结构。
- **proto2/proto3 重复实现**：当前 `MessageSchema` 中多处方法存在 proto2 与 proto3 的两套重复实现，需要在 Editions 迁移中加以统一：
  - `getSerializedSize` 合并 `getSerializedSizeProto2/3`
  - `writeTo` 合并 `writeFieldsInAscendingOrderProto2/3`
  - `mergeFrom` 合并 `parseProto2/3Message`
- **Group 编码处理**：在 message 字段上对 group 编码的处理方式取决于所选方案：
  - 若采用 "DELIMITED 即 group" 方案，则 `MessageSchema` 无需新增特殊处理逻辑。
  - 若采用 `kIsMessageEncodingDelimitedBit` 替代方案，则需在 `MessageSchema` 的 `case Message` 分支中根据该位额外按 group 方式进行编码处理。

## 应用
- 作为 Java Lite 在运行时持有的 schema 描述符，为消息字段提供解码、序列化、合并所需的元信息。
- 在 Protobuf Editions 迁移中，作为统一 proto2/proto3 重复实现的关键切入点，通过方法合并消除分支重复，降低维护成本。
- 在 message 字段的 group 编码方案选择中，作为决定编码路径的承载者，决定是否在 `case Message` 分支引入按位判断逻辑。

## 相关概念
- [[concepts/RawMessageInfo]]
- [[concepts/MessageInfo]]
- [[concepts/ManifestSchemaFactory.newSchema]]
- [[concepts/DescriptorMessageInfoFactory.convert]]

## 相关实体
- [[protobuf/java-lite|Java Lite]]

## 来源提及
- "This is decoded into `MessageSchema` which serves as the descriptor-like schema for Java lite for parsing and serialization." — [[protobuf/editions-java-lite-for-editions|editions-java-lite-for-editions]]