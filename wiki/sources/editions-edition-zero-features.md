---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-edition-zero-feature-enum-field-closedness.md]]"
tags:
  - "proto2 syntax"
  - "proto3 syntax"
  - "Protobuf Editions"
  - "features.field_presence"
  - "features.enum_type"
  - "features.repeated_field_encoding"
  - "features.string_field_validation"
  - "features.message_encoding"
  - "features.json_format"
  - "presence discipline"
  - "closed enum"
  - "open enum"
  - "packed encoding"
  - "extensions"
  - "groups"
  - "Large-Scale Change"
  - "EXPLICIT presence"
  - "IMPLICIT presence"
  - "LEGACY_REQUIRED"
  - "required keyword"
  - "optional keyword"
  - "defaulted fields"
  - "Features message"
  - "UTF-8 validation"
  - "protobuf JSON format"
  - "hasbit"
  - "Unknown field set"
  - "Wire types"
  - "proto3_optional"
  - "Field option attributes"
  - "TypeResolver"
  - "Custom default values"
  - "Required allowlist"
  - "Converged semantics"
  - "LEGACY_BEST_EFFORT"
  - "Parallel arrays"
  - "LENGTH_PREFIXED"
  - "U+FFFD replacement characters"
  - "Features as Custom Options"
  - "Out-of-conformance behavior"
  - "DELIMITED"
  - "EXPANDED encoding"
  - "no-syntax Protobuf"
  - "mixed syntax messages"
aliases:
  - "Edition Zero Features"
  - "editions-edition-zero-features"
---

## 来源
- Original file: [[protobuf/editions-edition-zero-features.md]]
- Ingested: 2026-06-13
- 作者：@mcy、@zhangskz、@mkruskal-google
- 批准日期：2022-07-22

## 核心内容
本文档是 [[entities/protocol-buffers|Protocol Buffers]] 项目关于 [[entities/edition-zero|Edition Zero]] 特性的设计提案，旨在通过引入一组特性标志（feature flags）取代 [[concepts/proto2-syntax|proto2 syntax]] 和 [[concepts/proto3-syntax|proto3 syntax]] 中固定的语法行为，从而迈向 [[concepts/no-syntax-protobuf|no-syntax Protobuf]] 的"第一版"。文档定义的核心特性包括 [[concepts/features-field_presence|features.field_presence]]（EXPLICIT/IMPLICIT/LEGACY_REQUIRED）、[[concepts/features-enum_type|features.enum_type]]（OPEN/CLOSED）、[[concepts/features-repeated_field_encoding|features.repeated_field_encoding]]（PACKED/EXPANDED）、[[concepts/features-string_field_validation|features.string_field_validation]]（MANDATORY/HINT/NONE）、[[concepts/features-message_encoding|features.message_encoding]]（LENGTH_PREFIXED/DELIMITED）以及 [[concepts/features-json_format|features.json_format]]（ALLOW/LEGACY_BEST_EFFORT），并通过 [[concepts/features-as-custom-options|Features as Custom Options]] 的语法将其封装在 [[concepts/features-message|Features message]] 中。文档明确的核心目标是使任意现有的 [[concepts/proto2-syntax|proto2]] 或 [[concepts/proto3-syntax|proto3]] 文件可通过应用适当的特性无变更地迁移到 editions，同时保留各语言代码生成器现有的 [[concepts/out-of-conformance-behavior|非一致性行为]] 以避免 [[concepts/large-scale-change|LSC]]（大规模变更）引入语义差异。

## 关键实体
- [[entities/edition-zero|Edition Zero]] — Protocol Buffers 的首个 edition，通过特性标志取代 proto2/proto3 固定语法
- [[entities/protocol-buffers|Protocol Buffers]] — Google 开发的语言中立结构化数据序列化机制
- [[entities/protoc|protoc]] — Protocol Buffers 的官方编译器，需实现所有新特性及其语义
- [[entities/google3|google3]] — Google 内部 monorepo，提供迁移规模数据（385,236 个 `optional`、12.3k 启用 packed 等）
- [[entities/protobuf-dev|protobuf.dev]] — Protocol Buffers 官方网站，承载后续取代本文件的特性文档

## 关键概念
### 特性标志（Feature Flags）
- [[concepts/features-field_presence|features.field_presence]] — 控制 singular 字段的 [[concepts/presence-discipline|presence discipline]]
- [[concepts/features-enum_type|features.enum_type]] — 控制枚举的开闭性
- [[concepts/features-repeated_field_encoding|features.repeated_field_encoding]] — 控制 repeated 字段的编码方式
- [[concepts/features-string_field_validation|features.string_field_validation]] — 控制字符串字段 UTF-8 验证严格程度
- [[concepts/features-message_encoding|features.message_encoding]] — 控制消息字段编码方式（LENGTH_PREFIXED 或 DELIMITED）
- [[concepts/features-json_format|features.json_format]] — 控制 JSON 格式支持

