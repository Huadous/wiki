---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "CodeGeneratorRequest"
  - "生成器请求消息"
---


# GeneratorRequest

## 定义
GeneratorRequest 是 protoc 与生成器（特别是非 C++ 插件）之间传递信息的 proto 消息。它是 protoc 向代码生成插件描述待生成代码所需的输入数据结构，其中在 Editions 体系中承担了**承载未解析特性**（unresolved features）的关键职责。

## 关键特征
- **protoc 与插件的通信协议载体**：GeneratorRequest 是 protoc 向非 C++ 插件（CodeGenerator）下发信息的主要 proto 消息。
- **承载全部未解析特性**：在推荐方案中，protoc 通过 GeneratorRequest 提供**完整的未解析特性集**（full set of unresolved features），由插件自行解析并应用选项保留剥离（option retention stripping）。
- **非 C++ 插件获取特性数据的唯一来源**：插件无法直接复用 C++ 端的特性解析工具，因此 GeneratorRequest 成为非 C++ 生成器唯一可用的事实数据来源。
- **支持默认特性的预序列化嵌入**：为减少插件重复实现 edition defaults 的工作量，文档提议通过 genrule 将 feature protos 转换为预序列化的 `EditionFeatureDefaults` 字符串并嵌入到生成器代码中，简化插件端的默认特性查找逻辑。

## 应用
- **Editions 模式下的代码生成**：在 Protobuf Editions 体系中，protoc 将特性集信息以 GeneratorRequest 形式下发给各类语言插件，用于生成对应语言的代码。
- **跨语言插件实现**：Java Lite、Go、Python 等非 C++ 语言插件通过解析 GeneratorRequest 中的未解析特性来适配新 Editions 行为。
- **默认特性查找优化**：通过嵌入预序列化的 `EditionFeatureDefaults` 数据，避免每个插件独立重新实现 edition defaults 解析逻辑。
- **选项保留（Option Retention）处理**：插件依据 GeneratorRequest 中携带的未解析特性，结合 retention 规则决定哪些选项需要被剥离。

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/option-retention|Option Retention]]
- [[concepts/edition-defaults|Edition Defaults]]
- [[concepts/source-features|Source Features]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/codegenerator|CodeGenerator]]
- [[entities/featureset|FeatureSet]]

## 来源提及
- "The `GeneratorRequest` from protoc will provide the full set of *unresolved* features, which they will need to resolve and apply retention stripping to." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]
- "We can package a genrule that converts from feature protos to a serialized `EditionFeatureDefaults` string, and embed this anywhere we want." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]