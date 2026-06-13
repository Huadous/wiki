---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[concepts/self-describing-messages]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "term"
aliases:
  - "动态消息"
  - "Dynamic Message模式"
  - "Dynamic Messages"
  - "动态消息"
  - "Dynamic Message模式"
---

## Related Concepts

- [[concepts/self-describing-messages|自描述消息]]：动态消息的核心实现方式之一，消息自身携带Schema信息。
- [[concepts/schema-on-read|读取时Schema]]：一种数据处理哲学，与动态消息的理念互补，强调在消费端决定数据解释方式。
- [[concepts/protocol-buffers-any|Protocol Buffers Any]]：Google Protobuf的Any类型，允许封装任意序列化消息，是实现动态消息的典型技术。
- [[concepts/edition-defaults|Edition Defaults]]：与运行时特性解析共同决定动态消息的最终行为。
- [[concepts/feature-resolution|Feature Resolution]]（特性解析）：动态消息因绕过 `protoc` 而无法直接套用该规范，需在运行时独立完成。
- [[concepts/descriptor-pool|Descriptor Pool]]：动态消息依赖其在运行时构建 Descriptor 的能力。
- [[concepts/validation-layer|Validation Layer]]：支持动态消息的运行时需额外引入的验证层，确保描述符的合法性。
- [[concepts/overridable-features|overridable_features]]：由 `protoc` 在编译默认值 IR 时打包的特性之一，运行时可基于此完成验证。
- [[concepts/fixed-features|fixed_features]]：由 `protoc` 在编译默认值 IR 时打包的特性之一，运行时可基于此完成验证。
- [[concepts/featureset|FeatureSet]]：动态消息运行时验证所围绕的核心数据结构。
- [[concepts/featuresupport|FeatureSupport]]：影响运行时如何解释和验证动态消息中的特性。
- [[concepts/edition-lifetimes|Edition Lifetimes]]：描述 Edition 演进与运行时支持的完整生命周期，与动态消息的验证时机密切相关。
- [[concepts/runtime-features|Runtime Features]]：动态消息本身就是一类重要的运行时特性。

## Related Entities

- [[entities/brpc|Apache brpc]]：该RPC框架内置对动态消息的支持，可通过解析请求中的元数据选择服务接口版本。
- [[entities/protocol-buffers|Protocol Buffers]]：其Any类型和反射机制是构建动态消息系统的基础工具之一。
- [[entities/apache-kafka|Apache Kafka]]：配合Schema Registry使用动态消息实现事件流的兼容性管理。
- [[entities/protoc|protoc]]：静态代码生成工具，动态消息刻意绕过该工具以获得运行时灵活性；同时也是 IR 中打包 overridable/fixed 特性信息的来源。

## Mentions in Source

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "There's also still the issue of descriptor pools that need to be able to build descriptors at runtime."
> - "**Runtime support for dynamic messages** - while dynamic messages are a less-frequently-used feature, they are a critical feature used by a lot of important systems."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "None of the generators where editions have already been rolled out require any changes. We likely will want to add validation layers to runtimes that support dynamic messages though, to make sure there are no invalid descriptors floating around."
> - "The advantage to splitting them means that we can fairly easily implement validation checks in every language that needs it for dynamic messages."