---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/implementing_proto3_presence|implementing_proto3_presence]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
tags:
  - "other"
aliases:
  - "google::protobuf::Descriptor"
  - "Protocol Buffers Descriptor"
  - "Protobuf 消息描述符"
---

## Related Entities
- [[entities/oneofdescriptor|OneofDescriptor]]
- [[entities/fielddescriptor|FieldDescriptor]]
- [[entities/descriptorpool|DescriptorPool]]
- [[entities/protoc|protoc]]
- [[entities/microproto|Microproto (μpb)]]

## Related Concepts
- [[concepts/synthetic_oneof|Synthetic Oneof]]
- [[concepts/reflection|Reflection]]
- [[concepts/oneof|Oneof]]
- [[concepts/global-features|Global Features]]
- [[concepts/language-scoped-features|Language-scoped Features]]
- [[concepts/fileddescriptorproto|FileDescriptorProto]]
- [[concepts/features|Features]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/unresolved-features|Unresolved Features]]

## Mentions in Source

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "Descriptor::real_oneof_decl_count(): like oneof_decl_count(), but returns the number of real oneofs only."
> - "Real oneofs are always first, and real_oneof_decl_count() will return the total number of oneofs, excluding synthetic oneofs."

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Global features require a `descriptor.h` change, and are relatively heavy weight, since defining one will also require providing helpers in `Descriptor` wrapper classes to avoid the need for users to resolve inheritance."
> - "Shape of a descriptor. Features should generally not cause fields, message, or enum descriptors to appear or disappear."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "Most of our runtimes provide APIs for converting descriptors back to their original state at runtime (e.g. CopyTo and DebugString in C++)."
> - "More inline with our descriptor APIs, which wrap descriptor protos but aren't strictly 1:1 with them."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "No directly relevant information"