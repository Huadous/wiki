---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [other]
aliases:
  - "google::protobuf::DescriptorPool"
  - "DescriptorPool"
---


# DescriptorPool

## 基本信息
- Type: other
- Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]

## 描述
DescriptorPool 是 Protocol Buffers 反射 API 中用于运行时加载与管理描述符的组件。当反射实现支持从 FileDescriptorProto 等格式运行时加载描述符时，必须验证所有合成 oneof（synthetic oneof）都排列在真实 oneof（real oneof）之后。DescriptorPool 通过 ErrorCollector 报告该不变量被违反的错误，例如检测到真实 oneof 出现在合成 oneof 之后时会发出 "Synthetic oneofs must be after all other oneofs" 错误。它还维护 `real_oneof_decl_count_` 内部字段，根据扫描结果计算真实 oneof 的总数，从而在运行时建立并校验消息描述符的内部结构。DescriptorPool 在 [[entities/descriptor|Descriptor]] 与 [[entities/oneofdescriptor|OneofDescriptor]] 的生命周期中扮演关键角色，是实现 [[concepts/反射 (Reflection)|反射]] 与 [[concepts/字段存在性 (Field Presence)|字段存在性（Field Presence）]] 等高级特性的基础组件。

## 相关实体
- [[entities/descriptor|Descriptor]]
- [[entities/oneofdescriptor|OneofDescriptor]]

## 相关概念
- [[concepts/合成 Oneof (Synthetic Oneof)|Synthetic Oneof]]
- [[concepts/反射 (Reflection)|Reflection]]
- [[concepts/字段存在性 (Field Presence)|Field Presence]]

## 来源提及
- "If your reflection implementation supports loading descriptors at runtime, you must verify that all synthetic oneofs are ordered after all \"real\" oneofs." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- `AddError(message->full_name(), proto.oneof_decl(i), DescriptorPool::ErrorCollector::OTHER, "Synthetic oneofs must be after all other oneofs");` — [[sources/implementing_proto3_presence|implementing_proto3_presence]]