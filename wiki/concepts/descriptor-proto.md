---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/options|options]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
  - "[[protobuf/editions-minimum-required-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
tags:
  - "term"
aliases:
  - "descriptor.proto file"
  - "google/protobuf/descriptor.proto"
  - "descriptor.proto"
  - "descriptor.proto file"
  - "google/protobuf/descriptor.proto"
---

## Description

`descriptor.proto` 作为 Protocol Buffers 的自描述协议文件，不仅承载了描述 `.proto` 文件所需的核心元数据结构，还充当了全局扩展注册表（global registry of known extensions），确保不同第三方项目在共享同一 protoc 编译器时不会发生扩展号（extension number）冲突。这一机制使得开发者可以安全地为自定义选项（custom options）申请扩展号，而无需担心冲突。

在 Editions 设计中，`descriptor.proto` 的角色进一步扩展。它与 `FeatureSet` 概念紧密耦合：现代功能解析机制（feature resolution）要求 `descriptor.proto` 本身也能参与功能推断（feature inference），由此推动了对引导构建（bootstrapping）方案的需求。由于生态系统中存在大量预先序列化的 `descriptor.proto` 描述符集（serialized descriptor sets），这些快照需要继续正常工作约数月之久，因此 Editions 零版本（edition zero）不能因功能解析失败而长时间阻塞——可能需要在 protoc 中为功能解析失败的情况提供回退机制（fallbacks）。同时，`descriptor.proto` 还在 Editions 体系下引入了 `target`、`retention` 等选项属性（通过 `FieldDescriptorOptions`）以及最低必需版本（Minimum Required Edition）机制，以防止不同编译器版本之间因功能差异导致的解析不匹配问题。

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

## Related Entities

- [[entities/protocolbuffersprotobuf|protocolbuffersprotobuf]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/buf|buf]]
- [[entities/protoc|protoc]]
- [[entities/prototiller|Prototiller]]

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