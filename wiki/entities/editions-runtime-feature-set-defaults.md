---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [other]
aliases:
  - "Runtime Feature Set Defaults"
  - "Editions Runtime Feature Set Defaults"
---


# Editions: Runtime Feature Set Defaults

## 基本信息
- Type: other
- Source: [[sources/editions-editions-life-of-a-featureset]]

## 描述
Editions: Runtime Feature Set Defaults 是一份早先的内部设计文档，紧随 "Exposing Editions Feature Sets" 之后撰写，专门解决各运行时（runtime）应如何获取 proto2、proto3 与 editions 的默认 FeatureSet 值的问题。该文档的提出源于一个关键洞察：descriptor pool 的使用者可以完全绕过 [[entities/...|protoc]]，从而在生态中不存在一个权威的 edition 默认值来源。其提议的解决方案是让 protoc 前端作为唯一的 source-of-truth，再将默认值向下传递给各个运行时。该文档虽标注为 "not available externally"（不对外公开），但被明确引用为 [[sources/editions-editions-life-of-a-featureset|Editions: Life of a FeatureSet]] 的直接前身，并影响了 [[entities/...|descriptor.proto]] 引导（bootstrap）阶段的特殊处理方式。

## 相关实体
- [[entities/...|protoc]]
- [[entities/...|descriptor.proto]]

## 相关概念
- [[concepts/...|Feature Resolution]]
- [[concepts/...|Edition Defaults]]
- [[concepts/...|Descriptor Pool]]
- [[concepts/...|FeatureSet]]
- [[concepts/...|Global Features]]

## 来源提及
- *Editions: Runtime Feature Set Defaults* (not available externally) was a follow-up attempt to specifically handle the default feature sets of an edition. — [[sources/editions-editions-life-of-a-featureset]]