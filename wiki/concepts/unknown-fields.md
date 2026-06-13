---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [term]
aliases:
  - "unknown field"
  - "Unknown Fields"
---


# Unknown fields

## 定义
Unknown fields 是 Protocol Buffers 解析过程中存储在 API 中但当前消息定义无法识别的字段。在 wire format 解析时，即使某个 tag 被识别（例如枚举字段的 tag），如果值超出枚举类型的有效范围，proto2 API 不会直接返回该值，而是可能将其存储为 unknown fields。

## 关键特征
- 在 wire format 解析阶段，tag 可被识别但值无法被当前消息定义解释时，字段内容会被保留为 unknown fields
- 接收方不会丢弃无法识别的数据，而是将其存储在消息对象中
- 提供了 Protocol Buffers 的向前兼容能力：发送方新增字段后，旧版本的接收方仍能正常解析并保留新字段的信息
- 当消息被序列化时，unknown fields 会被重新写入 wire format，从而实现数据透传
- 适用于 proto2 API 中的枚举字段等场景：超出枚举有效范围的值不会直接返回，而是作为 unknown fields 存储

## 应用
- 协议版本演进：消息定义新增字段后，旧版本接收方可保留未知字段，待升级后再处理
- 跨版本数据透传：中间节点不理解某字段时，可原样保留并在后续节点中恢复
- 调试与审计：通过检查 unknown fields 辅助诊断协议不一致问题

## 相关概念
- [[concepts/wire-format|Wire format]]
- [[concepts/field-presence|Field presence]]

## 相关实体
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]

## 来源提及
- "Out-of-range values are not returned for enum fields in generated proto2 APIs." — [[sources/field_presence|field_presence]]
- "However, out-of-range values may be stored as _unknown fields_ in the API, even though the wire-format tag was recognized." — [[sources/field_presence|field_presence]]