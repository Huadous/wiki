---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-minimum-required-edition]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-edition-evolution.md]]"
tags:
  - "term"
aliases:
  - "FileDescriptorProto 消息类型"
  - "FileDescriptorProto message"
---

## Related Concepts
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/edition|Edition]]
- [[concepts/edition-naming|Edition Naming]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/global-features|Global features]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/option-retention|Option Retention]]
- [[concepts/conformance-testing|Conformance Testing]]
- [[concepts/feature-set|Feature Set]]
- [[concepts/protobuf-features|Protobuf Features]]
- [[concepts/backend-features|Backend Features]]
- [[concepts/build-horizon|Build Horizon]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protobuf|Protobuf]]
- [[entities/protobuf-editions|Protobuf Editions]]

## Mentions in Source

> **Source: [[sources/editions-minimum-required-edition]]**
> - "We propose adding a new field to `FileDescriptorProto`:`optional string minimum_required_edition = ...;`"
> - "This field would exist alongside the `edition` field, and would have the following semantics:"

> **Source: [[sources/editions-life-of-an-edition]]**
> - "The `FileDescriptorProto.edition` field is a string, so that we can avoid nasty surprises around needing to mint multiple editions per year: even if we mint `edition = \"2022\";`, we can mint `edition = \"2022.1\";` in a pinch."
> - "We also need to track down and upgrade (by hand) any code that is using the value of `syntax`."

> **Source: [[sources/editions-life-of-an-edition]]**
> - 无直接相关信息

> **Source: [[sources/editions-editions-life-of-a-featureset]]**
> - "every generator that embeds a `FileDescriptorProto` into its gencode would see a massive code-size increase."
> - "For languages that have dynamic messages, one codegen strategy is to embed the `FileDescriptorProto` of the file and then parse and build it at the beginning of runtime."

> **Source: [[sources/editions-editions-life-of-a-featureset]]**
> - 无直接相关信息

> **Source: [[sources/editions-edition-evolution]]**
> - "The `FileDescriptorProto.edition` field is a string, so that we can avoid nasty surprises around needing to mint multiple editions per year: even if we mint `edition = \"2022\";`, we can mint `edition = \"2022b\";` in a pinch."
> - "However, suppose I have an older service running v4.2. It is compiled with a proto that was already edition 2023 at build time (alternatively, it dynamically loads a proto)."

> **Source: [[sources/editions-edition-evolution]]**
> - 无直接相关信息