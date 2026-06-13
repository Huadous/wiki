---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
tags:
  - "term"
aliases:
  - "RawMessageInfo"
  - "RawMessageInfo descriptor"
  - "MessageInfo"
  - "RawMessageInfo"
  - "RawMessageInfo descriptor"
---

## Description
`RawMessageInfo` 是 Java Lite 代码生成器在编译期写入的紧凑描述符容器，其内部以一段类似 descriptor 的 info 字符串编码 message 元信息，并由运行时库解码为 `MessageSchema`，驱动序列化、反序列化与反射等操作。其结构中包含一个 `flags` 字段：`flags & 0x1` 标识是否为 proto2 语法，`flags & 0x2` 标识条目是否为 message 类型。提案建议在空闲位中新增 `is_edition` 位（`flags & 0x4`），用于在 [[concepts/ProtoSyntax|ProtoSyntax]] 枚举中区分 `EDITIONS`。在字段条目层面，`RawMessageInfo`（与广义的 `MessageInfo` 编码共同构成 Java Lite 编码层）使用一组固定数量的位来表达 resolved features 与字段类型信息，多数位与 [[concepts/Editions Zero Features|Editions Zero Features]] 一一对应，例如 `kHasHasBit`（0x1000）对应 `features.field_presence`，`kUtf8CheckBit`（0x200）对应 `features.string_field_validation`。需要注意的是，当前 `MessageInfo` 编码存在位容量限制：当未来 editions 引入更多 features，或需要在 message-level 表达 features 时，必须升级到新的 `MessageInfo` 编码格式，但对于 Editions Zero 阶段该升级可以暂时避免。

## Related Concepts
- [[concepts/MessageInfo|MessageInfo]]
- [[concepts/MessageSchema|MessageSchema]]
- [[concepts/ProtoSyntax|ProtoSyntax]]
- [[concepts/kLegacyEnumIsClosedBit|kLegacyEnumIsClosedBit]]
- [[concepts/Editions Zero Features|Editions Zero Features]]
- [[concepts/MiniDescriptor|MiniDescriptor]]
- [[concepts/kHasHasBit|kHasHasBit]]
- [[concepts/kUtf8CheckBit|kUtf8CheckBit]]
- [[concepts/kMapWithProto2EnumValue|kMapWithProto2EnumValue]]

## Related Entities
- [[entities/Java-Lite|Java Lite]]

## Mentions in Source

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - The code generator for Java Lite encodes an descriptor-like info string which is stored into `RawMessageInfo`.
> - `RawMessageInfo` should be augmented with an additional `is_edition` bit in flags' unused bits.
> - Several other syntax usages need to be made to be editions compatible by merging implementations.
> - We will eventually need to revamp `MessageInfo` encoding to support these changes. However, this should be avoidable for Editions Zero.