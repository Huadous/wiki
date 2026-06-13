---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-feature-visibility]]"]
tags: [term]
aliases:
  - "descriptor APIs"
  - "proto descriptor"
---


# Descriptor API

## 定义
Descriptor API 是 Protocol Buffers 在运行时用于描述 proto 文件元数据的接口层，例如 C++ 中的 `CopyTo` 和 `DebugString` 等方法。在 Editions Feature Visibility 的语境下，descriptor 既是承载 [[concepts/feature-set|FeatureSet]] 的容器，也是用户访问 feature 的入口。

## 关键特征
- 提供运行时访问 proto 元数据的能力，是用户读取 descriptor 层信息的统一入口
- 推荐方案要求在 descriptor 上提供 helper 方法（如 `has_presence`、`requires_utf8_validation`），以便用户便捷获取关键 feature 状态
- 建议在 `options()` getter 中将 features 字段置空，使 descriptor API 不再与原始 proto 文件保持 1:1 对应关系
- 与历史上 `options()` 一直忠实反映 proto 文件内容的做法存在不一致，被文档明确承认为一种权衡取舍
- 不同运行时（μpb、Java Lite 等）需各自实现各自的 descriptor API 接口

## 应用
- 用户在运行时查询 message、field 等的元数据信息（如 `DebugString` 调试输出、`CopyTo` 序列化还原）
- 作为 Editions 体系下访问 [[concepts/resolved-features|Resolved Features]] 的入口，屏蔽底层 proto 文件的差异
- 为运行时反射（reflection）和代码生成提供底层支撑，使各类 helper 方法得以构建在 descriptor 之上

## 相关概念
- [[concepts/feature-set|FeatureSet]]
- [[concepts/editions-feature-visibility|Editions Feature Visibility]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/unresolved-features|Unresolved Features]]

## 相关实体
- [[entities/micro-pb|μpb]]
- [[entities/editions|Editions]]

## 来源提及
- Most of our runtimes provide APIs for converting descriptors back to their original state at runtime (e.g. `CopyTo` and `DebugString` in C++). — [[sources/editions-editions-feature-visibility|editions-editions-feature-visibility]]