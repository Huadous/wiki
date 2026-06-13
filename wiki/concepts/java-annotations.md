---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]"]
tags: [standard]
aliases:
  - "Java Annotation"
  - "Java 注解"
---


# Java annotations

## 定义
Java annotations are a standardized metadata mechanism in the Java programming language that allow developers to attach structured information to program elements such as classes, methods, and fields. In the context of Protobuf Editions design, the concept serves as the **conceptual reference model** for the `target` and `retention` attributes of features/options: just as Java annotations use `target` to restrict which program elements an annotation type can be applied to, and `retention` to specify how long annotations are kept (source-only versus runtime), the Protobuf options-attributes design borrows these two names to leverage developers' existing mental models.

## 关键特征
- **Standardized metadata**: A formal, language-level mechanism for attaching structured information to program elements (classes, methods, fields, etc.).
- **Target attribute**: Restricts which program elements an annotation type is allowed to annotate — directly mirrored by the `target` attribute on Protobuf features/options.
- **Retention attribute**: Controls the lifespan of annotations (e.g., `SOURCE`, `CLASS`, `RUNTIME`) — directly mirrored by the `retention` attribute on Protobuf features/options.
- **Cross-language design borrowing**: Protobuf Editions explicitly adopts the `target`/`retention` naming because the analogy with the well-known Java feature is immediately recognizable to developers.
- **Naming rationale**: Other candidate names were considered during design, but none proved superior to the Java-annotation-inspired terminology.

## 应用
- **Protobuf Editions options-attributes design**: The `target` attribute on a feature/option restricts the places (e.g., field, message, file, method) where the option can bind, mirroring Java annotations' target restriction mechanism.
- **Protobuf Editions retention policy**: The `retention` attribute on a feature/option specifies how long the option's effect is retained (analogous to Java annotation retention policies such as source-only vs. runtime).
- **Developer familiarity**: By aligning naming and semantics with a widely-known Java language feature, the design lowers the cognitive cost for developers moving between Java annotations and Protobuf options.

## 相关概念
- [[concepts/target-attributes|Target Attributes]]
- [[concepts/retention|Retention]]

## 相关实体
No related entities.

## 来源提及
- "To allow language specific extensions to restrict the places where options can bind, we will allow features to explicitly specify the targets they apply to (similar in concept to the \"target\" attribute on Java annotations)." — [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]