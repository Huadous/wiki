---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-stricter-schemas-with-editions.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "person"
aliases:
  - "Michael C. Y."
  - "mcy"
---

## Related Entities
- [[entities/google|Google]]
- [[entities/protobuf-runtime|protobuf-runtime]]
- [[entities/protobuf|Protobuf]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/fowles|@fowles]]
- [[entities/protoc|protoc]]
- [[entities/protoscope|Protoscope]]
- [[entities/prototiller|Prototiller]]

## Related Concepts
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/descriptor-proto|descriptor.proto]]
- [[concepts/file-descriptor-proto|FileDescriptorProto]]
- [[concepts/edition|Edition]]
- [[concepts/feature|Feature]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/legacy-treat-enum-as-closed|legacy_treat_enum_as_closed]]

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

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "Author: @mcy"
> - "On 2023-02-10, a CL @mcy submitted to delete google::protobuf::Reflection::SupportsUnknownEnumValue()."
> - "It turns out we misunderstood a critical corner-case of proto3 enums."