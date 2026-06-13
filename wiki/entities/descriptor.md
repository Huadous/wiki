---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/implementing_proto3_presence|implementing_proto3_presence]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
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

## Related Concepts
- [[concepts/synthetic_oneof|Synthetic Oneof]]
- [[concepts/reflection|Reflection]]
- [[concepts/oneof|Oneof]]
- [[concepts/global-features|Global Features]]
- [[concepts/language-scoped-features|Language-scoped Features]]
- [[concepts/fileddescriptorproto|FileDescriptorProto]]
- [[concepts/features|Features]]

## Mentions in Source
- "Descriptor::real_oneof_decl_count(): like oneof_decl_count(), but returns the number of real oneofs only." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "Real oneofs are always first, and real_oneof_decl_count() will return the total number of oneofs, excluding synthetic oneofs." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]

> **Source: [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]**
> - "Global features require a `descriptor.h` change, and are relatively heavy weight, since defining one will also require providing helpers in `Descriptor` wrapper classes to avoid the need for users to resolve inheritance."
> - "Shape of a descriptor. Features should generally not cause fields, message, or enum descriptors to appear or disappear."