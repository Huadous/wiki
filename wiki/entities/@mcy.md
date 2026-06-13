---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-stricter-schemas-with-editions.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "person"
aliases:
  - "Michael C. Y."
  - "mcy"
---

## Description
@mcy 是 Protobuf Editions 系列设计文档的核心作者之一，长期在 Google protobuf 团队工作，并主导了该机制多篇重要提案与说明文档的撰写。其工作覆盖 Editions 的基础介绍、收紧 Schema 的备忘录、最低必需版本（Minimum Required Edition）提案，以及对 Editions 中"特性分类、生命周期、宣告机制与大规模变更模板"的系统性阐述。@mcy 的文档风格以设计备忘录为主，强调实用性与可操作性，是理解 Protobuf Editions 系统设计理念和演进路径的关键参考资料。2022 年下半年，多篇由 @mcy 主笔的文档陆续获批，标志着 Protobuf Editions 在语义演进机制上趋于成熟。

## Related Entities
- [[entities/google|Google]]
- [[entities/protobuf-runtime|protobuf-runtime]]
- [[entities/protobuf|Protobuf]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/fowles|@fowles]]
- [[entities/protoc|protoc]]

## Related Concepts
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/descriptor-proto|descriptor.proto]]
- [[concepts/file-descriptor-proto|FileDescriptorProto]]
- [[concepts/edition|Edition]]
- [[concepts/feature|Feature]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Authors: [@mcy](https://github.com/mcy), [@fowles](https://github.com/mcy)"

> **Source: [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]**
> - "**Author:** [@mcy](https://github.com/mcy)"
> - "**Approved:** 2022-11-28"
> - "This is primarily a memo on a use-case for Editions, and not a design doc per se."

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "**Author:** [@mcy](https://github.com/mcy)"
> - "**Approved:** 2022-11-15"

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Author: @mcy"
> - "How to use Protobuf Editions to construct a large-scale change that modifies the semantics of Protobuf in some way."