---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-edition-naming.md]]"
tags: [Edition Naming, Edition, Edition enum, FeatureSet, Hyrum's Law, Calver, descriptor.proto, Edition Zero, Proto Merging, Life of an Edition, Editions: Life of a FeatureSet, Edition comparison, Open enum, Unknown Field Set]
aliases: ["Edition Naming Proposal", "protobuf/editions-edition-naming"]
---

# Edition Naming - Summary

## 来源
- Original file: [[protobuf/editions-edition-naming.md]]
- Ingested: 2026-06-13

## 核心内容

本文档由 [[entities/mkruskal-google|mkruskal-google]] 撰写，于 2023-08-25 获批，深入探讨了 Protocol Buffers 项目中 [[concepts/edition-naming|Edition 命名]] 规范的设计与决策过程。当前版本采用「年份+可选修订号」的宽松字符串命名方案，但存在诸多问题：[[concepts/edition-comparison|版本比较]] 逻辑复杂且边界情况繁多、需要在每种支持语言中重复实现、存在 [[concepts/hyrums-law|Hyrum's Law]] 风险、以及与 [[concepts/calver|Calver]] 风格版本号混淆导致沟通困难（如错误地称修订版本为「patch editions」）。

文档推荐解决方案：使用 [[concepts/edition-enum|Edition 枚举]] 类型，由 protobuf 集中定义所有合法版本值，proto 文件中以字符串书写，解析器在解析时迅速转换为枚举值，后续以整数进行比较。此外，文档决定暂时搁置修订版本概念，每年只发布一个 Edition 版本。文档还分析了多种替代方案的优缺点，并指出实施该方案需要等待 [[concepts/edition-zero|Edition 零]] 迁移完成后才能将枚举设为 [[concepts/open-enum|开放枚举]]，以避免版本被丢弃至 [[concepts/unknown-field-set|未知字段集]]。

## 关键实体
- [[entities/mkruskal-google|mkruskal-google]]：本文档作者，核心设计者
- [[entities/prototiller|Prototiller]]：已验证 Edition 枚举解析可行性的参考实现

## 关键概念
- [[concepts/edition-naming|Edition Naming]]：本文档核心主题
- [[concepts/edition|Edition]]：Protocol Buffers 替代 proto2/proto3 的版本概念
- [[concepts/edition-enum|Edition enum]]：推荐的版本表示方案
- [[concepts/featureset|FeatureSet]]：Edition 系统中描述功能特性的核心概念
- [[concepts/edition-comparison|Edition comparison]]：各语言必须重复实现的关键操作
- [[concepts/proto-merging|Proto Merging]]：与版本比较并列的最小操作集
- [[concepts/hyrums-law|Hyrum's Law]]：宽松命名方案面临的风险
- [[concepts/calver|Calver]]：导致沟通混淆的命名风格
- [[concepts/descriptor-proto|descriptor.proto]]：Edition 枚举必须所在的 proto 文件
- [[concepts/edition-zero|Edition Zero]]：迁移过渡阶段，决定开放枚举时机
- [[concepts/open-enum|Open enum]]：理想的 Edition 枚举设计
- [[concepts/unknown-field-set|Unknown Field Set]]：开放枚举旨在避免的目的地
- [[concepts/life-of-an-edition|Life of an Edition]]：背景参考文档
- [[concepts/editions-life-of-a-featureset|Editions: Life of a FeatureSet]]：影响命名决策的核心设计文档

## 要点
- 推荐方案：使用 Edition 枚举类型集中定义合法版本值，将版本比较简化为整数比较，大幅降低跨语言实现复杂度
- 决定搁置修订版本（revisions）概念，计划每年发布恰好一个 Edition 版本
- 当前宽松字符串命名方案存在 Hyrum's Law 风险，且与 Calver 风格相似导致沟通混淆
- Edition 核心语义：严格时间排序、可随时追加新 Edition、新特性可不更改 Edition 添加、特性只能在大版本中删除
- 文档对比了多种替代方案（带修订号的枚举、截断修订号、固定长度版本、消息结构等），分析各自优缺点
- Edition 枚举需要存在于 descriptor.proto 中，须等待 Edition 零迁移完成后才能成为开放枚举
- 设计目标：离散可控的合法值集合、简单可比较、跨语言支持、集合较小（<100）、缓慢增长（每年约一次）