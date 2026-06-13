---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/proto3]]"]
tags: [term]
aliases:
  - "Reserved Field Names"
  - "保留字段名称"
---


# Reserved Field Names

## 定义
Reserved Field Names（保留字段名称）是消息类型通过 `reserved` 关键字声明的一组不可被未来字段重新使用的字段名称。它是 Protocol Buffers 中用于在删除字段后保留其字段名称的机制，目的是防止字段名称被意外复用而引发兼容性问题。

## 关键特征
- 通过 `reserved` 关键字声明，使用字符串字面量指定字段名称（例如 `reserved "foo";`）
- 复用旧字段名称在使用 TextProto 或 JSON 编码（字段名称被序列化）时可能带来风险，因此可以将已删除字段的名称加入保留列表以规避风险
- 保留名称仅影响 `protoc` 编译器行为而非运行时行为
- 唯一例外是 C++ 和 Go 的 TextProto 实现会在解析时静默丢弃具有保留名称的未知字段
- 不能在同一个 `reserved` 语句中混合字段名称和字段编号
- 适用于所有使用 Protobuf 进行数据序列化的场景，特别是涉及跨语言、跨版本兼容的系统

## 应用
- 当删除一个字段后，保留其字段名称以防止后续开发者误用相同名称
- 在使用 JSON 或 TextProto 编码的系统中尤为关键，因为这些格式的序列化结果中包含字段名称
- 用于维护 Protobuf 消息的长期向前与向后兼容性
- 在公共 API 演进过程中，防止字段名称冲突带来的解析歧义

## 相关概念
- [[concepts/reserved-field-numbers|Reserved Field Numbers]]
- [[concepts/message-type|Message Type]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "You should also reserve the field name to allow JSON and TextFormat encodings of your message to continue to parse." — [[sources/proto3]]
- "Reusing an old field name later is generally safe, except when using TextProto or JSON encodings where the field name is serialized." — [[sources/proto3]]
- "Note that you can't mix field names and field numbers in the same reserved statement." — [[sources/proto3]]