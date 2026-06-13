---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]"]
tags: [method]
aliases:
  - "enforces_utf8"
  - "FieldDescriptor::enforces_utf8"
---


# FieldDescriptor::enforces_utf8

## 定义
`FieldDescriptor::enforces_utf8()` 是 Protocol Buffers Editions 提案（Tier 1）中为 C++ 运行时新增的一个布尔型实例方法，用于判断当前字段是否为一个会在编解码（parse/serialize）过程中强制进行 UTF-8 校验的字符串字段。该方法将被作为查询"是否对该字符串字段进行 UTF-8 验证"的独立 API。

## 关键特征
- 签名形式为 `bool enforces_utf8() const;`，属于 `FieldDescriptor` 类的方法。
- 专门用于判断字符串字段（string field）的 UTF-8 强制校验语义，而非泛用的语法标识。
- 替代了以往依赖 `syntax()` 间接推断字符串字段是否执行 UTF-8 验证的做法，使该语义成为可独立查询的字段级特性。
- 在迁移策略中被明确指定为「UTF-8 验证 on parse」用途的目标 API。

## 应用
- 在 Editions（特别是 [[entities/Edition Zero|Edition Zero]]）的迁移路径中，作为替换旧有 `syntax()` 间接判断方式的推荐 API，专门服务于"解析时 UTF-8 验证"这一场景。
- 为生成代码或反射库提供一种直接判定字符串字段是否需要执行 UTF-8 校验的查询接口，避免基于语法名称（proto2/proto3）的启发式判断。

## 相关概念
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/syntax-deprecation-migration|syntax() deprecation migration]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/edition-zero|Edition Zero]]

## 来源提及
- `bool enforces_utf8() const;` — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]
- `1. UTF-8 verification on parse (use new API).` — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]