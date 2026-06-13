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
  - "[[protobuf/editions-protobuf-editions-for-schema-producers.md]]"
  - "[[protobuf/editions-life-of-an-edition.md]]"
  - "[[protobuf/editions-legacy-syntax-editions.md]]"
  - "[[protobuf/editions-editions-feature-visibility.md]]"
  - "[[protobuf/editions-edition-zero-json-handling.md]]"
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "document"
aliases:
  - "Protocol Buffers Language Guide (proto3)"
  - "proto3 语言指南"
---

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
- 在 [[concepts/edition-zero|Edition Zero]] 推出之前,[[concepts/proto3|proto3]] 与 [[concepts/proto2|proto2]] 并存使用。
- [[concepts/edition-zero|Edition Zero]] 通过 [[concepts/features-enum-type|features]] 机制把 [[concepts/proto2|proto2]] 与 [[concepts/proto3|proto3]] 的差异统一到一组良定义的默认值上,因此 [[concepts/proto3|proto3]] 在 [[concepts/edition-zero|Edition Zero]] 的统一工作中扮演重要角色。
- 在过渡期内,[[entities/protoc|protoc]] 必须能够同时解析 [[concepts/proto3|proto3]]、[[concepts/proto2|proto2]] 和 editions 文件。
- [[entities/protobuf-team|Protobuf 团队]]将提供一个工具,能够以完全兼容的方式将 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]] 文件升级到 [[concepts/edition-zero|Edition Zero]],从而帮助 schema producers 完成迁移。
- 对于新发布的 `.proto` 文件,schema producers 应直接使用 [[concepts/edition-zero|Edition Zero]] 的默认值,而非继续沿用 [[concepts/proto3|proto3]] 语法。
- [[concepts/proto3|proto3]] 是 Protobuf 的第三代语法标准,在 [[concepts/protobuf-editions|Protobuf Editions]] 出现之前是 Protobuf 的最新语法版本。
- [[concepts/protobuf-editions|Editions]] 机制旨在统一替换 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]],提供更灵活、可演进的 [[concepts/features-enum-type|features]] 系统。
- 与 [[concepts/proto2|proto2]] 类似,从 [[concepts/proto3|proto3]] 到 [[concepts/protobuf-editions|Editions]] 的迁移也是通过 [[concepts/editions-upgrader|Editions upgrader]] 工具（即 `protoc --upgrade-edition`）完成的。
- 该工具会为文件添加适当的 edition 声明（如 `edition = "2023";`）和 `option features.* = ...;` 选项,使其保留原始行为。
- [[concepts/edition-zero|Edition Zero]] 的迁移涉及同时处理 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]] 这两种旧语法。
- 从 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]] 迁移到 [[concepts/protobuf-editions|Editions]] 属于大规模变更（[[concepts/large-scale-change|Large-scale Change]]）,且这一变更可以完全自动化,无需破坏性改动。
- 在 [[concepts/protobuf-editions|Editions]] 设计早期阶段,曾讨论过将 [[concepts/proto2|proto2]] 和 [[concepts/proto3|proto3]] 作为"特殊 edition"的方案,但该方案的具体形态和必要性当时并未确定。
- 提案建议将 [[concepts/proto3|proto3]] 视为 [[concepts/legacy-syntax-editions|Legacy Syntax Editions]] 中的特殊 edition,具体取值为 `EDITION_PROTO3 = 999`。
- 在 [[concepts/proto3|proto3]] 中,`optional` 关键字会将对应的 [[concepts/features-field-presence|field_presence]] feature 设置为 `EXPLICIT`,即设置显式存在性。
- [[concepts/proto3|proto3]] 的语法元素（如 `optional` 关键字设置的 `EXPLICIT` presence）与 [[concepts/protobuf-editions|Editions]] 的 [[concepts/feature-inference|feature inference]] 之间存在映射关系,需要通过专门的 [[concepts/feature-inference|feature inference]] 逻辑来正确推断出对应的 feature 行为。
- [[concepts/proto3|proto3]] 引入了对 [[concepts/proto2|proto2]] 的多项更改,包括字段默认值的设定（如 int32 的 0、string 的空字符串等）以及移除 required 字段。
- [[concepts/edition-zero|Edition Zero]] 保留了所有 [[concepts/proto2|proto2]]/[[concepts/proto3|proto3]] 行为,这使得 [[concepts/proto3|proto3]] 成为初始版本旨在向后兼容的两个前身标准之一。
- [[concepts/proto3|proto3]] 与 [[concepts/proto2|proto2]] 一起代表了 [[concepts/protobuf-editions|Editions]] 系统必须保持兼容的现有行为。
- [[concepts/protobuf-editions|Editions]] 系统的设计目标包括与 [[concepts/proto3|proto3]] 现有行为的兼容性,使得现有用户向新系统的迁移是无缝的。
- 在 UTF8 验证等 feature 建模方式的讨论中,由于 [[concepts/edition-zero|Edition Zero]] 保留了所有 [[concepts/proto2|proto2]]/[[concepts/proto3|proto3]] 行为,因此无论选择何种 feature 表达方式,都不会产生功能性差异,讨论的焦点仅在于应使用哪些 feature 来控制这些行为。
- [[concepts/proto3|proto3]] 是 [[entities/protocol-buffers|Protobuf]] 的第三版语法,是当前推荐使用的版本。
- 在 JSON 处理方面,[[concepts/proto3|proto3]] 默认完全验证 JSON 映射的唯一性:[[entities/protoc|protoc]] 会在解析时检测到任何 [[concepts/json-field-name-conflicts|JSON 冲突]]并直接报错。
- 可通过 `deprecated_legacy_json_field_conflicts` 选项禁用 [[concepts/proto3|proto3]] 的这一严格检查,使其退化为尽力而为模式（即 [[concepts/legacy-best-effort|LEGACY_BEST_EFFORT]] 行为）。
- 本次设计提案建议将 [[concepts/proto3|proto3]] 默认迁移到 `ALLOW` 状态,以调整其 JSON 字段名冲突的处理策略。
- 定义在 [[concepts/proto3|proto3]] 文件中的枚举是开放的（[[concepts/open-enum|Open Enum]]）,意味着它们可以具有未在枚举定义中显式列出的值。
- [[concepts/proto3|proto3]] 与 [[concepts/proto2|proto2]] 相比引入了多项变化,包括字段的隐式存在性（[[concepts/implicit-presence|implicit presence]]）以及开放枚举（[[concepts/open-enum|open enum]]）的概念。
- [[concepts/proto3|proto3]] 中枚举的开放性是讨论的核心,因为这些枚举在 [[concepts/proto2|proto2]] 字段中使用时,其在各语言实现中的行为差异显著。
- proto 编译器会拒绝在 [[concepts/proto3|proto3]] 消息中使用 [[concepts/proto2|proto2]] 枚举值类型的字段,原因是隐式存在性约束不允许非零默认值。
- 关于 [[concepts/proto3|proto3]] 枚举开放性的官方行为定义为:"枚举的开放性应由枚举自身的定义决定"。
- [[concepts/proto3|proto3]] 枚举的开放性是相关讨论中曾被误解的关键边界情况之一。