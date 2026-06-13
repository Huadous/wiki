---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [other]
aliases:
  - "string_type feature"
  - "string_type 特性"
---


# string_type

## 基本信息
- Type: other
- Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]

## 描述
string_type 是 Protobuf Editions 体系内 [[entities/New-String-APIs|New String APIs]] 项目所引入的一项具体特性（feature），作为新字符串相关 API 能力的一部分被加入。它在文档中并不是单纯的特性条目，而是充当了从抽象讨论过渡到具体推荐方案的关键桥梁：它的引入过程直接暴露了当前 Editions 系统中新特性与旧版本二进制之间缺乏生命周期约束的问题——当二进制尚未感知该特性时，proto 文件仍可能在旧 Edition 中覆盖（override）该特性，从而导致旧二进制无法正确处理相关字段。面对这一真实问题，作者采用的临时做法是编写一段 ad hoc 验证，禁止在 Edition 2023 中覆盖此特性直至正式发布。该案例也促使作者进一步提议：应将 edition_introduced、edition_deprecated、deprecation_warning、edition_removed 等生命周期字段作为通用机制加入到所有 feature 的定义中，从而避免每个新特性都重复发明临时校验逻辑。

## 相关实体
- [[entities/New-String-APIs|New String APIs]]
- [[entities/Edition-2023|Edition 2023]]
- [[entities/protoc|protoc]]

## 相关概念
- [[concepts/Feature-Lifetimes|Feature Lifetimes]]
- [[concepts/FeatureSupport|FeatureSupport]]
- [[concepts/Backward-Compatibility|Backward Compatibility]]
- [[concepts/Edition-Support-Window|Edition Support Window]]

## 来源提及
- We faced this problem when introducing the new `string_type` feature as part of *New String APIs* (not available externally). — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- Our solution at the time was to create some ad hoc validation that prohibited overriding this feature in Edition 2023 until we were ready to release it. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]