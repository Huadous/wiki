---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions]]"]
tags: [phenomenon]
aliases:
  - "依赖膨胀"
  - "proto dependency bloat"
---


# Dependency Bloat

## 定义
Dependency Bloat（依赖膨胀）是 Protocol Buffers 实践中因在单个 `.proto` 文件中定义过多消息类型（如 `message`、`enum`、`service`）而导致的问题。当大量消息具有不同依赖关系时，合并到一个文件会引入不必要的编译依赖，增加编译时间并使代码库变得臃肿。

## 关键特征
- 由过度聚合的文件组织引起：将多种消息类型（`message`、`enum`、`service`）全部放入一个 `.proto` 文件。
- 编译依赖膨胀：即使某个目标只需要少数消息类型，也必须包含整个 `.proto` 文件的所有依赖，导致不必要的构建开销。
- 编译时间增加：带来的间接依赖链越长，编译时间越长。
- 代码耦合度提升：文件间的依赖关系变得隐式且难以管理。

## 应用
- 在 Protocol Buffers 项目中进行 `.proto` 文件模块化设计时，寻求控制每个文件的消息类型数量。
- 在大型 Protobuf 项目中优化构建系统，通过拆分文件降低增量编译时间。
- 在代码审查和架构设计中作为指导原则，避免过度集成式的消息定义。

## 相关概念
- [[concepts/message-type|Message Type]]
- [[concepts/enumeration|Enumeration]]
- [[concepts/editions|edition]]

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]]

## 来源提及
- "While multiple message types (such as message, enum, and service) can be defined in a single .proto file, it can also lead to dependency bloat when large numbers of messages with varying dependencies are defined in a single file." — [[protobuf/editions|editions]]
- "It's recommended to include as few message types per .proto file as possible." — [[protobuf/editions|editions]]