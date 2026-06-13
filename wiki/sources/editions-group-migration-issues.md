---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-group-migration-issues.md]]"
tags: [Delimited encoding, Group fields, Smooth Extension, Group-like fields, Global Feature, Text format, Codegen, Aliases, Submessages: In Pursuit of a More Perfect Encoding, Proto2, Nerf Delimited Encoding in 2023, Feature Suite, Conformance tests, Extensions, Synthetic message, Wire format, API breaking change, Edition 2024]
aliases: ["Editions Group Migration Issues", "protobuf edition 2023 delimited encoding proposal"]
---

# Editions: Group Migration Issues - Summary

## 来源
- Original file: [[protobuf/editions-group-migration-issues.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 [[entities/mkruskal-google|mkruskal-google]] 撰写的 Protocol Buffers 设计提案，针对 [[entities/edition-2023|Edition 2023]] 在开源发布前暴露的 [[concepts/delimited-encoding|分隔编码]] 问题进行分析并提出解决方案。[[entities/joshua-humphries|Joshua Humphries]] 在测试 Edition 2023 早期版本时（参见 [[entities/github-issue-#16239|GitHub issue #16239]]）发现，新消息编码功能过度依赖 [[concepts/proto2|Proto2]] [[concepts/group-fields|group]] 逻辑，导致其在一般场景下几乎不可用。根本原因在于 Edition 2023 移除了[[concepts/synthetic-message|同步合成消息]]的生成机制，使用户可以显式定义消息并标记 DELIMITED 字段，从而打破了类型名与字段名保持同步的隐含假设。文档比较了各语言（基于 [[entities/protoc-explorer|protoc-explorer]] 调查 C++、Java、Python、Go、Dart、Objective-C、Swift、C# 以及 [[entities/upb|upb]]）的[[concepts/codegen|代码生成]]不一致性以及[[concepts/text-format|文本格式]]问题，提出五种替代方案：[[concepts/smooth-extension|Smooth Extension]]（推荐短期方案）、[[concepts/global-feature|Global Feature]]（长期缓解）、[[concepts/feature-suite|Feature Suite]]、[[concepts/nerf-delimited-encoding-in-2023|Nerf Delimited Encoding in 2023]]（紧急回退）和 [[concepts/aliases|Aliases]]（理想方案）。最终建议采用 Smooth Extension 解决当前问题，并在 Edition 2023 发布后尽快引入 Aliases 来统一旧行为。

## 关键实体
- [[entities/mkruskal-google|mkruskal-google]] — 本文档作者，Protobuf 团队成员
- [[entities/joshua-humphries|Joshua Humphries]] — 报告分隔编码问题的关键人物
- [[entities/protocol-buffers|Protocol Buffers]] — Google 开发的结构化数据序列化框架
- [[entities/edition-2023|Edition 2023]] — 首个正式 protobuf edition 版本
- [[entities/upb|upb]] — 用 C 编写的轻量级 protobuf 实现
- [[entities/protoc-explorer|protoc-explorer]] — Google 内部用于比较各语言代码生成的工具
- [[entities/google3|google3]] — Google 内部单体代码仓库，作为迁移影响范围评估基准
- [[entities/prototiller|Prototiller]] — Google 内部 .proto 转换工具
- [[entities/github-issue-#16239|GitHub issue #16239]] — 触发本次分析工作的源头 issue

## 关键概念
- [[concepts/delimited-encoding|delimited encoding]] — Edition 2023 引入的自定界消息编码方式
- [[concepts/group-fields|group fields]] — Proto2 特有的 group 字段语法及其合成消息机制
- [[concepts/smooth-extension|Smooth Extension]] — 推荐的短期方案，引入 "group-like" 概念保留旧行为
- [[concepts/group-like-fields|group-like fields]] — Smooth Extension 定义的概念性字段类别
- [[concepts/global-feature|Global Feature]] — 引入 `legacy_group_handling` 特性控制所有行为变更的长期方案
- [[concepts/text-format|text format]] — protobuf 的人类可读序列化形式，存在 group 名与字段名冲突问题
- [[concepts/codegen|codegen]] — 不同语言在 group 字段 API 生成上存在显著差异
- [[concepts/aliases|aliases]] — 理想的长期解决方案，可指定旧行为由 proto 语言统一处理
- [[concepts/submessages-in-pursuit-of-a-more-perfect-encoding|Submessages: In Pursuit of a More Perfect Encoding]] — Google 内部迁移整个生态到分隔编码的设计文档
- [[concepts/proto2|proto2]] — 引入 group 字段语法的 protobuf 早期版本
- [[concepts/nerf-delimited-encoding-in-2023|Nerf Delimited Encoding in 2023]] — 限制分隔编码功能的紧急回退方案
- [[concepts/feature-suite|Feature Suite]] — 将代码生成变更拆分为各语言独立功能的扩展方案
- [[concepts/conformance-tests|conformance tests]] — 用于锁定行为变更的 protobuf 一致性测试
- [[concepts/extensions|extensions]] — 在 editions 中不存在问题的 group 扩展机制
- [[concepts/synthetic-message|synthetic message]] — Proto2 为 group 自动生成的同步嵌套消息
- [[concepts/wire-format|wire format]] — protobuf 的线协议序列化表示
- [[concepts/api-breaking-change|API breaking change]] — 修改生成语言 API 导致的破坏性变更
- [[concepts/edition-2024|Edition 2024]] — Edition 2023 的计划后续版本，是修复 Nerf 方案后引入完整 DELIMITED 的最早时间点

## 要点
- **核心缺陷**：Edition 2023 的 DELIMITED 编码特性过度依赖旧 Proto2 group 逻辑，在类型名和字段名不同步时几乎不可用。
- **代码生成不一致**：不同语言（C++、Java、Python、Go、Dart、Objective-C、Swift、C#、upb）对 Proto2 group 的 API 生成行为差异显著，editions 升级可能产生令人惊讶的拼写冲突。
- **文本格式问题**：规范要求 group 使用消息名编码，但部分语言使用字段名，导致重构消息名会改变文本输出以及解析冲突。
- **推荐路径**：Smooth Extension（短期）+ Aliases（长期），前者引入 group-like 概念保留旧行为同时处理新场景，后者提供理想的统一机制。
- **长期机制**：Global Feature（`legacy_group_handling`）可作为 editions 逐步淘汰旧行为的工具，但引入时机偏晚且迁移路径不清晰。
- **紧急回退**：Nerf Delimited Encoding 通过禁止消息名和字段名不匹配来限制功能，会阻碍分隔编码生态迁移直至 Edition 2024。
- **不受影响的部分**：Group 扩展（[[concepts/extensions|extensions]]）一直使用字段名，因此在 editions 中不存在相关问题。