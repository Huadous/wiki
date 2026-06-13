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
  - "Target"
  - "FeatureTargetType"
---

## Related Concepts

- [[concepts/features|Features]]
- [[concepts/feature-inheritance|Feature Inheritance]]
- [[concepts/retention|Retention]]
- [[concepts/options-attributes|Options Attributes]]
- [[concepts/optiontargettype|OptionTargetType]]
- [[concepts/fieldoptions|FieldOptions]]

## Related Entities

- [[entities/protoc|protoc]]

## Mentions in Source

- While inheritance can be useful for minimizing changes or pushing defaults broadly, it can be overused in ways that would make simple refactoring of `.proto` files harder. — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "Historically, options have only applied to specific entities, but features will be available on most entities. To allow language specific extensions to restrict the places where options can bind, we will allow features to explicitly specify the targets they apply to (similar in concept to the \"target\" attribute on Java annotations)."
> - "`target` **only** specifies the semantic entity to which an option can apply. Features will be able to be set on both the `FILE` level and their semantic entity. Everything in between will be refused in the initial release."