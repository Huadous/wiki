---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "required whitelist"
  - "required 白名单"
  - "LEGACY_REQUIRED allowlist"
---


# Required allowlist

## 定义
Required allowlist（required 白名单）是 Protobuf Edition Zero 中用于控制 `LEGACY_REQUIRED` 字段使用范围的访问控制机制。当一个字段被设置为 `features.field_presence = LEGACY_REQUIRED` 时，要求该字段所在的文件必须位于 `required` allowlist 中，否则会触发错误。该机制与传统的 `proto:allow_required` 开关并列为两种实现方式，其核心目的是限制 wire-required 字段的引入，为未来彻底消除 `required` 创造条件。

## 关键特征
- **访问控制机制**：通过白名单限制哪些文件可以声明 `LEGACY_REQUIRED` 字段，不在白名单中的文件使用该字段会触发错误。
- **与 `LEGACY_REQUIRED` 强绑定**：仅当字段的 `features.field_presence` 设置为 `LEGACY_REQUIRED` 时，该白名单才会生效。
- **两种实现方式之一**：与传统的 `proto:allow_required` 开关并列为实现字段存在性控制的两种途径。
- **安全性设计的一部分**：属于 Edition Zero 安全性设计的一环，旨在避免新代码无节制地引入 wire-required 字段。
- **过渡性机制**：作为从 proto3 向完全消除 `required` 关键字过渡的中间方案存在。
- **可扩展性**：文档建议采用与 `required` 类似的 sidecar allowlist 模式，该扩展与现有机制大致正交。

## 应用
- **Edition Zero 中的字段存在性控制**：在采用 Edition Zero 的项目中，通过 `required` allowlist 管理哪些 `.proto` 文件可以使用 `LEGACY_REQUIRED`，从而对遗留 `required` 字段的使用范围进行细粒度管控。
- **迁移到 Editions 的过渡期管理**：在将既有 schema 从 proto3 迁移到 Editions 时，借助白名单有序地处理遗留 `required` 字段，避免大规模 schema 变更带来的风险。
- **为彻底移除 `required` 铺路**：通过限制新增 `LEGACY_REQUIRED` 字段，配合后续 Edition 的演进，最终实现完全消除 `required` 关键字的目标。
- **Sidecar allowlist 扩展**：当未来需要为其他字段特性引入类似机制时，可参考 `required` allowlist 的 sidecar 模式进行扩展。

## 相关概念
- [[concepts/LEGACY_REQUIRED|LEGACY_REQUIRED]]
- [[concepts/required-keyword|required keyword]]
- [[concepts/features-field-presence|features.field_presence]]

## 相关实体
无相关实体。

## 来源提及
- "LEGACY_REQUIRED - the field is wire-required and API-optional. Setting this will require being in the `required` allowlist." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- "Add a sidecar allowlist like we do for `required`. This is mostly orthogonal." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]