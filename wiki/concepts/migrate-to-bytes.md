---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-editions-feature-extension-layout.md]]"]
tags: [method]
aliases:
  - "Alternative 3"
  - "迁移为 bytes"
---


# Migrate to bytes

## 定义
Migrate to bytes（迁移为 bytes）是 [[sources/editions-editions-feature-extension-layout|Editions Feature Extension Layout]] 文档中提出的 Alternative 3 策略。它主张从 edition zero 中完全移除 [[concepts/utf8_validation|utf8_validation]] 功能，转而将当前所有不强制 UTF-8 的 proto 字段统一迁移到 `bytes` 类型。为保持 API 易用性，该方案仍需引入一个新的 codegen 功能，使 `bytes` 字段的 getter/setter 行为表现为字符串。

## 关键特征
- **完全移除而非开关化**：直接取消 utf8_validation 功能，而不是新增一个用于控制 UTF-8 行为的 toggle。
- **类型迁移**：将当前不强制 UTF-8 的所有 proto 字段迁移为 `bytes` 类型，从根源上绕过 UTF-8 校验问题。
- **配套 codegen 调整**：需要新增 codegen 特性，使 `bytes` 字段的 getter/setter 仍以字符串形式暴露，以维持开发者使用习惯。
- **被否决的方案**：文档最终判定该替代方案不可行。
- **否决理由一（语义非二元）**：UTF-8 验证在不同语言实现间差异显著——某些语言会验证，另一些则不验证；C++ 还存在一种 "hint" 行为，会记录错误但允许无效 UTF-8 通过，因此无法以简单的开关来一刀切处理。
- **否决理由二（迁移成本巨大）**：据估算，约有 1000 万个 proto2 字符串字段将被盲目地改为 `bytes`，迁移成本过高。

## 应用
该方案主要作为 [[concepts/Editions Zero|Editions Zero]] 设计阶段的备选提案出现，应用于 Protobuf Editions 中处理 utf8 校验特性 [[concepts/Generator Features|Generator Features]] 的策略权衡场景。由于其迁移代价过高且语义无法统一处理，最终未被采纳。

## 相关概念
- [[concepts/utf8_validation|utf8_validation]]
- [[concepts/Generator Features|Generator Features]]
- [[concepts/Editions Zero|Editions Zero]]

## 相关实体
- 暂无相关实体

## 来源提及
- "Since this whole discussion revolves around the utf8 validation feature, one option would be to just remove it from edition zero. Instead of adding a new toggle for UTF8 behavior, we could simply migrate everyone who doesn't enforce utf8 today to `bytes`."（既然整个讨论围绕 utf8 验证特性展开，一种方案就是直接从 edition zero 中移除它。我们不必新增一个用于控制 UTF8 行为的开关，而是可以直接将当前所有不强制 utf8 的字段迁移到 `bytes`。） — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]