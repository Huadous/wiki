---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
tags:
  - "method"
aliases:
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance tests"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance test"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
  - "Conformance tests"
  - "Conformance Testing"
  - "一致性测试"
  - "conformancetest"
---

## Description
Conformance Testing 在 protobuf 生态中扮演多重角色。一方面，在 Editions / FeatureSet 场景下，它借助现有 conformance runner 模型：runner 端构造测试样例并序列化请求，目标语言二进制完成解析/变换后返回响应，再与 C++ 真相源（source of truth）对比，从而保证各语言运行时对特性解析保持一致；为此文档提出了 `DescriptorConformanceRequest` / `DescriptorConformanceResponse` 的 proto 设计，以统一、可扩展的方式表达任意针对 descriptor 的转换，避免各语言重复造轮子。另一方面，Conformance Testing 也常被直接用作"行为锁定"工具：现存的 conformance test 已经锁定了 group 消息在 text-format 中使用消息名的正向行为（即消息名能正确往返），而反向行为（拒绝字段名）目前尚未被 conformance test 覆盖（但 C++/Java/Python 已达成共识且无已知反例）。在引入新的语言级方案（如 Smooth Extension）时，开发者也会显式承诺添加新的 conformance tests 来锁定该方案引入的行为变更。除此之外，由于 Editions 推荐方案将功能行为封装在每种语言运行时的高层帮助方法中（例如 `has_presence`、`requires_utf8_validation` 等），跨语言行为复制成为必然——这使得一致性测试成为确保各语言在解释 Editions 功能时行为统一的必要手段。该模型已经在 edition zero features 上成功落地，并将继续沿用为 Editions 系统推广过程中维护跨语言互操作性的核心方法论。

## Related Concepts
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/featureset|FeatureSet]]
- [[concepts/group-fields|Group Fields]] *(implied by group migration context — link deferred until page exists)*
- [[concepts/smooth-extension|Smooth Extension]] *(implied by Smooth Extension 方案 — link deferred until page exists)*
- [[concepts/text-format|Text Format]] *(implied by text-format 往返行为 — link deferred until page exists)*
- [[concepts/feature-visibility|Feature Visibility]] *(implied by Editions Feature Visibility 上下文 — link deferred until page exists)*

## Related Entities
- [[entities/protoc|protoc]]

## Mentions in Source

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "Code duplication means that we need a test strategy for making sure everyone stays conformant."
> - "Our current conformance tests provide a good model for accomplishing this, even though they don't quite fit the problem (they're designed for parsing/serialization)."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "We also have conformance tests locking down the positive path here (i.e. using the message name round-trip)."
> - "The negative path (i.e. failing to accept the field name) doesn't have a conformance test, but C++/Java/Python all agree and there's no known case that doesn't."

> **Source: [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]**
> - "Requires duplicating high-level feature behaviors across every language. For example, `has_presence` will need to be implemented identically in every language. We will likely need some kind of conformance test to make sure these all agree."
> - "This has already been done for edition zero features (e.g. `has_presence`, `requires_utf8_validation`, etc), and we should continue this model."