---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-java-lite-for-editions.md]]"
tags: [Editions, Editions Zero Features, RawMessageInfo, MessageSchema, ProtoSyntax, MessageInfo, MiniDescriptor, features.field_presence, features.message_encoding, java.legacy_closed_enum, features.repeated_field_encoding, features.string_field_validation, features.enum_type, Group encoding, DELIMITED message encoding, kHasHasBit, kUtf8CheckBit, kLegacyEnumIsClosedBit, kMapWithProto2EnumValue, kIsMessageEncodingDelimitedBit, is_proto3 bit, is_edition bit, GetExperimentalJavaFieldType, ManifestSchemaFactory.newSchema(), DescriptorMessageInfoFactory.convert()]
aliases: ["Java Lite Editions 提案", "protobuf-javalite editions migration"]
---

# Java Lite For Editions - Summary

## 来源
- Original file: [[protobuf/editions-java-lite-for-editions.md]]
- Ingested: 2026-06-13

## 核心内容
本文件为 [[entities/zhangskz|zhangskz]] 撰写并于 2023-05-26 获批的 Protocol Buffers [[entities/java-lite|Java Lite]] 兼容 [[concepts/editions|Editions]] 体系的设计提案。[[entities/java-lite|Java Lite]] 出于 Android 对代码体积与性能的严苛要求，并未嵌入完整描述符，而是由代码生成器将描述符信息编码进 [[concepts/rawmessageinfo|RawMessageInfo]]，运行时再解码为 [[concepts/messageschema|MessageSchema]] 用于解析与序列化。当前实现大量依赖 `is_proto3` 位区分语法，难以适配 [[concepts/editions|Editions]] 的特性化模型。提案给出 Editions Zero 阶段的最小改动方案：在 [[concepts/rawmessageinfo|RawMessageInfo]] flags 中新增 [[concepts/is_edition-bit|is_edition bit]]（0x4），扩展 [[concepts/protosyntax|ProtoSyntax]] 枚举包含 `EDITIONS`，并将原本读取 `is_proto3` 的代码路径统一迁移到已有的字段级 feature 位（如 [[concepts/khashasbit|kHasHasBit]]、[[concepts/kutf8checkbit|kUtf8CheckBit]]、重命名后的 [[concepts/klegacyenumisclosedbit|kLegacyEnumIsClosedBit]]）。文件同时分析了两种长期替代方案：升级 [[concepts/messageinfo|MessageInfo]] 编码格式或迁移至 [[concepts/minidescriptor|MiniDescriptor]]。

## 关键实体
- [[entities/java-lite|Java Lite]]
- [[entities/zhangskz|zhangskz]]

## 关键概念
- [[concepts/editions|Editions]]
- [[concepts/editions-zero-features|Editions Zero Features]]
- [[concepts/rawmessageinfo|RawMessageInfo]]
- [[concepts/messageschema|MessageSchema]]
- [[concepts/protosyntax|ProtoSyntax]]
- [[concepts/messageinfo|MessageInfo]]
- [[concepts/minidescriptor|MiniDescriptor]]
- [[concepts/features-field_presence|features.field_presence]]
- [[concepts/features-message_encoding|features.message_encoding]]
- [[concepts/java-legacy_closed_enum|java.legacy_closed_enum]]
- [[concepts/features-repeated_field_encoding|features.repeated_field_encoding]]
- [[concepts/features-string_field_validation|features.string_field_validation]]
- [[concepts/features-enum_type|features.enum_type]]
- [[concepts/group-encoding|Group encoding]]
- [[concepts/delimited-message-encoding|DELIMITED message encoding]]
- [[concepts/khashasbit|kHasHasBit]]
- [[concepts/kutf8checkbit|kUtf8CheckBit]]
- [[concepts/klegacyenumisclosedbit|kLegacyEnumIsClosedBit]]
- [[concepts/kmapwithproto2enumvalue|kMapWithProto2EnumValue]]
- [[concepts/kismessageencodingdelimitedbit|kIsMessageEncodingDelimitedBit]]
- [[concepts/is_proto3-bit|is_proto3 bit]]
- [[concepts/is_edition-bit|is_edition bit]]
- [[concepts/getexperimentaljavafieldtype|GetExperimentalJavaFieldType]]
- [[concepts/manifestschemafactory-newschema|ManifestSchemaFactory.newSchema()]]
- [[concepts/descriptormessageinfofactory-convert|DescriptorMessageInfoFactory.convert()]]

## 要点
- [[entities/java-lite|Java Lite]] 当前使用 [[concepts/is_proto3-bit|is_proto3 bit]] 区分 proto2/proto3 语法，提案在不破坏向后兼容性的前提下引入 [[concepts/is_edition-bit|is_edition bit]]（0x4）并扩展 [[concepts/protosyntax|ProtoSyntax]] 枚举包含 `EDITIONS` 选项，以适配 [[concepts/editions|Editions]] 体系。
- [[concepts/editions-zero-features|Editions Zero Features]] 中的多数特性（[[concepts/features-field_presence|features.field_presence]]、[[concepts/features-string_field_validation|features.string_field_validation]]、[[concepts/java-legacy_closed_enum|java.legacy_closed_enum]]、[[concepts/features-repeated_field_encoding|features.repeated_field_encoding]]）已与 [[concepts/messageinfo|MessageInfo]] 字段条目中的现有位（[[concepts/khashasbit|kHasHasBit]]、[[concepts/kutf8checkbit|kUtf8CheckBit]]、[[concepts/kmapwithproto2enumvalue|kMapWithProto2EnumValue]]）一一对应，仅需把读取 `is_proto3` 的代码路径迁移到对应 feature 位。
- [[concepts/java-legacy_closed_enum|java.legacy_closed_enum]] 对应的 [[concepts/kmapwithproto2enumvalue|kMapWithProto2EnumValue]]（0x800）被重命名为 [[concepts/klegacyenumisclosedbit|kLegacyEnumIsClosedBit]]，并扩展至所有枚举字段；过渡阶段仍需在 gencode 中检查 syntax 以兼容旧行为。
- 对于 [[concepts/features-message_encoding|features.message_encoding]] = DELIMITED，提案推荐在编译器层将消息字段按 [[concepts/group-encoding|Group 类型]]（17）写入 [[concepts/messageinfo|MessageInfo]]，复用现有 group 处理逻辑，最小化运行时改动；备选方案是新增 [[concepts/kismessageencodingdelimitedbit|kIsMessageEncodingDelimitedBit]]（0x1100），但需在多处处理 group 行为。
- Editions Zero 阶段还需统一 [[concepts/messageschema|MessageSchema]] 的 `getSerializedSize`、`writeTo`、`mergeFrom` 以及 [[concepts/manifestschemafactory-newschema|ManifestSchemaFactory.newSchema()]]、[[concepts/descriptormessageinfofactory-convert|DescriptorMessageInfoFactory.convert()]] 中的 proto2/proto3 重复实现，统一为基于 feature 位的单一代码路径。
- 长期替代方案：Alternative 1 引入新版 [[concepts/messageinfo|MessageInfo]] 编码格式以支持 message-level features 与更多 features；Alternative 2 将 [[entities/java-lite|Java Lite]] 整体迁移至 [[concepts/minidescriptor|MiniDescriptor]] 编码，两者均建议推迟到 Editions Zero 之后。