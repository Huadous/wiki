---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "phenomenon"
aliases:
  - "向后兼容"
  - "backward-compatible"
  - "downward compatible"
---

## Related Concepts
- [[concepts/Forward Compatibility|向前兼容性]]
- [[concepts/Field Number|字段编号]]
- [[concepts/edition-patches|Edition Patches]]
- [[concepts/edition-naming|Edition Naming]]
- [[concepts/editions|Editions]]

## Related Entities
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/google|google]]

## Mentions in Source

> **Source: [[protobuf/overview|overview]]**
> - "Because protocol buffers are used extensively across all manner of services at Google and data within them may persist for some time, maintaining backwards compatibility is crucial."
> - "Protocol buffers allow for the seamless support of changes, including the addition of new fields and the deletion of existing fields, to any protocol buffer without breaking existing services."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "In [Edition Naming](edition-naming.md) we decided to drop the idea of "patch" editions, because editions were always forward and backward compatible."
> - "This changes those assumptions though, since now editions are neither forward-compatible (new features don't work in old editions) or backward-compatible (old features may not work in new editions)."

> **Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]**
> - "No directly relevant information"