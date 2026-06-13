---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-readme|editions-readme]]"]
tags: [standard]
aliases:
  - "Enum Field Closedness"
  - "Edition Zero Feature: Enum Field Closedness"
  - "枚举字段闭合性"
---


# Edition Zero Feature: Enum Field Closedness

## 定义
Edition Zero Feature: Enum Field Closedness 是一份 Protobuf Editions 设计文档，定义了在 Edition Zero 中引入的"枚举字段闭合性（closedness）"特性。该特性允许 schema 生产者在 `.proto` 文件中显式声明一个枚举类型是"开放（open）"还是"闭合（closed）"，从而控制当消息中出现未在枚举中定义的未知值时，运行时与代码生成器应采取的策略。它属于 [[concepts/edition-zero-features|Edition Zero Features]] 集合中的标准（standard）级约定，服务于 [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]] 的整体目标。

## 关键特征
- 显式的开/闭合语义：schema 作者可在 enum 声明中标注枚举是 open（允许未知值经过）还是 closed（拒绝未知值或将其视为错误）。
- 与 Editions 机制集成：闭合性不是一个独立开关，而是通过 [[sources/editions|Protocol Buffers Editions 语言指南]] 中的 edition 级别设置进行声明和演进。
- 影响代码生成：对 C++、Java、Python、Go 等多种目标语言生成的访问器与校验逻辑不同，闭合枚举通常会生成更严格的检查。
- 影响运行时行为：决定序列化/反序列化路径在遇到未识别枚举值时是默默保留、警告还是报错。
- 服务于"更严格 schema"愿景：与字段存在性（field presence）等其他 Edition Zero 特性协同，使生产者能更精确地表达意图。
- 文档当前状态：作为历史设计记录保留在 [[sources/editions-readme|Protobuf Editions 设计文档索引]] 中，仅供历史参考，不应被视为当前规范。

## 应用
- API 演进场景：当业务枚举需要新增成员时，使用 open 枚举可保证旧消费者仍能解码新生产者写入的未知值。
- 强一致性场景：在内部服务或受控环境中使用 closed 枚举，可在反序列化阶段就检测到上下游枚举定义不一致。
- 多语言代码生成：为不同语言的运行时提供统一的枚举校验语义，避免各语言在未知值处理上各行其是。
- Schema 治理：配合 [[concepts/protobuf-editions-for-schema|Protobuf Editions for Schema Producers]] 的整体策略，帮助团队以最小破坏性方式收紧或放松其接口契约。
- 库与框架适配：brpc 等基于 Protobuf 的 RPC 框架在生成存根时可依据闭合性调整对未知枚举值的日志与告警行为。

## 相关概念
- [[concepts/edition-zero-features|Edition Zero Features]]
- [[concepts/stricter-schemas-with-editions|Stricter Schemas with Editions]]
- [[concepts/protobuf-editions-for-schema|Protobuf Editions for Schema Producers]]
- [[concepts/feature-settings-for-editions|Feature Settings for Editions]]
- [[concepts/editions-language-guide|Protocol Buffers Editions 语言指南]]
- [[concepts/application-note-field-presence|Application note: Field presence]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protobuf-editions|Protobuf Editions]]

## 来源提及
- "The following topics are in this repository:" — [[sources/editions-readme|editions-readme]]
- "*   [Edition Zero Feature: Enum Field Closedness](edition-zero-feature-enum-field-closedness.md)" — [[sources/editions-readme|editions-readme]]
- "These are purely for historical value and should not be treated as documentation of the current state." — [[sources/editions-readme|editions-readme]]