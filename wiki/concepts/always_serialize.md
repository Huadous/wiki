---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [term]
aliases:
  - "Always Serialize"
  - "ALWAYS_SERIALIZE"
---


# ALWAYS_SERIALIZE

## 定义

ALWAYS_SERIALIZE 是 Protobuf Editions 中 `features.field_presence` 字段的一个中间迁移值，用作从 [[concepts/LEGACY_REQUIRED|LEGACY_REQUIRED]] 迁移到 [[concepts/EXPLICIT_PRESENCE|EXPLICIT_PRESENCE]] 的关键桥梁。其行为类似 [[concepts/EXPLICIT_PRESENCE|EXPLICIT_PRESENCE]]，但如果 has-bit 未设置，则会序列化默认值。

## 关键特征

- **语义上等同 EXPLICIT_PRESENCE**：在字段存在性检查层面遵循 EXPLICIT_PRESENCE 的规则（has-bit 决定字段是否"存在"）。
- **默认行为不同**：当 has-bit 未设置（即字段为"未显式赋值"状态）时，仍会将默认值序列化到线上数据。
- **从 LEGACY_REQUIRED 升级安全**：将字段从 `required` 迁移到 ALWAYS_SERIALIZE 始终安全，因为 `required` 仅作为初始化检查的约束，客户端只要提供一个值即可满足；读取器不会因此报错。
- **为写入器松绑**：允许写入器不再实际设置该字段值，从而为最终迁移到 EXPLICIT_PRESENCE 铺平道路。
- **过渡性中间状态**：本身不是长期目标状态，而是经过适当构建时间窗口后，可以假定所有读取器都已能容忍字段可能缺失的中间过渡值。

## 应用

- **`required` 字段的渐进式解绑**：当 schema 中存在 `required` 字段需要去除 `required` 约束时，先将 `features.field_presence` 切换到 ALWAYS_SERIALIZE，使旧读取器继续看到默认值、不破坏解析，同时允许新写入器省略显式赋值。
- **多版本兼容性窗口**：在 [[concepts/ImmoLation of `required`|ImmoLation of `required`]] 推进过程中，利用 ALWAYS_SERIALIZE 作为兼容层，保证跨版本、跨语言读取器在过渡期内的稳定运行。
- **最终迁移到 EXPLICIT_PRESENCE**：经过足够长的构建与部署窗口后，可安全地将字段从 ALWAYS_SERIALIZE 升级到 EXPLICIT_PRESENCE，完成对 `required` 的彻底去除。
- 配合 [[concepts/Minimum Required Edition|Minimum Required Edition]] 机制进行 schema 演进管控，限制哪些语言运行时可以消费某个 edition 下的字段存在性策略。

## 相关概念

- [[concepts/LEGACY_REQUIRED|LEGACY_REQUIRED]]
- [[concepts/EXPLICIT_PRESENCE|EXPLICIT_PRESENCE]]
- [[concepts/features.field_presence|features.field_presence]]
- [[concepts/ImmoLation of `required`|ImmoLation of `required`]]

## 相关实体

无可引用实体。

## 来源提及

- "To do this, we introduce a new value for `features.field_presence`, `ALWAYS_SERIALIZE`, which behaves like `EXPLICIT_PRESENCE`, but, if the has-bit is not set, the default is serialized." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]