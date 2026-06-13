---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-life-of-an-edition]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "method"
aliases:
  - "Feature GC"
  - "feature garbage collection"
  - "Features GC"
  - "Garbage Collection"
  - "Feature GC"
  - "feature garbage collection"
  - "Features GC"
---

## Description
Features GC 是 [[entities/protoc|protoc]] 提供的一款命令行工具，运行 `protoc --gc-features foo.proto` 时会针对处于 editions 模式下的 proto 文件，计算为维持文件原有行为而需要显式设置的特性最小集。该工具读取文件中声明的 edition，并基于此推导出所有可继承的特性默认值，从而仅保留必须显式覆盖的特性，避免冗余显式设置；输出是 Protochangifier [[concepts/ProtoChangeSpec|ProtoChangeSpec]]，可用于自动清理大量 proto 文件。

在 Edition Lifetimes 的设计语境下，"垃圾回收"还被赋予了另一层含义：特性相关代码的实际清理（即从运行时与实现中彻底移除）只有在所有早于其 `edition_removed` 声明的 edition 都已被完全下线之后才会发生。这将特性支持的生命周期与 edition 支持的生命周期直接绑定——只要最老的还需要该特性的 edition 仍然存在，相关特性代码就必须保留。这一约束在开源生态中尤为突出，因为开源场景下 proto 文件无法被强制升级到最新 edition，老旧 edition 可能长期共存，从而延缓特性代码的回收。

## Related Concepts
- [[concepts/Editions-adopter]]
- [[concepts/Editions-upgrader]]
- [[concepts/ProtoChangeSpec]]
- [[concepts/Feature]]

## Related Entities
- [[entities/protoc]]
- [[entities/upb]]

## Mentions in Source
> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "The features GC. Running protoc --gc-features foo.proto on a file in editions mode will compute the minimal (or a heuristically minimal, if this proves expensive) set of features to set on things, given the edition specified in the file."
> - "This will produce a Protochangifier ProtoChangeSpec that describes how to clean up the file."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "Another consequence of this is that we can't actually clean up feature-related code until every edition before its `edition_removed` declaration has been dropped."
> - "This ties feature support directly to edition support, especially in OSS where we can't forcibly upgrade protos to the latest edition."