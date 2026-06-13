---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/features.md]]"
  - "[[protobuf/editions.md]]"
tags:
  - "document"
aliases:
  - "Protocol Buffers Language Guide (proto3)"
  - "proto3 语言指南"
---

## 关键概念
- [[concepts/proto3|proto3]]
- [[concepts/proto2|proto2]]
- [[concepts/message-type|Message Type]]
- [[concepts/field-number|Field Number]]
- [[concepts/field-number-encoding|Field Number Encoding]]
- [[concepts/field-cardinality|Field Cardinality]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/no-presence-discipline|No presence discipline]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
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
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/edition-2024|Edition 2024]]
- [[concepts/features-enum-type|features.enum_type]]
- [[concepts/features-field-presence|features.field_presence]]
- [[concepts/features-enforce-naming-style|features.enforce_naming_style]]

## 要点
- [[concepts/proto3|proto3]] 是 [[entities/protocol-buffers|Protocol Buffers]] 语言的第三个主要版本,发布于 2016 年。
- [[concepts/proto3|proto3]] 引入了隐式字段存在性（implicit field presence）概念,在从 proto3 迁移到 editions 时,原有的 implicit 字段会使用 field_presence feature 并设置为 IMPLICIT 值。
- [[concepts/proto3|proto3]] 文件首行必须通过 `syntax = "proto3"` 显式声明,否则 [[entities/protocol-buffers|Protocol Buffers]] 编译器默认假定使用 proto2。
- 每个消息字段必须分配 1 到 536,870,911 之间的唯一 [[concepts/field-number|字段编号]],其中 19000-19999 为 Protocol Buffers 实现保留,字段编号一旦投入使用便不可更改。
- 字段编号 1-15 仅占用 1 字节[[concepts/wire-format|线格式]]空间,应分配给最常设置的字段以节省空间。
- [[concepts/proto3|proto3]] 中 singular 字段分 optional（推荐）与 implicit 两种模式,repeated 数值字段默认采用 [[concepts/packed-encoding|packed 编码]],[[concepts/maps|map]] 字段用于键/值对类型,消息类型字段自动具有字段存在性。
- [[concepts/proto3|proto3]] 默认采用无存在性（[[concepts/no-presence-discipline|no presence]]）模式以简化 API,但通过 `optional` 标签可以为基本类型字段（数值、字符串、字节、枚举）启用显式存在性（[[concepts/explicit-presence-discipline|explicit presence]]）跟踪。
- 从 v3.15.0 版本开始,proto3 中 optional 字段的显式存在性跟踪功能默认启用;在 v3.12.0 之前,需要使用 `--experimental_allow_proto3_optional` 编译标志才能启用该功能。
- 根据 proto3 语法规则,所有枚举类型都必须包含一个映射到 0 的枚举值,通常命名为 `UNKNOWN`。
- [[concepts/deleting-fields|删除字段]] 时必须将对应字段编号加入 [[concepts/reserved-field-numbers|保留列表]]（也建议保留[[concepts/reserved-field-names|字段名称]]）,否则复用编号会导致解析错误、PII 泄漏或数据损坏。
- [[entities/protoc|protoc]] 编译器为 C++、Java、Kotlin、Python、Go、Ruby、Objective-C、C#、PHP 等目标语言分别生成不同格式的数据访问代码。
- singular 字段在线格式字节中出现多次时,解析器仅保留最后一次出现的实例,体现 [[concepts/last-one-wins|Last One Wins]] 语义。
- 推荐使用 optional 字段标签以获得与 [[concepts/protobuf-editions|Protobuf Editions]] 和 proto2 的最大兼容性。
- 相比 proto2,[[concepts/proto3|proto3]] 简化了语法并修改了字段存在性的默认行为,消除了对 required 字段的支持以及默认值设置的复杂性。
- 相较于 [[concepts/proto2|proto2]] 默认追踪字段存在性,[[concepts/proto3|proto3]] 默认不追踪 [[concepts/field-presence|字段存在性]]。
- [[concepts/proto3|proto3]] 通过 `optional` 关键字或 wrapper 类型两种方式支持 [[concepts/field-presence|字段存在性]];被标记为 `optional` 的基本类型 singular 字段（数值、字符串、字节、枚举）会像 [[concepts/proto2|proto2]] 一样追踪 [[concepts/field-presence|字段存在性]],而 implicit singular 字段则继续省略存在性信息。
- [[concepts/proto3|proto3]] 描述符已使用 `[[concepts/label-optional|LABEL_OPTIONAL]]` 描述不追踪存在性的 singular 字段,因此不能直接复用 [[concepts/proto2|proto2]] 的 `[[concepts/label-optional|LABEL_OPTIONAL]]` 描述符来表示存在性——大量现有反射代码已假设 [[concepts/proto3|proto3]] 中的 `[[concepts/label-optional|LABEL_OPTIONAL]]` 不包含存在性信息。
- 在 [[concepts/features-enum-type|features.enum_type]] 这一 feature 方面,[[concepts/proto3|proto3]] 默认采用 OPEN（open enums）枚举模式。
- 在 [[concepts/features-field-presence|features.field_presence]] 这一 feature 方面,[[concepts/proto3|proto3]] 默认为 IMPLICIT[[concepts/field-presence|字段存在性]];除非字段带有 `optional` 标签,此时其行为类似于 EXPLICIT。
- [[concepts/proto3|proto3]] 在符号可见性方面默认采用 EXPORT_ALL。
- [[concepts/proto3|proto3]] 在命名风格方面默认采用 STYLE_LEGACY。
- 需要注意的是,[[concepts/features-enum-type|features.enum_type]] 这一 feature 对 [[concepts/proto3|proto3]] 文件不产生影响。
- [[concepts/proto3|proto3]] 的语言指南是一个独立的文档,但 editions 指南对其向 [[concepts/protobuf-editions|Protobuf Editions]] 迁移时的行为做了相应说明。