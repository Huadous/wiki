---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/field_presence]]"
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
tags:
  - "standard"
aliases:
  - "Forward and backward compatibility"
  - "向前向后兼容性"
  - "wire format compatibility"
  - "Wire Format Compatibility"
  - "Forward and backward compatibility"
  - "向前向后兼容性"
  - "wire format compatibility"
---

## Related Concepts
- [[concepts/wire-format|Wire format]]
- [[concepts/field-presence|Field presence]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/feature|Feature]]
- [[concepts/schema-producer|Schema Producer]]
- [[concepts/schema-consumer|Schema Consumer]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]]

## Mentions in Source
- "The generated API for a proto message includes (de)serialization definitions which translate between API types and a stream of definitionally _present_ (tag, value) pairs."（proto 消息的生成 API 包含（反）序列化定义，用于在 API 类型与 definitionally _present_ 的 (tag, value) 对流之间转换。）— [[sources/field_presence]]
- "This translation is designed to be forward- and backward-compatible across changes to the message definition."（该转换被设计为在消息定义变更时保持向前和向后兼容。）— [[sources/field_presence]]

> **Source: [[sources/editions-protobuf-editions-for-schema-producers|editions-protobuf-editions-for-schema-producers]]**
> - "As a reminder, features will generally not change the wire format of messages and thus changing the edition for a `.proto` will not change the wire format of message."（提醒一下，features 一般不会改变消息的 wire format，因此更改 `.proto` 文件的 edition 也不会改变消息的 wire format。）
> - "Because language-specific features will not change the wire format of messages, clients will be able to update to newer editions or specify specific features appropriate to their environment while still connecting to external endpoints."（由于语言特定的 features 不会改变消息的 wire format，客户端将能够在保持与外部端点连接的同时，升级到更新的 edition 或按需指定适合其环境的特定 features。）