---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions]]"]
tags: [term]
aliases:
  - "Reserved Keywords"
  - "Protobuf 保留字"
  - "Reserved keyword"
---


# Reserved keywords

## 定义
Reserved keywords 指 Protobuf 语言中**不再允许作为标识符使用**的保留字集合。在 editions 体系中,文档列出了 36 个将被彻底保留的关键字:`bool`、`bytes`、`double`、`edition`、`enum`、`extend`、`extensions`、`fixed32`、`fixed64`、`float`、`group`、`import`、`int32`、`int64`、`map`、`max`、`message`、`oneof`、`option`、`optional`、`package`、`public`、`repeated`、`required`、`reserved`、`returns`、`rpc`、`service`、`sfixed32`、`sfixed64`、`sint32`、`sint64`、`stream`、`string`、`syntax`、`to`、`uint32`、`uint64`、`weak`。

## 关键特征
- **显式保留集合**:共 36 个关键字被列为最终保留字,涵盖基础类型(`int32` 等)、结构声明(`message`、`enum`、`oneof` 等)、修饰符(`optional`、`repeated`、`required`)、流式 RPC 标识(`stream`、`returns`)以及编辑体系新增的关键字(`edition`、`to`)等。
- **转义语法**:为兼容历史代码,文档引入 `#optional` 形式的转义语法,**该语法仅能作用于关键字**,用于在不可避免的场景下显式将关键字作为标识符使用。
- **平滑迁移路径**:新增关键字的标准做法是——先以 **contextual keyword(上下文关键字)** 形式引入,在下一 edition 升级为真正的保留字。该设计参考了 Rust 的 editions 演进机制。
- **当前限制的动机**:当前 Protobuf 允许关键字作为标识符,导致解析器复杂度上升且遮蔽(shadowing)行为未明确规范,转保留字旨在简化解析器并消除歧义。

## 应用
- 适用于 **Protobuf Editions** 体系下新版本的 .proto 文件编写,避免使用上述关键字作为字段名、消息名、枚举值等标识符。
- 在不可避免的历史代码迁移中,可使用 `#optional` 转义语法保留关键字作为标识符。
- 指导语言设计者在引入新关键字时遵循"先 contextual、后保留"的渐进式流程,降低对存量生态的破坏。

## 相关概念
- [[concepts/feature-gating|Feature gating]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/identifier-naming-conventions|Identifier naming conventions]]

## 相关实体
- [[entities/protocol-buffers-v3-15-0|protocol-buffers-v3-15-0]]
- [[entities/protocol-buffers-v3-12-0|protocol-buffers-v3-12-0]]

## 来源提及
- "Currently, the Protobuf language allows using keywords as identifiers. This makes the parser somewhat more complicated than it has to be for minimal benefit, and shadowing behavior is not well-specified." — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]