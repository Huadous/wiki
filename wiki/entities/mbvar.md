---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/bvar_c++.md]]"]
tags: [product]
aliases:
  - "多维度bvar"
  - "mbvar (multi-dimensional bvar)"
---


# mbvar

## 基本信息
- Type: product
- Source: [[sources/bvar_c++|bvar_c++]]

## 描述
mbvar 是 brpc 中 bvar 的多维度版本，提供了多维标签的统计能力。它在 [[sources/bvar_c++|bvar_c++]] 文档开头被明确指引：单维度 bvar 的使用请参考该文档，而多维度场景则需要使用 mbvar。mbvar 与单维度的 [[entities/bvar|bvar]] 在 API 上有所差异，其设计支持类似 Prometheus 的标签维度查询方式，允许用户通过多个标签组合来定义和查询指标。mbvar 是 [[entities/brpc|brpc]] 监控统计体系的重要组成部分，专门用于处理需要多维度聚合的复杂监控场景。

## 相关实体
- [[entities/bvar|bvar]] — mbvar 的单维度版本，提供基础的单标签统计能力
- [[entities/brpc|brpc]] — mbvar 所属的 RPC 框架项目

## 相关概念
- No related concepts

## 来源提及
- 单维度bvar使用文档，多维度mbvar请移步(mbvar_c++.md)。 — [[sources/bvar_c++|bvar_c++]]