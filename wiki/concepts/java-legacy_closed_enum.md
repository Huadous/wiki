---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-java-lite-for-editions|editions-java-lite-for-editions]]"
  - "[[protobuf/editions-java-lite-for-editions.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
tags:
  - "term"
aliases:
  - "legacy_closed_enum"
  - "java legacy closed enum"
  - "kLegacyEnumIsClosedBit"
---

## Related Concepts
- [[concepts/features.enum_type]]
- [[concepts/kMapWithProto2EnumValue]]
- [[concepts/kLegacyEnumIsClosedBit]]
- [[concepts/EnumLiteGenerator]]
- [[concepts/Editions Zero Features]]
- [[concepts/kHasHasBit]]
- [[concepts/utf8_validation]]
- [[concepts/Feature Extension Layout]]
- [[concepts/Runtime Implementation Features]]
- [[concepts/Generator Features]]

## Related Entities
- [[entities/Java Lite]]
- [[entities/C++ Protobuf Implementation]]
- [[entities/Python Protobuf Implementation]]

## Mentions in Source

> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - "Replace with `kLegacyEnumIsClosedBit`"
> - "This will now be set for all enum fields, instead of just enum map values."
> - "We will still need to check syntax in the interim in case of gencode."

> **Source: [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]**
> - "While the sole feature we had originally created (`legacy_closed_enum` in Java and C++) didn't have any ambiguity here, this one did."
> - "Specifically in Python, the current behaviors across proto2/proto3 are distinct for all 3 implementations: pure python, Python/C++, Python/upb."