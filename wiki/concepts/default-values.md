---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/proto3]]"]
tags: [term]
aliases:
  - "默认值"
  - "零值"
  - "Default Values"
---


# Default Values

## 定义
Default Values 是 Protocol Buffers proto3 中定义的规则：当 protobuf 消息中某个字段未被用户显式设置值时，访问该字段会返回一个与该字段类型对应的默认值。对于标量类型，默认值根据类型定义（如数值类型为 0、布尔类型为 false、字符串为 ""、字节为 empty bytes）；对于消息类型（message fields），其行为类似于 `optional` 字段。所有隐式字段（即未标记 `optional` 或 `required` 的字段）的默认值**不会被序列化**到线格式中，因此接收方无法区分该字段是显式设置为默认值，还是从未被设置。

## 关键特征
- **类型相关默认值**：每种标量类型有固定的默认值——数值型为 0、布尔型为 false、字符串为 ""、字节类型为空字节序列。
- **不被序列化**：默认值（包括显式赋值与未赋值）不会出现在序列化后的二进制数据中，这是 proto3 为了节省带宽和存储空间而做的优化。
- **隐含语义模糊**：由于默认值不被序列化，接收方在解析时无法判断字段的原始值是否来自传输。如果需要区分“未设置”与“显式设置为零值”，必须使用 `optional` 字段配合字段存在性检查（field presence）。
- **消息类型的特殊处理**：对于消息类型字段，当消息未被设置时返回默认的空消息（而不是零值），且该行为与 `optional` 字段一致（proto3 中消息字段默认即具有存在性语义）。

## 应用
- **数据传输优化**：在 RPC 调用和序列化过程中，大量字段取默认值时不会被传输，显著减少网络 I/O 和序列化开销。
- **增量同步与补丁**：当仅需传输非默认值的字段时，可简化增量更新（例如在 brpc 等 RPC 框架中传递部分数据）。
- **向后兼容处理**：当 protobuf 定义新增字段后，旧客户端产生的消息中该字段为默认值，新服务端能正确识别并返回默认值，保证兼容性。

## 相关概念
- [[concepts/field-presence|field-presence]]
- [[concepts/scalar-types|scalar-types]]
- [[concepts/field-cardinality|field-cardinality]]

## 相关实体
- [[entities/Protocol-Buffers|Protocol Buffers]]

## 来源提及
- "the field is unset, and will return the default value. It will not be serialized to the wire." — [[sources/proto3|proto3]]
- "the field is set to the default (zero) value. It will not be serialized to the wire." — [[sources/proto3|proto3]]