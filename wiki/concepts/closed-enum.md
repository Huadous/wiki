---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [term]
aliases:
  - "closed enum"
  - "封闭枚举"
---


# 封闭枚举

## 定义
封闭枚举（Closed Enum）是枚举类型的一种处理方式，其核心特征为：未在`.proto`文件中显式定义的枚举值不会被解析为合法的枚举成员，而是被放入未知字段（unknown fields）中。在Protobuf Editions中，通过feature `.proto` 文件级别的特性控制`feature.enum = CLOSED`来启用此行为。封闭枚举是proto2的默认行为，也是proto2与proto3之间不可调和的差异之一。

## 关键特征
- 严格的枚举值检查：仅接受`.proto`文件中显式声明的枚举值。
- 未知值处理：任何未声明的枚举值都被视为未知字段，序列化与反序列化时保留原始字节。
- 向后兼容性：与proto2的枚举语义完全一致。
- 由特性控制：在Protobuf Editions生态中，通过`feature.enum = CLOSED`显式声明。

## 应用
- 保护强类型约定：当团队需要强制所有参与者仅使用预定义枚举值时，封闭枚举可防止意外使用未定义值。
- 迁移场景：从proto2迁移到Editions时，保留原有的封闭枚举行为以避免破坏现有系统。
- 安全敏感场景：防止攻击者通过注入未定义枚举值绕过类型检查或触发非预期行为。

## 相关概念
- [[concepts/open-enum|开放枚举]]
- [[concepts/feature|Feature]]

## 相关实体
- [[entities/Protocol Buffers]]

## 来源提及
- "whether values not specified in an enum go into unknown fields vs producing an enum value outside of the bounds of the specified values in the .proto file (i.e., so-called closed and open enums) will be controlled by feature.enum = OPEN or feature.enum = CLOSED." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]