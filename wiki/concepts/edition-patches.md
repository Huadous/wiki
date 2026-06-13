---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [method]
aliases:
  - "Edition Patch"
  - "Edition Patches 补丁版本"
  - "Patching Old Editions"
---


# Edition Patches

## 定义
**Edition Patches**（补丁版本）是文档 [[sources/editions-edition-lifetimes|editions-edition-lifetimes]] 提出的一种应急机制，用于应对 Editions 不再完全向前/向后兼容的新情况。原本在 [[sources/editions-edition-naming|editions-edition-naming]] 中已经决定放弃"补丁版本"的想法，因为 Editions 假定始终是向前和向后兼容的；然而当特性生命周期绑定到 Edition 后，旧 Edition 可能因新 Edition 中删除特性而出现问题，补丁机制由此被重新引入。文档建议通过在 `FileDescriptorProto` 中新增 `edition_patch` 整数字段来支持补丁版本。

## 关键特征
- **应急性补丁机制**：原本 Editions 假定无需补丁版本，但特性生命周期绑定到版本后，旧版本可能因新版本中删除特性而出现问题，因此重新引入补丁机制。
- **受限的适用范围**：只要补丁不引入/删除特性（features），且不改变默认值（defaults），补丁就可以被应用。
- **统一的"最新补丁"约定**：`protoc` 和插件始终使用它们已知的最新补丁来代表该版本，从而在保证兼容性的同时简化实现。
- **`FileDescriptorProto` 中的 `edition_patch` 字段**：以整数字段的形式在描述符协议缓冲区中表达补丁编号。
- **向后兼容性的破坏前提**：补丁机制存在的前提是 Editions 已不再是完全向前兼容（新特性无法在旧 Edition 中工作）或完全向后兼容（旧特性在新 Edition 中可能失效）。

## 应用
- 在 `FileDescriptorProto` 中暴露 `edition_patch` 整数字段，使工具链能识别同一 Edition 下不同的补丁级别。
- 在不改变特性集合与默认值的前提下，通过补丁对旧 Edition 进行问题修复，使 `protoc` 及插件无需感知旧 Edition 中存在的缺陷。
- 为旧 Edition 中的用户提供补救通道，避免因新 Edition 删除特性而完全无法继续使用旧版本。

## 相关概念
- [[concepts/editions|Editions]]
- [[concepts/edition-lifetimes|Edition Lifetimes]]
- [[concepts/feature-lifetimes|Feature Lifetimes]]

## 相关实体
- [[entities/protobuf|Protobuf]]

## 来源提及
- "In [Edition Naming](edition-naming.md) we decided to drop the idea of "patch" editions, because editions were always forward and backward compatible." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- "This changes those assumptions though, since now editions are neither forward-compatible (new features don't work in old editions) or backward-compatible (old features may not work in new editions)." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]