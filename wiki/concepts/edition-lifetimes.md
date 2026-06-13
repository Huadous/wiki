---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme|editions-readme]]"]
tags: [term]
aliases:
  - "Edition 寿命"
  - "Edition Lifetimes Document"
---


# Edition Lifetimes

## 定义
**Edition Lifetimes**（Edition 寿命文档）是 Protobuf Editions 设计文档体系中专门定义 Edition 版本支持周期与长期维护策略的设计文档。它规定了每个 Edition 版本的发布时点、活跃支持期、扩展维护期以及最终废弃的具体时间线，是 Editions 长期演进策略与向后兼容性保证的制度基础。

## 关键特征
- **版本支持周期制度化**：明确定义 Edition 的发布、活跃支持、扩展维护、废弃四个阶段的时间线。
- **与版本演进策略强绑定**：与 [[concepts/life-of-an-edition|Life of an Edition]] 共同构成 Edition 生命周期管理的核心机制。
- **兼容性窗口可预测**：为生产者和消费者提供清晰的升级窗口与版本兼容性预期。
- **长期维护承诺**：通过文档化的时间线保证 Edition 在可预见的时间段内获得官方支持。
- **废弃流程透明**：为 Edition 的最终废弃设定明确的时间表，避免维护方与使用方出现预期偏差。

## 应用
- **版本升级规划**：使用 Editions 的团队据此规划内部库、服务的升级路径与时间节点。
- **生态工具适配**：Protobuf 编译器、运行时、各语言 binding 依据 Edition 寿命文档决定支持范围。
- **企业生产决策**：生产者在评估长期维护成本时，参考 Edition Lifetimes 选择目标 Edition。
- **跨语言互操作**：消费者根据各 Edition 的活跃期判断版本组合的互操作性风险。
- **Editions 文档体系索引**：作为 [[sources/editions-readme|editions-readme]] 中列出的核心设计文档之一，与 [[sources/editions|editions]] 等文档协同构成完整参考体系。

## 相关概念
- [[concepts/life-of-an-edition|Life of an Edition]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "The following topics are in this repository: — [[sources/editions-readme|editions-readme]]"
- "[Edition Lifetimes](edition-lifetimes.md) — [[sources/editions-readme|editions-readme]]"