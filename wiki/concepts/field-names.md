---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/style]]"
tags:
  - "standard"
aliases:
  - "字段命名"
  - "Field naming"
  - "Avoid Field Names and Oneof Names that Could Potentially Cause Collisions"
  - "字段命名"
  - "Field naming"
  - "Avoiding Language Keywords in Protobuf Identifiers"
  - "字段命名"
  - "Field naming"
  - "Avoid Field Names and Oneof Names that Could Potentially Cause Collisions"
  - "字段命名"
  - "Field naming"
---

## Related Concepts
- [[concepts/Identifier-naming-styles|Identifier naming styles]]
- [[concepts/Message-Names|Message Names]]
- [[concepts/Field-Names|Field Names]]
- [[concepts/Oneof-Names|Oneof Names]]
- [[concepts/Service-Naming|Service Naming]]
- [[concepts/Enum-Names|Enum Names]]
- [[concepts/Avoid-Language-Keywords|Avoid Language Keywords]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## Mentions in Source
> **Source: [[sources/style|style]]**
> - "Use snake_case for field names, including extensions."
> - "Use pluralized names for repeated fields. `string song_name repeated Song songs`"
> - "Using certain names together can cause collisions in generated code, which may prevent it from compiling."
> - "Prefixes: has_, get_, set_, clear_. Suffixes: _value. Names: descriptor."
> - "Avoid using prefixes, suffixes, and names that could potentially cause collisions such as has_, get_, set_, clear_ and _value and descriptor."
> - "Use snake_case for field names, including extensions." — [[sources/style|style]]
> - "Use pluralized names for repeated fields." — [[sources/style|style]]
> - "string song_name" — [[sources/style|style]]
> - "repeated Song songs" — [[sources/style|style]]
> - "To reduce the risk of language-specific breakages, avoid certain prefixes, suffixes, and names. Prefixes: has_, get_, set_, clear_. Suffixes: _value. Names: descriptor." — [[sources/style|style]]
> - "Other language keywords and reserved words should be avoided; see Avoid Using Language Keywords." — [[sources/style|style]]
> - "Python keyword conflicts" — [[sources/style|style]]

> **Source: [[sources/style|style]]**
> - (新增信息：无新增相关内容，未提供与字段名直接相关的额外信息)