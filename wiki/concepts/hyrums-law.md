---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "theory"
aliases:
  - "海勒姆定律"
  - "Hyrum's Law"
---

## Description
Hyrum's Law 揭示了一个 API 演进过程中的核心矛盾：开发者无法仅凭文档和契约来约束用户实际依赖的行为集合——任何实现细节、错误模式、性能特征等可见行为，都可能成为下游用户隐式依赖的一部分。在 Protobuf Editions 设计中，该定律被反复引用以论证一系列决策的合理性：在 [[concepts/featureset|FeatureSet]] 层面，将未解析特性（[[concepts/unresolved-features|Unresolved Features]]）仅通过代码生成和运行时辅助函数间接暴露，以避免这些尚未稳定的决策被 Hyrum's Law 固化；在 [[concepts/editions-feature-visibility|Editions Feature Visibility]] 层面，对未解析特性的可见性保持严格限制，以防止大规模修改（[[concepts/large-scale-change|Large-Scale Change]]）被大量隐式依赖所拖累；在 [[concepts/edition-naming|Edition Naming]] 层面，文档反对采用允许无限数量 Edition 名称（如 `2023.a`、`very-cool`）的宽松字符串方案，因为一旦发布就无法收回——用户对这些名称的依赖会通过 Hyrum's Law 形成对未预期行为的固化风险，相比之下，集中定义的枚举方案可以有效避免此类风险。

## Related Concepts
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/edition-naming|Edition Naming]]
- [[concepts/edition-enum|Edition enum]]

## Related Entities
无

## Mentions in Source
> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Users will only be exposed to them indirectly, via codegen changes or runtime helper functions, in order to avoid Hyrum's law cementing every decision we make about them."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "If people have easy access to unresolved features though, we can expect a lot of Hyrum's law issues slowing down these large-scale changes."
> - "Deciding to loosen this in the future would be a bit awkward for `options()`. If we stop stripping it, people will suddenly start seeing a new field and Hyrum's law might result in breakages."

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "There's also a very real Hyrum's law risk when we permit an infinite number of edition names that we never expect to exist in practice."
> - "Leaves us open to Hyrum's law and unexpected abuse"