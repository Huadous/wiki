---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/overview]]"
  - "[[sources/features]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "standard"
aliases:
  - "proto2"
  - "Protocol Buffers version 2"
  - "Protobuf 2"
---

## Related Concepts
- [[concepts/proto3|proto3]]
- [[concepts/edition-2024|edition-2024]]
- [[concepts/edition-2023|edition-2023]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/field-cardinality|field-cardinality]]
- [[concepts/forward-compatibility|forward-compatibility]]
- [[concepts/backward-compatibility|backward-compatibility]]
- [[concepts/serialization|serialization]]
- [[concepts/proto-file|proto-file]]
- [[concepts/field-number|field-number]]
- [[concepts/features-field_presence|features-field_presence]]
- [[concepts/features-default_symbol_visibility|features-default_symbol_visibility]]
- [[concepts/optional|optional]]
- [[concepts/message|message]]
- [[concepts/field-presence|field-presence]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/features|Features]]
- [[concepts/groups|groups]]
- [[concepts/packed|packed]]

## Related Entities
- [[entities/protoc|protoc]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/google|google]]
- [[entities/prototiller|prototiller]]
- [[entities/c++|C++]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "When defining .proto files, you can specify cardinality (singular or repeated). In proto2 and proto3, you can also specify if the field is optional."
> - "For more information about the options available, see the language guide for proto2, proto3, or edition 2023."

> **Source: [[sources/features|features]]**
> - "Default behavior per syntax/edition: proto2 -> EXPORT_ALL"
> - "proto2 -> CLOSED (for enum_type)"
> - "proto2 -> EXPLICIT (for field_presence)"
> - "The following code sample shows a proto2 file: syntax \"proto2\""

> **Source: [[sources/proto3|proto3]]**
> - "For information on the proto2 syntax, see the Proto2 Language Guide."
> - "If no edition or syntax is specified, the protocol buffer compiler will assume you are using proto2."
> - "optional is recommended over implicit fields for maximum compatibility with protobuf editions and proto2."

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "The proto2/proto3 distinction is going away."
> - "Messages with any permutation of features are always interoperable (they can import each other freely and use messages from each other)."
> - "We still have `required` and `group`, `packed` is not everywhere, and string accessors in C++ still return `const std::string&`."
> - "Edition Zero should be viewed as the 'completion' of the union of proto2 and proto3: it contains both syntaxes as subsets (although with different spellings to disambiguate things) as well as new behavior that was previously inexpressible."
> - "Everything expressible today will remain so in Edition Zero."