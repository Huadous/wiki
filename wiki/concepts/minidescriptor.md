---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [term]
aliases:
  - "MiniDescriptor 编码规范"
  - "MiniDescriptor encoding specification"
---


# MiniDescriptor

## 定义
MiniDescriptor 是一种轻量级描述符编码规范，其设计目标与 Java Lite 类似，都是以最小化描述符信息为核心来满足性能与代码体积方面的要求。MiniDescriptor 当前并不编码 proto2/proto3 语法，因此天然接近 [[concepts/editions|Editions]] 兼容；它通过 `FieldModifier`/`MessageModifier` 位来表达与 [[concepts/editions-zero-features|Editions Zero Features]] 对应的字段级 / 消息级特性。源文件将其作为 Alternative 2 提出：将 Java Lite 整体迁移到 MiniDescriptor 编码，可降低长期维护成本。

## 关键特征
- 轻量化描述符编码：与 Java Lite 类似，追求最小化描述符信息，以满足性能与代码体积要求。
- 不编码 proto2/proto3 语法：天然接近 Editions 兼容，规避遗留语法带来的负担。
- 通过 `FieldModifier`/`MessageModifier` 位表达字段级 / 消息级特性，与 [[concepts/editions-zero-features|Editions Zero Features]] 对应。
- 尚有若干待定变更未稳定。
- 对 Java Lite 现有 Schema 兼容性与代码体积的影响尚未充分验证。

## 应用
- 作为 Java Lite 迁移的备选方案（Alternative 2）：在长期视角下将 Java Lite 整体迁移到 MiniDescriptor 编码，以降低维护成本。
- 作为 [[concepts/editions|Editions]] 体系下描述符编码的潜在替代方案，因其不编码 proto2/proto3 语法，天然契合 Editions 设计。
- 在 [[concepts/editions-zero-features|Editions Zero]] 阶段作为评估对象：源文件建议 Editions Zero 阶段不立即采纳，待其待定变更收敛、Schema 兼容性与代码体积影响验证充分后再行评估。

## 相关概念
- [[concepts/editions|Editions]]
- [[concepts/editions-zero-features|Editions Zero Features]]
- [[concepts/messageinfo|MessageInfo]]
- [[concepts/java-lite|Java Lite]]

## 相关实体
- 无相关实体

## 来源提及
- "We could switch Java Lite to use the MiniDescriptor encoding specification." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- "Like Java Lite, this encoding seems to be optimized to be lightweight and with minimal descriptor information." — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]