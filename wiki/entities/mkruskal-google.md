---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "person"
aliases:
  - "Mike Kruskal"
  - "mkruskal-google"
---

## Description
该源系列文档集合了 Protocol Buffers Editions 体系下的多项关键设计提案，涵盖功能扩展布局、JSON 处理以及 Edition 命名规范等核心议题。mkruskal-google 作为核心设计者贯穿于这些文档中，主导了 Edition Zero 的 JSON 处理方案以及使用 Edition 枚举类型替代宽松字符串命名方案的推荐设计。整体工作聚焦于为 Editions 提供更清晰、更严格的语义约束，并推动从 proto2/proto3 向 Editions 的平滑过渡。

## Related Entities
- [[entities/prototiller|Prototiller]]
- [[entities/protoc|protoc]]
- [[entities/zhangskz|zhangskz]]
- [[entities/mkruskal-google|mkruskal-google]]
- Joshua Humphries
- Protocol Buffers
- Protobuf
- Edition Zero
- [[entities/protocolbuffers-protobuf|protocolbuffers/protobuf]]

## Related Concepts
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/editions|Editions]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/feature-extension|Feature Extension]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/edition-naming|Edition Naming]]
- Delimited encoding
- Group fields
- Smooth Extension
- Global Feature
- JSON Field Name Conflicts
- [[concepts/json-format-feature|json_format feature]]
- Edition enum

## Mentions in Source
> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "**Author:** [@mkruskal-google](https://github.com/mkruskal-google),"
> - "[@zhangskz](https://github.com/zhangskz)"

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "**Author:** [@mkruskal-google](https://github.com/mkruskal-google)"
> - "**Approved:** 2023-05-10"

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "**Author:** [@mkruskal-google](https://github.com/mkruskal-google)"
> - "**Approved:** 2023-08-25"