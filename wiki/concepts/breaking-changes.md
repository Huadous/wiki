---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"]
tags: [term]
aliases:
  - "Schema Breaking Changes"
  - "破坏性变更"
---


# Breaking Changes

## 定义
在 Protobuf Schema 演进的语境下，"破坏性变更"（Breaking Changes）特指任何会**提高 schema 最低必需版本（Minimum Required Edition）**的改动。其原因在于：基于更新后 schema 编译得到的 descriptor 在运行时将无法被那些支持的最高版本低于该最低必需版本的旧 runtime 所加载。从广义上讲，这一概念适用于任何使用"最低版本门控"（minimum-version gate）机制的 schema 演进体系。

## 关键特征
- **触发条件**：对 schema 进行的任何使其最低必需版本（Minimum Required Edition）数值变大的修改。
- **运行时后果**：基于新 schema 编译生成的 descriptor 将无法在旧版 runtime 中加载，因为旧 runtime 所支持的 Edition 范围达不到新 schema 所要求的下限。
- **生产者责任**：schema 生产者应当将任何提高最低必需版本号的改动视为破坏性变更，因为该改动会阻断已编译 descriptor 的运行时加载。
- **可推广性**：该概念可推广到所有采用"最低版本门控"作为兼容性约束的 schema 演进机制。

## 应用
- **Protobuf Editions 兼容性规划**：在升级 `.proto` 文件引入新 Edition 特性时，评估该改动是否会抬高最低必需版本，并据此判断其是否属于破坏性变更。
- **版本发布与回滚策略**：由于提高最低必需版本会破坏旧 runtime 加载能力，相关改动需在发布说明中明确标记，并配合版本号与升级窗口谨慎推进。
- **跨 runtime 互操作**：在多语言、多 runtime 共同消费同一份编译产物的场景下，避免无意识地抬升最低必需版本，以维持下游消费方的向后兼容。
- **一般 Schema 演进治理**：作为一条通用准则，提示设计者慎重对待任何抬升"最低支持版本"门槛的演进决定。

## 相关概念
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-total-order|Edition Total Order]]

## 相关实体
- [[entities/descriptor-proto|descriptor.proto]]
- [[entities/file-descriptor-proto|FileDescriptorProto]]

## 来源提及
- "Schema producers should consider changes to their schemas that increase the minimum required edition to be breaking changes, since it will stop compiled descriptors from being loaded at runtime." — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]