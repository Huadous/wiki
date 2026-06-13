---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [other]
aliases:
  - "google::protobuf::Descriptor"
  - "Protocol Buffers Descriptor"
  - "Protobuf 消息描述符"
---


# Descriptor

## 基本信息
- Type: other
- Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]

## 描述
Descriptor 是 Protocol Buffers 反射 API 中表示消息类型描述符的类，提供对消息字段、oneof 等结构信息的编程化访问。在 proto3 optional 字段的支持中，Descriptor 引入了 [[concepts/real_oneof_decl_count|real_oneof_decl_count()]] 方法，该方法返回消息中真实 oneof 的数量，不包括由编译器为支持 optional 字段而合成的 [[concepts/synthetic_oneof|Synthetic Oneof]]。真实 oneof 在 Descriptor 的 oneof 列表中始终位于合成 oneof 之前，这是 [[entities/descriptorpool|DescriptorPool]] 加载时必须验证的不变量。代码生成器迭代 oneof 时应优先使用 real_oneof_decl_count()，以避免触及仅用于实现细节的合成 oneof。Descriptor 与 [[entities/oneofdescriptor|OneofDescriptor]] 和 [[entities/fielddescriptor|FieldDescriptor]] 共同构成 protobuf 反射系统的核心，通过 [[concepts/reflection|Reflection]] 在运行时对消息结构进行查询和操作。

## 相关实体
- [[entities/oneofdescriptor|OneofDescriptor]]
- [[entities/fielddescriptor|FieldDescriptor]]
- [[entities/descriptorpool|DescriptorPool]]

## 相关概念
- [[concepts/synthetic_oneof|Synthetic Oneof]]
- [[concepts/reflection|Reflection]]
- [[concepts/oneof|Oneof]]

## 来源提及
- "Descriptor::real_oneof_decl_count(): like oneof_decl_count(), but returns the number of real oneofs only." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "Real oneofs are always first, and real_oneof_decl_count() will return the total number of oneofs, excluding synthetic oneofs." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]