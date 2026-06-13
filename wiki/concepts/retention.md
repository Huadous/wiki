---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
tags:
  - "term"
aliases:
  - "Retention"
  - "FeatureRetention"
  - "Option Retention"
  - "Retention"
  - "FeatureRetention"
---

## Description
Option Retention 起源于 [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]] 中提出的简化运行时 descriptor 体积的需求，其设计灵感来自 Java 注解的 retention 属性。在 [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]] 中，该机制被形式化为 `FeatureRetention` 枚举，提供 `RETENTION_UNKNOWN`、`RETENTION_RUNTIME` 与 `RETENTION_SOURCE` 三种取值，其中面向 `protoc` 与代码生成器的 option 默认采用 `SOURCE` 保留，而所有其他 option 默认采用 `RUNTIME` 保留（即维持当前行为）。在 [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]] 中，这一保留策略被进一步用于 FeatureSet 的生命周期管理：在 retention 应用之前对 `protoc` 与生成器可见的为 Source Features，应用之后对运行时可见的为 Runtime Features。借助这种分离，[[entities/protoc|protoc]] 与生成器可以剥离无需暴露给运行时的特性，既保护内部决策又减小生成代码体积，并据此把已解析与未解析的 FeatureSet 拆分为公开与内部 API。

## Related Concepts
- [[concepts/Features|Features]]
- [[concepts/Target Attributes|Target Attributes]]
- [[concepts/Options Attributes|Options Attributes]]
- [[concepts/FeatureRetention|FeatureRetention]]
- [[concepts/FieldOptions|FieldOptions]]
- [[concepts/OptionTargetType|OptionTargetType]]
- [[concepts/Source Features|Source Features]]
- [[concepts/Runtime Features|Runtime Features]]
- [[concepts/FeatureSet|FeatureSet]]

## Related Entities
- [[entities/protoc|protoc]]

## Mentions in Source
- "To reduce the size of descriptors in protobuf runtimes, features will be permitted to specify retention rules (again similar in concept to "retention" attributes on Java annotations)." — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]
- "enum FeatureRetention { SOURCE = 0; RUNTIME = 1; }" — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "To reduce the size of descriptors in protobuf runtimes, features will be permitted to specify retention rules (again similar in concept to "retention" attributes on Java annotations)."
> - "Options intended to inform code generators or `protoc` itself can be annotated with `SOURCE` retention. The default retention will be `RUNTIME` as that is the current behavior for all options."
> - "```
enum FeatureRetention {
  RETENTION_UNKNOWN = 0;
  RETENTION_RUNTIME = 1;
  RETENTION_SOURCE = 2;
}
"
> - "The retention enum did not have an `UNKNOWN` type."

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "We support a retention specification on all options, including features"
> - "Source features - The features available to protoc and generators, before option retention has been applied."