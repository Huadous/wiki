---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]"]
tags: [term]
aliases:
  - "基础特征"
  - "Base features"
  - "default features"
---


# Base features

## 定义
Base features（基础特征）是指每一个 edition 在默认情况下所激活的整套语义或语言特性集合。它是 protobuf editions 模型的核心：用户可以通过 `features` 选项对基础特征进行 opt-in 或 opt-out，从而在每个 edition 的默认行为之上自定义特性集合。

## 关键特征
- **Edition 默认行为**：每个 edition 都有一个由其"基础特征集"决定的默认激活特性集合，用户无需显式声明即可获得这些默认行为。
- **语言特定特征的语言自主性**：对于 language-specific features，各语言的代码生成器可以独立地决定给定 edition 下的基础特征集合，并独立定义 edition 之间的迁移路径。
- **语义特征的跨语言一致性**：对于 semantic features，其作用域跨越语言，因此每个语言必须（1）知晓每个 edition 的基础特征规范化集合，或者（2）在 protoc 自身中解析 edition 的默认特征集合并显式传递到 descriptor 中。
- **用户可定制性**：基础特征可以通过 `features` 选项进行 opt-in 或 opt-out，从而在默认集合基础上扩展或缩减特性。
- **迁移路径独立**：每个语言独立定义 edition 之间的迁移路径，迁移过程中基础特征集的变化由各语言自行决定。

## 应用
- **代码生成器的 edition 适配**：各语言代码生成器（如 C++、Java、Go、Python 等）依据自身维护的基础特征表，为给定的 edition 输出符合该语言惯例和迁移路径的代码。
- **protoc 的 descriptor 生成**：protoc 在生成 `FileDescriptorProto` 时，需确保每个语言都能获得一致的语义特征集合，必要时由 protoc 自身解析 edition 的默认特征并显式传递。
- **特性迁移与升级**：当用户从一个 edition 迁移到另一个 edition 时，基础特征集的差异决定了哪些行为会改变，各语言据此提供迁移工具和兼容层。
- **自定义特性集合**：开发者通过 `features` 选项在基础特征之上声明额外启用或禁用的特性，从而构建符合自身需求的特性集合。
- **跨语言一致性保障**：通过对语义特征基础集的规范化定义，确保不同语言在相同 edition 下对同一 `.proto` 文件的语义解释保持一致。

## 相关概念
- [[concepts/edition-keyword|edition keyword]]
- [[concepts/features-option|features option]]
- [[concepts/language-specific-features|Language-specific features]]
- [[concepts/semantic-features|Semantic features]]
- [[concepts/protoc|protoc]]
- [[concepts/converged-semantics|Converged Semantics]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]

## 来源提及
- "Each language's code generator can independently decide what the 'base' set of features is for any given edition. Each language defines the migration path between editions independently." — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]