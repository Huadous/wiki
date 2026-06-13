---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]"]
tags: [term]
aliases:
  - "重复字段编码"
  - "RepeatedFieldEncoding"
---


# RepeatedFieldEncoding

## 定义
RepeatedFieldEncoding 是 Protobuf Edition Zero Features 中定义的一个功能字段（feature field），用于控制 `repeated` 字段在序列化时的编码方式。该字段是一个枚举类型，其取值为 `PACKED`（值为 0）和 `EXPANDED`（值为 1）。其中 `PACKED` 表示在 wire 格式上以连续字节流（紧凑打包）的方式编码，而 `EXPANDED` 则表示采用传统的逐元素编码方式。

## 关键特征
- 枚举类型，包含两个取值：`PACKED = 0` 和 `EXPANDED = 1`
- 在 2023 edition 中的默认值为 `PACKED`
- `retention` 属性为 `RUNTIME`，即该 feature 在运行时仍然保留，可被运行时动态解析
- `target` 属性为 `FIELD`，表示该 feature 作用于字段级别
- 支持文件级默认值与字段级覆盖：示例中展示了在文件级别设置 `EXPANDED` 作为默认值，在字段级别使用 `PACKED` 进行覆盖，体现了 feature 继承机制的灵活性
- 与 [[concepts/Feature-Inheritance|Feature Inheritance]] 机制配合，可在不同作用域层级灵活配置

## 应用
- 控制 Protobuf `repeated` 字段在 wire 格式上的序列化编码策略
- 在需要兼容旧版逐元素编码行为的场景中使用 `EXPANDED`
- 在追求更高序列化效率与紧凑性的现代场景中使用 `PACKED`（2023 edition 默认）
- 通过文件级与字段级组合配置，实现细粒度的编码策略管理

## 相关概念
- [[concepts/Features|Features]]
- [[concepts/Edition-Defaults|Edition Defaults]]
- [[concepts/Target-Attributes|Target Attributes]]
- [[concepts/Feature-Inheritance|Feature Inheritance]]

## 相关实体
- 无相关实体

## 来源提及
- `enum RepeatedFieldEncoding { PACKED = 0; EXPANDED = 1; }` — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]
- `optional RepeatedFieldEncoding repeated_field_encoding = 3 [ retention = RUNTIME, target = FIELD, (edition_defaults) = { edition: "2023", default: "PACKED" } ];` — [[sources/editions-protobuf-editions-design-features|editions-protobuf-editions-design-features]]