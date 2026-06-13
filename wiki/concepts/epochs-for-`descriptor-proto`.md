---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"]
tags: [standard]
aliases:
  - "Epochs for descriptor.proto"
  - "Epoch Versioning"
---


# Epochs for `descriptor.proto`

## 定义
**Epochs for `descriptor.proto`** 是一种为 `descriptor.proto` 提出的替代性描述符版本控制机制。它不使用 Protobuf 的 edition 值进行版本标识，而是引入一个独立的版本号（即 "epoch"）来追踪 `descriptor.proto` 的演进。该提案记录于一份未对外公开的独立文档中，在 [[sources/editions-minimum-required-edition|Minimum Required Edition 提案]] 中作为对比方案被讨论，并最终未被采纳。

## 关键特征
- **独立的版本号维度**：不依赖 Protobuf edition 值，而采用专门的版本号（epoch）进行版本标识。
- **低频更新节奏**：epoch 仅在较长时间跨度（3-5 年）内才会递增一次，属于稀疏型版本演进。
- **引入第二版本维度**：会带来与 edition 值并存的第二个版本号，及其独立的演进节奏（cadence）。
- **存在版本号混淆风险**：额外的 epoch 版本号可能与现有 edition 值产生混淆，使版本语义复杂化。
- **同样面临 bootstrapping 难题**：文档指出该方案与 Minimum Required Edition 一样，存在引导（bootstrapping）方面的顾虑。
- **作为替代方案被否决**：在 [[sources/editions-minimum-required-edition|Minimum Required Edition 提案]] 的论证中，因引入冗余版本维度等问题被弃用，转而采用复用 edition total order 的方案。

## 应用
- 该提案主要作为**版本控制机制设计的对比案例**，用于论证为什么 Minimum Required Edition 方案更为优越。
- 可作为研究 Protobuf 描述符演进策略时的**历史参照点**，帮助理解版本号设计中避免冗余维度的重要性。
- 在讨论 `descriptor.proto` 演进路径时，作为**已被否决的替代方案**被引用，以说明版本机制的设计权衡。

## 相关概念
- [[concepts/Minimum Required Edition|Minimum Required Edition]]
- [[concepts/Edition|Edition]]
- [[concepts/Edition Total Order|Edition Total Order]]
- [[concepts/Poison Pill|Poison Pill]]

## 相关实体
- [[entities/descriptor.proto|descriptor.proto]]
- [[entities/FileDescriptorProto|FileDescriptorProto]]

## 来源提及
- "Epochs for `descriptor.proto`" (not available externally) describes a potential issue with bootstrapping. — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]
- Rather than using the editions value, use some other version number. This number would be incremented rarely (3-5 year horizon). This is the approach proposed in "Epochs for `descriptor.proto`." — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]