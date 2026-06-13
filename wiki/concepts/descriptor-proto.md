---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/options|options]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
  - "[[protobuf/editions-edition-zero-converged-semantics.md]]"
  - "[[protobuf/editions-edition-naming.md]]"
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
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/bootstrapping|Bootstrapping]]
- [[concepts/serialized-descriptors|Serialized Descriptors]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/feature-inference|Feature Inference]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/features-option|Features Option]]
- [[concepts/semantic-features|Semantic Features]]
- [[concepts/edition-keyword|Edition Keyword]]
- [[concepts/edition-enum|Edition Enum]]

## Related Entities
- [[entities/protocolbuffersprotobuf|protocolbuffersprotobuf]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/buf|buf]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|Prototiller]]
- [[entities/protobuf-team|Protobuf Team]]
- [[entities/edition-zero|Edition Zero]]

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

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - "As we now know, there are a lot of serialized `descriptor.proto` descriptor sets out there that need to continue working for O(months)."
> - "In order to avoid blocking edition zero for that long, we may need fallbacks in protoc for the case where feature resolution *fails*."
> - "No directly relevant information"

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "In languages that have dynamic messages, one codegen strategy is to embed the FileDescriptorProto of the file and then parse and build it at the beginning of runtime."
> - "this file will never have any generator feature overrides, since it can't import those files."
> - "No directly relevant information"

> **Source: [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]**
> - "The `features` option will be added to `descriptor.proto` for the following descriptor options:"
> - "Rev'ing `descriptor.proto` is a far more intrusive change that affects many downstream systems."
> - "No directly relevant information"

> **Source: [[sources/editions-edition-naming|editions-edition-naming]]**
> - "However, since it needs to exist in descriptor.proto, we won't be able to make it open until the end of our edition zero migration."
> - "Might require parser changes to get descriptor.proto onto editions"
> - "No directly relevant information"