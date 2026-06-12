---
type: source
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
tags:
  - "document"
aliases:
  - "Protobuf Proto3 Language Guide"
---

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers (protobuf)]] — 语言无关、平台无关的序列化机制，定义了数据结构和协议
- [[entities/protoc|protoc (Protocol Buffer Compiler)]] — 将 `.proto` 文件编译成目标语言代码的编译器工具
- [[entities/C++|C++]] — proto3 支持的主要语言之一，在 Editions 演进中具有重要地位

## 关键概念
- [[concepts/proto3|proto3]] — Protocol Buffers 的第三个主要修订版，于 2016 年首次发布。与 proto2 相比，proto3 简化了语法，移除了 required 关键字，并默认使用打包编码。本文档详细介绍了其语法规则和最佳实践，是开发者使用 proto3 的核心参考。需要注意的是，proto3 的引入分裂了生态，而 [[concepts/protobuf-editions|Protobuf Editions]] 通过 Feature 统一了所有差异。
- [[concepts/proto2|proto2]] — 旧版语言语法，本文档通过对比提及；在 Editions 中两者差异已被消除
- [[concepts/protobuf-editions|Protobuf Editions]] — 新的版本管理机制，提供更细粒度的控制，并能机械迁移 proto2/proto3 文件
- [[concepts/edition-zero|Edition Zero]] — Protobuf Editions 的初始版本，设计支持从 proto2/proto3 无缝迁移
- [[concepts/feature|Feature]] — Editions 中统一管理语义差异的机制，用于表达 proto2 和 proto3 之间不可调和的少数差异
- [[concepts/field-number|字段编号]] — 消息字段的唯一标识整数，一旦分配不得更改
- [[concepts/field-cardinality|字段基数]] — 定义了字段在序列化中的出现次数（singular、repeated、map）
- [[concepts/field-presence|字段存在性]] — 判断字段是否被显式设置的能力，optional 字段具有此特性
- [[concepts/packed-encoding|打包编码]] — proto3 中重复标量字段的默认序列化方式
- [[concepts/reserved|reserved 保留字段]] — 用于防止已删除字段编号被误用的关键字
- [[concepts/scalar-types|标量类型]] — 基本数据类型（int32、string、bool 等）
- [[concepts/enumeration|枚举类型]] — 一组命名的数值常量
- [[concepts/map-fields|映射字段]] — 键值对数据类型
- [[concepts/wire-format|线格式]] — 二进制序列化格式，字段编号不可变的原因
- [[concepts/json-representation|JSON 表示]] — 消息的 JSON 序列化格式
- [[concepts/default-values|默认值]] — 字段未设置时返回的默认零值
- [[concepts/well-formed-message|格式良好的消息]] — 描述序列化/反序列化字节流的规范性
- [[concepts/last-one-wins|Last One Wins]] — 解析器处理重复 singular 字段的规则
- [[concepts/optional-field|optional 字段]] — 推荐使用的显式基数标签，具有字段存在性
- [[concepts/implicit-field|隐式字段]] — 无显式基数标签，不推荐使用
- [[concepts/repeated-field|repeated 字段]] — 可重复零次或多次的字段类型
- [[concepts/protobuf-code-generation|代码生成]] — protoc 为多种语言生成数据访问类的功能

## 要点
- proto3 于 2016 年首次发布，简化了语法，移除了 required 关键字，并默认使用打包编码
- 字段编号一旦分配不得更改，删除时必须使用 reserved 保留以防止重用
- 推荐使用 optional 字段而非隐式字段，以确保字段存在性和最大兼容性
- repeated 字段的标量数值类型默认使用打包编码以节省空间
- 文档是开发者使用 proto3 的核心参考，同时提供与 proto2 和 editions 的对比
- proto3 是 Protocol Buffers 历史上最后一次激进的语言变化，其引入导致了生态系统分裂
- 在 Protobuf Editions 中，proto2 与 proto3 的差异通过 Feature 机制统一管理，Edition Zero 支持机械无缝迁移

## 别名
- proto3 revision — 指代 proto3 修订版本
- Protocol Buffers version 3 — 版本号正式名称
- Proto3 — 常见简写形式
- protobuf3 — 另一种常见简写
- proto3 syntax — 强调其语法层面的含义