---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [method]
aliases:
  - "group encoding migration"
  - "Group-Encoded Messages Migration"
---


# Group-Encoded Messages migration

## 定义
Group-Encoded Messages migration（群组编码消息迁移）是一种带有 wire format break（线格式不兼容变更）的大规模变更模板，其目的是通过将消息编码为 group（群组）形式而非传统的 length-prefixed submessages（带长度前缀的子消息）形式，从而捕获 CPU 与 RAM 方面的性能收益。该迁移采用多阶段推进策略：先修改解析器使其同时接受 group 编码与 length-prefixed 编码，再让此状态"浸泡"约三年，随后在整个代码库中逐步为消息字段添加 `features.group_encoded`，最后当迁移率达到 95% 时，升级 protoc 以在新版本（editions）中将该 feature 默认设为 true。

## 关键特征
- 属于 large-scale change（大规模变更）的一种特殊模板，伴随 wire format break。
- 第一阶段先在反序列化端使 `TYPE_MESSAGE` 与 `TYPE_GROUP` 成为同义词，使新旧编码可被同时接受。
- 解析器改造完成后需进行约三年的"浸泡期"（soak period），以等待生态逐步适配。
- 迁移通过在消息字段上逐个启用 `features.group_encoded` 来推进，而非一次性切换。
- 当 95% 的字段完成迁移时，由 protoc 在新 editions 中将该 feature 的默认值翻转为 true。
- 与大多数 features 不同，`group_encoded` 几乎永远不会被完全消除，因为 length-prefixed 消息仍会持续使用。

## 应用
- 适用于 Protocol Buffers 中消息字段编码格式的演进式迁移场景。
- 用于在保持向后兼容性的同时，将消息从 length-prefixed 编码逐步过渡到更高效的 group 编码。
- 作为 Editions（版本）体系中一种大规模不兼容变更的标准化实施模板。

## 相关概念
- [[concepts/features.group_encoded|features.group_encoded]]
- [[concepts/large-scale-change|Large-scale Change]]
- [[concepts/feature-lifetime|Feature lifetime]]

## 相关实体
（暂无相关实体）

## 来源提及
- "First, we modify parsers to accept message fields that are encoded as either groups or messages (i.e., `TYPE_MESSAGE` and `TYPE_GROUP` become synonyms in the deserializer). We will let this soak for three years[^2] and bide our time." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]