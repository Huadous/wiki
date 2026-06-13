---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [project]
aliases:
  - "New String APIs project"
  - "New String APIs 项目"
---


# New String APIs

## 基本信息
- Type: project
- Source: [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]

## 描述
New String APIs 是 Protobuf 中引入 `string_type` 特性的具体功能项目，文中作为案例研究出现，并未对外发布。该项目在引入 `string_type` 新特性时遇到了一个核心问题：在已有版本（如 [[concepts/edition-2023|Edition 2023]]）中引入新特性会导致旧二进制无法正确处理该特性。为应对此问题，Protobuf 团队当时采用了临时的 `ad hoc` 验证方案，禁止在 Edition 2023 中覆盖 `string_type`，直到该特性准备发布。该案例直接驱动了原文关于[[concepts/feature-lifetimes|Feature Lifetimes]]管理的设计建议，是[[entities/protobuf|Protobuf]]版本演进中的重要实证参考。

## 相关实体
- [[entities/protobuf|Protobuf]]

## 相关概念
- [[concepts/feature-lifetimes|Feature Lifetimes]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/feature-deprecation|Feature Deprecation]]

## 来源提及
- We faced this problem when introducing the new `string_type` feature as part of *New String APIs* (not available externally). — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- Our solution at the time was to create some ad hoc validation that prohibited overriding this feature in Edition 2023 until we were ready to release it. — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]