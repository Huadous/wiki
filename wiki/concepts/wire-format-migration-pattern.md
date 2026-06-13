---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [method]
aliases:
  - "Wire format migration pattern"
  - "线格式迁移模式"
  - "readers-first migration"
---


# Wire format migration pattern

## 定义
线格式迁移模式（Wire format migration pattern）是一种在 Protobuf 中以向后兼容方式改变线编码的方法论。其核心思路是：先用一段时间让读取器（reader/parser）同时接受旧编码与新编码，从而在生态系统中建立对新格式的"宽容"；待绝大多数旧读取器自然淘汰之后，再将新编码设为默认值，完成真正的线格式切换。该模式以 packed 编码迁移为成功先例，并被规划用于 `features.group_encoded` 所代表的子消息组编码（group-encoded messages）迁移。

## 关键特征
- **读取器先行（readers-first）**：优先修改解析器/反序列化器，使其能够同时识别旧编码与新编码（例如在反序列化器中使 `TYPE_MESSAGE` 与 `TYPE_GROUP` 成为同义词）。
- **长浸润期（long soak period）**：在切换写入器之前，新宽容读取器需要在生态中长期浸润以逐步替换旧读取器；本文建议浸润时长约三年。
- **写入器后迁（writers later）**：浸润期结束后再大规模推动写入器（序列化器）迁移到新编码。
- **默认值翻转收尾**：最终在某一版 edition 中将新编码设为默认值，此时旧读取器已基本淘汰，不会造成大规模解析失败。
- **成功的先例**：packed 字段编码的迁移是此模式已被验证的范例。
- **适用对象**：例如 `features.group_encoded` 所代表的消息字段组编码迁移——因为组编码比长度前缀消息（length-prefixed submessages）在 CPU 与内存上更廉价。
- **长视野规划**：与一次性的简单 editions 升级不同，这种模式要求多年的整体时间规划。

## 应用
- **`packed` 编码迁移**：该模式已成功应用于将 repeated 标量字段默认编码从非 packed 改为 packed。
- **`features.group_encoded` 迁移**：规划中用于将消息字段的线编码从 length-prefixed 切换为 group 编码（end-marker-delimited），以获得 CPU 与 RAM 上的性能收益。
- **任何涉及线编码不兼容变更的演进**：当新编码能带来性能或效率提升但属于 wire-breaking change 时，可借助此模式平滑过渡。
- **跨生态的长生命周期部署场景**：例如长期存在的预算手机、旧版客户端等场景，旧读取器的缓慢淘汰正好被长浸润期吸收。

## 相关概念
- [[concepts/large-scale-change|Large-Scale Change]]
- [[concepts/group-encoded-messages-migration|Group-Encoded Messages migration]]
- [[concepts/packed-migration|`packed` migration]]
- [[concepts/features-group-encoded|features.group_encoded]]
- [[concepts/features-packed|features.packed]]
- [[concepts/feature-lifetime|Feature lifetime]]

## 相关实体
（本概念无关联实体）

## 来源提及
- "It turns out that encoding and decoding groups (end-marker-delimited submessages) is cheaper than handling length-prefixed messages. There are likely CPU and RAM savings in switching messages to use the group encoding. Unfortunately, that would be a wire-breaking change, causing old readers to be unable to parse new messages." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]