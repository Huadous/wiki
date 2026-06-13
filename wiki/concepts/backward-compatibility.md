---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/overview]]"]
tags: [phenomenon]
aliases:
  - "向后兼容"
  - "backward-compatible"
  - "downward compatible"
---


# 向后兼容性

## 定义

向后兼容性指的是新版本的协议缓冲区定义能够被使用旧版本 protobuf 代码的消费者正确解析和读取，而不引发错误或数据丢失。这是 Protocol Buffers 设计中确保系统长期稳定演进的核心属性。

## 关键特征
- **字段新增安全**：旧代码在遇到未知字段时会自动忽略，不会中断解析过程。
- **数据持久性**：即使服务版本更新，存储在磁盘或消息队列中的旧序列化数据依然可被新系统读取。
- **无需停机升级**：允许不同服务以不同节奏升级 protobuf 定义，保持互操作性。
- **设计约束**：通过严格遵循字段编号规则和语义来实现——已删除字段的编号不得复用，新增字段只能使用新编号。

## 应用
- **微服务架构**：不同团队维护的微服务各自独立升级 protobuf schema，后端服务添加新字段后，前端旧版本依然能正常工作。
- **长期归档系统**：存储于持久化存储（如 Bigtable）中的 protobuf 数据，在新旧版本之间迁移时无需重写全部数据。
- **跨版本 API**：公共 API 提供商（如 Google Maps API）允许客户端使用不同版本的 protobuf 定义通信而不中断。

## 相关概念
- [[concepts/Forward Compatibility|向前兼容性]]
- [[concepts/Field Number|字段编号]]
- [[entities/protocol-buffers|protocol-buffers]]

## 相关实体
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/google|google]]

## 来源提及
- "Because protocol buffers are used extensively across all manner of services at Google and data within them may persist for some time, maintaining backwards compatibility is crucial." — [[protobuf/overview|overview]]
- "Protocol buffers allow for the seamless support of changes, including the addition of new fields and the deletion of existing fields, to any protocol buffer without breaking existing services." — [[protobuf/overview|overview]]