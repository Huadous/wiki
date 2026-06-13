---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "term"
aliases:
  - "Reflection API"
  - "Protobuf Reflektion"
---

## Related Concepts
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/protobuf-editions|Edition]]
- [[concepts/feature|Feature]]
- [[concepts/language-scoped-feature|Language-scoped Feature]]
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/unresolved-features|Unresolved Features]]
- [[concepts/enum-field-closedness|Enum Field Closedness]]
- [[concepts/open-enum|Open Enum]]
- [[concepts/fielddescriptor|FieldDescriptor]]
- [[concepts/filedescriptor|FileDescriptor]]
- [[concepts/proto2|proto2]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/oneofdescriptor|oneofdescriptor]]
- [[entities/descriptor|descriptor]]
- [[entities/descriptorpool|descriptorpool]]
- [[entities/codegeneratorresponse|codegeneratorresponse]]
- [[entities/mupb|μpb]]

## Mentions in Source
> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "We plan to upgrade reflection to be feature-aware in a way that minimizes code we need to change."
> - "We do not expect anyone to implement feature-inheritance logic themselves; feature inheritance should be fully transparent to users, behaving as if features had been placed explicitly everywhere."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Since oneof fields in proto3 already track presence, existing proto3 reflection-based algorithms should correctly preserve presence for proto3 optional fields with no code changes."
> - "For example, the JSON and TextFormat parsers/serializers in C++ and Java did not require any changes to support proto3 presence."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "The one notable place where we *can't* completely hide features is in reflection."
> - "Most of our runtimes provide APIs for converting descriptors back to their original state at runtime (e.g. CopyTo and DebugString in C++)."

> **Source: [[sources/editions-edition-zero-feature-enum-field-closedness|editions-edition-zero-feature-enum-field-closedness]]**
> - "On 2023-02-10, a CL @mcy submitted to delete google::protobuf::Reflection::SupportsUnknownEnumValue()."
> - "Oddly, this function used the containing message's syntax, rather than the enum field's, to determine whether the enum was open."