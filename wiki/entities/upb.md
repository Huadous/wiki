---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-group-migration-issues|editions-group-migration-issues]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-editions-feature-extension-layout.md]]"
  - "[[protobuf/editions-edition-lifetimes.md]]"
tags:
  - "product"
aliases:
  - "upb"
  - "micro protobuf"
  - "upb C runtime"
  - "μpb"
  - "upb"
  - "micro protobuf"
  - "upb C runtime"
---

## Related Entities
- [[entities/protobuf|Protobuf]]

## Related Concepts
- [[concepts/codegen|Codegen]]
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/shared-implementations|Shared Implementations]] *(待确认)*
- [[concepts/polyglot|Polyglot]] *(待确认)*
- [[concepts/generator-features|Generator Features]]
- [[concepts/runtime-implementation-features|Runtime Implementation Features]]
- [[concepts/reflection-based-validation|Reflection-Based Validation]]
- [[concepts/dynamic-messages|Dynamic Messages]]
- [[concepts/edition-support-window|Edition Support Window]]

## Mentions in Source
- ** This includes all upb-based runtimes as well (e.g. Ruby, Rust, etc.) — editions-group-migration-issues
- While using the field name for generated APIs required less special-casing in the generators, the field name ends up producing slightly-less-readable APIs for multi-word camelcased groups. — editions-group-migration-issues

> **Source: editions-editions-feature-visibility**
> - "One notable standout here is μpb, which is a runtime *implementation*, but not a full runtime."
> - "Since μpb only provides APIs to the wrapping runtime in a target language, it's free to expose features anywhere it wants. The wrapping language should be responsible for stripping them out where appropriate."

> **Source: editions-editions-feature-extension-layout**
> - "Runtimes like upb and C++ are used as backing implementations of multiple other languages (e.g. Python, Rust, Ruby, PHP)."
> - "Possible complexity in upb to understand which language's features to respect. UPB is not currently aware of what language it is being used for."
> - "Limits in-process sharing across languages with shared implementations (e.g. Python upb, PHP upb) in the case of conflicting behaviors."

> **Source: editions-edition-lifetimes**
> - "Performance concerns, especially in upb"
> - "Generators in a monorepo like Protobuf's this seems fine, but may not be desirable elsewhere."