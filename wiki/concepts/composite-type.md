---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/proto3]]"]
tags: [term]
aliases:
  - "复合类型"
  - "message-type field"
---


# 复合类型

## 定义
复合类型（composite type）是 Protocol Buffers 中由其他已定义类型组合而成的一种字段类型，最常见的例子是其他消息类型。它允许消息字段嵌套使用自定义的结构化数据，从而实现复杂的数据建模。与标量类型和枚举不同，复合类型字段在 wire format 中会递归编码，且始终具有字段存在性（field presence），即使没有显式声明 optional。复合类型是构建多层消息结构的关键机制，支持消息内部引用自定义消息类型。

## 关键特征
- 由其他已定义类型（如消息、枚举）组合而成，支持结构化嵌套
- 与标量类型和枚举不同，复合类型字段在 wire format 中始终递归地编码其内部字段
- 在 proto3 中，复合类型字段天生具有字段存在性（field presence），无需显式声明 optional 修饰符
- 支持消息内部引用其他自定义消息类型，构建多层消息结构
- 字段取值可以是「默认消息实例」或自定义实例，通过判断是否为默认实例来确定字段是否存在

## 应用
- **嵌套数据结构建模**：如用户消息中包含地址消息，订单消息中包含商品消息列表
- **复杂 API 设计**：RPC 请求和响应中使用复合类型封装多层业务逻辑
- **模块化重用**：将公共数据结构（如分页参数、错误信息）定义为独立消息，被多个字段复用
- **Protocol Buffers 编码优化**：利用复合类型的字段存在性特性减少序列化/反序列化开销

## 相关概念
- [[concepts/message|message]]
- [[concepts/field|field]]
- [[concepts/field-presence|field presence]]
- [[concepts/optional|optional]]
- [[concepts/wire-format|wire format]]
- [[concepts/enumeration|enumeration]]
- [[concepts/scalar-types|scalar types]]

## 相关实体
无

## 来源提及
- "You can also specify enumerations and composite types like other message types for your field." — [[protobuf/proto3|proto3]]
- "In proto3, message-type fields already have field presence. Because of this, adding the optional modifier doesn’t change the field presence for the field." — [[protobuf/proto3|proto3]]