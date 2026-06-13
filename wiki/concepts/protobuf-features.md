---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-evolution|editions-edition-evolution]]"]
tags: [term]
aliases:
  - "Features"
  - "Protobuf 特性"
---


# Protobuf Features

## 定义
Protobuf Features 是 [[concepts/Protobuf Editions|Protobuf Editions]] 体系中的基本配置单元，以**标志（flag）**的形式关联到 `.proto` 文件的语法项上。每个 feature 既可由 edition 隐式推导得出，也可由用户在 `.proto` 文件中显式设定。feature 的命名通常采用 `namespace:feature_name` 的形式，例如 `proto:closed_enums` 或 `cpp:string_view`。其中 `proto:` 前缀的特性由 `protoc` 前端实现，而 `backend:` 前缀的特性则由对应的代码生成后端负责实现并定义其默认值。

## 关键特征
- **标志形式**：每个 feature 是一个与语法项绑定的标志位，可隐式推导或显式声明。
- **命名空间前缀**：采用 `namespace:feature_name` 形式，`proto:` 前缀对应 protoc 前端行为（如 `proto:closed_enums`），`backend:` 前缀对应特定代码生成后端（如 `cpp:string_view`）。
- **职责划分**：
  - `proto:` 前缀特性由 [[entities/protoc|protoc]] 前端实现；
  - `backend:` 前缀特性由对应代码生成后端实现并定义默认值。
- **显式或隐式**：用户可在 `.proto` 文件中显式设置，也可由当前 edition 自动推导。

## 应用
- **协议演进控制**：在 [[concepts/Protobuf Editions|Protobuf Editions]] 模式下，通过 feature 精确控制不同 edition 下的语法行为，避免全局破坏性变更。
- **后端行为定制**：借助 `backend:` 前缀特性（如 `cpp:string_view`），针对特定语言后端启用或关闭生成代码层面的优化与行为。
- **Schema 兼容性管理**：通过 feature 的显式/隐式设定，精细调整 enum 封闭性、字段存在性、JSON 行为等语义。
- **跨后端一致性**：与 [[concepts/Backend Features|Backend Features]] 配合，区分 protoc 通用语义与各语言后端实现细节。

## 相关概念
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/Backend Features|Backend Features]]
- [[concepts/Total Ordering of Editions|Total Ordering of Editions]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "Features are flags associated with syntax items of a `.proto` file; they can be either set explicitly, or they can be implied by the edition." — [[sources/editions-edition-evolution|editions-edition-evolution]]
- "Features can either correspond to behavior in `protoc`'s frontend (e.g. `proto:closed_enums`), or to a specific backend (`cpp:string_view`)." — [[sources/editions-edition-evolution|editions-edition-evolution]]