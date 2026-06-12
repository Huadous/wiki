---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [term]
aliases:
  - "open enum"
  - "开放式枚举"
---


# Open Enum

## 定义

Open Enum（开放式枚举）是 Protocol Buffers 中枚举类型的一种处理方式。当解析器遇到未在 .proto 文件中显式定义的枚举值时，不会将其视为未知字段而丢弃或忽略，而是将其作为枚举值保留在目标字段中，该值可能超出定义的枚举范围。在 Protobuf Editions 中，通过 `feature.enum = OPEN` 特征控制。此行为对应 proto3 的默认枚举行为。

## 关键特征

- **值保留**：未指定的枚举值会被保留为原始整数值，而不是被放入未知字段
- **向后兼容**：适用于需要向前兼容的场景，客户端可以接收服务端未来可能添加的新枚举值
- **行为控制**：在 Protobuf Editions 中通过 `feature.enum = OPEN` 显式启用
- **proto3 默认行为**：Open Enum 是 proto3 中枚举处理的默认方式
- **类型安全较弱**：允许字段持有枚举定义范围之外的值，减弱了编译期类型检查的严格性

## 应用

- **渐进式枚举扩展**：当枚举值会随时间增加，且需要保证旧代码能处理新值时使用
- **跨版本兼容通信**：在微服务架构中，服务提供方增加新的枚举值，消费方无需立即更新代码
- **动态枚举场景**：枚举值依赖于外部配置或未知的业务扩展
- **Protobuf Editions 迁移**：从 proto3 迁移到 Editions 时，保持原有枚举行为

## 相关概念

- [[concepts/closed-enum|Closed Enum]]
- [[concepts/feature|Feature]]
- [[concepts/proto3|Proto3]]

## 相关实体

- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及

- "whether values not specified in an enum go into unknown fields vs producing an enum value outside of the bounds of the specified values in the .proto file (i.e., so-called closed and open enums) will be controlled by feature.enum = OPEN or feature.enum = CLOSED." — [[protobuf/editions-what-are-protobuf-editions]]