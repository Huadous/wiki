---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-stricter-schemas-with-editions]]"]
tags: [term]
aliases:
  - "Nonempty package"
  - "非空 package 要求"
  - "强制 package 声明"
---


# Nonempty package

## 定义
Nonempty package 是 [[sources/editions-stricter-schemas-with-editions|Editions 收紧 Schema 备忘录]] 中提出的一项强制要求:每个 `.proto` 文件都必须声明一个 package,彻底移除当前允许的 package 为空的语法。该备忘录将"允许 package 缺失"视为一项应当完全移除的语言功能(而非可选项),并建议引入一个类似 `feature.allow_missing_package` 的布尔 feature 进行受控迁移——默认值设为 `true`,在未来某个 edition 中切换为 `false`,以完成过渡。

## 关键特征
- **强制性**:将"必须声明 package"作为语言的硬性要求,而非可选风格建议。
- **完全移除**:不是放宽或软化当前规则,而是将"允许空 package"作为功能彻底删除。
- **Feature gating 迁移路径**:通过引入 `feature.allow_missing_package` 之类的布尔 feature,默认 `true`,在后续 edition 中翻转为 `false`,实现平稳过渡。
- **与"Package Is First"协同**:与"package 声明须最先出现"的要求以及名称解析的收紧共同构成 package 相关语法的整体收紧策略。
- **面向 Editions 设计**:作为 Editions 阶段对 proto 语言进行严格化(schema strictness)的一部分。

## 应用
- 在 [[sources/editions|Editions]] 中定义必须显式声明 `package` 语句的 `.proto` 文件编写规范。
- 通过 `feature.allow_missing_package` 控制旧式无 package 文件在迁移期内的兼容行为。
- 与 [[concepts/Package declaration position|Package declaration position]]、[[concepts/Name resolution in Protobuf|Name resolution in Protobuf]] 一同,构成 Editions 中 package 语法的整体收紧框架。

## 相关概念
- [[concepts/Feature gating|Feature gating]]
- [[concepts/Package declaration position|Package declaration position]]
- [[concepts/Name resolution in Protobuf|Name resolution in Protobuf]]

## 相关实体
- [[entities/protocol-buffers-v3-15-0|protocol-buffers-v3-15-0]]

## 来源提及
- "Right now, an empty package is technically permitted. We should remove this functionality from the language completely and require every file to declare a package." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]
- "We would introduce a feature like `feature.allow_missing_package`, start it out as true, and switch it to false." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]