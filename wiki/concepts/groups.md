---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/style]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
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

## Description
Groups 是 Protocol Buffers 在 proto2 中引入的一种嵌套消息语法糖，它在语义上等价于一个嵌套消息字段，但在底层使用了不同的 wire format：使用 wire type 3（START_GROUP）和 wire type 4（END_GROUP）定界符来编码消息边界，而不是通常的 wire type 2（length-delimited）方式。Group 语法可视为一种带内嵌语法的消息字段形式。在 proto3 中，group 语法被移除；到了 Edition 2023，原 proto2 的 group 字段会被转换为带 DELIMITED 编码的嵌套消息表示。Edition Zero 进一步决定彻底删除 `group` 语法，原 proto2 group 字段被自动转换为嵌套消息类型加上设置了 `features.message_encoding = DELIMITED` 的字段。这一决定简化了解析器实现，使消息编码方式更一致，并允许 `message_encoding` 特性在未来应用于更多字段编码优化场景。总体而言，protobuf 的演进方向是弃用 group 语法并统一使用嵌套消息加 `message_encoding` 特性来表达相同语义。

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
- [[concepts/message-encoding|message_encoding]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/edition-2023|Edition 2023]]
- [[entities/edition-zero|Edition Zero]]

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

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
- "Groups. Proto2 has groups, proto3 does not."
- "The `group` syntax does not exist under editions."