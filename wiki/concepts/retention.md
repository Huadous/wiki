---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
tags:
  - "term"
aliases:
  - "Retention"
  - "FeatureRetention"
---

## Related Concepts
- [[concepts/Features|Features]]
- [[concepts/Target Attributes|Target Attributes]]
- [[concepts/Options Attributes|Options Attributes]]
- [[concepts/FeatureRetention|FeatureRetention]]
- [[concepts/FieldOptions|FieldOptions]]
- [[concepts/OptionTargetType|OptionTargetType]]

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