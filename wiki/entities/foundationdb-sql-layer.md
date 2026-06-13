---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [product]
aliases:
  - "SQL Layer"
  - "FoundationDB SQL Layer"
---


# FoundationDB SQL Layer

## 基本信息
- Type: product
- Source: [[sources/options|options]]

## 描述
FoundationDB SQL Layer 是 FoundationDB 在其分布式键值存储之上构建的 SQL 接口层,旨在为 FoundationDB 提供 ANSI SQL 兼容性,使传统关系型数据库应用能够利用 FoundationDB 的事务保证与水平扩展能力。该项目注册了 Protocol Buffers 全局扩展编号 1014,代码托管在 GitHub 的 FoundationDB/sql-layer 仓库中。SQL Layer 使用 Protocol Buffers 作为其内部 API 与客户端通信的序列化格式,并通过 [[concepts/descriptor-proto|descriptor.proto]] 扩展自定义选项。由于 FoundationDB 调整产品方向,该项目已不再积极开发,但其代码与设计文档仍可供参考,作为在分布式 KV 存储之上构建 SQL 层的典型案例。

## 相关实体
- [[entities/protocolbuffersprotobuf|protobuf]]
- Protobuf Global Extension Registry

## 相关概念
- Extension numbers
- Custom options
- descriptor.proto

## 来源提及
- FoundationDB SQL Layer — [[sources/options|options]]
- Website: https://github.com/FoundationDB/sql-layer — [[sources/options|options]]
- Extensions: 1014 — [[sources/options|options]]