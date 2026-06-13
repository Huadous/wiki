---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-evolution|editions-edition-evolution]]"]
tags: [term]
aliases:
  - "Backend Features"
  - "backend: features"
  - "后端特性"
---


# Backend Features

## 定义
Backend Features 是指命名空间为 `backend:` 前缀的 Protobuf 特性。与由 protoc 前端实现的 `proto:` 特性不同，backend features 由特定的代码生成后端（code generator backend）实现并定义其默认值。后端需要生成一种类似 `message Edition { repeated Feature defaults = 1; }` 的描述性 proto，通过 `EditionIsLaterThan`、`EditionIsBetween` 等谓词声明该 feature 在哪些 edition 范围内生效；protoc 前端据此汇总所有后端提供的特性信息，向用户呈现完整的特性集合。

## 关键特征
- 命名空间前缀为 `backend:`，与前端特性 `proto:` 在作用域上明确区分
- 由具体的代码生成后端（language-specific backend）实现，非 protoc 前端实现
- 默认值由后端自行定义，后端需声明每个 feature 在哪些 edition 区间内生效
- 生效范围通过 `EditionIsLaterThan`、`EditionIsBetween` 等比较/区间谓词描述
- 后端需产出形如 `message Edition { repeated Feature defaults = 1; }` 的描述性 proto 供 protoc 汇总
- protoc 前端负责跨后端汇总，最终向用户展示统一的特性清单

## 应用
- 在 Protobuf Editions 体系中区分前端通用特性与语言/后端专属特性
- 支持 C++、Java、Python 等不同语言后端各自扩展专属特性而互不干扰
- 为 Edition Evolution 提案中的特性注册与默认值机制提供后端侧的声明通道
- 在跨后端场景下，让 protoc 能聚合所有 backend features 形成完整的 FeatureSet 描述

## 相关概念
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/Protobuf Features|Protobuf Features]]
- [[concepts/Total Ordering of Editions|Total Ordering of Editions]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "If the feature is a backend feature, the backend must be able to produce some kind of proto like `message Edition { repeated Feature defaults = 1; }` that describes what a specific edition must look like, based on less-than/is-between predicates like those above." — [[sources/editions-edition-evolution|editions-edition-evolution]]