---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-editions-for-schema-producers]]"]
tags: [term]
aliases:
  - "Support Matrix"
  - "支持矩阵"
  - "Protobuf Support Matrix"
---


# Support Matrix

## 定义
Support Matrix（支持矩阵）指的是 schema producer 声明其所支持的一组 protobuf 版本范围的概念，是决定 edition 升级策略的关键依据。一个 schema producer 通过支持矩阵明确自身能够处理哪些 protobuf 版本，进而约束其在选择 edition 时必须满足的兼容性边界。

## 关键特征
- 描述 schema producer 所声明支持的 protobuf 版本范围，是 edition 升级的前置约束
- schema producer 不应支持自身已不被官方支持的 protobuf 版本
- 发布 `.proto` 文件时应统一使用同一 edition，以简化用户的使用
- 更新 edition 时必须选择其支持矩阵中所有 protobuf 版本都共同支持的 edition
- 经验法则：目标是选取支持矩阵中最旧版本所支持的最新 edition

## 应用
- 作为 schema producer 制定 edition 升级路径时的核心决策依据
- 在跨语言、跨版本 protobuf 生态中，约束 edition 的兼容性与发布策略
- 帮助发布者确定在保留向后兼容的同时能够使用的最新 edition

## 相关概念
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/wire-format-compatibility|Wire Format Compatibility]]

## 相关实体
- [[entities/schema-producer|Schema Producer]]
- [[entities/protobuf-editions|Protobuf Editions]]

## 来源提及
- "Any schema producer should already specify what versions of protobuf they support and should not support versions of protobuf that are themselves unsupported." — [[sources/editions-protobuf-editions-for-schema-producers]]