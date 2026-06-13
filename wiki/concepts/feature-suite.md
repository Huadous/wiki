---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues]]"]
tags: [method]
aliases:
  - "Feature Suite"
  - "Per-language features"
  - "每语言功能拆分方案"
---


# Feature Suite

## 定义
Feature Suite 是文档 [[sources/editions-group-migration-issues]] 中提出的一种备选方案，作为对 "Global Feature" 方案的扩展。该方案将代码生成（codegen）的相关变更拆分为独立的、针对每种语言的功能（per-language features），从而分别控制 API 层面的破坏性变更与 "wire"（序列化格式）层面的破坏性变更。

## 关键特征
- **per-language 拆分**：将原本集中的 codegen 变更拆分为独立的、按语言划分的 feature，每个 feature 对应一种语言的代码生成行为变化。
- **API 与 wire 变更分离**：将破坏性变更分为两类——影响用户 API 的变更与影响序列化格式（wire）的变更，二者可独立演进。
- **更好的迁移体验**：由于上述分离，用户可以分别处理 API 兼容性问题与 wire 兼容性问题，迁移路径更加清晰。
- **复杂度上升**：需要新增大量 per-language feature，其中很多 feature 在首次配置时较为困难；并且每个需要在 edition 间保持兼容的运行时（runtime）都必须进行协调修改，显著增加 edition 2023 的整体复杂度。

## 应用
- 作为 Protobuf Editions（edition 2023）迁移方案设计中的一种备选方案提出。
- 适用于希望精细化控制 API 与 wire 兼容性的迁移场景，使用户可以分阶段升级而不必一次性接受所有破坏性变更。
- 与 [[concepts/global-feature]] 方案形成对比：当后者粒度不够、不利于分别管理 API 与 wire 变更时，Feature Suite 作为更细粒度的替代选择。

## 相关概念
- [[concepts/global-feature]]
- [[concepts/edition-2023]]
- [[concepts/codegen]]
- [[concepts/delimited-encoding]]

## 相关实体
无相关实体。

## 来源提及
- "An extension of [Global feature](?tab=t.0#heading=h.mvtf74vplkdg) would be to split the codegen changes out into separate per-language features." — [[sources/editions-group-migration-issues]]
- "Better migration story for users, since it separates API and "wire" breaking changes" — [[sources/editions-group-migration-issues]]