### 存在性规约（Presence Discipline）
- [[concepts/presence-discipline|presence discipline]] — 描述字段是否被显式设置的机制
- [[concepts/explicit-presence|EXPLICIT presence]] — 默认值，API 暴露 hasbit
- [[concepts/implicit-presence|IMPLICIT presence]] — 对应 proto3 implicit 字段
- [[concepts/legacy_required|LEGACY_REQUIRED]] — wire-required 且 API-optional
- [[concepts/hasbit|hasbit]] — 字段存在性底层机制

### 关键字与迁移
- [[concepts/required-keyword|required keyword]] — proto2 中将被消除的关键字
- [[concepts/optional-keyword|optional keyword]] — 将被消除，需删除 google3 中 385,236 个实例
- [[concepts/proto3_optional|proto3_optional]] — proto3 中赋予显式存在的能力，将成为解析错误
- [[concepts/defaulted-fields|defaulted fields]] — proto3 中与 required 对应的规约
- [[concepts/required-allowlist|Required allowlist]] — 控制 LEGACY_REQUIRED 使用范围
- [[concepts/large-scale-change|Large-Scale Change]]（LSC）— Google 内部大规模自动化重构工具

### 枚举语义
- [[concepts/closed-enum|closed enum]] — proto2 行为，需验证值在已知集合内
- [[concepts/open-enum|open enum]] — 默认行为，直接解析超出范围的值
- [[concepts/unknown-field-set|Unknown field set]] — closed enum 超范围值的存储位置
- [[concepts/parallel-arrays|Parallel arrays]] — closed enum 易破坏的并行数组模式
- [[concepts/legacy_best_effort|LEGACY_BEST_EFFORT]] — JSON 模式的宽松选项

### 编码机制
- [[concepts/packed-encoding|packed encoding]] — repeated 字段的打包编码（默认）
- [[concepts/expanded-encoding|EXPANDED encoding]] — proto2 默认的非打包编码
- [[concepts/length_prefixed|LENGTH_PREFIXED]] — 消息字段默认编码（wire type 2）
- [[concepts/delimited|DELIMITED]] — 分组编码（wire type 3/4），替代 group 语法
- [[concepts/groups|groups]] — proto2 中将被删除的 group 语法
- [[concepts/wire-types|Wire types]] — Protobuf 二进制编码格式标识符

### 扩展与扩展性
- [[concepts/extensions|extensions]] — editions 中始终允许，取消 proto3 限制
- [[concepts/typeresolver|TypeResolver]] — 与 extensions 兼容性不佳的运行时类型解析 API

### 核心架构概念
- [[concepts/protobuf-editions|Protobuf Editions]] — 取代固定 syntax 关键字的新机制
- [[concepts/no-syntax-protobuf|no-syntax Protobuf]] — editions 背后的哲学愿景
- [[concepts/features-as-custom-options|Features as Custom Options]] — 特性作为自定义选项的语法
- [[concepts/features-message|Features message]] — 承载所有特性配置的 protobuf message 定义
- [[concepts/field-option-attributes|Field option attributes]] — retention 与 target 元属性
- [[concepts/converged-semantics|Converged semantics]] — Edition Zero 定义的统一语义
- [[concepts/out-of-conformance-behavior|Out-of-conformance behavior]] — 需保留的语言实现非一致性
- [[concepts/mixed-syntax-messages|mixed syntax messages]] — 跨不同语法的消息迁移关注点

### 验证与格式
- [[concepts/utf-8-validation|UTF-8 validation]] — 字符串字段 UTF-8 合法性校验
- [[concepts/protobuf-json-format|protobuf JSON format]] — protobuf 消息的 JSON 序列化格式
- [[concepts/u+fffd-replacement-characters|U+FFFD replacement characters]] — 无效 UTF-8 的替换字符
- [[concepts/custom-default-values|Custom default values]] — 字段自定义默认值（IMPLICIT 字段不支持）

## 要点
- **核心目标**：任意现有的 proto2 或 proto3 文件都可通过应用适当的特性无变更地迁移到 editions。
- **特性系统**：文档定义了 6 个核心特性（field_presence、enum_type、repeated_field_encoding、string_field_validation、message_encoding、json_format），每个特性具有明确的取值与默认值。
- **关键字消除**：`optional` 和 `required` 关键字被完全消除，使其成为解析错误；singular 字段的存在性完全通过 `features.field_presence` 控制。
- **数据驱动的默认**：PACKED 设为默认编码（基于 google3 中 12.3k 启用 vs 200 禁用的数据）；OPEN 设为默认枚举类型。
- **group 语法移除**：group 语法在 editions 中删除，原 proto2 group 字段转换为嵌套消息加上 `features.message_encoding = DELIMITED`。
- **extensions 全面允许**：editions 取消了 proto3 对 extensions 的限制，所有消息都允许使用扩展。
- **设计权衡**：保留各语言代码生成器现有的非一致性行为（[[concepts/out-of-conformance-behavior|Out-of-conformance behavior]]），以便 LSC 迁移是无变更的（no-op）。
- **迁移规模**：google3 迁移需删除 385,236 个 `optional` 实例，是 Edition Zero 迁移工作的重要参考数据点。
- **后续取代**：本文档已大部分被 [[entities/protobuf-dev|protobuf.dev]] 上的"Feature Settings for Editions"页面取代。