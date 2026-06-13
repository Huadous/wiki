---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/field_presence]]"]
tags: [standard]
aliases:
  - "Forward and backward compatibility"
  - "向前向后兼容性"
  - "wire format compatibility"
---


# Forward and backward compatibility

## 定义
Forward and backward compatibility（向前和向后兼容性）是 Protocol Buffers wire format 的核心设计目标。生成的消息 API 包含在 API 类型和 definitionally present 的 (tag, value) 对流之间转换的（反）序列化定义，这些转换被设计为在消息定义变更时保持向前和向后兼容。然而，这种兼容性也带来了一些值得注意的考虑，例如 empty length-delimited 值在 no presence API 中可能不会在序列化往返中保留。在 explicit presence 和 no presence 之间切换时，序列化的二进制兼容，但表示可能会有所不同。

## 关键特征
- 生成的 proto 消息 API 提供 (de)serialization 定义，用于在 API 类型与 definitionally present 的 (tag, value) 对流之间转换
- 该转换在消息定义（.proto 文件）发生变更时，被设计为保持向前和向后兼容
- empty length-delimited 值在 no presence API 中可能无法在序列化往返中保留
- 在 explicit presence 与 no presence 两种语义之间切换时，序列化结果保持二进制兼容，但内存/表示层面的行为可能不同
- 作为 wire format 层面的标准兼容性保证，独立于具体的字段存在性（field presence）规则

## 应用
- 跨版本的 Protocol Buffers 消息演进：在不破坏现有部署的前提下向消息中添加、修改或废弃字段
- 跨语言、跨平台的服务通信：保证旧客户端能读取新服务端发出的消息，以及新客户端能读取旧服务端发出的消息
- 大规模分布式系统中渐进式协议升级：在不停机的情况下滚动部署不同版本的客户端和服务端
- 在 field presence 语义（explicit presence / no presence）之间迁移时，作为二进制兼容性的底线参考

## 相关概念
- [[concepts/wire-format|Wire format]]
- [[concepts/field-presence|Field presence]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/no-presence-discipline|No presence discipline]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "The generated API for a proto message includes (de)serialization definitions which translate between API types and a stream of definitionally _present_ (tag, value) pairs."（proto 消息的生成 API 包含（反）序列化定义，用于在 API 类型与 definitionally _present_ 的 (tag, value) 对流之间转换。）— [[sources/field_presence]]
- "This translation is designed to be forward- and backward-compatible across changes to the message definition."（该转换被设计为在消息定义变更时保持向前和向后兼容。）— [[sources/field_presence]]