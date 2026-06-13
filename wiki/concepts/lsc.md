---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "method"
aliases:
  - "Large-Scale Change"
  - "大规模变更"
  - "Large-scale Change"
  - "Large-Scale Change"
  - "大规模变更"
---

## Description
Large-Scale Change (LSC) 是 Google 内部用于在整个代码库中执行大规模自动化重构的工具和流程。在 Editions 体系中，LSC 是将 proto2 与 proto3 文件批量迁移到 editions 语法的关键手段——文档明确指出"proto2/proto3 → editions LSC"必须是一个 no-op（即不产生语义变化），这意味着 Edition Zero 必须在迁移前后保持行为一致，才能让大规模自动替换安全进行。LSC 同样被用于执行 Editions 的"消亡"流程：不再需要的特性会被 LSC 从代码库中批量移除，模板与普通的 feature/edition 迁移一致。LSC 在 Edition 升级中的角色由 proto 团队主导，他们负责每年将新 edition 推送到 Google 内部仓库（根据 churn policy 至少覆盖 80%）。然而，如果未解决的特性（unresolved features）被轻易开放访问，将触发海勒姆定律（Hyrum's Law），大量用户依赖这些未公开保证的行为，从而显著拖慢大规模变更的推进速度。

在 Edition Zero 的具体迁移方案中，LSC 的工作量可以通过具体数字体现：迁移过程需要通过 LSC 删除 google3 中所有 385,236 个 `optional` 实例，并处理 proto2 文件到 editions 的转换。许多遗留特性（如 `required`）的兼容支持也依赖于 LSC 级别的 allowlist 机制，在不引入语义变化的前提下完成语法替换。

## Related Concepts
- [[concepts/Feature|Feature]]
- [[concepts/Edition|Edition]]
- [[concepts/Edition Zero|Edition Zero]]
- [[concepts/Immolation of required|Immolation of required]]
- [[concepts/Unresolved Features|Unresolved Features]]
- [[concepts/Resolved Features|Resolved Features]]
- [[concepts/Hyrum's Law|Hyrum's Law]]
- [[concepts/Editions Feature Visibility|Editions Feature Visibility]]
- [[concepts/proto2 syntax|proto2 syntax]]
- [[concepts/proto3 syntax|proto3 syntax]]
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/LEGACY_REQUIRED|LEGACY_REQUIRED]]
- [[concepts/required keyword|required keyword]]
- [[concepts/optional keyword|optional keyword]]

## Related Entities
- [[entities/Google|Google]]
- [[entities/Protobuf Editions|Protobuf Editions]]
- [[entities/protoc|protoc]]
- [[entities/Prototiller|Prototiller]]
- [[entities/Editions|Editions]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Undesirable features will be LSC'd away, using the same template as any other feature/edition migration."
> - "The migration to edition "2025" across google will move very fast as it is a no-op."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "How to use Protobuf Editions to construct a large-scale change that modifies the semantics of Protobuf in some way."
> - "The following are sketches of large-scale change designs for feature changes we would like to execute, presented as example use-cases."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "Bumpy Edition Large-scale Change - The proto team is going to be responsible for rolling out the next edition to internal Google repositories every year (at least 80% of it per our churn policy)."
> - "If people have easy access to unresolved features though, we can expect a lot of Hyrum's law issues slowing down these large-scale changes."

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "For edition zero, we must preserve these idiosyncratic behaviors, because that is the only way for a proto2/proto3 -> editions LSC to be a no-op."
> - "Migration will require deleting every instance of `optional` in proto files in google3, of which there are 385,236."