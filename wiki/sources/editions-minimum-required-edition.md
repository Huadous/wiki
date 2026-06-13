---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/editions-minimum-required-edition.md]]"
tags:
  - Minimum Required Edition
  - FileDescriptorProto
  - descriptor.proto
  - Edition
  - Edition Total Order
  - Poison Pill
  - 'Epochs for `descriptor.proto`'
  - Bootstrapping
  - Breaking Changes
aliases: ["最低必需版本机制", "Minimum Required Edition 提案"]
---

# Minimum Required Edition - Summary

## 来源
- Original file: [[protobuf/editions-minimum-required-edition.md]]
- Ingested: 2026-06-13

## 核心内容
本文档由 [[entities/@mcy|@mcy]] 提出并于 2022-11-15 获得批准，描述了一种名为"最低必需版本"（Minimum Required Edition）的 Protobuf 描述符版本控制机制。其核心思路是在 [[concepts/filedescriptorproto|FileDescriptorProto]] 中新增 `minimum_required_edition` 字段，作为防止旧版运行时加载包含未知特性描述符的 [[concepts/poison-pill|毒丸机制]]：每个 [[entities/protobuf|Protobuf]] 运行时需声明自身能处理的最新 [[concepts/edition|Edition]]，若描述符所要求的最低版本超出运行时支持范围，则加载失败。[[entities/protoc|protoc]] 编译器自动追踪文件中各构造所需的最低版本，确保仅在实际使用新特性时才提升该值。文档还讨论了 [[concepts/bootstrapping|引导编译]]问题，比较了多种替代方案（包括 [[concepts/epochs-for-`descriptor-proto`|Epochs for `descriptor.proto`]]），最终建议在 protoc 前端中完整实现该逻辑。

## 关键实体
- [[entities/@mcy|@mcy]] —— 文档作者，提案提出者
- [[entities/protobuf|Protobuf]] —— 版本控制机制的载体
- [[entities/protoc|protoc]] —— 负责追踪与计算最低必需版本的编译器
- [[entities/protobuf-editions|Protobuf Editions]] —— 提供按年递增的 Edition 概念
- [[entities/prototiller|Prototiller]] —— 用于在不提升最低必需版本的前提下升级文件 Edition

## 关键概念
- [[concepts/minimum-required-edition|Minimum Required Edition]] —— 核心机制，描述符中的最低版本要求字段
- [[concepts/filedescriptorproto|FileDescriptorProto]] —— 新增字段的承载消息类型
- [[concepts/descriptor-proto|descriptor.proto]] —— Protobuf 的元模式文件
- [[concepts/edition|Edition]] —— Protobuf Editions 引入的版本概念
- [[concepts/edition-total-order|Edition Total Order]] —— Edition 之间的全序比较算法
- [[concepts/poison-pill|Poison Pill]] —— 拒绝旧运行时加载过新描述符的兼容性策略
- [[concepts/epochs-for-`descriptor-proto`|Epochs for `descriptor.proto`]] —— 被否决的替代方案
- [[concepts/bootstrapping|Bootstrapping]] —— 编译器自举问题
- [[concepts/breaking-changes|Breaking Changes]] —— 提升最低必需版本的变更被视为破坏性变更

## 要点
- 最低必需版本机制通过在 [[concepts/filedescriptorproto|FileDescriptorProto]] 中新增 `minimum_required_edition` 字段，防止旧版运行时加载包含其不支持特性的描述符。
- [[entities/protoc|protoc]] 编译器需精确计算每个 `.proto` 文件实际所需的最低版本，仅在文件实际使用需要特定版本支持的构造时才提升该值。
- [[concepts/edition|Edition]] 的按年递增特性使其天然适合充当 [[concepts/poison-pill|毒丸机制]]，无需运行时实现复杂的特性探测逻辑。
- 升级 protoc 编译器本身以及通过 [[entities/prototiller|Prototiller]] 升级文件 edition 不应提升最低必需版本。
- [[concepts/bootstrapping|引导编译]]方面不存在问题：[[concepts/descriptor-proto|descriptor.proto]] 等元模式文件不会立即使用新特性，因此新特性的引入不会破坏 protoc 编译自身的能力。
- Schema 维护者应将任何会提升最低必需版本的变更视为 [[concepts/breaking-changes|破坏性变更]]，因为它会导致旧版运行时无法加载编译后的描述符。
- 文档建议在 protoc 前端中完整实现最低必需版本的计算逻辑，以集中管理版本追踪职责。
- 文档比较了多种替代方案（包括独立 epoch 版本号、不保证最低版本最小化、以及不做任何变更），并最终推荐采用本文提出的方案。