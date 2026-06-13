---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-readme|editions-readme]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
tags:
  - "standard"
aliases:
  - "MRE"
  - "最低必需 Edition"
---

## 相关概念
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/edition-evolution|Edition Evolution]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/protobuf-editions-for-schema-producers|Protobuf Editions for Schema Producers]]
- [[concepts/edition-total-order|Edition Total Order]]
- [[concepts/file-descriptor-proto|FileDescriptorProto]]
- [[concepts/poison-pill|Poison Pill]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/protobuf|protobuf]]

## Mentions in Source
> **Source: [[sources/editions-readme|editions-readme]]**
> - "The following topics are in this repository:"
> - "[Minimum Required Edition](minimum-required-edition.md)"

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "A versioning mechanism for descriptors that ensures old runtimes do not load descriptors that are \"too new.\""
> - "We propose adding a new field to `FileDescriptorProto`:"
> 
>   ```
>   optional string minimum_required_edition = ...;
> ```
> - "No directly relevant information"