---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]"]
tags: [standard]
aliases:
  - "non-decimal field numbers"
  - "Decimal field numbers"
  - "十进制字段号"
---


# Decimal field numbers

## 定义
十进制字段号（Decimal field numbers）是 Protobuf Editions 提案中的一项语言规范标准，要求在 `.proto` 文件中声明字段号时必须使用十进制整数字面量，禁止使用十六进制或其他进制形式。该提案旨在简化 Protobuf 语言解析器，并消除允许其他进制所带来但缺乏实际价值的灵活性。

## 关键特征
- 强制字段号采用十进制整数字面量书写，例如 `optional int32 x = 1;`，而非 `optional int32 x = 0x01;`
- 明确禁止十六进制、八进制等其他进制形式的整数字面量用于字段号
- 已不允许在数字前添加前导 `+` 或 `-` 号（即当前语法不认 `+1` 或 `-1` 这样的写法）
- 通过特性标志 `features.non_decimal_field_numbers` 进行管理
- 该特性标志在初始 edition 中默认为 `true`（即允许非十进制），将在未来 edition 中切换为 `false`（即强制十进制）
- 变更动机：允许其他进制几乎没有任何实际用途，反而使 Protobuf 语言解析更加复杂

## 应用
- 适用于所有新设计的 Protobuf Editions schema 中的字段号声明
- 在迁移至禁用 `non_decimal_field_numbers` 特性的 edition 时，需要将已有 `.proto` 文件中的十六进制字段号改写为十进制形式
- 帮助 Protobuf 编译器（protoc）简化词法分析阶段对字段号字面量的处理
- 与 Editions 的整体收紧策略一致，提升语言的一致性与可解析性

## 相关概念
- [[concepts/feature-gating|Feature gating]]
- [[concepts/field-number-reservation|Field number reservation]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## 相关实体
- [[entities/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- We permit non-decimal integer literals for field numbers, e.g. `optional int32 x = 0x01;`. Thankfully(?) we do not already permit a leading + or -. We should require decimal literals, since there is very little reason to allow other literals and makes the Protobuf language harder to parse. — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]