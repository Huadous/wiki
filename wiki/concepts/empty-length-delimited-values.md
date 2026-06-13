---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/field_presence|field_presence]]"]
tags: [term]
aliases:
  - "Empty length-delimited values"
  - "empty wire format values"
  - "空长度分隔值"
---


# Empty length-delimited values

## 定义
Empty length-delimited values 是 wire format 中一类特殊的字段值表示：指那些虽然内容为空（如空字符串、空字节序列等 length-delimited 类型字段的零长度值），但其字段标签（tag）仍然被合法地写入到 wire format 中的序列化结果。在 wire format 的语义下，这些空值所对应的字段被视为"存在"（present）。然而，当生成代码所采用的 API 不跟踪显式存在性（_no presence_ discipline）时，这些空字段在反序列化后再重新序列化时可能不会再次被写入——即经历一次序列化 round trip 之后，原本"存在"的空字段在新的 wire format 中会变为"不存在"。这一现象揭示了 wire format 层面对"present"的定义与 API 层面对"present"的定义之间的一个微妙差异。

## 关键特征
- **合法可序列化**：空字符串、空字节等空值是 length-delimited 字段的有效序列化结果，其字段 tag 会被正常写入 wire format。
- **wire format 层面"存在"**：在序列化后的二进制数据中，该字段的 tag 及其 length-delimited 编码均存在，因此从 wire format 角度该字段是 present 的。
- **API 层面可能"不存在"**：在采用 _no presence_ discipline 的 API 中，运行时数据模型并不显式跟踪字段是否被设置，仅依靠默认值进行判断。
- **round trip 不稳定**：反序列化后再次序列化时，原本的空值可能因为 API 不区分"显式空值"与"未设置"而丢失字段的 tag 写入。
- **语义层级错位**：这一现象体现了 wire format 的 present 定义与 API 的 present 定义并非完全一致，是序列化框架设计中的重要细节。

## 应用
- **Protocol Buffers 字段存在性分析**：在讨论 proto2/proto3 以及 Editions 中字段存在性（field presence）行为差异时，空 length-delimited 值的 round trip 行为是关键的判定依据。
- **API 与 wire format 兼容性研究**：用于揭示采用 _no presence_ discipline 的 API（如部分 proto3 实现）在跨语言、跨平台互操作时可能产生的边界行为。
- **序列化框架的语义验证**：在实现或测试自定义编解码层、验证 round trip 一致性时，需要关注空 length-delimited 值的处理是否符合预期。
- **Protocol Buffers 演进（Editions）讨论**：在 Proto3 可选字段、Editions 等特性的语义模型设计中，空 length-delimited 值的存在性行为是重要的讨论点。

## 相关概念
- [[concepts/wire-format|Wire format]]
- [[concepts/self-delimiting-values|Self-delimiting values]]
- [[concepts/field-presence|Field presence]]
- [[concepts/no-presence-discipline|No presence discipline]]

## 相关实体
- 无相关实体

## 来源提及
- ""Empty" length-delimited values (such as empty strings) can be validly represented in serialized values: the field is "present," in the sense that it appears in the wire format." — [[sources/field_presence|field_presence]]
- "However, if the generated API does not track presence, then these values may not be re-serialized; i.e., the empty field may be "not present" after a serialization round-trip." — [[sources/field_presence|field_presence]]