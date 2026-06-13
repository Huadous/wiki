---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-edition-zero-features.md]]"
tags:
  - "method"
aliases:
  - "扩展"
  - "message extension"
  - "字段扩展"
---

## Description
Extensions 是 Protocol Buffers 中的一种字段扩展机制，允许在不修改原始 .proto 文件的情况下向已有消息类型添加新的字段，从而实现消息功能的扩展而不破坏兼容性。该机制使第三方或下游使用者可以在不直接编辑原 schema 的前提下，自行定义专属字段，例如 protobuf 库内部消息 schema 就允许 extensions 用于自定义的、使用场景相关的 options。Proto2 原生支持 extensions，但 Proto3 不支持——在 proto3 中，标准的替代方案是使用 `Any` 类型来承载任意消息。Editions 体系下的 Edition Zero 取消了对 extensions 的这一限制，明确规定 "Extensions may be used on all messages"，即 extensions 可被应用于所有消息类型，从而解除了 proto3 时期施加的禁令。值得注意的是，extensions 与 TypeResolver 的兼容性被认为存在一定问题，但这些问题被视为可修复的，且只有在该方向上获得足够反馈时才值得投入实施。

## Related Concepts
- [[concepts/proto2|Proto2]]
- [[concepts/proto3|Proto3]]
- [[concepts/field-number|Field number]]
- [[concepts/proto-file|.proto file]]
- [[concepts/message-type|message-type]]
- [[concepts/group-fields|Group fields]] *(to be created — referenced by new source)*
- [[concepts/any-type|Any type]] *(to be created — referenced as proto3 canonical workaround)*

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/edition-zero|Edition Zero]] *(to be created — referenced by new source)*

## Mentions in Source

> **Source: [[sources/overview|overview]]**
> - "Messages can allow extensions to define fields outside of the message, itself. For example, the protobuf library's internal message schema allows extensions for custom, usage-specific options."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "To make things even stranger, for *extensions* (group fields extending other messages), we always use the field name for groups. So as far as group extensions are concerned, there's no problem for editions."
> - "There are a few problems with non-extension group fields in editions:"

> **Source: [[sources/editions-edition-zero-features|editions-edition-zero-features]]**
> - "Extensions. Proto2 has extensions, while Proto3 does not (`Any` is the canonical workaround)."
> - "Extensions may be used on all messages. This lifts a restriction from proto3."