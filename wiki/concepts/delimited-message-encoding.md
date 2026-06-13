---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [method]
aliases:
  - "DELIMITED encoding"
  - "DELIMITED 消息编码"
---


# DELIMITED message encoding

## 定义
`DELIMITED` 是 [[sources/features|features]] 中 `features.message_encoding` 字段的一种取值，表示在 wire 上以 group 风格（即 `start_group` / `end_group` 标记）编码消息体。它与 `LENGTH_PREFIXED`（普通带长度前缀的消息编码）相对：提案在示例中将 post-editions 的 `Bar bar = 1 [features.message_encoding = DELIMITED];` 视为与 pre-editions 的 `group Bar = 1 { ... }` 等价。Editions Zero 推荐实现路径是：编译器在编码 `MessageInfo` 之前就把 `DELIMITED` 字段类型改写为 `GROUP`（wire type 17），运行时无需识别 `DELIMITED` 与 `LENGTH_PREFIXED` 之间的差别，以最小化编码与运行时代码改动。

## 关键特征
- 属于 [[sources/features|features.message_encoding]] 枚举的一种取值，与 `LENGTH_PREFIXED` 构成 wire-level 编码选项。
- 在 wire 上表现为 `start_group` / `end_group`（即 wire type 17，GROUP）的 group 风格编码，而非长度前缀形式。
- 与 pre-editions 的 `group` 字段在语义和编码结果上等价，因此可在源码层面保持现代字段声明同时复用 legacy group 行为。
- Editions Zero 实现策略：编译器在编码 `MessageInfo` 前把 `DELIMITED` 字段改写为 `GROUP`，运行时不需要区分两种 `message_encoding`，从而把差异集中在编译期。
- 由 `MessageSchema` 将其当作 pre-editions 等价形式处理：`will be encoded and treated by MessageSchema like its pre-editions equivalent below.`

## 应用
- 用于在 Protobuf Editions 中复刻 pre-editions `group` 字段的 wire 编码，使新版 schema 与旧版消息二进制保持兼容。
- 在 [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]] 等 Editions 实现路径中，作为"显式选择 legacy group 编码"的入口，供需要兼容老消息格式的场景使用。
- 在 [[sources/editions-protobuf-editions-design-features|Protobuf Editions Features Design]] 等 features 设计语境下，与 `LENGTH_PREFIXED` 共同构成 `message_encoding` 这一 features 选项的两个可选值。

## 相关概念
- [[concepts/features-message-encoding|features.message_encoding]]
- [[concepts/group-encoding|Group encoding]]
- [[concepts/messageschema|MessageSchema]]
- [[concepts/rawmessageinfo|RawMessageInfo]]

## 相关实体
无相关实体。

## 来源提及
- In the compiler, message fields with `features.message_encoding = DELIMITED` should be treated as a group *before* encoding message info. — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- will be encoded and treated by `MessageSchema` like its pre-editions equivalent below. — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]