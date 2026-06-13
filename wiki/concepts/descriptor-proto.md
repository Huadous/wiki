---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/options|options]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
tags:
  - "term"
aliases:
  - "descriptor.proto file"
  - "google/protobuf/descriptor.proto"
  - "descriptor.proto"
  - "descriptor.proto file"
  - "google/protobuf/descriptor.proto"
---

## Related Concepts

- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/field-options|FieldOptions]]
- [[concepts/options-attributes|Options Attributes]]
- [[concepts/target-attributes|Target Attributes]]
- [[concepts/retention|Retention]]
- [[concepts/minimum-required-edition|Minimum Required Edition]]

## Related Entities

- [[entities/protocolbuffersprotobuf|protocolbuffersprotobuf]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/buf|buf]]
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/options|options]]**
> - "This file contains a global registry of known extensions for descriptor.proto"
> - "so that any developer who wishes to use multiple 3rd party projects, each with their own extensions, can be confident that there won't be collisions in extension numbers."
> - "If you need an extension number for your custom option (see [custom options]"

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "Both `target` and `retention` attributes are no-ops when applied to fields that are not options (either from descriptor.proto or custom options)."
> - "While the proximal motivation for these options is for use with \"features\" in \"editions\", I believe they provide sufficient general utility that adding them directly to `FieldDescriptorOptions` is warranted."
> - "No directly relevant information"

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "This document describes an addition to `descriptor.proto` that prevents this version mismatch issue."
> - "Since `descriptor.proto` and other schemas used by `protoc` and the backends would not use new features immediately, introducing a new feature does not immediately stop the compiler from being able to compile itself."
> - "No directly relevant information"