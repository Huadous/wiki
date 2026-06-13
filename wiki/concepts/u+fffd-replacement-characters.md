---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "U+FFFD"
  - "Unicode replacement character"
  - "replacement characters"
---


# U+FFFD replacement characters

## 定义
U+FFFD 替换字符（即 Unicode 标准的 "replacement character"，渲染为 �）是一种由某些宿主语言（如 Java）在解析字符串字段时遇到无效 UTF-8 序列时所使用的占位符。源文档在讨论 `features.string_field_validation` 的未来工作时提到此概念，主张在某些场景下，用户可能希望字符串类型在遇到非法输入时显式返回 U+FFFD，而不是直接拒绝字段或静默修改原始字节。

## 关键特征
- Unicode 标准中用于表示"无法解码的输入"的占位符，码点为 U+FFFD，渲染形式为 �
- 由部分宿主语言在字符串字段遇到非法 UTF-8 字节时自动生成
- 不会导致字段反序列化失败，而是以可识别的替换字符形式出现在结果字符串中
- 与"拒绝"或"静默修改字节"形成对比的第三种语义处理策略
- 与代码生成特性（如建议中的 `java.bytes_as_string`）密切相关，可借此为 `bytes` 字段提供类似字符串的 API，并文档化其替换字符行为

## 应用
- 讨论 `features.string_field_validation` 时，作为"显式接受非法输入并替换为 U+FFFD"这一未来方向的核心论据
- 提议通过 per-codegen 特性（如 `java.bytes_as_string`）在 Java 代码生成中提供具有文档化 U+FFFD 行为的字符串语义
- 评估是否应在 Protocol Buffers 中将"返回 U+FFFD"作为官方支持的字符串字段校验选项
- 进一步的用户研究将决定是否将其纳入正式的 Edition 特性

## 相关概念
- [[concepts/utf-8-validation|UTF-8 validation]]
- [[concepts/features-string-field-validation|features.string_field_validation]]
- [[concepts/custom-default-values|Custom default values]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- There is an argument to be made for "I want a string type, and I explicitly want replacement U+FFFD characters if I get something that isn't UTF-8." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]