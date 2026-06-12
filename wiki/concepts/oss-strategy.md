---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [method]
aliases:
  - "Protobuf OSS Strategy"
  - "开源策略"
---


# OSS Strategy

## 定义
OSS Strategy 是指 Protocol Buffers 团队为 Protobuf Editions 制定的开源迁移策略。该策略的核心目标是确保非 Google 外部用户（OSS 社区）能够平稳、有序地从现有的 proto2/proto3 语法升级到新的 Protobuf Editions 体系。此策略包括发布迁移指南、提供自动化迁移工具（如 `proto2`/`proto3` -> `edition` 迁移器），以及为第三方代码生成器提供支持，以减少迁移过程中的摩擦。

## 关键特征
- **透明公开**：计划将内部迁移文档分享给 OSS 社区，确保迁移路径的透明度。
- **工具化支持**：尽可能提供公开的迁移工具（如代码迁移器），降低手动修改的工作量。
- **外部友好**：致力于减少对非官方后端的摩擦，帮助第三方代码生成器（protoc 插件）平滑过渡。
- **时间缓冲**：给予 OSS 用户完整的内部迁移周期加上公开弃用期，提供充足的升级窗口。
- **常见模式**：体现了 Google 内部项目向外部迁移的典型做法——对内快速迭代，对外提供稳定、有文档的迁移路径。

## 应用
- **Protobuf 版本迁移**：用于指导 OSS 项目从 proto2/proto3 迁移到 Eds（Editions），确保兼容性。
- **第三方工具生态**：帮助非 Google 维护的 protoc 插件（如 [[entities/rust|rust]] 或 [[entities/c++|C++]] 代码生成器）适配新版 Protobuf 特性。
- **社区沟通与文档**：通过发布迁移指南和工具，建立社区信任，减少升级过程中的不确定性。

## 相关概念
- [[concepts/Edition|Edition]]
- [[concepts/Feature Lifecycle|Feature Lifecycle]]
- [[concepts/Incremental Migration|Incremental Migration]]
- [[concepts/Feature Deprecation Window|Feature Deprecation Window]]

## 相关实体
- [[entities/protobuf-team|protobuf-team]]
- [[entities/Google|Google]]

## 来源提及
- "We want to share a variant of this document with the OSS community." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "We plan to publish migration guides and, where feasible, any migration tooling, such as the `proto2`/`proto3` -> `edition` migrator." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]