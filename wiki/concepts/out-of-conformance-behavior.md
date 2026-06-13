---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "non-conformance preservation"
  - "preserving idiosyncratic behavior"
  - "out-of-conformance quirks"
---


# Out-of-conformance behavior

## 定义
Out-of-conformance behavior 是 Edition Zero 中确立的一项设计原则：对于现有各语言实现偏离已记录的 proto2/proto3 语义的行为，Edition Zero 必须予以保留（preserve）而非修复（fix）。其根本理由在于 proto2/proto3 向 Editions 的迁移是以 Large-Scale Change（LSC）的形式执行的，只有保留这些历史遗留的差异（quirks），该 LSC 对现有用户而言才能是 no-op。该原则将"定义 Edition Zero 的 features 与 semantics"明确划入 in-scope 工作，而将"修复各语言代码生成器以完美匹配这些 semantics"明确划入 out-of-scope 工作。

## 关键特征
- **保留优先（Preservation over Correction）**：明确反对在 Edition Zero 阶段统一修正各语言实现的语义偏差。
- **LSC 兼容性约束**：原则的成立依赖于迁移以 LSC 形式进行；任何会改变现有 wire 行为或运行时行为的"修正"都会破坏 LSC 的 no-op 性质。
- **职责边界清晰**：语义定义（in-scope）与代码生成器修正（out-of-scope）分离，避免 Edition Zero 范围蔓延。
- **承认现状混乱（Status Quo is Messy）**：承认当前各语言实现存在与 proto2/proto3 文档语义不一致的区域，并将这种混乱作为既定事实接受。
- **具体例子：Go 的 proto2 enum 不实现 closed-enum 语义**，尽管文档理应如此，但 Edition Zero 仍需保留这一行为。

## 应用
- 在定义 Edition Zero 各 feature（如 field presence、enum 类型、默认值处理等）的语义时，不应假设所有语言实现已严格遵循这些语义，而应在文档中说明各语言的实际表现。
- 在制定 proto2/proto3 → Editions 的迁移工具链时，保证同一份 `.proto` 文件在迁移前后生成的代码行为一致（包括已知的偏差），从而实现用户无感升级。
- 为后续 Editions（如 Edition 2024 等）的"语义收敛"（[[concepts/converged-semantics|Converged semantics]]）工作留下明确的起点：Edition Zero 是"保留分歧"的状态，后续 Edition 再逐步统一。
- 用于指导各语言代码生成器维护者：Edition Zero 阶段不应合入"修复语义偏差"的 PR，因为其属于 out-of-scope。

## 相关概念
- [[concepts/large-scale-change|Large-Scale Change]]
- [[concepts/converged-semantics|Converged semantics]]
- [[concepts/closed-enum|closed enum]]
- [[concepts/open-enum|open enum]]
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/proto3-syntax|proto3 syntax]]

## 相关实体
- [[entities/edition-zero|Edition Zero]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/google3|google3]]

## 来源提及
- "We must keep in mind that the status quo is messy. Many languages have some areas where they currently diverge from the correct proto2/proto3 semantics." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- "For edition zero, we must preserve these idiosyncratic behaviors, because that is the only way for a proto2/proto3 -> editions LSC to be a no-op." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]