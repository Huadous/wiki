---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-edition-zero-converged-semantics]]"]
tags: [term]
aliases:
  - "features"
  - "features option"
---


# features option

## 定义
`features` 选项是 `descriptor.proto` 中提议新增的一个描述符选项（descriptor option），被统一定义为可重复的字符串集合（repeated set of strings）。其核心用途是允许通过 `features` 字段对描述符所代表的特性进行声明，既可以以 `-` 前缀语法 opt-out 一个特性（例如 `"-string_view"`），也可以 opt-in 一个未来或实验性的特性（例如 `"string_view"`）。该选项仅在与 `edition` 关键字配合时生效。

## 关键特征
- 统一定义为 `repeated string`，以可重复字符串集合的形式编码特性声明。
- 支持 opt-out 语义：通过 `-` 前缀禁用一个特性，如 `"-string_view"`。
- 支持 opt-in 语义：用于启用未来或实验性特性，如 `"string_view"`。
- 作用范围广，将被加到 File、Message、Field、Enum、Enum Value、Oneof、Service、Method 以及内部 Stream 等多种描述符上。
- 仅在 [[concepts/edition-keyword|edition keyword]] 配合下生效，不依赖传统 proto2/proto3 语法。
- 不进行正确性校验（correctness check），以保证前向/后向兼容性。
- 特性可声明于任何描述符层级，并可能影响（affect）其后代类型（descendant types）。

## 应用
- 作为 [[concepts/converged-semantics|Converged Semantics]] 提案中的核心描述符选项，用于替代分散的布尔开关（boolean toggles）。
- 与 [[concepts/edition-keyword|edition keyword]] 联合使用，构成 [[entities/edition-zero|Edition Zero]] 中特性的声明与激活机制。
- 支持语言相关特性（Language-specific features）以及语义特性（Semantic features）的统一注册与表达。
- 为 [[entities/descriptor.proto|descriptor.proto]] 在不同层级（文件、消息、字段、枚举、枚举值、oneof、服务、方法、流）提供一致的特性扩展入口。

## 相关概念
- [[concepts/edition-keyword|edition keyword]]
- [[concepts/language-specific-features|Language-specific features]]
- [[concepts/semantic-features|Semantic features]]
- [[concepts/converged-semantics|Converged Semantics]]

## 相关实体
- [[entities/descriptor.proto|descriptor.proto]]
- [[entities/edition-zero|Edition Zero]]

## 来源提及
- This option will be uniformly defined as a repeated set of strings which can be used to encode the ability to opt-out of a specific feature (eg: `"-string_view"`), or to potentially opt-in to a future/experimental feature (eg: `"string_view"`). — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]