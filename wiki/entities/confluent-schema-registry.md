---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Confluent Schema Registry"
  - "schema-registry"
  - "CSR"
---


# Confluent Schema Registry

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Confluent Schema Registry 是由 [[entities/confluent|Confluent]] 公司提供的模式注册服务，专门用于管理 [[entities/kafka|Kafka]] 消息的模式演化。它在 [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] 中分配到的扩展编号为 1088，源代码托管在 https://github.com/confluentinc/schema-registry。该项目在 Kafka 生态系统中扮演关键角色，支持 Avro、JSON Schema 和 Protocol Buffers 等多种模式格式的版本化管理和兼容性检查，确保上下游服务在模式演进过程中保持兼容性，避免因模式变更导致的数据处理错误。Confluent Schema Registry 与 [[entities/kafka|Kafka]] 紧密结合，提供了 RESTful API 用于模式的注册、查询和兼容性验证。

## 相关实体
- [[entities/perfetto|Perfetto]]
- [[entities/cloudstate|Cloudstate]]
- [[entities/confluent|Confluent]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- Confluent Schema Registry — [[sources/options|options]]
- Website: https://github.com/confluentinc/schema-registry — [[sources/options|options]]
- Extensions: 1088 — [[sources/options|options]]