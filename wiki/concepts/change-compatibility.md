---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [standard]
aliases:
  - "change compatibility"
  - "binary-compatible change"
  - "二进制兼容变更"
---


# Change-compatibility

## 定义
Change-compatibility（变更兼容性）描述了在 Protocol Buffers 中，proto3 字段在 _explicit presence_（显式存在性）与 _no presence_（无存在性）之间进行切换时所涉及的二进制兼容性语义。该切换在 wire format 层面属于二进制兼容变更——序列化后的值在二进制层面相互兼容，不会因协议层面解析失败而中断通信。然而，由于两种存在性规则在序列化时对默认值的处理方式不同，消息的序列化表示可能因发送方与接收方所使用的消息定义版本不同而产生差异：_no presence_ 序列化规则不会输出默认值字段，而 _explicit presence_ 序列化规则会为每个"存在"的字段显式输出其值（含默认值）。此类变更是否安全取决于应用程序的具体语义。

## 关键特征
- 在 wire format 层面上，_explicit presence_ 与 _no presence_ 之间的字段存在性切换是二进制兼容的，序列化值可以互相解析。
- _no presence_ 序列化规则不会输出字段值为默认值的情况，因此无法在序列化结果中区分"未设置"与"设置为默认值"。
- _explicit presence_ 序列化规则会为每个显式存在的字段输出其值，即使该值与默认值相同。
- 字段的二进制兼容并不保证语义上的无损"往返"（round trip）。
- 安全性取决于应用程序是否依赖字段的显式存在性以及默认值语义。

## 应用
- 在升级 Protocol Buffers 消息定义时，评估字段存在性规则变更对现有客户端与服务端通信的影响。
- 设计需要"往返"保证的跨版本通信协议时，判断哪些字段可以在 _explicit presence_ 与 _no presence_ 之间安全切换。
- 制定消息演进策略时，区分"wire format 兼容"与"语义无损"两个不同层面的兼容性要求。
- 在包含多个使用不同消息定义版本的客户端的分布式系统中，识别潜在的"有损往返"风险。

## 相关概念
- [[concepts/field-presence|Field presence]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/wire-format|Wire format]]
- [[concepts/forward-and-backward-compatibility|Forward and backward compatibility]]

## 相关实体
- 无相关实体。

## 来源提及
- "Changing a field between _explicit presence_ and _no presence_ is a binary-compatible change for serialized values in wire format." — [[sources/field_presence]]
- "If client A depends on _explicit presence_ for `foo`, then a 'round trip' through client B will be lossy from the perspective of client A." — [[sources/field_presence]]
- "This change may or may not be safe, depending on the application's semantics." — [[sources/field_presence]]