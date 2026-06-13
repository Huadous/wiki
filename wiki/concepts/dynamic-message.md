---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[concepts/self-describing-messages]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
tags:
  - "term"
aliases:
  - "动态消息"
  - "Dynamic Message模式"
  - "Dynamic Messages"
  - "动态消息"
  - "Dynamic Message模式"
---

## Description

动态消息是 protobuf 生态中在运行时构建和操作消息的能力，其核心特征是绕过 `protoc` 的静态代码生成流程，直接通过运行时机制构造、序列化与反序列化消息对象。现有资料强调，动态消息虽然使用频率不高，却是被许多重要系统所依赖的关键特性（critical feature），因此在特性解析（Feature Resolution）体系中必须被显式处理——它们不能简单地遵循为静态生成代码所设计的特性解析规范。文档提出的解决思路是：让所有运行时独立完成特性解析，使动态消息与通过 `protoc` 编译得到的文件处于同等地位，从而避免在用户开发体验上产生不一致。此外，动态消息的实现还面临 Descriptor Pool 必须在运行时构建 Descriptor 的问题，这也对底层基础设施提出了额外要求。

## Related Concepts

- [[concepts/self-describing-messages|自描述消息]]：动态消息的核心实现方式之一，消息自身携带Schema信息。
- [[concepts/schema-on-read|读取时Schema]]：一种数据处理哲学，与动态消息的理念互补，强调在消费端决定数据解释方式。
- [[concepts/protocol-buffers-any|Protocol Buffers Any]]：Google Protobuf的Any类型，允许封装任意序列化消息，是实现动态消息的典型技术。
- **Feature Resolution**（特性解析）：动态消息因绕过 `protoc` 而无法直接套用该规范，需在运行时独立完成。
- **Descriptor Pool**：动态消息依赖其在运行时构建 Descriptor 的能力。
- **Edition Defaults**：与运行时特性解析共同决定动态消息的最终行为。
- **Runtime Features**：动态消息本身就是一类重要的运行时特性。

## Related Entities

- [[entities/brpc|Apache brpc]]：该RPC框架内置对动态消息的支持，可通过解析请求中的元数据选择服务接口版本。
- [[entities/protocol-buffers|Protocol Buffers]]：其Any类型和反射机制是构建动态消息系统的基础工具之一。
- [[entities/apache-kafka|Apache Kafka]]：配合Schema Registry使用动态消息实现事件流的兼容性管理。
- [[entities/protoc|protoc]]：静态代码生成工具，动态消息刻意绕过该工具以获得运行时灵活性。

## Mentions in Source

*(No previous source mentions on this page.)*

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "There's also still the issue of descriptor pools that need to be able to build descriptors at runtime."
> - "**Runtime support for dynamic messages** - while dynamic messages are a less-frequently-used feature, they are a critical feature used by a lot of important systems."