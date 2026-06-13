---
type: source
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[protobuf/editions-README.md]]"
tags:
  - "document"
  - "protobuf"
  - "editions"
  - "features"
  - "migration"
aliases:
  - "Protobuf Editions 介绍文档"
  - "What are Protobuf Editions"
---

---

# What are Protobuf Editions? - Summary

## 来源
- Original file: [[protobuf/editions-what-are-protobuf-editions.md]]
- Ingested: 2026-06-12

## 核心内容

本文是 [[entities/protobuf-editions|Protobuf Editions]] 项目的介绍文档，阐述了一个旨在替代传统 `syntax` 声明、实现 Protobuf 生态系统渐进式演进的新机制。文档引入 **Edition** 和 **Feature** 两大核心概念：Edition 是按年编号的版本，定义了所有 Feature 的默认值；Feature 是控制代码生成和运行时行为的细粒度选项，具有 [[concepts/feature-inheritance|Feature Inheritance]] 机制。首个版本 [[concepts/edition-zero|Edition Zero]] 合并了 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]] 的语义，支持无行为变化的机械迁移。该设计受 [[entities/rust|Rust]] editions 和 [[entities/carbon|Carbon]] 语言启发，核心目标是避免生态分裂，允许不同版本间互操作。文档还详细描述了 [[concepts/feature-lifecycle|Feature Lifecycle]]、[[concepts/oss-strategy|OSS Strategy]] 以及未来计划，包括移除 `required`、统一枚举处理、优化 C++ 字符串访问等。

## 关键实体

- [[entities/protocol-buffers|Protocol Buffers]] —— 核心序列化框架，本文演进机制的目标对象
- [[entities/protobuf-editions|Protobuf Editions]] —— 文档介绍的版本演进项目
- [[entities/google|Google]] —— Protobuf 的维护组织，主导 Editions 项目
- [[entities/protoc|protoc]] —— Protobuf 编译器，负责解析 Edition 和处理 Feature
- [[entities/rust|Rust]] —— 其 edition 机制是 Protobuf Editions 的设计灵感
- [[entities/carbon|Carbon]] —— 演化哲学相似的参考语言
- [[entities/protobuf-team|protobuf-team]] —— Google 内部负责 Protobuf 开发和维护的团队
- [[entities/c++|C++]] —— 主要的代码生成目标语言，有大量语言特定改进计划

## 关键概念

- [[concepts/edition|Edition]] —— 按年编号的版本集合，定义了所有 Feature 的默认值
- [[concepts/feature|Feature]] —— 控制代码生成和运行时行为的细粒度选项
- [[concepts/feature-inheritance|Feature Inheritance]] —— 父实体 Feature 值自动传递给子实体的机制
- [[concepts/edition-zero|Edition Zero]] —— 首个 Edition，合并 proto2 和 proto3 语义
- [[concepts/proto2|proto2]] —— Protobuf 的第二个主要语法版本
- [[concepts/proto3|proto3]] —— 导致生态分裂的上一次激进语言变更
- [[concepts/feature-lifecycle|Feature Lifecycle]] —— Feature 从引入到移除的完整演进过程
- [[concepts/oss-strategy|OSS Strategy]] —— 面向外部社区的迁移策略
- [[concepts/incremental-migration|Incremental Migration]] —— 循序渐进的迁移原则
- [[concepts/reflection|Reflection]] —— 需要升级以兼容 Editions 的动态类型机制
- [[concepts/language-scoped-feature|Language-scoped Feature]] —— 针对特定语言代码生成后端的 Feature

## 要点

- **Editions 替代 Syntax**：使用 `edition = "2025"` 声明替代 `syntax` 声明，允许按年发布新版本。
- **Feature 提供细粒度控制**：通过继承机制在文件、消息、字段级别控制行为，减少重复声明。
- **Edition Zero 兼容性**：合并 proto2 和 proto3 的全部语义，支持无行为变化的机械迁移。
- **不分裂生态**：不同 Edition 的消息可以互操作，类似 Rust editions 的设计哲学。
- **自动化迁移工具**：内部使用 [[concepts/lsc|LSC（大规模变更）]] 自动化迁移，外部提供工具和指南。
- **可预测的 Feature 生命周期**：Feature 经历引入→默认值调整→弃用→移除的完整流程，用户有足够时间迁移。