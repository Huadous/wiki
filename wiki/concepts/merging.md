---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence|field_presence]]"]
tags: [method]
aliases:
  - "Merging"
  - "merge-from"
  - "merge semantics"
---


# Merging

## 定义
Merging（合并）是 Protocol Buffers 中的一项 API 操作，用于将一个源消息（source message）的字段值更新到另一个目标消息（target message）中。该操作的行为在不同的字段存在性（field presence）规则下有本质区别。

## 关键特征
- **API 操作语义**：Merging 是 Protobuf 提供的运行时 API 操作，用于在两个消息实例之间传递字段值。
- **与 field presence 强耦合**：Merging 的行为直接受字段存在性规则的约束，不同 presence 模式下语义不同。
- **No presence 规则下的限制**：在 no presence 规则下，默认值（default value）在序列化时被跳过，因此目标字段实际上无法通过 Merging 从默认值进行更新——仅靠 patch 更新无法表示对默认值的更新。
- **Explicit presence 规则下的行为**：在 explicit presence 规则下，所有显式设置的值（包括与默认值相同的值）都会从源消息合并到目标消息。
- **影响部分更新协议的正确性**：对于依赖部分 patch 更新（例如 [[entities/fieldmask|google.protobuf.FieldMask]]）的协议，presence 跟踪能力直接影响 Merging 操作的正确性。

## 应用
- **增量更新（Incremental Updates）**：在分布式系统中使用 Merging API 将客户端的部分更新请求应用到服务端已有状态。
- **Patch 更新协议**：结合 [[entities/fieldmask|FieldMask]] 实现按字段粒度的部分更新，此时 Merging 的语义决定了哪些字段变化能被正确捕获与传播。
- **消息合并与覆盖**：在配置加载、默认值合并等场景中，将来自多个源的配置消息合并为最终消息。
- **跨版本兼容性处理**：在 proto 演进过程中使用 Merging 将旧消息字段值迁移到新消息结构中。

## 相关概念
- [[concepts/field-presence|Field presence]]
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/default-value|Default value]]
- [[concepts/fieldmask|FieldMask]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- Under the _no presence_ rules, it is effectively impossible for a target field to merge-from its default value (using the protobuf's API merging functions). — [[sources/field_presence|field_presence]]
- This is because default values are skipped, similar to the _no presence_ serialization discipline. — [[sources/field_presence|field_presence]]