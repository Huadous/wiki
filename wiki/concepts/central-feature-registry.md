---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "中央特性注册表"
  - "Central Feature Registry"
  - "CFR"
---


# Central Feature Registry

## 定义
Central Feature Registry（中央特性注册表）是一种在 Protobuf Editions 设计中被讨论过的替代方案。该方案主张将所有已知的 feature proto 提交到一个统一的中央注册表中，而不是依赖各 generator 通过 import 机制使其特性可被 protoc 发现。在源文档中，该方案被明确列为一种**被拒绝的备选设计（rejected alternative）**，并未被实际采纳。

## 关键特征
- **集中式注册**：所有 generator 拥有的 feature proto 不再通过 import 传递，而是必须提交至一个中央特性仓库。
- **替代 import 发现机制**：不再仅凭"声明一个扩展号"即可使用特性，而是要求特性 proto 在注册表中登记。
- **两种设想的实现路径**：
  1. 将注册表集成进 protoc 本身，并有可能最终**取消 import 需求**；
  2. 保留现有的 extension/import 方案，但让 protoc 显式依赖每一个已注册的特性。
- **主要收益**：实现特性的普遍可发现性（universal feature discoverability），并消除特性描述在多个 generator 之间重复维护的问题。
- **已知缺点**：
  - 未能解决运行时的代码体积与内存开销问题；
  - 引入令人困惑的**版本偏移（version skew）**；
  - 引入了复杂的**所有权语义（ownership semantics）**问题。

## 应用
本概念在源文档中仅作为被拒绝的备选方案出现，未被实际部署到任何 Protobuf Editions 实现中。它的提出主要用于：
- 在 [[sources/editions-editions-life-of-a-featureset]] 文档中作为对比基线，衬托最终采用的 [[concepts/Feature Resolution|特性解析]] 方案的合理性；
- 展示 Protobuf Editions 在特性发现机制设计上的权衡考量，凸显[[concepts/Generator Features|生成器特性]]在生态中分布式的现实约束。

## 相关概念
- [[concepts/Generator Features]]
- [[concepts/Feature Resolution]]
- [[concepts/Option Retention]]
- [[concepts/Descriptor Pool]]

## 相关实体
- [[entities/protoc]]
- [[entities/descriptor.proto]]

## 来源提及
- "Instead of relying on generators and imports to supply feature specs, we could pivot to a central registry of all known features. Instead of simply claiming an extension number, generator owners could be required to submit all the feature protos to a central repository of feature protos." — [[sources/editions-editions-life-of-a-featureset]]