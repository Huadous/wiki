---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "required field"
  - "required label"
  - "wire-required"
---


# required keyword

## 定义
`required` 是 Protocol Buffers proto2 语法中用于声明字段为 **wire-required**（连线必填）的关键字。被 `required` 修饰的字段必须在序列化消息时出现，且在反序列化时必须存在，否则该消息被视为畸形（malformed）。proto3 语法中移除了 `required`，改用 `defaulted` 概念描述字段缺失时的默认行为。在 Edition Zero 设计中，文档决定将 `optional` 和 `required` 两个关键字全部消除，使其成为解析错误（parse errors），singular 字段的存在性规约改由 `features.field_presence` 注解来指定，使用 `LEGACY_REQUIRED` 规约的字段必须位于 `required` allowlist 中。

## 关键特征
- 属于 proto2 字段标签三态（`required` / `optional` / `repeated`）之一，用于强制字段存在性
- 缺失 `required` 字段的消息在反序列化时会被判定为畸形，序列化器也会拒绝生成不含该字段的消息
- proto3 不再支持 `required`，存在性语义由 `defaulted` 字段隐式处理
- Edition Zero 把 `required`（连同 `optional`）列入解析错误，转而通过 `features.field_presence` 注解控制 singular 字段的存在性
- 迁移至 Edition Zero 时，若字段使用 `LEGACY_REQUIRED` 规约，则该字段必须出现在 `required` allowlist 中方可被编译器接受

## 应用
- **proto2 模式定义**：在历史遗留的 proto2 schema 中，用来声明业务上不可缺失的关键字段（如 `User.id`、`Order.timestamp`）
- **Editions 迁移场景**：将 proto2/proto3 描述文件迁移到 Edition Zero 时，用于识别需放入 `required` allowlist 的字段，并将其转为 `LEGACY_REQUIRED` + `features.field_presence` 表达
- **API 兼容性分析**：在评估 wire-format 与 JSON 互转行为时，作为判断字段存在性约束的参考点
- **解析器实现**：影响反序列化器在缺失字段时的报错路径，是解析错误归类（畸形消息 vs. 默认值填充）的重要依据

## 相关概念
- [[concepts/LEGACY_REQUIRED|LEGACY_REQUIRED]]
- [[concepts/optional-keyword|optional keyword]]
- [[concepts/defaulted-fields|defaulted fields]]
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/Large-Scale-Change|Large-Scale Change]]
- [[concepts/field-presence|field presence]]

## 相关实体
（暂无关联实体）

## 来源提及
- "After discussing the tradeoffs, we have chosen to *eliminate both the `optional` and `required` keywords, making them parse errors*." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- "Required. Proto2 has `required` but not `defaulted`; Proto3 has `defaulted` but not `required`." — [[sources/editions-edition-zero-features|editions-edition-zero-features]]