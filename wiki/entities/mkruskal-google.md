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
tags:
  - "person"
aliases:
  - "Mike Kruskal"
  - "mkruskal-google"
---

## Description
mkruskal-google 是 Google 的 Protocol Buffers（Protobuf）语言设计与 Editions 体系的核心贡献者之一，活跃于 GitHub 平台，账号为 `@mkruskal-google`。在 Editions 体系的设计演进中，该作者参与了多份关键设计文档的撰写，包括与 [[entities/zhangskz|zhangskz]] 等人合作的 [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]] 文档，对 [[concepts/feature-extension|Feature Extension]] 的布局机制进行了系统设计。2023 年 5 月 10 日，该作者独立撰写的 [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]（即《Edition Zero: JSON Handling》）设计提案获得批准，旨在统一 proto2 与 proto3 在 JSON 字段名冲突行为上的不一致问题，引入了 `json_format` 特性机制。该作者在 Protobuf 社区中长期担任设计者角色，提出的技术方案对 [[concepts/editions|Editions]] 体系下 [[concepts/json-format-feature|JSON 格式特性]]与 [[concepts/json-field-name-conflicts|JSON 字段名冲突]]等关键概念产生了直接影响。

## Related Entities
- [[entities/prototiller|Prototiller]]
- [[entities/protoc|protoc]]
- [[entities/zhangskz|zhangskz]]
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
- Delimited encoding
- Group fields
- Smooth Extension
- Global Feature
- JSON Field Name Conflicts
- [[concepts/json-format-feature|json_format feature]]

## Mentions in Source
> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "**Author:** [@mkruskal-google](https://github.com/mkruskal-google),"
> - "[@zhangskz](https://github.com/zhangskz)"

> **Source: [[sources/editions-edition-zero-json-handling|editions-edition-zero-json-handling]]**
> - "**Author:** [@mkruskal-google](https://github.com/mkruskal-google)"
> - "**Approved:** 2023-05-10"