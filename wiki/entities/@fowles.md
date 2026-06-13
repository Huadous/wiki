---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/editions-protobuf-editions-design-features.md]]"
  - "[[protobuf/editions-protobuf-design-options-attributes.md]]"
tags:
  - "person"
aliases:
  - "Fowles"
  - "fowles"
  - "@kfm"
  - "Fowles"
  - "fowles"
---

## Description
@fowles（GitHub 用户名 fowles，亦以 @kfm 身份出现）是 Protobuf Editions 项目的重要贡献者，参与了多项核心设计提案的撰写与推动。他是《What are Protobuf Editions》介绍文档的共同作者，与 @mcy 共同向开发者介绍 Editions 的基本概念；同时也是《Protobuf Editions Features》设计提案的共同作者，与 @haberman 合作规划 Editions 中 Features 的语法与机制。除文档和特性设计外，@fowles 还单独撰写了《Protobuf Editions: Options Attributes》设计提案（以 @kfm 名义署名），为 Protobuf 选项系统引入 target 与 retention 属性，该提案于 2022-08-26 获得批准。综合来看，@fowles 的工作横跨 Editions 的概念介绍、Features 语法设计以及底层选项机制扩展三个层面，是 Protobuf Editions 演进过程中的关键贡献者之一。

## Related Entities
- [[entities/@mcy|@mcy]] — 《What are Protobuf Editions》文档的共同作者
- [[entities/@haberman|@haberman]] — Protobuf Editions Features 设计提案的共同作者
- [[entities/protobuf-team|protobuf-team]] — @fowles 隶属的 Protobuf 开发团队
- [[entities/google|Google]] — @fowles 可能的所属组织

## Related Concepts
- [[concepts/protobuf-editions|Protobuf Editions]] — @fowles 共同作者的项目核心概念
- [[concepts/features|Features]] — Editions 中通过自定义选项定义的特性
- [[concepts/custom-options|Custom Options]] — 用于实现 Features 语法的 Protobuf 现有机制
- [[concepts/options-attributes|Options Attributes]] — @fowles 在 Options Attributes 设计提案中扩展的 Protobuf 选项属性
- [[concepts/target-attributes|Target Attributes]] — Options Attributes 提案中新增的 target 属性
- [[concepts/retention|Retention]] — Options Attributes 提案中新增的 retention 属性

## Mentions in Source

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Authors: [@mcy](https://github.com/mcy), [@fowles](https://github.com/fowles)"

> **Source: [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]**
> - "**Author:** [@haberman](https://github.com/haberman), [@fowles](https://github.com/fowles)"
> - "Protobuf already supports custom options and we will leverage these to provide a rich syntax without introducing new syntactic forms into Protobuf."
> - "No directly relevant information"

> **Source: [[sources/editions-protobuf-design-options-attributes|editions-protobuf-design-options-attributes]]**
> - "**Author:** [@kfm](https://github.com/fowles)"
> - "**Approved:** 2022-08-26"