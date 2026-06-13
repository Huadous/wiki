---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [method]
aliases:
  - "增量迁移"
  - "Incremental evolution"
  - "gradual migration"
---


# Incremental Migration

## 定义
Incremental Migration（增量迁移）是Protobuf Editions设计的核心原则，强调通过逐步、非破坏性的方式演进整个生态，避免一次性断裂式升级。用户和项目可以根据自身节奏，逐个文件独立升级到新版本，而不需要整个组织或仓库同时迁移。

## 关键特征
- **非断裂性（Non-breaking）**：迁移过程不破坏现有.proto文件的行为，允许新旧版本共存于同一生态中。
- **独立升级**：每个.proto文件可以独立选择Edition和Feature，不强制全局同步升级。
- **自动化工具支持**：通过Feature inheritance和工具链（如`protoc`），多数迁移步骤可自动化完成，用户几乎无感。
- **借鉴成功经验**：设计灵感来源于[[entities/rust|Rust]]和Carbon等语言的渐进式演进策略。
- **无永久分叉**：每个Edition都是临时的、可废弃的，社区始终跟随最新Edition，避免语言长期分裂。

## 应用
- **跨组织协作**：在大型组织中，不同团队可以按自身时间表从Proto2/Proto3迁移至Protobuf Editions，降低协调成本。
- **遗留系统升级**：对包含大量历史.proto文件的代码库，允许逐步迁移，避免一次性重构风险。
- **生态共融**：在Protobuf生态内，新Edition发布后，旧Edition仍然可用，但会被标记为废弃，指引用户平滑过渡。

## 相关概念
- [[concepts/edition|Edition]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/lsc|LSC]]

## 相关实体
- [[entities/rust|Rust]]
- [[entities/carbon|Carbon]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protobuf-team|protobuf-team]]

## 来源提及
- "enable incremental evolution of Protobuf across the entire ecosystem **without** introducing permanent forks in the Protobuf language." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Arguably the biggest hard-earned lesson among Software Foundations is that successful migrations are incremental." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]