---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]"]
tags: [term]
aliases:
  - "deprecation of syntax keyword"
  - "syntax 关键字弃用"
  - "syntax keyword deprecation"
---


# syntax keyword deprecation

## 定义
syntax 关键字弃用是本文档提出的策略调整，指在引入 `edition` 关键字后，`syntax` 关键字将不再被要求或观察，因其已被视为冗余。当 `edition` 与 `syntax` 同时出现于一个 proto 文件时，`edition` 优先且 `syntax` 被忽略。此变更旨在让用户从依赖粗粒度 `syntax`（即 proto2/proto3）切换到显式的 edition + features 模型，从而使隐含行为变得透明可管理。

## 关键特征
- **冗余性判定**：在 `edition` 关键字存在的前提下，`syntax` 关键字被判定为冗余，不再被强制要求或被工具/编译器观察。
- **优先级冲突解决**：若 `edition` 与 `syntax` 同时出现于同一 proto 文件中，`edition` 优先，`syntax` 被静默忽略。
- **过渡导向**：该策略旨在引导用户从粗粒度的 `syntax`（proto2/proto3）模型迁移到显式的 edition + features 模型。
- **行为透明化**：通过弃用 `syntax`，使原本由 proto2/proto3 隐含的行为通过显式的 edition 与 feature 选项暴露出来，变得可管理、可审计。

## 应用
- **proto 文件迁移**：在新生成的 proto 文件中直接使用 `edition` 关键字，无需再声明 `syntax = "proto2";` 或 `syntax = "proto3";`。
- **存量代码演进**：在混合声明场景下（同时含 `edition` 与 `syntax`）的现有 proto 文件，可安全删除 `syntax` 行而不影响行为。
- **工具链与编译器实现**：Protobuf 编译器（protoc）及相关插件需在解析阶段优先识别 `edition`，并对 `syntax` 进行忽略处理。
- **教育与文档**：通过明确弃用 `syntax`，在用户文档与迁移指南中传达 Edition Zero 及后续 editions 的语义变化。

## 相关概念
- [[concepts/edition-keyword|edition keyword]]
- [[concepts/features-option|features option]]
- [[concepts/converged-semantics|Converged Semantics]]
- [[concepts/proto2-proto3|proto2/proto3]]

## 相关实体
- [[entities/edition-zero|Edition Zero]]
- [[entities/protobuf-team|Protobuf Team]]

## 来源提及
- The `syntax` keyword shall no longer be required/observed when an `edition` keyword is present, as it is now considered redundant. — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]
- If `edition` and `syntax` are both present, `edition` takes precedence and `syntax` is ignored. — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]