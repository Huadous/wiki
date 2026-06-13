---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
tags:
  - "method"
aliases:
  - "扩展"
  - "message extension"
  - "字段扩展"
---

## Related Concepts
- [[concepts/proto2|Proto2]]
- [[concepts/proto3|Proto3]]
- [[concepts/field-number|Field number]]
- [[concepts/proto-file|.proto file]]
- [[concepts/message-type|message-type]]
- [[concepts/group-fields|Group fields]] *(to be created — referenced by new source)*

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "Messages can allow extensions to define fields outside of the message, itself. For example, the protobuf library's internal message schema allows extensions for custom, usage-specific options."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "To make things even stranger, for *extensions* (group fields extending other messages), we always use the field name for groups. So as far as group extensions are concerned, there's no problem for editions."
> - "There are a few problems with non-extension group fields in editions:"