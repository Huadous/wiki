---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/options|options]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
tags:
  - "term"
aliases:
  - "protobuf custom options"
  - "Protocol Buffers 自定义选项"
  - "Custom Options"
---

## Related Concepts
- [[concepts/Protobuf Global Extension Registry|Protobuf Global Extension Registry]]
- [[concepts/Extension numbers|Extension numbers]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/Features|Features]]
- [[concepts/Editions|Editions]]
- [[concepts/FieldOptions|FieldOptions]]
- [[concepts/Target Attributes|Target Attributes]]
- [[concepts/Retention|Retention]]

## Related Entities
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/buf|buf.build]]
- [[entities/protoc|protoc]]
- [[entities/protobuf-editions|Protobuf Editions]]

## Mentions in Source

> **Source: [[sources/options|options]]**
> - "If you need an extension number for your custom option (see custom options), please send us a pull request to add an entry to this doc, or create an issue with info about your project (name and website) so we can add an entry for you."

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - "Protobuf already supports custom options and we will leverage these to provide a rich syntax without introducing new syntactic forms into Protobuf."
> - "This will allow third party code generators to use editions for their own evolution as long as they reserve a single extension number in `descriptor.proto`."

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "The [Protobuf Editions](what-are-protobuf-editions.md) project plans to use [custom options](protobuf-editions-design-features.md) to model features and encourage language bindings to build custom features off options as well."
> - "Rather than building `retention` and `target` directly as fields of `FieldOptions`, we could use custom options to define an equivalent thing. This option was rejected because it pushes extra syntax onto users for a fundamental feature."