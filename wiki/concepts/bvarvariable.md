---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "bvar::Variable 基类"
  - "Variable 基类"
---


# bvar::Variable

## 定义
`bvar::Variable` 是所有 bvar 的基类，主要提供全局注册、列举、查询等功能。它是 bvar 体系中所有具体计数器类型的共同父类，统一管理 bvar 的曝光（expose）与查询接口。

## 关键特征
- 作为基类，为 `bvar::Adder`、`bvar::Status`、`bvar::Window`、`bvar::PerSecond` 等具体 bvar 类型提供公共行为。
- 用户以默认参数建立一个 bvar 时，该 bvar 并未注册到任何全局结构中，此时 bvar 纯粹是一个更快的计数器。
- 通过 `expose` 或 `expose_as` 函数可以将 bvar 曝光到全局表中。
- 曝光后的 bvar 可通过 `describe_exposed`、`list_exposed`、`count_exposed`、`find_exposed` 等 static 函数查询。
- 全局曝光后的 bvar 名字为 `name` 或 `prefix + name`，可通过以 `_exposed` 为后缀的 static 函数查询。
- 当重名时 `expose` 会打印 FATAL 日志并返回 -1；如果设置了 `-bvar_abort_on_same_name` 为 true 则直接 abort。

## 应用
- 作为 bvar 类型体系的统一基类，支撑各类监控指标的注册与查询。
- 在 brpc 服务中用于将内部计数器曝光到全局表，便于通过 `/vars` 等 HTTP 接口对外暴露运行时指标。
- 提供全局查询能力，便于运维和监控系统统一采集与展示指标数据。

## 相关概念
- [[concepts/bvar::Adder]]
- [[concepts/bvar::Status]]
- [[concepts/bvar::Window]]
- [[concepts/bvar::PerSecond]]

## 相关实体
- [[entities/bvar]]

## 来源提及
- Variable是所有bvar的基类，主要提供全局注册，列举，查询等功能。 — [[sources/bvar_c++|bvar_c++]]
- 全局曝光后的bvar名字便为name或prefix + name，可通过以_exposed为后缀的static函数查询。 — [[sources/bvar_c++|bvar_c++]]