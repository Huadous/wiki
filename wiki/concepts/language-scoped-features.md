---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
tags:
  - "term"
aliases:
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
  - "Language-scoped Feature"
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
  - "Language-Specific Features"
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
  - "Language-scoped Feature"
  - "语言特性"
  - "语言作用域特性"
  - "language-scoped features"
---

## Related Concepts

- [[concepts/features|Features]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/editions|Editions]]
- [[concepts/custom-options|Custom Options]]
- [[concepts/global-features|Global Features]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]

## Related Entities

- [[entities/protobuf-team|protobuf-team]]
- [[entities/protoc|Protoc]]
- [[entities/c++|C++]]

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Because features can be extensions, language backends can specify **language-scoped** features. For example, `[ctype = CORD]` could instead be phrased as `[features.(pb.cpp).string_type = CORD]`."
> - "Codegen backends own the definitions of their features."

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - "We will use extensions to manage features specific to individual code generators."
> - "This will allow third-party code generators to use editions for their own evolution as long as they reserve a single extension number in `descriptor.proto`."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Language-scoped features, which are defined in a typed extension field for that language. In this document, we refer to them as `features.(<lang>).name`, e.g. `features.(proto.cpp).legacy_string`."
> - "Language-scoped features require only a change in a backend's feature extension, which has a smaller blast radius (except in C++ and Java). Often these are relevant only for codegen and do not require reflective introspection."