---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
tags:
  - "document"
aliases:
  - "Protocol Buffers Language Guide (proto3)"
  - "proto3 语言指南"
---

## 核心内容
本文档是 [[concepts/proto3|proto3]] 版本的官方参考指南,介绍了如何使用 [[entities/protocol-buffers|Protocol Buffers]] 语言构建结构化数据,涵盖 .proto 文件语法以及如何通过 [[entities/protoc|protoc]] 编译器从 .proto 文件生成数据访问类。指南详细说明了消息类型定义、字段类型、字段编号分配规则、字段基数（singular、repeated、map）、字段存在性、repeated 字段的 [[concepts/packed-encoding|packed 编码]]、保留字段编号与名称的必要性、消息合并策略（[[concepts/last-one-wins|Last One Wins]]）以及 [[concepts/deleting-fields|删除字段]] 的正确做法。同时讨论了 proto3 与 proto2 的差异,以及与 [[concepts/protobuf-editions|Protobuf Editions]] 语法的兼容性建议。

[[concepts/proto3|proto3]] 是 [[entities/protocol-buffers|Protocol Buffers]] 语言的第三个修订版本,相比 proto2 简化了语法并修改了字段存在性的默认行为。[[concepts/proto3|proto3]] 引入 optional 和 implicit 两种 singular 字段模式,repeated 标量数值字段默认采用 [[concepts/packed-encoding|packed 编码]],消息类型字段自动具有字段存在性。[[concepts/proto3|proto3]] 推荐使用 optional 关键字标注以获得与 [[concepts/protobuf-editions|protobuf editions]] 和 proto2 的最大兼容性。文件首行必须通过 `syntax = "proto3"` 显式声明 proto3,否则编译器默认假定使用 proto2。

### 字段存在性实现细节
相较于 [[concepts/proto2|proto2]] 默认追踪字段存在性,[[concepts/proto3|proto3]] 默认不追踪 [[concepts/field-presence|字段存在性]],仅支持 singular 字段和 repeated 字段。[[concepts/proto3|proto3]] 通过以下两种方式支持存在性:一是使用 `optional` 关键字（自 3.12 起为实验性,用于显式开启 [[concepts/field-presence|字段存在性]] 追踪）;二是使用 wrapper 类型。在 [[concepts/proto3|proto3]] 中,被标记为 `optional` 的字段会像 [[concepts/proto2|proto2]] 一样追踪 [[concepts/field-presence|字段存在性]],而没有任何标签的字段（即"singular 字段"）则继续省略存在性信息。

值得注意的是,[[concepts/proto3|proto3]] 的描述符已经将 `LABEL_OPTIONAL` 用于不追踪存在性的 singular 字段,这正是 [[concepts/proto3|proto3]] 不能直接复用 [[concepts/proto2|proto2]] 中 `LABEL_OPTIONAL` 描述符来表示存在性的原因——大量现有的反射代码已假设 [[concepts/proto3|proto3]] 中的 `LABEL_OPTIONAL` 不包含存在性信息。

## 别名
- proto 3

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/proto-file|.proto file]]

## 关键概念
- [[concepts/proto3|proto3]]
- [[concepts/proto2|proto2]]
- [[concepts/message-type|Message Type]]
- [[concepts/field-number|Field Number]]
- [[concepts/field-number-encoding|Field Number Encoding]]
- [[concepts/field-cardinality|Field Cardinality]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/wire-format|Wire Format]]
- [[concepts/packed-encoding|packed encoding]]
- [[concepts/reserved-field-numbers|Reserved Field Numbers]]
- [[concepts/reserved-field-names|Reserved Field Names]]
- [[concepts/maps|Maps]]
- [[concepts/well-formed-messages|Well-formed Messages]]
- [[concepts/last-one-wins|Last One Wins]]
- [[concepts/deleting-fields|Deleting Fields]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/json-encoding|JSON encoding]]
- [[concepts/textformat|TextFormat]]
- [[concepts/textproto|TextProto]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/label-optional|LABEL_OPTIONAL]]

## 要点
- [[concepts/proto3|proto3]] 文件首行必须通过 `syntax = "proto3"` 显式声明,否则 [[entities/protocol-buffers|Protocol Buffers]] 编译器默认假定使用 proto2。
- 每个消息字段必须分配 1 到 536,870,911 之间的唯一 [[concepts/field-number|字段编号]],其中 19000-19999 为 Protocol Buffers 实现保留,字段编号一旦投入使用便不可更改。
- 字段编号 1-15 仅占用 1 字节[[concepts/wire-format|线格式]]空间,应分配给最常设置的字段以节省空间。
- [[concepts/proto3|proto3]] 中 singular 字段分 optional（推荐）与 implicit 两种模式,repeated 数值字段默认采用 [[concepts/packed-encoding|packed 编码]],[[concepts/maps|map]] 字段用于键/值对类型,消息类型字段自动具有字段存在性。
- [[concepts/deleting-fields|删除字段]] 时必须将对应字段编号加入 [[concepts/reserved-field-numbers|保留列表]]（也建议保留[[concepts/reserved-field-names|字段名称]]）,否则复用编号会导致解析错误、PII 泄漏或数据损坏。
- [[entities/protoc|protoc]] 编译器为 C++、Java、Kotlin、Python、Go、Ruby、Objective-C、C#、PHP 等目标语言分别生成不同格式的数据访问代码。
- singular 字段在线格式字节中出现多次时,解析器仅保留最后一次出现的实例,体现 [[concepts/last-one-wins|Last One Wins]] 语义。
- 推荐使用 optional 字段标签以获得与 [[concepts/protobuf-editions|Protobuf Editions]] 和 proto2 的最大兼容性。
- 相比 proto2,[[concepts/proto3|proto3]] 简化了语法并修改了字段存在性的默认行为,消除了对 required 字段的支持以及默认值设置的复杂性。
- 相较于 [[concepts/proto2|proto2]] 默认追踪字段存在性,[[concepts/proto3|proto3]] 默认不追踪 [[concepts/field-presence|字段存在性]]。
- [[concepts/proto3|proto3]] 通过 `optional` 关键字（自 3.12 起为实验性）或 wrapper 类型两种方式支持 [[concepts/field-presence|字段存在性]];被标记为 `optional` 的字段会像 [[concepts/proto2|proto2]] 一样追踪 [[concepts/field-presence|字段存在性]],而 singular 字段则继续省略存在性信息。
- [[concepts/proto3|proto3]] 描述符已使用 `[[concepts/label-optional|LABEL_OPTIONAL]]` 描述不追踪存在性的 singular 字段,因此不能直接复用 [[concepts/proto2|proto2]] 的 `[[concepts/label-optional|LABEL_OPTIONAL]]` 描述符来表示存在性——大量现有反射代码已假设 [[concepts/proto3|proto3]] 中的 `[[concepts/label-optional|LABEL_OPTIONAL]]` 不包含存在性信息。