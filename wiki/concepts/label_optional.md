---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [term]
aliases:
  - "LABEL_OPTIONAL"
  - "FieldDescriptorProto::LABEL_OPTIONAL"
---


# LABEL_OPTIONAL

## 定义
`LABEL_OPTIONAL` 是 protobuf descriptor（[[entities/descriptor|Descriptor]]）中 `FieldDescriptorProto::Label` 枚举的一个取值，用于表示"可选字段"。在 proto2 中它对应具有显式存在性（presence）的 optional 字段；而在 proto3 中，由于 `LABEL_OPTIONAL` 被复用来表示不跟踪存在性的 singular 字段，导致仅凭该标签无法在 descriptor 层区分 proto2 的 optional 与 proto3 的 singular 字段。

## 关键特征
- 属于 `google.protobuf.FieldDescriptorProto.Label` 枚举的标准值之一。
- 在 proto2 语义下，表示字段具有显式存在性（field presence），可通过 `has_xxx()` 判断是否被赋值。
- 在 proto3 语义下，被复用为所有 singular 字段的默认标签，**不**携带存在性信息。
- 由于上述语义重叠，仅检查 `LABEL_OPTIONAL` 已不足以判断字段是否具有 presence。
- 文档明确要求代码生成器不要直接读取 `proto3_optional` 字段，而应通过 `has_presence()` 这一抽象来判断字段是否具有存在性。
- 是引入"合成 oneof"（[[concepts/synthetic-oneof|Synthetic Oneof]]）机制的直接动因之一。

## 应用
- 在实现 protobuf 反射、代码生成器或静态分析工具时，依赖该标签判断字段可选性。
- 在 proto3 启用显式存在性（`optional` 关键字）的场景中，需要结合合成 oneof 信息来还原字段的真实语义。
- 在实现跨 proto2/proto3 兼容的 descriptor 反射代码时，应避免直接基于 `LABEL_OPTIONAL` 做语义假设。

## 相关概念
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/proto3|proto3]]
- [[concepts/field-presence|Field Presence]]

## 相关实体
- [[entities/descriptor|Descriptor]]

## 来源提及
- "Proto3 descriptors already use `LABEL_OPTIONAL` for proto3 singular fields, which do not track presence." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "There is a lot of existing code that reflects over proto3 protos and assumes that `LABEL_OPTIONAL` in proto3 means 'no presence.'" — [[sources/implementing_proto3_presence|implementing_proto3_presence]]