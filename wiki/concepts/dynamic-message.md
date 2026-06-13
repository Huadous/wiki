---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[concepts/self-describing-messages]]"]
tags: [term]
aliases:
  - "动态消息"
  - "Dynamic Message模式"
---

# dynamic-message

> 动态消息是一种在运行时才能确定完整结构和类型的信息传输单元，其Schema或格式定义不预先固定，而是随消息本身一起传递或通过外部协定动态解析。

## 定义

动态消息（Dynamic Message）是指在通信或数据交换过程中，消息的结构、字段定义、数据类型等信息不是在编译期或静态契约中固定的，而是在运行时根据消息携带的元数据或外部Schema动态确定的。与静态类型消息（如基于预定义Protocol Buffers或Thrift IDL的消息）不同，动态消息允许通信双方在不重新部署代码的情况下变更数据格式。该概念在[[concepts/self-describing-messages|自描述消息]]系统中尤为关键，因为自描述消息是动态消息的一种实现形式，其元数据嵌入在载荷中。

## 关键特征

- **类型延后确定**：消息的完整类型信息在发送或接收时才解析，而非在编译期绑定。
- **Schema与数据解耦**：Schema定义可以与数据流分离（如通过Schema Registry），也可内嵌于消息中。
- **灵活性优先**：支持协议演进、字段增删和兼容性变更，无需重新生成代码。
- **运行时开销**：动态解析会引入额外的序列化/反序列化性能损耗。
- **向后兼容**：通常配合版本号或兼容性规则（如编号机制）实现新旧版本共存。

## 应用

- **分布式系统中的协议演进**：在微服务或RPC框架（如[[entities/brpc|Apache brpc]]）中，使用动态消息实现接口升级而不中断线上服务，常与自描述消息结合。
- **通用数据管道**：如Kafka或Pulsar中，采用动态消息（Avro/JSON Schema with Schema Registry）支持多版本数据共存。
- **配置管理与控制协议**：在[[entities/nginx|nginx]]或[[entities/envoy-proxy|Envoy]]等代理的动态控制面中，使用动态消息（如xDS协议中的protobuf Any类型）分发配置。
- **跨语言通信**：无预编译IDL的场景（如REST/GraphQL API），请求和响应结构动态定义，通过反射或元数据驱动。

## 相关概念

- [[concepts/self-describing-messages|自描述消息]]：动态消息的核心实现方式之一，消息自身携带Schema信息。
- [[concepts/schema-on-read|读取时Schema]]：一种数据处理哲学，与动态消息的理念互补，强调在消费端决定数据解释方式。
- [[concepts/protocol-buffers-any|Protocol Buffers Any]]：Google Protobuf的Any类型，允许封装任意序列化消息，是实现动态消息的典型技术。

## 相关实体

- [[entities/brpc|Apache brpc]]：该RPC框架内置对动态消息的支持，可通过解析请求中的元数据选择服务接口版本。
- [[entities/protocol-buffers|Protocol Buffers]]：其Any类型和反射机制是构建动态消息系统的基础工具之一。
- [[entities/apache-kafka|Apache Kafka]]：配合Schema Registry使用动态消息实现事件流的兼容性管理。

## 来源提及

*(No source content available for this page)*