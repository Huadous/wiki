---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [standard]
aliases:
  - "Submessages encoding paper"
  - "Submessages 编码文档"
---


# Submessages: In Pursuit of a More Perfect Encoding

## 定义
Submessages: In Pursuit of a More Perfect Encoding 是 Google 内部的一份设计文档，副标题"In Pursuit of a More Perfect Encoding"体现了其追求更优编码方式的核心理念。该文档旨在将整个 protobuf 生态系统迁移到全面使用 delimited encoding（定界编码）替代旧的 group 语法，目前外部尚不可访问。

## 关键特征
- **内部文档**：由 Google 内部维护，尚未对外公开。
- **迁移目标导向**：长期目标是将 protobuf 生态系统全面迁移至 delimited encoding。
- **替代 group 语法**：明确意图用 delimited encoding 取代传统 group 编码方式。
- **生态影响深远**：文档的存在使得 edition 2023 中 delimited encoding 功能的缺陷问题变得更加紧迫，因为该功能本是为了支持这一长期迁移目标而设计的"迁移工具"。
- **追求更优编码**：副标题"In Pursuit of a More Perfect Encoding"强调对更完善编码方案的持续追求。

## 应用
- 为 protobuf edition 2023 中 delimited encoding 功能的设计提供战略方向。
- 作为 group 字段迁移到 delimited encoding 的长期路线图依据。
- 推动 protobuf 生态系统中编码方式的统一与优化。

## 相关概念
- [[concepts/Delimited encoding|Delimited encoding]]
- [[concepts/Edition 2023|Edition 2023]]
- [[concepts/Group fields|Group fields]]

## 相关实体
无相关实体。

## 来源提及
- All of this is especially problematic in light of *Submessages: In Pursuit of a More Perfect Encoding* (not available externally yet), which intends to migrate the ecosystem to use delimited encoding everywhere. — [[sources/editions-group-migration-issues|editions-group-migration-issues]]