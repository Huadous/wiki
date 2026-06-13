---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes]]"]
tags: [term]
aliases:
  - "Edition Legacy"
  - "EDITION_LEGACY"
---


# EDITION_LEGACY

## 定义
EDITION_LEGACY 是文档建议新增的一个特殊版本占位符，充当"无限过去"（infinite past）的标记。对于任何早于特性 `edition_introduced` 的版本，EDITION_LEGACY 所指定的默认值将被采用；该默认值必须始终表示特性出现之前的 noop 行为，且 proto 文件不允许在 EDITION_LEGACY 下覆盖该特性。

## 关键特征
- 作为一个语义上的"无限过去"占位符，统一表示所有未被特性显式引入的旧版本。
- 为每个特性的 `edition_introduced` 之前的所有版本提供一个统一且安全的默认行为锚点。
- 所指定的默认值始终对应特性引入前的 noop 行为，避免旧代码路径下产生非预期的副作用。
- proto 文件禁止在 EDITION_LEGACY 之上对相关特性进行覆盖，保证默认行为的不可变性。
- 作为机制支撑，使 [[concepts/FeatureSupport|FeatureSupport]] 能够在不枚举全部历史版本的情况下回退到一致的状态。

## 应用
- 在 Protobuf Editions 体系下，为早于特性引入版本（`edition_introduced`）的历史代码提供统一的默认行为。
- 与 [[concepts/Feature Lifetimes|Feature Lifetimes]] 配合，简化版本演进过程中对旧版本的兼容处理。
- 在 [[concepts/Edition Lifetimes|Edition Lifetimes]] 框架内，作为"无限过去"的时间锚点，避免在配置中显式列举所有旧版本。
- 供运行时与代码生成器解析某个特性的有效值时，定位"特性尚未存在"这一历史区间的标准值。

## 相关概念
- [[concepts/FeatureSupport|FeatureSupport]]
- [[concepts/Feature Lifetimes|Feature Lifetimes]]
- [[concepts/Edition Lifetimes|Edition Lifetimes]]

## 相关实体
- 无

## 来源提及
- "We will also add a new special edition `EDITION_LEGACY`, to act as a placeholder for 'infinite past'." — [[sources/editions-edition-lifetimes]]
- "For editions earlier than `edition_introduced`, the default assigned to `EDITION_LEGACY` will be assigned and should always signal the *noop behavior that predated the feature*." — [[sources/editions-edition-lifetimes]]