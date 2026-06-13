---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/style]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
tags:
  - "term"
aliases:
  - "Group"
  - "分组语法"
  - "group syntax"
  - "Group Fields"
  - "Group"
  - "分组语法"
  - "group syntax"
  - "Group fields"
  - "Group"
  - "分组语法"
  - "group syntax"
  - "Group Fields"
  - "Group"
  - "分组语法"
  - "group syntax"
---

## Related Concepts
- [[concepts/nested-messages|Nested Messages]]
- [[concepts/required-fields|Required Fields]]
- [[concepts/message-names|Message Names]]
- [[concepts/wire-format|Wire Format]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature|Feature]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]
- [[concepts/editions-2023|Edition 2023]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/group-like-fields|Group-like fields]]
- [[concepts/smooth-extension|Smooth Extension]]
- [[concepts/text-format|Text format]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/edition-2023|Edition 2023]]

## Mentions in Source

> **Source: [[sources/style|style]]**
- "Groups is an alternate syntax and wire format for nested messages. Groups are considered deprecated in proto2, were removed from proto3, and are converted to a delimited representation in edition 2023."
- "Use a nested message definition and field of that type instead of using the group syntax, using the message_encoding feature for wire-compatibility."
- "Avoid Groups"

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
- "We still have `required` and `group`, `packed` is not everywhere..."
- "groups will turn into sub message fields with a special encoding."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
- "Proto2 splits groups into a synthetic nested message with a type name equivalent to the group specification (required to be capitalized), and a field name that's fully lowercased."
- "The casing here is very important, since the transformation is irreversible. We can't recover the group name from the field name in general, only if the group is a single word."
- "No directly relevant information"