---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
tags:
  - "phenomenon"
aliases:
  - "Compiler Bootstrapping"
  - "自举问题"
  - "Bootstrapping"
---

## Related Concepts
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/epochs-for-descriptor-proto|Epochs for `descriptor.proto`]]
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/legacy-syntax-editions|Legacy Syntax Editions]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/source-features|Source Features]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/descriptor-proto|descriptor.proto]]
- [[entities/file-descriptor-proto|FileDescriptorProto]]
- [[entities/code-generator|CodeGenerator]]

## Mentions in Source
> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "Epochs for `descriptor.proto`" (not available externally) describes a potential issue with bootstrapping.
> - It is not the case here: minimum edition is only incremented once a particular file uses a new feature.

> **Source: [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]**
> - In order to get feature resolution running in proto2 and proto3, we need to be able to support bootstrapped protos.
> - For these builds, we can't use any reflection without deadlocking, which means feature defaults can't be compiled during runtime.
> - No directly relevant information.

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - One major complication we're likely to hit revolves around our bootstrapping of `descriptor.proto`.
> - For `descriptor.proto` in particular, handling options can be very challenging.
> - No directly relevant information.